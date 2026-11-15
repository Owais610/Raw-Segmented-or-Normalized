# CASIA-Interval: E2-D

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | 396 | 147 | 249 | 29 | 45 | 260 | 10226 | 245 |

Unavailable ROI cases:

| reason | images |
| --- | --- |
| no_same_row_matched_disk_left_q0.05;no_same_row_matched_disk_left_q0.1 | 17 |
| no_same_row_matched_disk_left_q0.1 | 89 |
| no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 19 |
| no_same_row_matched_disk_right_q0.05;no_same_row_matched_disk_right_q0.1 | 5 |
| no_same_row_matched_disk_right_q0.1 | 119 |

Absolute metrics:

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | baseline | 2.8401 ± 0.6197 | 0.9941 ± 0.0011 | 95.3846 ± 2.6923 | 86.1538 ± 13.1615 |
| CASIA-Interval | ResNet-18 | q05_left_iris | 3.1335 ± 0.7754 | 0.9924 ± 0.0022 | 94.6154 ± 2.0352 | 84.2308 ± 10.6865 |
| CASIA-Interval | ResNet-18 | q05_left_periocular | 2.9487 ± 0.8006 | 0.9937 ± 0.0021 | 95.2564 ± 3.2256 | 85.2564 ± 12.9709 |
| CASIA-Interval | ResNet-18 | q05_right_iris | 2.8978 ± 0.5174 | 0.9928 ± 0.0012 | 94.1026 ± 2.6180 | 80.2564 ± 11.2156 |
| CASIA-Interval | ResNet-18 | q05_right_periocular | 2.8435 ± 0.3257 | 0.9947 ± 0.0010 | 94.8718 ± 3.2256 | 84.6154 ± 14.7363 |
| CASIA-Interval | ResNet-18 | q10_left_iris | 3.6094 ± 0.2072 | 0.9917 ± 0.0022 | 92.4359 ± 2.1183 | 78.3333 ± 10.9418 |
| CASIA-Interval | ResNet-18 | q10_left_periocular | 2.9487 ± 0.8006 | 0.9938 ± 0.0018 | 95.2564 ± 2.5609 | 85.1282 ± 13.8533 |
| CASIA-Interval | ResNet-18 | q10_right_iris | 2.9281 ± 0.4630 | 0.9931 ± 0.0013 | 94.1026 ± 3.5529 | 80.6410 ± 14.8977 |
| CASIA-Interval | ResNet-18 | q10_right_periocular | 2.8924 ± 0.4820 | 0.9945 ± 0.0009 | 95.2564 ± 2.8868 | 85.1282 ± 13.1071 |
| CASIA-Interval | SwinV2-Tiny | baseline | 2.8205 ± 0.5875 | 0.9953 ± 0.0011 | 95.1282 ± 1.5544 | 82.8205 ± 13.9012 |
| CASIA-Interval | SwinV2-Tiny | q05_left_iris | 3.2051 ± 0.5875 | 0.9952 ± 0.0012 | 94.7436 ± 1.4561 | 83.4615 ± 13.7227 |
| CASIA-Interval | SwinV2-Tiny | q05_left_periocular | 2.8130 ± 0.2289 | 0.9953 ± 0.0012 | 94.6154 ± 1.7625 | 83.3333 ± 12.9709 |
| CASIA-Interval | SwinV2-Tiny | q05_right_iris | 3.1313 ± 0.3067 | 0.9950 ± 0.0005 | 95.0000 ± 1.6765 | 82.1795 ± 13.6326 |
| CASIA-Interval | SwinV2-Tiny | q05_right_periocular | 2.7935 ± 0.5646 | 0.9953 ± 0.0013 | 94.8718 ± 1.7343 | 82.9487 ± 13.3253 |
| CASIA-Interval | SwinV2-Tiny | q10_left_iris | 2.9487 ± 0.4441 | 0.9954 ± 0.0012 | 94.4872 ± 1.6013 | 83.0769 ± 11.7355 |
| CASIA-Interval | SwinV2-Tiny | q10_left_periocular | 2.9499 ± 0.2231 | 0.9946 ± 0.0006 | 94.7436 ± 1.6013 | 83.5897 ± 11.4505 |
| CASIA-Interval | SwinV2-Tiny | q10_right_iris | 2.9542 ± 0.4394 | 0.9950 ± 0.0008 | 94.8718 ± 1.4561 | 83.9744 ± 12.2253 |
| CASIA-Interval | SwinV2-Tiny | q10_right_periocular | 2.6305 ± 0.4928 | 0.9954 ± 0.0015 | 95.0000 ± 1.9231 | 82.0513 ± 12.5831 |

Paired iris-occluded minus periocular-occluded effects:

| dataset | architecture | area_fraction | side | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | 0.05 | left | 0.1848 ± 0.3200 | -0.0012 ± 0.0041 | -0.6410 ± 1.2364 | -1.0256 ± 2.3500 |
| CASIA-Interval | ResNet-18 | 0.05 | right | 0.0543 ± 0.2130 | -0.0019 ± 0.0004 | -0.7692 ± 0.7692 | -4.3590 ± 3.6958 |
| CASIA-Interval | ResNet-18 | 0.1 | left | 0.6607 ± 0.8542 | -0.0021 ± 0.0034 | -2.8205 ± 1.2364 | -6.7949 ± 3.9474 |
| CASIA-Interval | ResNet-18 | 0.1 | right | 0.0358 ± 0.1067 | -0.0014 ± 0.0016 | -1.1538 ± 0.6662 | -4.4872 ± 1.8176 |
| CASIA-Interval | SwinV2-Tiny | 0.05 | left | 0.3922 ± 0.3734 | -0.0000 ± 0.0002 | 0.1282 ± 0.9679 | 0.1282 ± 0.8006 |
| CASIA-Interval | SwinV2-Tiny | 0.05 | right | 0.3378 ± 0.2588 | -0.0003 ± 0.0010 | 0.1282 ± 0.9679 | -0.7692 ± 0.3846 |
| CASIA-Interval | SwinV2-Tiny | 0.1 | left | -0.0012 ± 0.3863 | 0.0008 ± 0.0013 | -0.2564 ± 0.8882 | -0.5128 ± 0.8006 |
| CASIA-Interval | SwinV2-Tiny | 0.1 | right | 0.3237 ± 0.0703 | -0.0004 ± 0.0012 | -0.1282 ± 0.8006 | 1.9231 ± 0.3846 |