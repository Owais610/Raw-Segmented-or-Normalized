# E2-C: Frozen polar C1/C2 input swap

Publication summary of saved findings. Complete numerical records and interpretation are in [the detailed report](Results/DETAILED_REPORT.md) and [result index](Results/README.md).

The same frozen C1 or C2 checkpoint receives both C1 and C2 input, creating the original 2×2 design.
Diagonal scores reuse the original embeddings. Crossed cells retain the original matched-domain inference order, batch 24 and per-checkpoint AMP policy.
Exact C2-valid ⊆ C1-valid and common-valid grayscale equality are checked directly; this notebook does not depend on E2-B having run.
Input-swap sensitivity includes distribution mismatch and cannot isolate a causal eyelash effect.

## Population

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 634 | 89473 | 844 |
| CASIA-Interval | 395 | 1353 | 75272 | 1190 |
| IITD | 308 | 628 | 45936 | 714 |
| AMF | 523 | 1015 | 134214 | 1274 |
| UTIRIS_NIR | 770 | 1544 | 292613 | 1908 |

## Numerical overview

Within the SAME checkpoint: C2-input minus C1-input EER.

| dataset | architecture | condition | EER change (pp) |
| --- | --- | --- | --- |
| AMF | ResNet-18 | E1-C1 | -0.355 ± 0.230 |
| AMF | ResNet-18 | E1-C2 | -0.113 ± 0.382 |
| AMF | SwinV2-Tiny | E1-C1 | 0.030 ± 0.152 |
| AMF | SwinV2-Tiny | E1-C2 | -0.078 ± 0.074 |
| CASIA-Interval | ResNet-18 | E1-C1 | 0.876 ± 0.333 |
| CASIA-Interval | ResNet-18 | E1-C2 | 0.334 ± 0.473 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | 0.504 ± 0.344 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | 0.121 ± 0.460 |
| CUST-Iris | ResNet-18 | E1-C1 | 0.091 ± 0.085 |
| CUST-Iris | ResNet-18 | E1-C2 | 0.028 ± 0.160 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | -0.018 ± 0.092 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | 0.027 ± 0.364 |
| IITD | ResNet-18 | E1-C1 | 0.090 ± 0.348 |
| IITD | ResNet-18 | E1-C2 | 0.066 ± 0.438 |
| IITD | SwinV2-Tiny | E1-C1 | 0.083 ± 0.067 |
| IITD | SwinV2-Tiny | E1-C2 | 0.321 ± 0.216 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | 0.130 ± 0.621 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | -0.035 ± 0.143 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | -0.063 ± 0.310 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | -0.373 ± 0.668 |

## Reproduce and inspect

Open [E2-C.ipynb](E2-C.ipynb); configure direct external assets and enable `RUN_ANALYSIS`. No preceding notebook is required. [METHOD.md](METHOD.md) states exact definitions and interpretation limits. New outputs never overwrite recorded results.
