# E2-B: Image quality and eyelash-mask footprints

Native quality measurements include the original evaluation inventory, including geometry failures as missing measurements.
Recognition associations in this publication view use the common matched population only. Radius/center/segmentation proxies, invalid-neighbor-eroded texture measures, four radial/eight angular mask bins and minimum eight-subject Spearman rules are unchanged.
Subject summaries are descriptive; dependent captures, segmentation error and acquisition differences do not establish a mechanism.

| Open | Content |
| --- | --- |
| [Notebook](E2-B.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
