# E2-C: Frozen polar C1/C2 input swap

The same frozen C1 or C2 checkpoint receives both C1 and C2 input, creating the original 2×2 design.
Diagonal scores reuse the original embeddings. Crossed cells retain the original matched-domain inference order, batch 24 and per-checkpoint AMP policy.
Exact C2-valid ⊆ C1-valid and common-valid grayscale equality are checked directly; this notebook does not depend on E2-B having run.
Input-swap sensitivity includes distribution mismatch and cannot isolate a causal eyelash effect.

| Open | Content |
| --- | --- |
| [Notebook](E2-C.ipynb) | Complete standalone implementation; editable paths at the top |
| [Report](REPORT.md) | Original findings with clearer publication navigation |
| [Results](Results/README.md) | Actual tables, statistical figures and diagnostics |
| [Method](METHOD.md) | Fixed definitions and interpretation limits |

The five datasets are independent. All three seeds are retained. No retraining or threshold fitting.
Default execution inspects the saved results. To reproduce, follow [asset setup](../../ASSETS.md), configure direct assets and enable `RUN_ANALYSIS`.
It is unnecessary to run another E2 notebook first. Required memberships, pairs and model metadata are supplied directly as data.
New outputs remain separate under a fresh `OUTPUT_ROOT`.
