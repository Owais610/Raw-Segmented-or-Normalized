# E2-E: Raw-trained iris-only and complementary inputs

Publication summary of saved findings. Complete numerical records and interpretation are in [the detailed report](Results/DETAILED_REPORT.md) and [result index](Results/README.md).

Original E1-A checkpoints only; A→A, existing B1/B2 black-fill inputs, predefined mean-fill versions and black/mean complementary inputs.
All conditions use the identical common image/pair population. Complementary support removes the iris annulus but retains the pupil and other ocular information; it is not strictly periocular-only.
The full Cartesian coordinate and pixel checks quantify interpolation footprints rather than assuming that native texture differs only by masking.
Degradation is not proof of periocular identity reliance; preservation means sufficiency under the tested intervention.

## Population

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic | complement_available | complement_unreliable_images | existing_b1_b2_tensors_bit_exact | retained_iris_pixels_bit_exact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 | True | 0 | True | True |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 | True | 0 | True | True |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 | True | 0 | True | True |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 | True | 0 | True | True |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 | True | 0 | True | True |

## Numerical overview

EER (%), mean ± sample SD across all three seeds. Individual results and all four metrics are retained in the tables.

| Model | Input | CUST-Iris | CASIA-Interval | IITD | AMF | UTIRIS_NIR |
| --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 1.400 ± 0.287 | 2.101 ± 0.667 | 0.760 ± 0.360 | 1.024 ± 0.454 | 6.973 ± 0.357 |
| ResNet-18 | A_B1_black | 8.240 ± 0.720 | 9.398 ± 1.485 | 3.220 ± 0.233 | 4.103 ± 0.467 | 13.385 ± 0.099 |
| ResNet-18 | A_B1_mean | 7.639 ± 0.533 | 6.796 ± 0.719 | 3.698 ± 0.721 | 5.568 ± 0.521 | 14.390 ± 1.720 |
| ResNet-18 | A_B2_black | 9.213 ± 0.744 | 10.983 ± 1.074 | 3.435 ± 0.380 | 5.305 ± 0.316 | 13.540 ± 0.595 |
| ResNet-18 | A_B2_mean | 7.438 ± 0.294 | 7.160 ± 0.593 | 3.571 ± 0.969 | 5.641 ± 0.639 | 13.338 ± 1.186 |
| ResNet-18 | A_nonannulus_black | 2.734 ± 0.364 | 7.539 ± 0.517 | 3.185 ± 0.637 | 2.059 ± 0.187 | 13.331 ± 1.090 |
| ResNet-18 | A_nonannulus_mean | 2.734 ± 0.778 | 7.057 ± 0.735 | 2.866 ± 0.730 | 1.862 ± 0.557 | 12.046 ± 1.459 |
| SwinV2-Tiny | A_A | 1.872 ± 0.318 | 3.306 ± 0.357 | 1.612 ± 0.507 | 1.336 ± 0.294 | 9.956 ± 2.944 |
| SwinV2-Tiny | A_B1_black | 7.261 ± 0.561 | 6.150 ± 0.398 | 2.683 ± 0.544 | 3.204 ± 0.583 | 12.937 ± 3.843 |
| SwinV2-Tiny | A_B1_mean | 5.591 ± 0.489 | 6.719 ± 0.780 | 2.533 ± 0.363 | 3.371 ± 0.511 | 12.920 ± 3.699 |
| SwinV2-Tiny | A_B2_black | 7.137 ± 0.429 | 6.525 ± 0.441 | 2.990 ± 0.847 | 3.417 ± 0.575 | 12.871 ± 3.608 |
| SwinV2-Tiny | A_B2_mean | 5.589 ± 0.348 | 6.599 ± 0.338 | 2.972 ± 0.092 | 3.154 ± 0.601 | 12.919 ± 3.182 |
| SwinV2-Tiny | A_nonannulus_black | 2.995 ± 0.458 | 6.184 ± 0.894 | 2.645 ± 1.097 | 2.104 ± 0.248 | 14.486 ± 1.657 |
| SwinV2-Tiny | A_nonannulus_mean | 3.511 ± 0.648 | 5.807 ± 0.309 | 2.825 ± 0.716 | 1.909 ± 0.242 | 13.015 ± 2.418 |

## Reproduce and inspect

Open [E2-E.ipynb](E2-E.ipynb); configure direct external assets and enable `RUN_ANALYSIS`. No preceding notebook is required. [METHOD.md](METHOD.md) states exact definitions and interpretation limits. New outputs never overwrite recorded results.
