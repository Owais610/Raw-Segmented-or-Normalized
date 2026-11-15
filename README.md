# Raw, Segmented, or Normalized?

Reproducibility package for an iris-verification study of how **architecture and input representation interact**.
We compare **ResNet-18** and **SwinV2-Tiny** using raw ocular images, Cartesian iris segmentation and native rubber-sheet normalization, with and without predicted eyelashes.
The question is which information supports verification and how each architecture responds when available image information changes.

**Start with the [matched-population results](E2%20Experiments/E2-A/REPORT.md).**
All five representations share the same eligible images and exhaustive verification pairs within each dataset. All three seeds—42, 123 and 2025—are retained. The paper results use this single comparison protocol.

## Find an experiment

| Condition | Input | ResNet-18 | SwinV2-Tiny |
| --- | --- | --- | --- |
| E1-A | Raw ocular frame | [Notebook](ResNet-18/Training%20Codes/E1-A_Raw_Ocular.ipynb) | [Notebook](SwinV2-Tiny/Training%20Codes/E1-A_Raw_Ocular.ipynb) |
| E1-B1 | Cartesian iris annulus; eyelashes retained | [Notebook](ResNet-18/Training%20Codes/E1-B1_Cartesian_Unmasked.ipynb) | [Notebook](SwinV2-Tiny/Training%20Codes/E1-B1_Cartesian_Unmasked.ipynb) |
| E1-B2 | Cartesian iris annulus; predicted eyelashes masked | [Notebook](ResNet-18/Training%20Codes/E1-B2_Cartesian_Masked.ipynb) | [Notebook](SwinV2-Tiny/Training%20Codes/E1-B2_Cartesian_Masked.ipynb) |
| E1-C1 | Pure-V2 polar iris; eyelashes retained | [Notebook](ResNet-18/Training%20Codes/E1-C1_Polar_Unmasked.ipynb) | [Notebook](SwinV2-Tiny/Training%20Codes/E1-C1_Polar_Unmasked.ipynb) |
| E1-C2 | Pure-V2 polar iris; predicted eyelashes masked | [Notebook](ResNet-18/Training%20Codes/E1-C2_Polar_Masked.ipynb) | [Notebook](SwinV2-Tiny/Training%20Codes/E1-C2_Polar_Masked.ipynb) |

Each notebook contains its own input pipeline, model, losses, sampler, training and validation loops. No project-module imports or notebook execution order are required.
Original completed run records are in [ResNet-18 histories](ResNet-18/Training%20Histories) and [SwinV2-Tiny histories](SwinV2-Tiny/Training%20Histories); each has all 15 runs, per-epoch JSONL, curves, validation metrics and frozen scientific settings.
Per-condition **matched** results are also linked from each architecture README. Learned checkpoints are external assets, with selected epochs listed in [Assets/checkpoints.json](Assets/checkpoints.json).

## Explanatory experiments

| Stage | Question | Code | Findings | Saved outputs |
| --- | --- | --- | --- | --- |
| E2-A | Matched architecture–representation verification | [Notebook](E2%20Experiments/E2-A/E2-A.ipynb) | [Report](E2%20Experiments/E2-A/REPORT.md) | [Tables / figures](E2%20Experiments/E2-A/Results) |
| E2-B | Image quality and eyelash-mask footprints | [Notebook](E2%20Experiments/E2-B/E2-B.ipynb) | [Report](E2%20Experiments/E2-B/REPORT.md) | [Tables / figures](E2%20Experiments/E2-B/Results) |
| E2-C | Frozen polar C1/C2 input swap | [Notebook](E2%20Experiments/E2-C/E2-C.ipynb) | [Report](E2%20Experiments/E2-C/REPORT.md) | [Tables / figures](E2%20Experiments/E2-C/Results) |
| E2-D | Matched-area iris/periocular partial occlusion | [Notebook](E2%20Experiments/E2-D/E2-D.ipynb) | [Report](E2%20Experiments/E2-D/REPORT.md) | [Tables / figures](E2%20Experiments/E2-D/Results) |
| E2-E | Raw-trained iris-only and complementary inputs | [Notebook](E2%20Experiments/E2-E/E2-E.ipynb) | [Report](E2%20Experiments/E2-E/REPORT.md) | [Tables / figures](E2%20Experiments/E2-E/Results) |
| E2-F | Pair-conditioned Grad-CAM | [Notebook](E2%20Experiments/E2-F/E2-F.ipynb) | [Report](E2%20Experiments/E2-F/REPORT.md) | [Tables / figures](E2%20Experiments/E2-F/Results) |

These analyses were developed after the initial architecture–representation results, with existing checkpoints and preprocessing held fixed. They describe matched comparisons, input sensitivity and spatial attribution; they do not establish causal shortcut use.
E2-D preserves its original matched **feasible-occlusion** cohort across all its controls; its geometry-based coverage is reported separately from the common five-representation population.

## Datasets and primary evaluation population

CUST-Iris, CASIA-Interval and IITD use the original held-out test subjects. AMF and UTIRIS NIR are independent external zero-shot datasets; none of their subjects enters training or checkpoint selection. Results are calculated independently within each dataset.

| Dataset | Images | Subjects | Physical eyes | Genuine | Different-subject impostors | Opposite-eye diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 |

Subject partitions use **dataset + subject**. Iris identities use **dataset + subject + eye side**. Both eyes and every capture stay in the subject's frozen partition. Exact duplicate exclusions and identity review decisions are retained. CASIA-Lamp is outside this study.

## Run one notebook

1. Create a Python 3.11 environment and install [requirements.txt](requirements.txt), choosing the appropriate PyTorch CUDA build for your system.
2. Obtain the licensed datasets and documented caches/checkpoints in [ASSETS.md](ASSETS.md). Biometric images, weights and large embedding caches are not committed.
3. Open the desired notebook, run the imports cell at the top, and edit the configuration cell that follows. For a copied notebook, set the asset and recorded-result paths explicitly.
4. Run all cells to inspect definitions and recorded results. Enable its training or analysis switch only when ready. Every notebook defaults to **no training and no new recognition inference**.

New outputs go to a fresh, configurable `reproduced_outputs/` directory. Completed records are read-only inputs and are never overwritten.
The [validation report](VALIDATION.md) distinguishes executed checks from unexecuted full workloads.

## Scope of this release

Only the used methods and relevant completed results are included. E1-C contains **pure V2 geometry and native sampling**, shared by C1/C2. The earlier unmatched evaluation outputs and superseded preprocessing implementations remain solely in the original [IrisCueLab archive](https://github.com/Owais610/IrisCueLab).
This release does not change any subject assignments, scientific settings or saved metric values. The author's [FedHAT](https://github.com/Owais610/FedHAT) is prior work by the same author and informed the metric-learning implementation.
