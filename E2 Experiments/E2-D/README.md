# E2-D: Matched-area iris/periocular partial occlusion

Original E1-A models only. Equal-shape/equal-area disks replace pixels with the frozen training mean at 5% and 10% of segmented annulus area, on image-coordinate left/right sides.
Both paired disks share center y; all eight variants must fit completely inside their respective guarded ROIs. No relaxed placement or fallback.
This analysis has its original **matched feasible-occlusion cohort**, shared across its baseline and every variant, distinct from the all-five-representation common cohort. Frozen membership/pairs are provided directly; no other notebook must run.
Different texture energy, spatial position, segmentation and feasibility selection limit interpretation.

| Open | Content |
| --- | --- |
| [Notebook](E2-D.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
