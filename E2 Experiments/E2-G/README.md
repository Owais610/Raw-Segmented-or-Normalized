# E2-G: geometry-only inputs for frozen Cartesian models

Start with **[the report](REPORT.md)**. Twelve original E1-B1/B2 best checkpoints (two architectures × three seeds) receive their own white-on-black support masks, with all grayscale iris texture removed.

| Open | Content |
| --- | --- |
| [Notebook](E2-G.ipynb) | Complete standalone implementation; all imports and editable paths at the top |
| [Report](REPORT.md) | Findings and compact numerical overview |
| [Results](Results/README.md) | Every seed, mean/sample SD, paired effects, subject diagnostics and plots |
| [Method](METHOD.md) | Fixed input/pair definitions and interpretation limits |

The same E2-A matched membership and exhaustive verification pairs are reused independently within CUST-Iris, CASIA-Interval, IITD, AMF and UTIRIS NIR. No training, new subject assignments or test-threshold selection.

Default notebook execution only defines the implementation, runs synthetic checks and displays the actual recorded results. Configure [private assets](../../ASSETS.md), then enable `RUN_ANALYSIS` explicitly to reproduce. A saved E2-G embedding cache can be supplied directly, or explicitly recomputed with the original best checkpoint; no preceding notebook is required. New outputs go to a fresh `OUTPUT_ROOT` and never overwrite recorded records.
