# IITD: E2-D

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | 319 | 151 | 168 | 28 | 43 | 236 | 10911 | 178 |

Unavailable ROI cases:

| reason | images |
| --- | --- |
| no_same_row_matched_disk_left_q0.05;no_same_row_matched_disk_left_q0.1 | 8 |
| no_same_row_matched_disk_left_q0.1 | 56 |
| no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 9 |
| no_same_row_matched_disk_right_q0.05;no_same_row_matched_disk_right_q0.1 | 13 |
| no_same_row_matched_disk_right_q0.1 | 82 |

Absolute metrics:

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | baseline | 1.0446 ± 0.5647 | 0.9994 ± 0.0007 | 99.1525 ± 0.7339 | 97.7401 ± 0.2446 |
| IITD | ResNet-18 | q05_left_iris | 1.0324 ± 0.5768 | 0.9997 ± 0.0003 | 99.2938 ± 0.8821 | 97.7401 ± 0.2446 |
| IITD | ResNet-18 | q05_left_periocular | 0.9132 ± 0.6769 | 0.9992 ± 0.0012 | 99.2938 ± 0.8821 | 97.5989 ± 0.2446 |
| IITD | ResNet-18 | q05_right_iris | 0.9880 ± 0.6482 | 0.9996 ± 0.0004 | 99.1525 ± 0.8475 | 97.7401 ± 0.4893 |
| IITD | ResNet-18 | q05_right_periocular | 0.9887 ± 0.6473 | 0.9994 ± 0.0007 | 99.1525 ± 0.7339 | 97.5989 ± 0.2446 |
| IITD | ResNet-18 | q10_left_iris | 0.8857 ± 0.7232 | 0.9997 ± 0.0003 | 99.2938 ± 0.8821 | 98.0226 ± 0.4893 |
| IITD | ResNet-18 | q10_left_periocular | 1.2850 ± 0.4031 | 0.9987 ± 0.0017 | 98.8701 ± 0.6473 | 97.4576 ± 0.0000 |
| IITD | ResNet-18 | q10_right_iris | 1.0693 ± 0.9124 | 0.9995 ± 0.0006 | 98.8701 ± 1.0664 | 97.5989 ± 0.9786 |
| IITD | ResNet-18 | q10_right_periocular | 1.2026 ± 0.5300 | 0.9993 ± 0.0009 | 98.8701 ± 0.6473 | 97.7401 ± 0.2446 |
| IITD | SwinV2-Tiny | baseline | 1.1598 ± 0.5987 | 0.9995 ± 0.0003 | 98.7288 ± 0.7339 | 97.8814 ± 0.7339 |
| IITD | SwinV2-Tiny | q05_left_iris | 1.2712 ± 0.4237 | 0.9994 ± 0.0004 | 98.5876 ± 0.4893 | 98.0226 ± 0.8821 |
| IITD | SwinV2-Tiny | q05_left_periocular | 1.1751 ± 0.5740 | 0.9996 ± 0.0003 | 98.7288 ± 0.7339 | 98.0226 ± 0.8821 |
| IITD | SwinV2-Tiny | q05_right_iris | 1.1537 ± 0.6086 | 0.9995 ± 0.0004 | 98.7288 ± 0.7339 | 97.4576 ± 0.4237 |
| IITD | SwinV2-Tiny | q05_right_periocular | 1.1537 ± 0.6086 | 0.9995 ± 0.0003 | 98.8701 ± 0.6473 | 97.8814 ± 0.7339 |
| IITD | SwinV2-Tiny | q10_left_iris | 1.1323 ± 0.6434 | 0.9995 ± 0.0004 | 98.7288 ± 0.7339 | 97.7401 ± 0.6473 |
| IITD | SwinV2-Tiny | q10_left_periocular | 1.1851 ± 0.6200 | 0.9995 ± 0.0003 | 98.7288 ± 0.7339 | 98.0226 ± 0.8821 |
| IITD | SwinV2-Tiny | q10_right_iris | 1.2712 ± 0.4237 | 0.9995 ± 0.0003 | 98.7288 ± 0.4237 | 97.8814 ± 0.7339 |
| IITD | SwinV2-Tiny | q10_right_periocular | 1.1299 ± 0.6473 | 0.9995 ± 0.0003 | 98.8701 ± 0.6473 | 97.8814 ± 0.7339 |

Paired iris-occluded minus periocular-occluded effects:

| dataset | architecture | area_fraction | side | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | 0.05 | left | 0.1191 ± 0.1191 | 0.0005 ± 0.0008 | 0.0000 ± 0.0000 | 0.1412 ± 0.2446 |
| IITD | ResNet-18 | 0.05 | right | -0.0007 ± 0.0012 | 0.0002 ± 0.0004 | 0.0000 ± 0.4237 | 0.1412 ± 0.6473 |
| IITD | ResNet-18 | 0.1 | left | -0.3993 ± 0.3460 | 0.0010 ± 0.0014 | 0.4237 ± 0.4237 | 0.5650 ± 0.4893 |
| IITD | ResNet-18 | 0.1 | right | -0.1333 ± 0.3953 | 0.0002 ± 0.0003 | -0.0000 ± 0.4237 | -0.1412 ± 0.8821 |
| IITD | SwinV2-Tiny | 0.05 | left | 0.0961 ± 0.1665 | -0.0002 ± 0.0001 | -0.1412 ± 0.2446 | 0.0000 ± 0.0000 |
| IITD | SwinV2-Tiny | 0.05 | right | 0.0000 ± 0.0000 | -0.0000 ± 0.0000 | -0.1412 ± 0.2446 | -0.4237 ± 0.4237 |
| IITD | SwinV2-Tiny | 0.1 | left | -0.0529 ± 0.0482 | -0.0000 ± 0.0001 | 0.0000 ± 0.0000 | -0.2825 ± 0.4893 |
| IITD | SwinV2-Tiny | 0.1 | right | 0.1412 ± 0.2446 | -0.0001 ± 0.0001 | -0.1412 ± 0.2446 | 0.0000 ± 0.0000 |