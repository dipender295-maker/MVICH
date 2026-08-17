import numpy as np
from scipy import sparse
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingClassifier


class MVICH:
    def __init__(
        self,
        gamma=1.0,
        k_max=64,
        radius_quantile=0.90,
        epsilon=1e-12,
        random_state=0,
    ):
        self.gamma = float(gamma)
        self.k_max = int(k_max)
        self.radius_quantile = float(radius_quantile)
        self.epsilon = float(epsilon)
        self.random_state = int(random_state)

    def fit_predict(
        self,
        X_source,
        y_source,
        source_project_ids,
        X_target,
        semantic_views=None,
    ):
        Xs = np.asarray(X_source, dtype=float)
        ys = np.asarray(y_source, dtype=int).reshape(-1)
        project_ids = np.asarray(source_project_ids)
        Xt = np.asarray(X_target, dtype=float)

        self._validate_inputs(Xs, ys, project_ids, Xt)

        Xs, Xt = self._impute(Xs, Xt)
        Xs, Xt = self._project_balanced_robust_scale(Xs, Xt, project_ids)

        views = self._prepare_views(Xs.shape[1], semantic_views)
        layer_edges = {}
        layer_contexts = {}

        for layer_id, indices in views.items():
            contexts, edges = self._build_layer(
                Xs[:, indices],
                Xt[:, indices],
                ys,
                project_ids,
                layer_id,
            )
            layer_contexts[layer_id] = contexts
            if edges:
                layer_edges[layer_id] = edges

        edges = self._normalize_layer_weights(layer_edges)
        ns = Xs.shape[0]
        X = np.vstack([Xs, Xt])
        H, propagation_weights, intrinsic_confidences = self._build_incidence(
            X.shape[0], ns, edges
        )
        Z = self._propagate(X, H, propagation_weights)

        Zs = Z[:ns]
        Zt = Z[ns:]
        sample_weights = self._classifier_weights(
            ys,
            ns,
            edges,
            intrinsic_confidences,
        )

        classifier = GradientBoostingClassifier(random_state=self.random_state)
        classifier.fit(Zs, ys, sample_weight=sample_weights)
        probabilities = classifier.predict_proba(Zt)[:, 1]

        self.source_location_ = self.source_location
        self.source_scale_ = self.source_scale
        self.views_ = views
        self.contexts_ = layer_contexts
        self.hyperedges_ = edges
        self.incidence_matrix_ = H
        self.propagation_weights_ = propagation_weights
        self.intrinsic_confidences_ = intrinsic_confidences
        self.representation_ = Z
        self.source_sample_weights_ = sample_weights
        self.classifier_ = classifier
        self.target_probabilities_ = probabilities

        return probabilities

    def _validate_inputs(self, Xs, ys, project_ids, Xt):
        if Xs.ndim != 2 or Xt.ndim != 2:
            raise ValueError("X_source and X_target must be two-dimensional arrays.")
        if Xs.shape[1] != Xt.shape[1]:
            raise ValueError("Source and target must have the same feature dimension.")
        if Xs.shape[0] != ys.shape[0] or Xs.shape[0] != project_ids.shape[0]:
            raise ValueError("Source features, labels, and project identifiers must align.")
        if Xs.shape[0] == 0 or Xt.shape[0] == 0:
            raise ValueError("Source and target data must be nonempty.")
        if not np.all(np.isin(np.unique(ys), [0, 1])):
            raise ValueError("y_source must contain binary labels 0 and 1.")
        if np.unique(project_ids).size == 0:
            raise ValueError("At least one source project is required.")

    def _impute(self, Xs, Xt):
        medians = np.nanmedian(Xs, axis=0)
        medians = np.where(np.isfinite(medians), medians, 0.0)
        Xs = np.where(np.isfinite(Xs), Xs, medians)
        Xt = np.where(np.isfinite(Xt), Xt, medians)
        self.imputation_values_ = medians
        return Xs, Xt

    def _weighted_quantile(self, values, weights, q):
        values = np.asarray(values, dtype=float)
        weights = np.asarray(weights, dtype=float)
        order = np.argsort(values, kind="mergesort")
        values = values[order]
        weights = weights[order]
        total = weights.sum()
        if total <= 0:
            return float(np.quantile(values, q))
        positions = (np.cumsum(weights) - 0.5 * weights) / total
        positions = np.concatenate(([0.0], positions, [1.0]))
        values = np.concatenate(([values[0]], values, [values[-1]]))
        return float(np.interp(q, positions, values))

    def _project_balanced_robust_scale(self, Xs, Xt, project_ids):
        project_weights = self._project_equal_module_weights(project_ids)
        d = Xs.shape[1]
        location = np.empty(d, dtype=float)
        scale = np.empty(d, dtype=float)

        for j in range(d):
            location[j] = self._weighted_quantile(Xs[:, j], project_weights, 0.50)
            q75 = self._weighted_quantile(Xs[:, j], project_weights, 0.75)
            q25 = self._weighted_quantile(Xs[:, j], project_weights, 0.25)
            scale[j] = q75 - q25

        self.source_location = location
        self.source_scale = scale
        Xs = (Xs - location) / (scale + self.epsilon)
        Xt = (Xt - location) / (scale + self.epsilon)
        return Xs, Xt

    def _project_equal_module_weights(self, project_ids):
        weights = np.empty(project_ids.shape[0], dtype=float)
        for p in np.unique(project_ids):
            mask = project_ids == p
            weights[mask] = 1.0 / np.sum(mask)
        return weights

    def _prepare_views(self, d, semantic_views):
        views = {}
        used = set()
        if semantic_views:
            for name, indices in semantic_views.items():
                idx = np.asarray(indices, dtype=int).reshape(-1)
                idx = np.unique(idx[(idx >= 0) & (idx < d)])
                if any(int(j) in used for j in idx):
                    raise ValueError("Semantic metric views must be disjoint.")
                if idx.size:
                    views[str(name)] = idx
                    used.update(int(j) for j in idx)
        views["full"] = np.arange(d, dtype=int)
        return views

    def _context_number(self, ns):
        if ns < 2:
            return 1
        return min(self.k_max, max(2, int(np.ceil(np.log2(ns)))))

    def _build_layer(self, Xs, Xt, ys, project_ids, layer_id):
        ns = Xs.shape[0]
        nt = Xt.shape[0]
        k = min(self._context_number(ns), ns)
        cluster_weights = self._project_equal_module_weights(project_ids)

        if k == 1:
            labels = np.zeros(ns, dtype=int)
        else:
            model = KMeans(
                n_clusters=k,
                init="k-means++",
                n_init="auto",
                random_state=self.random_state,
            )
            model.fit(Xs, sample_weight=cluster_weights)
            labels = model.labels_

        context_ids = np.unique(labels)
        contexts = []
        prototypes = {}

        for cid in context_ids:
            members = np.flatnonzero(labels == cid)
            represented_projects = np.unique(project_ids[members])
            project_prototypes = {}

            for p in represented_projects:
                pmembers = members[project_ids[members] == p]
                project_prototypes[p] = Xs[pmembers].mean(axis=0)

            prototype = np.mean(
                np.vstack([project_prototypes[p] for p in represented_projects]),
                axis=0,
            )
            prototypes[cid] = prototype
            contexts.append(
                {
                    "layer": layer_id,
                    "context_id": int(cid),
                    "members": members,
                    "projects": represented_projects,
                    "project_prototypes": project_prototypes,
                    "prototype": prototype,
                }
            )

        assigned_distances = np.empty(ns, dtype=float)
        for cid in context_ids:
            members = np.flatnonzero(labels == cid)
            assigned_distances[members] = np.linalg.norm(
                Xs[members] - prototypes[cid], axis=1
            )

        project_median_distances = []
        for p in np.unique(project_ids):
            values = assigned_distances[project_ids == p]
            if values.size:
                project_median_distances.append(np.median(values))
        tau = float(np.median(project_median_distances)) if project_median_distances else 0.0

        source_projects = np.unique(project_ids)
        project_defect_rates = []
        for p in source_projects:
            mask = project_ids == p
            project_defect_rates.append((ys[mask].sum() + 1.0) / (mask.sum() + 2.0))
        source_defect_rate = float(np.mean(project_defect_rates))

        for context in contexts:
            members = context["members"]
            represented_projects = context["projects"]
            prototype = context["prototype"]

            coverage = len(represented_projects) / len(source_projects)

            project_dispersions = []
            project_defect_tendencies = []
            project_radii = []

            for p in represented_projects:
                pmembers = members[project_ids[members] == p]
                distances = np.linalg.norm(Xs[pmembers] - prototype, axis=1)
                project_dispersions.append(float(np.mean(distances)))
                project_defect_tendencies.append(
                    float((ys[pmembers].sum() + 1.0) / (len(pmembers) + 2.0))
                )
                project_radii.append(
                    float(np.quantile(distances, self.radius_quantile))
                )

            dispersion = float(np.mean(project_dispersions))
            compactness = float(np.exp(-dispersion / (tau + self.epsilon)))

            if len(represented_projects) >= 2:
                stability_distance = float(
                    np.mean(
                        [
                            np.linalg.norm(
                                context["project_prototypes"][p] - prototype
                            )
                            for p in represented_projects
                        ]
                    )
                )
                stability = float(
                    np.exp(-stability_distance / (tau + self.epsilon))
                )
            else:
                stability = None

            context_defect_rate = float(np.mean(project_defect_tendencies))
            discriminativeness = float(
                abs(context_defect_rate - source_defect_rate)
                / (max(source_defect_rate, 1.0 - source_defect_rate) + self.epsilon)
            )

            if stability is None:
                reliability = (coverage + compactness + discriminativeness) / 3.0
            else:
                reliability = (
                    coverage + compactness + stability + discriminativeness
                ) / 4.0

            context["coverage"] = float(coverage)
            context["compactness"] = compactness
            context["stability"] = stability
            context["defect_tendency"] = context_defect_rate
            context["discriminativeness"] = discriminativeness
            context["reliability"] = float(np.clip(reliability, 0.0, 1.0))
            context["radius"] = float(np.mean(project_radii))

        target_limit = max(1, int(np.ceil(nt / max(1, len(contexts)))))
        edges = []

        for context in contexts:
            distances = np.linalg.norm(Xt - context["prototype"], axis=1)
            normalized = distances / (context["radius"] + self.epsilon)
            candidates = np.flatnonzero(normalized <= self.gamma)

            if candidates.size == 0:
                continue

            order = np.lexsort((candidates, normalized[candidates]))
            selected = candidates[order[:target_limit]]
            compatibility = float(np.exp(-np.mean(normalized[selected])))
            confidence = float(context["reliability"] * compatibility)

            edges.append(
                {
                    "layer": layer_id,
                    "context_id": context["context_id"],
                    "source_members": context["members"].copy(),
                    "target_members": selected.copy(),
                    "compatibility": compatibility,
                    "confidence": confidence,
                    "weight": 0.0,
                }
            )

        return contexts, edges

    def _normalize_layer_weights(self, layer_edges):
        if not layer_edges:
            return []

        active_layers = list(layer_edges.keys())
        layer_mass = 1.0 / len(active_layers)
        edges = []

        for layer_id in active_layers:
            current = layer_edges[layer_id]
            total_confidence = sum(edge["confidence"] for edge in current)
            denominator = total_confidence + self.epsilon
            for edge in current:
                edge = dict(edge)
                edge["weight"] = layer_mass * edge["confidence"] / denominator
                edges.append(edge)

        return edges

    def _build_incidence(self, n_nodes, ns, edges):
        if not edges:
            return sparse.csr_matrix((n_nodes, 0), dtype=float), np.empty(0), np.empty(0)

        rows = []
        cols = []

        for eidx, edge in enumerate(edges):
            source_nodes = edge["source_members"]
            target_nodes = ns + edge["target_members"]
            nodes = np.concatenate([source_nodes, target_nodes]).astype(int, copy=False)
            rows.extend(nodes.tolist())
            cols.extend([eidx] * len(nodes))

        data = np.ones(len(rows), dtype=float)
        H = sparse.coo_matrix(
            (data, (np.asarray(rows), np.asarray(cols))),
            shape=(n_nodes, len(edges)),
        ).tocsr()
        propagation_weights = np.asarray([edge["weight"] for edge in edges], dtype=float)
        intrinsic_confidences = np.asarray(
            [edge["confidence"] for edge in edges], dtype=float
        )
        return H, propagation_weights, intrinsic_confidences

    def _apply_propagation(self, X, H, edge_weights):
        if H.shape[1] == 0:
            return np.zeros_like(X)

        edge_degrees = np.asarray(H.sum(axis=0)).ravel()
        node_degrees = np.asarray(H @ edge_weights).ravel()

        inv_node_sqrt = np.zeros_like(node_degrees)
        positive_nodes = node_degrees > 0
        inv_node_sqrt[positive_nodes] = 1.0 / np.sqrt(node_degrees[positive_nodes])

        normalized_X = inv_node_sqrt[:, None] * X
        edge_messages = H.T @ normalized_X
        edge_scale = edge_weights / np.maximum(edge_degrees, self.epsilon)
        edge_messages = edge_scale[:, None] * edge_messages
        node_messages = H @ edge_messages
        return inv_node_sqrt[:, None] * node_messages

    def _propagate(self, X, H, edge_weights):
        SX = self._apply_propagation(X, H, edge_weights)
        S2X = self._apply_propagation(SX, H, edge_weights)
        return np.hstack([X, SX, S2X])

    def _classifier_weights(self, ys, ns, edges, intrinsic_confidences):
        eta = np.ones(ns, dtype=float)
        confidence_sum = np.zeros(ns, dtype=float)
        incidence_count = np.zeros(ns, dtype=float)

        for edge, confidence in zip(edges, intrinsic_confidences):
            members = edge["source_members"]
            confidence_sum[members] += confidence
            incidence_count[members] += 1.0

        mask = incidence_count > 0
        eta[mask] = 1.0 + confidence_sum[mask] / incidence_count[mask]

        class_weights = np.ones(ns, dtype=float)
        for c in (0, 1):
            count = np.sum(ys == c)
            if count > 0:
                class_weights[ys == c] = ns / (2.0 * count)

        weights = class_weights * eta
        weights /= weights.mean() + self.epsilon
        return weights
