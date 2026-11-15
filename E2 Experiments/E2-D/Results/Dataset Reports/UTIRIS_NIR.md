# UTIRIS_NIR: E2-D

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | 793 | 542 | 251 | 78 | 147 | 873 | 144715 | 1023 |

Unavailable ROI cases:

| reason | images |
| --- | --- |
| empty_anatomical_support | 1 |
| no_same_row_matched_disk_left_q0.05;no_same_row_matched_disk_left_q0.1 | 11 |
| no_same_row_matched_disk_left_q0.05;no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 2 |
| no_same_row_matched_disk_left_q0.1 | 89 |
| no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 33 |
| no_same_row_matched_disk_right_q0.05;no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 4 |
| no_same_row_matched_disk_right_q0.05;no_same_row_matched_disk_right_q0.1 | 21 |
| no_same_row_matched_disk_right_q0.1 | 90 |

Absolute metrics:

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | baseline | 7.3355 ± 0.2224 | 0.9786 ± 0.0033 | 80.6033 ± 2.2456 | 60.7102 ± 3.1013 |
| UTIRIS_NIR | ResNet-18 | q05_left_iris | 7.7978 ± 0.2421 | 0.9755 ± 0.0040 | 78.5032 ± 3.6120 | 57.8465 ± 5.0661 |
| UTIRIS_NIR | ResNet-18 | q05_left_periocular | 7.6430 ± 0.0789 | 0.9768 ± 0.0038 | 79.9160 ± 2.5235 | 60.5193 ± 3.4863 |
| UTIRIS_NIR | ResNet-18 | q05_right_iris | 8.1616 ± 0.5972 | 0.9734 ± 0.0038 | 76.6705 ± 3.4788 | 55.5937 ± 4.3953 |
| UTIRIS_NIR | ResNet-18 | q05_right_periocular | 7.2208 ± 0.2207 | 0.9785 ± 0.0032 | 80.4506 ± 2.3260 | 59.7556 ± 3.8375 |
| UTIRIS_NIR | ResNet-18 | q10_left_iris | 8.3562 ± 0.2293 | 0.9720 ± 0.0035 | 76.4414 ± 2.9211 | 54.5628 ± 3.9220 |
| UTIRIS_NIR | ResNet-18 | q10_left_periocular | 7.6542 ± 0.2811 | 0.9751 ± 0.0042 | 78.3887 ± 2.6969 | 58.5338 ± 3.2661 |
| UTIRIS_NIR | ResNet-18 | q10_right_iris | 8.2856 ± 0.5765 | 0.9713 ± 0.0042 | 74.8377 ± 4.5594 | 54.6392 ± 5.3618 |
| UTIRIS_NIR | ResNet-18 | q10_right_periocular | 7.3928 ± 0.2566 | 0.9774 ± 0.0034 | 79.2669 ± 2.9716 | 58.2283 ± 3.3774 |
| UTIRIS_NIR | SwinV2-Tiny | baseline | 9.8335 ± 3.2223 | 0.9630 ± 0.0205 | 68.6140 ± 8.0811 | 46.6590 ± 7.3456 |
| UTIRIS_NIR | SwinV2-Tiny | q05_left_iris | 10.1920 ± 3.1047 | 0.9616 ± 0.0197 | 67.2776 ± 7.5064 | 45.8954 ± 6.1369 |
| UTIRIS_NIR | SwinV2-Tiny | q05_left_periocular | 9.8442 ± 3.3210 | 0.9624 ± 0.0207 | 68.1558 ± 8.1329 | 46.3918 ± 7.1928 |
| UTIRIS_NIR | SwinV2-Tiny | q05_right_iris | 10.2711 ± 3.3383 | 0.9602 ± 0.0202 | 66.6285 ± 7.2829 | 44.4826 ± 5.2708 |
| UTIRIS_NIR | SwinV2-Tiny | q05_right_periocular | 9.7954 ± 3.1309 | 0.9630 ± 0.0210 | 68.2321 ± 8.0757 | 46.4299 ± 7.3884 |
| UTIRIS_NIR | SwinV2-Tiny | q10_left_iris | 10.4829 ± 2.9735 | 0.9599 ± 0.0192 | 66.3994 ± 6.8157 | 44.4444 ± 5.6918 |
| UTIRIS_NIR | SwinV2-Tiny | q10_left_periocular | 10.0895 ± 3.2934 | 0.9618 ± 0.0216 | 68.0794 ± 8.1113 | 46.1245 ± 7.7439 |
| UTIRIS_NIR | SwinV2-Tiny | q10_right_iris | 10.6054 ± 3.2790 | 0.9594 ± 0.0200 | 65.4830 ± 6.1944 | 43.2990 ± 4.4849 |
| UTIRIS_NIR | SwinV2-Tiny | q10_right_periocular | 9.8066 ± 3.4337 | 0.9627 ± 0.0210 | 68.0794 ± 8.1340 | 46.2390 ± 7.2359 |

Paired iris-occluded minus periocular-occluded effects:

| dataset | architecture | area_fraction | side | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | 0.05 | left | 0.1548 ± 0.1641 | -0.0013 ± 0.0004 | -1.4128 ± 1.1588 | -2.6728 ± 2.3596 |
| UTIRIS_NIR | ResNet-18 | 0.05 | right | 0.9408 ± 0.4825 | -0.0051 ± 0.0019 | -3.7801 ± 2.1854 | -4.1619 ± 3.6410 |
| UTIRIS_NIR | ResNet-18 | 0.1 | left | 0.7020 ± 0.1297 | -0.0031 ± 0.0008 | -1.9473 ± 0.3031 | -3.9710 ± 3.3676 |
| UTIRIS_NIR | ResNet-18 | 0.1 | right | 0.8928 ± 0.3433 | -0.0061 ± 0.0024 | -4.4292 ± 2.9256 | -3.5892 ± 4.1496 |
| UTIRIS_NIR | SwinV2-Tiny | 0.05 | left | 0.3478 ± 0.2171 | -0.0009 ± 0.0011 | -0.8782 ± 0.6712 | -0.4964 ± 1.2618 |
| UTIRIS_NIR | SwinV2-Tiny | 0.05 | right | 0.4756 ± 0.2557 | -0.0028 ± 0.0009 | -1.6037 ± 0.8946 | -1.9473 ± 2.1215 |
| UTIRIS_NIR | SwinV2-Tiny | 0.1 | left | 0.3935 ± 0.3222 | -0.0019 ± 0.0028 | -1.6800 ± 1.4549 | -1.6800 ± 2.0629 |
| UTIRIS_NIR | SwinV2-Tiny | 0.1 | right | 0.7988 ± 0.3179 | -0.0032 ± 0.0017 | -2.5964 ± 2.0016 | -2.9401 ± 2.7523 |