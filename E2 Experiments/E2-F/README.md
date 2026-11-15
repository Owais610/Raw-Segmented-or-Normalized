# E2-F: Pair-conditioned Grad-CAM

The fixed selection contains 12 genuine, 12 ordinary-impostor and six high-similarity-impostor pairs per dataset, shared by all six original raw checkpoints.
High-similarity selection uses mean average-tie impostor percentile across the six models and is explicitly outcome-conditioned. Selection is fixed before maps and supplied directly as data; optional exact reconstruction code is included.
Pair cosine is differentiated through both inputs of one shared encoder in FP32. ResNet layer4 and Swin final normalization both yield native 10×10 spatial grids.
Positive Grad-CAM is L1-normalized over nonpadding content. Nonannulus includes pupil and outside-disc regions. Parameter-randomization and fixed-anchor partner controls remain in memory only.
The original saved-AMP agreement tolerance stays 0.001. The 30 unsupported primary branch maps remain disclosed and excluded from supported paired summaries; numerical replay never rescues them.
Grad-CAM does not establish causal identity reliance. Private biometric galleries can be regenerated locally but are not redistributed.

| Open | Content |
| --- | --- |
| [Notebook](E2-F.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
