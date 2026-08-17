# MVICH: Multi-View Invariant Context Hypergraph Learning for Cross-Project Defect Prediction

This repository provides the replication package for MVICH, a
multi-source cross-project defect prediction framework that discovers
project-balanced local contexts, evaluates their transferability from
complementary semantic metric views and the complete metric space, and
represents supported source--target contexts using a weighted context
hypergraph.

The replication package contains the datasets and the MVICH implementation.
This README provides dataset details, metric definitions, semantic metric-view
mappings, implementation and parameter settings, and the complete RQ1
experimental results reported in the study.

# Details of Datasets
1 ReLink dataset :"Wu, Rongxin, et al. "Relink: recovering links between bugs and changes." Proceedings of the 19th ACM SIGSOFT symposium and the 13th European conference on Foundations of software engineering. 2011".


2 AEEEM dataset :"D’Ambros, Marco, Michele Lanza, and Romain Robbes. "Evaluating defect prediction approaches: a benchmark and an extensive comparison." Empirical Software Engineering 17 (2012): 531-577".


3 JIRA dataset :"Yatish, Suraj, et al. "Mining software defects: Should we consider affected releases?." 2019 IEEE/ACM 41st international conference on software engineering (ICSE). IEEE, 2019".

4 Y. Kamei, E. Shihab, B. Adams, A. E. Hassan, A. Mockus, A. Sinha, N. Ubayashi, A large-scale empirical study of just-in-time quality assurance, IEEE Transactions on Software Engineering 39 (6) (2012) 757–773.

5 L. Song, L. L. Minku, A procedure to continuously evaluate predictive performance of just-in-time software defect prediction models during software development, IEEE Transactions on Software Engineering 49 (2) (2022) 646–666.


# Metrics Details of ReLink Dataset
| **Abbreviation**      | **Description**                                                |
| --------------------- | -------------------------------------------------------------- |
| AvgCyclomatic         | Average Cyclomatic Complexity                                  |
| AvgCyclomaticModified | Average Modified Cyclomatic Complexity                         |
| AvgCyclomaticStrict   | Average Strict Cyclomatic Complexity                           |
| AvgEssential          | Average Essential Complexity                                   |
| AvgLine               | Average Lines                                                  |
| AvgLineBlank          | Average Blank Lines                                            |
| AvgLineCode           | Average Code Lines                                             |
| AvgLineComment        | Average Comment Lines                                          |
| CountLine             | Number of Lines                                                |
| CountLineBlank        | Number of Blank Lines                                          |
| CountLineCode         | Number of Code Lines                                           |
| CountLineCodeDecl     | Number of Declarative Code Lines                               |
| CountLineCodeExe      | Number of Executable Code Lines                                |
| CountLineComment      | Number of Comment Lines                                        |
| CountSemicolon        | Number of Semicolons                                           |
| CountStmt             | Number of Statements                                           |
| CountStmtDecl         | Number of Declarative Statements                               |
| CountStmtExe          | Number of Executive Statements                                 |
| MaxCyclomatic         | Maximum Cyclomatic Complexity of all nested functions          |
| MaxCyclomaticModified | Maximum Modified Cyclomatic Complexity of all nested functions |
| MaxCyclomaticStrict   | Maximum Strict Cyclomatic Complexity of all nested functions   |
| RatioCommentToCode    | Ratio of Comment Lines to Code Lines                           |
| SumCyclomatic         | Sum of Cyclomatic Complexity of all nested functions           |
| SumCyclomaticModified | Sum of Modified Cyclomatic Complexity of all nested functions  |
| SumCyclomaticStrict   | Sum of Strict Cyclomatic Complexity of all nested functions    |
| SumEssential          | Sum of Essential Complexity of all nested functions            |

# Metrics Details of AEEEM Dataset
| **Abbreviation**                   | **Description**                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| ck\_oo\_wmc                        | Weighted method count                                                              |
| ck\_oo\_dit                        | Depth of inheritance tree                                                          |
| ck\_oo\_rfc                        | Response for class                                                                 |
| ck\_oo\_noc                        | Number of children                                                                 |
| ck\_oo\_cbo                        | Coupling between objects                                                           |
| ck\_oo\_lcom                       | Lack of cohesion in methods                                                        |
| ck\_oo\_fanin                      | Number of other classes that reference the class                                   |
| ck\_oo\_fanout                     | Number of other classes referenced by the class                                    |
| ck\_oo\_noa                        | Number of attributes                                                               |
| ck\_oo\_nopa                       | Number of public attributes                                                        |
| ck\_oo\_nopra                      | Number of private attributes                                                       |
| ck\_oo\_noai                       | Number of attributes inherited                                                     |
| ck\_oo\_loc                        | Number of lines of code                                                            |
| ck\_oo\_nom                        | Number of methods                                                                  |
| ck\_oo\_nopm                       | Number of public methods                                                           |
| ck\_oo\_noprm                      | Number of private methods                                                          |
| ck\_oo\_nomt                       | Number of methods inherited                                                        |
| WCHU\_wmc                          | Weighted churn of weighted method count                                            |
| WCHU\_dit                          | Weighted churn of depth of inheritance tree                                        |
| WCHU\_rfc                          | Weighted churn of response for class                                               |
| WCHU\_noc                          | Weighted churn of number of children                                               |
| WCHU\_cbo                          | Weighted churn of coupling between objects                                         |
| WCHU\_lcom                         | Weighted churn of lack of cohesion in methods                                      |
| WCHU\_fanin                        | Weighted churn of number of other classes that reference the class                 |
| WCHU\_fanout                       | Weighted churn of number of other classes referenced by the class                  |
| WCHU\_noa                          | Weighted churn of number of attributes                                             |
| WCHU\_nopa                         | Weighted churn of number of public attributes                                      |
| WCHU\_nopra                        | Weighted churn of number of private attributes                                     |
| WCHU\_noai                         | Weighted churn of number of attributes inherited                                   |
| WCHU\_loc                          | Weighted churn of number of lines of code                                          |
| WCHU\_nom                          | Weighted churn of number of methods                                                |
| WCHU\_nopm                         | Weighted churn of number of public methods                                         |
| WCHU\_noprm                        | Weighted churn of number of private methods                                        |
| WCHU\_nomt                         | Weighted churn of number of methods inherited                                      |
| LDHH\_wmc                          | Linear decayed history entropy of weighted method count                            |
| LDHH\_dit                          | Linear decayed history entropy of depth of inheritance tree                        |
| LDHH\_rfc                          | Linear decayed history entropy of response for class                               |
| LDHH\_noc                          | Linear decayed history entropy of number of children                               |
| LDHH\_cbo                          | Linear decayed history entropy of coupling between objects                         |
| LDHH\_lcom                         | Linear decayed history entropy of lack of cohesion in methods                      |
| LDHH\_fanin                        | Linear decayed history entropy of number of other classes that reference the class |
| LDHH\_fanout                       | Linear decayed history entropy of number of other classes referenced by the class  |
| LDHH\_noa                          | Linear decayed history entropy of number of attributes                             |
| LDHH\_nopa                         | Linear decayed history entropy of number of public attributes                      |
| LDHH\_nopra                        | Linear decayed history entropy of number of private attributes                     |
| LDHH\_noai                         | Linear decayed history entropy of number of attributes inherited                   |
| LDHH\_loc                          | Linear decayed history entropy of number of lines of code                          |
| LDHH\_nom                          | Linear decayed history entropy of number of methods                                |
| LDHH\_nopm                         | Linear decayed history entropy of number of public methods                         |
| LDHH\_noprm                        | Linear decayed history entropy of number of private methods                        |
| LDHH\_nomt                         | Linear decayed history entropy of number of methods inherited                      |
| CvsEntropy                         | Entropy of CVS change log                                                          |
| CvsWEntropy                        | Weighted Entropy of CVS change log                                                 |
| CvsLogEntropy                      | Logarithmic Entropy of CVS change log                                              |
| CvsExpEntropy                      | Exponential Entropy of CVS change log                                              |
| CvsLinEntropy                      | Linear Entropy of CVS change log                                                   |
| numberOfNonTrivialBugsFoundUntil   | Number of non-trivial bugs found until the corresponding fix                       |
| numberOfCriticalBugsFoundUntil     | Number of critical bugs found until the corresponding fix                          |
| numberOfHighPriorityBugsFoundUntil | Number of high priority bugs found until the corresponding fix                     |
| numberOfMajorBugsFoundUntil        | Number of major bugs found until the corresponding fix                             |
| numberOfBugsFoundUntil             | Number of bugs found until the corresponding fix                                   |

# Metrics Details of JIRA Dataset
| **Abbreviation**          | **Description**                                                            |
| ------------------------- | -------------------------------------------------------------------------- |
| AvgCyclomatic             | Average cyclomatic complexity for all nested functions or methods          |
| SumCyclomatic             | Sum of cyclomatic complexity of all nested functions or methods            |
| AvgCyclomaticModified     | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified     | Sum of modified cyclomatic complexity of all nested functions              |
| AvgCyclomaticStrict       | Average strict cyclomatic complexity for all nested functions or methods   |
| SumCyclomaticStrict       | Sum of strict cyclomatic complexity of all nested functions or methods     |
| AvgEssential              | Average essential complexity for all nested functions or methods           |
| SumEssential              | Sum of essential complexity of all nested functions or methods             |
| AvgLine                   | Average number of lines for all nested functions or methods                |
| AvgLineBlank              | Average number of blank lines for all nested functions or methods          |
| AvgLineCode               | Average number of lines containing source code for all nested functions    |
| AvgLineComment            | Average number of comment lines for all nested functions or methods        |
| CountClassBase            | Number of immediate base classes                                           |
| CountClassCoupled         | Number of other classes coupled to                                         |
| CountClassDerived         | Number of immediate subclasses                                             |
| MaxInheritanceTree        | Maximum depth of class in inheritance tree                                 |
| PercentLackOfCohesion     | 100% minus the average cohesion for package entities                       |
| CountDeclClass            | Number of classes                                                          |
| CountDeclClassMethod      | Number of class methods                                                    |
| CountDeclClassVariable    | Number of class variables                                                  |
| CountDeclFunction         | Number of functions                                                        |
| CountDeclInstanceMethod   | Number of instance methods                                                 |
| CountDeclInstanceVariable | Number of instance variables                                               |
| CountDeclMethod           | Number of local (non-inherited) methods                                    |
| CountDeclMethodDefault    | Number of local default methods                                            |
| CountDeclMethodPrivate    | Number of local (non-inherited) private methods                            |
| CountDeclMethodProtected  | Number of local protected methods                                          |
| CountDeclMethodPublic     | Number of local (non-inherited) public methods                             |
| CountLine                 | Number of physical lines                                                   |
| CountLineBlank            | Number of blank lines                                                      |
| CountLineCode             | Number of lines containing source code                                     |
| CountLineCodeDecl         | Number of lines containing declarative source code                         |
| CountLineCodeExe          | Number of lines containing executable source code                          |
| CountLineComment          | Number of lines containing comment                                         |
| CountSemicolon            | Number of semicolons                                                       |
| CountStmt                 | Number of statements                                                       |
| CountStmtDecl             | Number of declarative statements                                           |
| CountStmtExe              | Number of executable statements                                            |
| MaxCyclomatic             | Maximum cyclomatic complexity of all nested functions or methods           |
| MaxCyclomaticModified     | Maximum modified cyclomatic complexity of nested functions or methods      |
| MaxCyclomaticStrict       | Maximum strict cyclomatic complexity of nested functions or methods        |
| RatioCommentToCode        | Ratio of comment lines to code lines                                       |
| CountInput\_Min           | Min number of calling subprograms plus global variables read               |
| CountInput\_Mean          | Mean number of calling subprograms plus global variables read              |
| CountInput\_Max           | Max number of calling subprograms plus global variables read               |
| CountOutput\_Min          | Min number of called subprograms plus global variables set                 |
| CountOutput\_Mean         | Mean number of called subprograms plus global variables set                |
| CountOutput\_Max          | Max number of called subprograms plus global variables set                 |
| CountPath\_Min            | Min number of unique paths through a body of code                          |
| CountPath\_Mean           | Mean number of unique paths through a body of code                         |
| CountPath\_Max            | Max number of unique paths through a body of code                          |
| MaxNesting\_Min           | Min of maximum nesting level of control constructs in the function         |
| MaxNesting\_Mean          | Mean of maximum nesting level of control constructs in the function        |
| MaxNesting\_Max           | Max of maximum nesting level of control constructs in the function         |
| COMM                      | Number of Git commits                                                      |
| ADDED\_LINES              | Normalized number of lines added to the module                             |
| DEL\_LINES                | Normalized number of lines deleted from the module                         |
| ADEV                      | Number of active developers                                                |
| DDEV                      | Number of distinct developers                                              |
| MINOR\_COMMIT             | Developers contributing <5% of total code changes                          |
| MINOR\_LINE               | Developers contributing <5% of total LOC                                   |
| MAJOR\_COMMIT             | Developers contributing >5% of total code changes                          |
| MAJOR\_LINES              | Developers contributing >5% of total LOC                                   |
| OWN\_COMMIT               | Proportion of code changes by top contributor                              |
| OWN\_LINE                 | Proportion of lines of code by top contributor                             |

# Metrics Details of GitHub-Python Dataset
| **Abbreviation** | **Description**                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| fix            | Whether or not the change is a defect fix                                     |
| ns            | Number of modified subsystems in the change                                   |
| nd             | Number of modified code directories                                           |
| nf             | Number of files modified                                                      |
| entropy        | Distribution of code changes across files, computed using information entropy |
| la             | Lines of code added                                                           |
| ld             | Lines of code deleted                                                         |
| lt             | Lines of code in a file before the change                                     |
| ndev           | Number of developers who previously modified the changed files                |
| age            | Average time interval between the last and the current change                 |
| nuc            | Number of unique prior changes to the modified files                          |
| exp            | Developer overall experience                                                  |
| rexp           | Developer recent experience                                                   |
| sexp           | Developer experience within the modified subsystem                            |


# Metrics Details of Kamei Dataset
| **Abbreviation** | **Description** |
|----------|----------------|
| NS     | Number of modified subsystems. |
| ND     | Number of modified directories. |
| NF     | Number of modified files. |
| Entropy | Distribution of modified code across each file, measuring the spread of changes. |
| LA     | Lines of code added during the change. |
| LD     | Lines of code deleted during the change. |
| LT     | Lines of code in a file before the change. |
| FIX    | Binary indicator of whether the change is a defect fix (`1`) or not (`0`). |
| NDEV   | Number of distinct developers who previously modified the affected files. |
| PD     | Average time interval between the current and previous changes to the files. |
| NPT    | Number of unique previous changes to the files. |
| EXP    | Developer’s overall experience, typically measured by number of prior commits. |
| REXP   | Developer’s recent experience, often computed with time-decay weighting. |
| SEXP   | Developer’s experience within the specific subsystem of the modified files. |



# Semantic Metric-View Mapping

MVICH represents the retained software metrics through multiple
semantically related views. The mapping is defined separately for each
dataset family according to the documented meaning of its metrics and is
fixed before model evaluation.

Each retained metric is assigned to at most one semantic view. Therefore,
the semantic views are non-overlapping. In addition to these semantic
views, MVICH constructs a full-space layer containing all retained metrics
of the corresponding dataset family.

The semantic-view mapping does not depend on feature values, defect labels,
source--target similarity, target-project information, or prediction
performance.

## ReLink

The ReLink metrics describe two main aspects of software modules:
structural complexity and code size/volume.

| **Semantic View** | **Metrics** |
| ----------------- | ----------- |
| Complexity | `AvgCyclomatic`, `AvgCyclomaticModified`, `AvgCyclomaticStrict`, `AvgEssential`, `MaxCyclomatic`, `MaxCyclomaticModified`, `MaxCyclomaticStrict`, `SumCyclomatic`, `SumCyclomaticModified`, `SumCyclomaticStrict`, `SumEssential` |
| Size / Code Volume | `AvgLine`, `AvgLineBlank`, `AvgLineCode`, `AvgLineComment`, `CountLine`, `CountLineBlank`, `CountLineCode`, `CountLineCodeDecl`, `CountLineCodeExe`, `CountLineComment`, `CountSemicolon`, `CountStmt`, `CountStmtDecl`, `CountStmtExe`, `RatioCommentToCode` |

**Number of semantic views:** 2

**Full-space layer:** all retained ReLink metrics.

---

## AEEEM

The AEEEM metrics describe structural characteristics, dependencies,
inheritance, and software evolution/history. They are organized into
four semantic views.

| **Semantic View** | **Metrics** |
| ----------------- | ----------- |
| Complexity / Size | `ck_oo_wmc`, `ck_oo_noa`, `ck_oo_nopa`, `ck_oo_nopra`, `ck_oo_loc`, `ck_oo_nom`, `ck_oo_nopm`, `ck_oo_noprm` |
| Coupling / Cohesion | `ck_oo_rfc`, `ck_oo_cbo`, `ck_oo_lcom`, `ck_oo_fanin`, `ck_oo_fanout` |
| Inheritance | `ck_oo_dit`, `ck_oo_noc`, `ck_oo_noai`, `ck_oo_nomt` |
| Evolution / History | `WCHU_wmc`, `WCHU_dit`, `WCHU_rfc`, `WCHU_noc`, `WCHU_cbo`, `WCHU_lcom`, `WCHU_fanin`, `WCHU_fanout`, `WCHU_noa`, `WCHU_nopa`, `WCHU_nopra`, `WCHU_noai`, `WCHU_loc`, `WCHU_nom`, `WCHU_nopm`, `WCHU_noprm`, `WCHU_nomt`, `LDHH_wmc`, `LDHH_dit`, `LDHH_rfc`, `LDHH_noc`, `LDHH_cbo`, `LDHH_lcom`, `LDHH_fanin`, `LDHH_fanout`, `LDHH_noa`, `LDHH_nopa`, `LDHH_nopra`, `LDHH_noai`, `LDHH_loc`, `LDHH_nom`, `LDHH_nopm`, `LDHH_noprm`, `LDHH_nomt`, `CvsEntropy`, `CvsWEntropy`, `CvsLogEntropy`, `CvsExpEntropy`, `CvsLinEntropy`, `numberOfNonTrivialBugsFoundUntil`, `numberOfCriticalBugsFoundUntil`, `numberOfHighPriorityBugsFoundUntil`, `numberOfMajorBugsFoundUntil`, `numberOfBugsFoundUntil` |

**Number of semantic views:** 4

**Full-space layer:** all retained AEEEM metrics.

---

## JIRA

The JIRA metrics cover structural complexity, dependencies,
inheritance/cohesion, software change activity, and developer
activity/ownership.

| **Semantic View** | **Metrics** |
| ----------------- | ----------- |
| Complexity / Size | `AvgCyclomatic`, `SumCyclomatic`, `AvgCyclomaticModified`, `SumCyclomaticModified`, `AvgCyclomaticStrict`, `SumCyclomaticStrict`, `AvgEssential`, `SumEssential`, `AvgLine`, `AvgLineBlank`, `AvgLineCode`, `AvgLineComment`, `CountDeclClass`, `CountDeclClassMethod`, `CountDeclClassVariable`, `CountDeclFunction`, `CountDeclInstanceMethod`, `CountDeclInstanceVariable`, `CountDeclMethod`, `CountDeclMethodDefault`, `CountDeclMethodPrivate`, `CountDeclMethodProtected`, `CountDeclMethodPublic`, `CountLine`, `CountLineBlank`, `CountLineCode`, `CountLineCodeDecl`, `CountLineCodeExe`, `CountLineComment`, `CountSemicolon`, `CountStmt`, `CountStmtDecl`, `CountStmtExe`, `MaxCyclomatic`, `MaxCyclomaticModified`, `MaxCyclomaticStrict`, `RatioCommentToCode`, `CountPath_Min`, `CountPath_Mean`, `CountPath_Max`, `MaxNesting_Min`, `MaxNesting_Mean`, `MaxNesting_Max` |
| Coupling / Dependency | `CountClassCoupled`, `CountInput_Min`, `CountInput_Mean`, `CountInput_Max`, `CountOutput_Min`, `CountOutput_Mean`, `CountOutput_Max` |
| Inheritance / Cohesion | `CountClassBase`, `CountClassDerived`, `MaxInheritanceTree`, `PercentLackOfCohesion` |
| Change Activity | `COMM`, `ADDED_LINES`, `DEL_LINES` |
| Developer Activity / Ownership | `ADEV`, `DDEV`, `MINOR_COMMIT`, `MINOR_LINE`, `MAJOR_COMMIT`, `MAJOR_LINES`, `OWN_COMMIT`, `OWN_LINE` |

**Number of semantic views:** 5

**Full-space layer:** all retained JIRA metrics.

---

## GitHub

The GitHub metrics describe change diffusion, change size, and
development history/developer experience.

| **Semantic View** | **Metrics** |
| ----------------- | ----------- |
| Change Diffusion | `ns`, `nd`, `nf`, `entropy` |
| Change Size | `la`, `ld`, `lt` |
| Development History / Experience | `fix`, `ndev`, `age`, `nuc`, `exp`, `rexp`, `sexp` |

**Number of semantic views:** 3

**Full-space layer:** all retained GitHub metrics.

---

## Kamei

The Kamei metrics describe change diffusion, change size, and
development history/developer experience.

| **Semantic View** | **Metrics** |
| ----------------- | ----------- |
| Change Diffusion | `NS`, `ND`, `NF`, `Entropy` |
| Change Size | `LA`, `LD`, `LT` |
| Development History / Experience | `FIX`, `NDEV`, `PD`, `NPT`, `EXP`, `REXP`, `SEXP` |

**Number of semantic views:** 3

**Full-space layer:** all retained Kamei metrics.

---

## Summary of Metric Views

| **Dataset Family** | **Semantic Views** | **No. of Semantic Views** | **Full-Space Layer** |
| ------------------ | ------------------ | -------------------------: | :------------------: |
| ReLink | Complexity; Size / Code Volume | 2 | Yes |
| AEEEM | Complexity / Size; Coupling / Cohesion; Inheritance; Evolution / History | 4 | Yes |
| JIRA | Complexity / Size; Coupling / Dependency; Inheritance / Cohesion; Change Activity; Developer Activity / Ownership | 5 | Yes |
| GitHub | Change Diffusion; Change Size; Development History / Experience | 3 | Yes |
| Kamei | Change Diffusion; Change Size; Development History / Experience | 3 | Yes |

The full-space layer is not treated as another semantic view. It contains
all retained metrics and complements the view-specific layers by capturing
relationships that depend on interactions between metrics belonging to
different semantic groups.

The semantic-view mapping remains unchanged across all
leave-one-project-out target folds within a dataset family.


# Implementation Details and Main Hyperparameters

The following table summarizes the main implementation settings and
hyperparameters used for MVICH. The same configuration is used across all
target projects unless otherwise specified.

| **Component** | **Setting / Hyperparameter** | **Value / Configuration** |
|---|---|---|
| Evaluation protocol | Source--target construction | Leave-one-project-out (LOPO) within each dataset family |
| Target information | Target labels | Withheld throughout model construction; used only for final evaluation |
| Missing values | Imputation | Estimated using source-project data only |
| Feature scaling | Scaling strategy | Project-balanced robust scaling using source-derived weighted median and IQR |
| Data balancing | Synthetic oversampling | None |
| Metric representation | Semantic views | Predefined, non-overlapping metric groups for each dataset family |
| Metric representation | Full-space layer | All retained metrics |
| Context discovery | Clustering algorithm | Project-balanced weighted K-means |
| Context discovery | Clustering data | Genuine source modules only |
| Number of contexts | Context count | Logarithmic size-adaptive rule defined in the MVICH methodology |
| Context prototype | Source contribution | Project-balanced |
| Context reliability | Reliability score | \(q_C\), combining source coverage, compactness, stability, and discriminativeness |
| Source-supported range | Context radius | Project-balanced 90th percentile of source-module distances from the context prototype |
| Target compatibility | Compatibility coefficient | \(\gamma = 1\) |
| Target compatibility | Compatibility rule | Target module distance must lie within the estimated source-supported context radius |
| Target neighborhood | \(k_t^v\) | \(\max\left(1,\left\lceil n_t / |\mathcal{C}_v|\right\rceil\right)\) |
| Hyperedge construction | Hyperedge | Complete source context + compatible target modules |
| Hyperedge confidence | \(c_e\) | \(q_C a_C^v\) |
| Layer contribution | \(\lambda_v\) | \(1/|\mathcal{L}^{+}|\) for each active layer |
| Hypergraph propagation | Propagation operator | Normalized incidence-based hypergraph propagation |
| Hypergraph propagation | Number of propagation steps | 2 |
| Final representation | Context-enhanced representation | \(Z=[X,SX,S^2X]\) |
| Source weighting | Context weight | \(\eta_i = 1 + \frac{\sum_{e\in E(i)} c_e}{\max(1,|E(i)|)}\) |
| Class weighting | Class weight | \(b_i = \frac{n_s}{2n_{y_i}}\) |
| Final training weight | \(\omega_i\) | \(b_i\eta_i\), normalized to unit mean |
| Classifier | Prediction model | Gradient Boosting classifier |
| Classifier settings | Hyperparameters | Default scikit-learn Gradient Boosting settings |
| Decision threshold | Threshold selection | Determined from source-only out-of-fold predictions |
| Target prediction | Threshold use | Source-derived threshold applied unchanged to target probabilities |
| Repeated experiments | Number of runs | 30 random seeds per target project |
| Randomization control | Seed sequence | Same seed sequence used across MVICH and controlled variants |
| Reported performance | Final project-level result | Mean performance over the 30 runs |



# RQ1: Comparison with Representative CPDP Methods

**RQ1: How effective is MVICH compared with representative cross-project defect prediction methods?**

MVICH is compared with six representative CPDP methods: **CFPS, DSSDPP,
ARRAY, SSE, MASTER, and FEDL**. All methods are evaluated under the same
evaluation protocol.

The following tables provide the complete project-level results for
**AUC, MCC, and G-Mean** across the 23 target projects.

All project-level values are reported to two decimal places, consistent
with the results reported in the paper.

## AUC Results

| Target Project | MVICH | CFPS | DSSDPP | ARRAY | SSE | MASTER | FEDL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Equinox | 0.74 | 0.69 | 0.64 | 0.72 | 0.62 | 0.73 | 0.63 |
| Jdt | 0.80 | 0.77 | 0.71 | 0.78 | 0.64 | 0.77 | 0.71 |
| Lucene | 0.75 | 0.72 | 0.67 | 0.73 | 0.71 | 0.72 | 0.74 |
| Mylyn | 0.75 | 0.69 | 0.62 | 0.71 | 0.66 | 0.68 | 0.63 |
| Pde | 0.74 | 0.67 | 0.62 | 0.71 | 0.64 | 0.70 | 0.68 |
| Corefx | 0.70 | 0.66 | 0.53 | 0.66 | 0.62 | 0.69 | 0.62 |
| Django | 0.77 | 0.70 | 0.56 | 0.71 | 0.70 | 0.73 | 0.66 |
| Nova | 0.76 | 0.66 | 0.60 | 0.71 | 0.67 | 0.73 | 0.62 |
| Activemq-5.0.0 | 0.83 | 0.79 | 0.80 | 0.78 | 0.78 | 0.81 | 0.82 |
| Camel-2.10.0 | 0.82 | 0.77 | 0.75 | 0.80 | 0.79 | 0.81 | 0.79 |
| Derby-10.2.1.6 | 0.76 | 0.80 | 0.70 | 0.77 | 0.69 | 0.78 | 0.78 |
| Groovy-1_5_7 | 0.85 | 0.84 | 0.73 | 0.80 | 0.82 | 0.80 | 0.84 |
| Hbase-0.94.0 | 0.87 | 0.85 | 0.64 | 0.76 | 0.70 | 0.79 | 0.82 |
| Hive-0.10.0 | 0.89 | 0.83 | 0.68 | 0.80 | 0.78 | 0.82 | 0.83 |
| Jruby-1.1 | 0.90 | 0.89 | 0.81 | 0.83 | 0.79 | 0.88 | 0.89 |
| Lucene-2.3.0 | 0.86 | 0.79 | 0.74 | 0.73 | 0.67 | 0.70 | 0.85 |
| Wicket-1.3.0.a-1 | 0.85 | 0.73 | 0.81 | 0.83 | 0.77 | 0.85 | 0.75 |
| Bugzilla | 0.73 | 0.70 | 0.59 | 0.69 | 0.64 | 0.63 | 0.72 |
| Columba | 0.73 | 0.73 | 0.63 | 0.70 | 0.65 | 0.71 | 0.72 |
| Postgres | 0.76 | 0.76 | 0.66 | 0.74 | 0.65 | 0.76 | 0.74 |
| Apache | 0.68 | 0.73 | 0.66 | 0.71 | 0.68 | 0.69 | 0.74 |
| Safe | 0.81 | 0.80 | 0.69 | 0.80 | 0.62 | 0.78 | 0.72 |
| Zxing | 0.64 | 0.62 | 0.59 | 0.62 | 0.58 | 0.63 | 0.56 |
| **Average** | **0.78** | 0.75 | 0.67 | 0.74 | 0.69 | 0.75 | 0.73 |

### AUC Summary

| Method | Average AUC | Improvement of MVICH | W/T/L (MVICH vs Method) | Average Rank |
|---|---:|---:|:---:|---:|
| **MVICH** | **0.78** | – | – | **1.46** |
| CFPS | 0.75 | 4.00% | 19/2/2 | 3.43 |
| DSSDPP | 0.67 | 16.42% | 23/0/0 | 6.20 |
| ARRAY | 0.74 | 5.41% | 21/0/2 | 3.74 |
| SSE | 0.69 | 13.04% | 22/1/0 | 5.85 |
| MASTER | 0.75 | 4.00% | 19/2/2 | 3.37 |
| FEDL | 0.73 | 6.85% | 21/0/2 | 3.96 |

---

## MCC Results

| Target Project | MVICH | CFPS | DSSDPP | ARRAY | SSE | MASTER | FEDL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Equinox | 0.29 | 0.18 | 0.29 | 0.32 | 0.26 | 0.17 | 0.22 |
| Jdt | 0.31 | 0.29 | 0.28 | 0.26 | 0.21 | 0.29 | 0.23 |
| Lucene | 0.35 | 0.25 | 0.24 | 0.24 | 0.25 | 0.36 | 0.30 |
| Mylyn | 0.26 | 0.20 | 0.21 | 0.20 | 0.17 | 0.15 | 0.18 |
| Pde | 0.27 | 0.21 | 0.17 | 0.21 | 0.19 | 0.20 | 0.16 |
| Corefx | 0.13 | 0.12 | 0.03 | 0.11 | 0.11 | 0.11 | 0.09 |
| Django | 0.37 | 0.28 | 0.10 | 0.36 | 0.33 | 0.10 | 0.19 |
| Nova | 0.34 | 0.13 | 0.18 | 0.31 | 0.27 | 0.11 | 0.10 |
| Activemq-5.0.0 | 0.41 | 0.30 | 0.46 | 0.32 | 0.39 | 0.38 | 0.29 |
| Camel-2.10.0 | 0.27 | 0.20 | 0.25 | 0.17 | 0.21 | 0.26 | 0.20 |
| Derby-10.2.1.6 | 0.37 | 0.36 | 0.45 | 0.37 | 0.34 | 0.35 | 0.35 |
| Groovy-1_5_7 | 0.39 | 0.37 | 0.27 | 0.15 | 0.27 | 0.35 | 0.38 |
| Hbase-0.94.0 | 0.51 | 0.49 | 0.36 | 0.34 | 0.31 | 0.35 | 0.41 |
| Hive-0.10.0 | 0.45 | 0.38 | 0.37 | 0.29 | 0.36 | 0.34 | 0.39 |
| Jruby-1.1 | 0.46 | 0.49 | 0.47 | 0.34 | 0.37 | 0.53 | 0.46 |
| Lucene-2.3.0 | 0.47 | 0.32 | 0.44 | 0.30 | 0.19 | 0.17 | 0.25 |
| Wicket-1.3.0.a-1 | 0.28 | 0.17 | 0.35 | 0.22 | 0.24 | 0.27 | 0.24 |
| Bugzilla | 0.29 | 0.22 | 0.18 | 0.27 | 0.24 | -0.01 | 0.14 |
| Columba | 0.31 | 0.24 | 0.24 | 0.28 | 0.24 | 0.24 | 0.27 |
| Postgres | 0.30 | 0.26 | 0.29 | 0.34 | 0.21 | 0.32 | 0.32 |
| Apache | 0.23 | 0.45 | 0.33 | 0.43 | 0.44 | 0.38 | 0.19 |
| Safe | 0.48 | 0.45 | 0.36 | 0.46 | 0.21 | 0.47 | 0.33 |
| Zxing | 0.15 | 0.13 | 0.13 | 0.14 | 0.09 | 0.14 | 0.12 |
| **Average** | **0.33** | 0.28 | 0.28 | 0.28 | 0.26 | 0.26 | 0.25 |

### MCC Summary

| Method | Average MCC | Improvement of MVICH | W/T/L (MVICH vs Method) | Average Rank |
|---|---:|---:|:---:|---:|
| **MVICH** | **0.33** | – | – | **1.76** |
| CFPS | 0.28 | 17.86% | 21/0/2 | 3.93 |
| DSSDPP | 0.28 | 17.86% | 17/1/5 | 4.07 |
| ARRAY | 0.28 | 17.86% | 19/1/3 | 3.98 |
| SSE | 0.26 | 26.92% | 22/0/1 | 5.04 |
| MASTER | 0.26 | 26.92% | 19/0/4 | 4.28 |
| FEDL | 0.25 | 32.00% | 21/1/1 | 4.93 |

---

## G-Mean Results

| Target Project | MVICH | CFPS | DSSDPP | ARRAY | SSE | MASTER | FEDL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Equinox | 0.60 | 0.26 | 0.59 | 0.63 | 0.62 | 0.39 | 0.49 |
| Jdt | 0.69 | 0.66 | 0.68 | 0.64 | 0.55 | 0.71 | 0.52 |
| Lucene | 0.67 | 0.34 | 0.65 | 0.66 | 0.69 | 0.54 | 0.31 |
| Mylyn | 0.66 | 0.36 | 0.55 | 0.63 | 0.54 | 0.32 | 0.54 |
| Pde | 0.67 | 0.44 | 0.59 | 0.63 | 0.61 | 0.49 | 0.29 |
| Corefx | 0.63 | 0.60 | 0.36 | 0.60 | 0.58 | 0.64 | 0.58 |
| Django | 0.69 | 0.54 | 0.49 | 0.66 | 0.66 | 0.24 | 0.37 |
| Nova | 0.64 | 0.34 | 0.56 | 0.64 | 0.64 | 0.24 | 0.30 |
| Activemq-5.0.0 | 0.75 | 0.38 | 0.80 | 0.69 | 0.75 | 0.53 | 0.35 |
| Camel-2.10.0 | 0.67 | 0.48 | 0.74 | 0.71 | 0.69 | 0.51 | 0.45 |
| Derby-10.2.1.6 | 0.70 | 0.48 | 0.64 | 0.67 | 0.65 | 0.61 | 0.52 |
| Groovy-1_5_7 | 0.83 | 0.74 | 0.71 | 0.67 | 0.84 | 0.80 | 0.67 |
| Hbase-0.94.0 | 0.81 | 0.78 | 0.56 | 0.67 | 0.64 | 0.69 | 0.66 |
| Hive-0.10.0 | 0.75 | 0.58 | 0.63 | 0.69 | 0.74 | 0.66 | 0.58 |
| Jruby-1.1 | 0.82 | 0.80 | 0.81 | 0.72 | 0.77 | 0.80 | 0.76 |
| Lucene-2.3.0 | 0.69 | 0.40 | 0.72 | 0.65 | 0.61 | 0.45 | 0.32 |
| Wicket-1.3.0.a-1 | 0.77 | 0.67 | 0.81 | 0.69 | 0.73 | 0.54 | 0.64 |
| Bugzilla | 0.60 | 0.41 | 0.53 | 0.62 | 0.52 | 0.12 | 0.30 |
| Columba | 0.67 | 0.62 | 0.61 | 0.62 | 0.61 | 0.52 | 0.57 |
| Postgres | 0.68 | 0.48 | 0.64 | 0.67 | 0.62 | 0.53 | 0.65 |
| Apache | 0.61 | 0.73 | 0.62 | 0.69 | 0.63 | 0.69 | 0.55 |
| Safe | 0.71 | 0.65 | 0.69 | 0.70 | 0.60 | 0.69 | 0.63 |
| Zxing | 0.56 | 0.49 | 0.53 | 0.53 | 0.45 | 0.43 | 0.43 |
| **Average** | **0.69** | 0.53 | 0.63 | 0.66 | 0.64 | 0.53 | 0.50 |

MVICH achieves the highest average G-Mean of **0.69**. ARRAY is the
strongest competing method with an average G-Mean of **0.66**, corresponding
to an improvement of **4.55%** for MVICH. MVICH obtains the best G-Mean
average rank of **1.85**.

---

## Statistical Comparison

The Friedman test is first applied across all seven methods. Pairwise
Wilcoxon signed-rank tests are subsequently performed between MVICH and
each competing method, with Benjamini–Hochberg correction for multiple
comparisons.

### Friedman Test

| Metric | Friedman χ² | p-value |
|---|---:|---:|
| AUC | 77.74 | 1.05 × 10⁻¹⁴ |
| MCC | 35.68 | 3.18 × 10⁻⁶ |
| G-Mean | 58.11 | 1.09 × 10⁻¹⁰ |

The Friedman test indicates statistically significant differences among
the seven evaluated methods for all three performance measures.

### Pairwise Wilcoxon and Vargha–Delaney Effect-Size Results

| Comparison | AUC: A12-Magnitude (pBH) | MCC: A12-Magnitude (pBH) | G-Mean: A12-Magnitude (pBH) |
|---|---|---|---|
| MVICH vs CFPS | 0.64-M (1.37 × 10⁻³) | 0.65-M (2.14 × 10⁻³) | 0.81-L (2.10 × 10⁻⁴) |
| MVICH vs DSSDPP | 0.86-L (1.18 × 10⁻⁴) | 0.64-M (7.02 × 10⁻³) | 0.68-M (6.02 × 10⁻³) |
| MVICH vs ARRAY | 0.67-M (2.30 × 10⁻⁴) | 0.65-M (4.62 × 10⁻³) | 0.64-M (6.02 × 10⁻³) |
| MVICH vs SSE | 0.81-L (1.18 × 10⁻⁴) | 0.74-L (1.12 × 10⁻³) | 0.68-M (1.26 × 10⁻³) |
| MVICH vs MASTER | 0.65-M (3.37 × 10⁻⁴) | 0.65-M (4.62 × 10⁻³) | 0.79-L (2.10 × 10⁻⁴) |
| MVICH vs FEDL | 0.68-M (4.26 × 10⁻⁴) | 0.71-L (3.40 × 10⁻⁴) | 0.90-L (1.62 × 10⁻⁴) |

**M:** Medium effect size  
**L:** Large effect size  
**pBH:** Benjamini–Hochberg adjusted p-value

All pairwise comparisons remain statistically significant after
Benjamini–Hochberg correction at α = 0.05.

Overall, MVICH achieves the most favorable average performance across
AUC, MCC, and G-Mean among the evaluated methods.
