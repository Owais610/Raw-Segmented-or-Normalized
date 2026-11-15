# E2-E: Raw-trained iris-only and complementary inputs

Original E1-A checkpoints only; A→A, existing B1/B2 black-fill inputs, predefined mean-fill versions and black/mean complementary inputs.
All conditions use the identical common image/pair population. Complementary support removes the iris annulus but retains the pupil and other ocular information; it is not strictly periocular-only.
The full Cartesian coordinate and pixel checks quantify interpolation footprints rather than assuming that native texture differs only by masking.
Degradation is not proof of periocular identity reliance; preservation means sufficiency under the tested intervention.

| Open | Content |
| --- | --- |
| [Notebook](E2-E.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
