# AMF: E2-D

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | 524 | 479 | 45 | 52 | 104 | 906 | 112442 | 1133 |

Unavailable ROI cases:

| reason | images |
| --- | --- |
| no_same_row_matched_disk_left_q0.1 | 21 |
| no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 4 |
| no_same_row_matched_disk_right_q0.1 | 20 |

Absolute metrics:

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | baseline | 1.1199 ± 0.5278 | 0.9991 ± 0.0006 | 98.7859 ± 0.9430 | 95.4378 ± 1.6159 |
| AMF | ResNet-18 | q05_left_iris | 1.1597 ± 0.5099 | 0.9990 ± 0.0007 | 98.6755 ± 1.0529 | 95.1067 ± 1.1802 |
| AMF | ResNet-18 | q05_left_periocular | 1.2141 ± 0.5058 | 0.9991 ± 0.0006 | 98.6387 ± 1.0490 | 95.6954 ± 1.7135 |
| AMF | ResNet-18 | q05_right_iris | 1.3344 ± 0.5010 | 0.9991 ± 0.0005 | 98.1972 ± 1.2307 | 94.9227 ± 1.7206 |
| AMF | ResNet-18 | q05_right_periocular | 1.0959 ± 0.4534 | 0.9991 ± 0.0006 | 99.0434 ± 0.7831 | 95.1803 ± 1.6008 |
| AMF | ResNet-18 | q10_left_iris | 1.1734 ± 0.4784 | 0.9990 ± 0.0007 | 98.7123 ± 1.1056 | 95.2907 ± 1.4020 |
| AMF | ResNet-18 | q10_left_periocular | 1.0907 ± 0.4573 | 0.9992 ± 0.0006 | 98.8227 ± 0.7831 | 96.3576 ± 1.4092 |
| AMF | ResNet-18 | q10_right_iris | 1.3109 ± 0.6774 | 0.9991 ± 0.0005 | 98.4915 ± 1.2793 | 94.7388 ± 1.4822 |
| AMF | ResNet-18 | q10_right_periocular | 1.1539 ± 0.3864 | 0.9991 ± 0.0005 | 98.8962 ± 0.7238 | 95.2539 ± 1.3786 |
| AMF | SwinV2-Tiny | baseline | 1.4669 ± 0.2719 | 0.9986 ± 0.0006 | 98.4180 ± 0.3548 | 94.9963 ± 0.9954 |
| AMF | SwinV2-Tiny | q05_left_iris | 1.5619 ± 0.3204 | 0.9984 ± 0.0008 | 98.1236 ± 0.2208 | 93.7454 ± 1.0256 |
| AMF | SwinV2-Tiny | q05_left_periocular | 1.4516 ± 0.3204 | 0.9986 ± 0.0005 | 98.3444 ± 0.3311 | 94.5548 ± 1.4405 |
| AMF | SwinV2-Tiny | q05_right_iris | 1.5505 ± 0.3428 | 0.9983 ± 0.0007 | 98.2340 ± 0.2920 | 94.0029 ± 1.1802 |
| AMF | SwinV2-Tiny | q05_right_periocular | 1.4437 ± 0.2874 | 0.9986 ± 0.0006 | 98.3444 ± 0.2920 | 94.5180 ± 1.2793 |
| AMF | SwinV2-Tiny | q10_left_iris | 1.6508 ± 0.3384 | 0.9982 ± 0.0008 | 98.0868 ± 0.2298 | 93.3775 ± 0.9622 |
| AMF | SwinV2-Tiny | q10_left_periocular | 1.5085 ± 0.3186 | 0.9986 ± 0.0005 | 98.3076 ± 0.2549 | 94.9595 ± 1.3801 |
| AMF | SwinV2-Tiny | q10_right_iris | 1.6515 ± 0.3888 | 0.9981 ± 0.0006 | 98.0500 ± 0.3548 | 93.2671 ± 1.1629 |
| AMF | SwinV2-Tiny | q10_right_periocular | 1.4752 ± 0.3112 | 0.9986 ± 0.0006 | 98.3812 ± 0.3186 | 94.8859 ± 1.4363 |

Paired iris-occluded minus periocular-occluded effects:

| dataset | architecture | area_fraction | side | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 0.05 | left | -0.0544 ± 0.1369 | -0.0002 ± 0.0001 | 0.0368 ± 0.0637 | -0.5887 ± 0.5664 |
| AMF | ResNet-18 | 0.05 | right | 0.2385 ± 0.1169 | -0.0000 ± 0.0001 | -0.8462 ± 0.6653 | -0.2575 ± 0.8990 |
| AMF | ResNet-18 | 0.1 | left | 0.0827 ± 0.0312 | -0.0002 ± 0.0003 | -0.1104 ± 0.3824 | -1.0670 ± 1.0015 |
| AMF | ResNet-18 | 0.1 | right | 0.1570 ± 0.3583 | 0.0000 ± 0.0001 | -0.4047 ± 0.7753 | -0.5151 ± 0.5664 |
| AMF | SwinV2-Tiny | 0.05 | left | 0.1103 ± 0.0001 | -0.0002 ± 0.0003 | -0.2208 ± 0.1104 | -0.8094 ± 0.4179 |
| AMF | SwinV2-Tiny | 0.05 | right | 0.1068 ± 0.1155 | -0.0003 ± 0.0001 | -0.1104 ± 0.0000 | -0.5151 ± 0.1275 |
| AMF | SwinV2-Tiny | 0.1 | left | 0.1423 ± 0.1750 | -0.0004 ± 0.0003 | -0.2208 ± 0.1912 | -1.5820 ± 0.8573 |
| AMF | SwinV2-Tiny | 0.1 | right | 0.1763 ± 0.1621 | -0.0006 ± 0.0001 | -0.3311 ± 0.3824 | -1.6188 ± 0.3186 |