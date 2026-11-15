# E2-A: Matched architecture–representation verification

All 30 validation-selected models, all five independent datasets, identical common images and exhaustive genuine/different-subject impostor pairs within each dataset.
The optional opposite-eye diagnostic stays separate. All three seeds are reported; no pooled-domain ROC or favorable-seed selection.
Saved original full-population embeddings are scored only on the published matched pairs. If recomputing inference, retain the original full inference order and batch size before filtering.

| Open | Content |
| --- | --- |
| [Notebook](E2-A.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
