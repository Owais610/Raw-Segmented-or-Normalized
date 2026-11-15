# CUST-Iris: E2-D

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 432 | 398 | 34 | 53 | 106 | 572 | 77670 | 761 |

Unavailable ROI cases:

| reason | images |
| --- | --- |
| no_same_row_matched_disk_left_q0.1 | 7 |
| no_same_row_matched_disk_left_q0.1;no_same_row_matched_disk_right_q0.1 | 12 |
| no_same_row_matched_disk_right_q0.1 | 15 |

Absolute metrics:

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | baseline | 1.4907 ± 0.2624 | 0.9985 ± 0.0009 | 98.2517 ± 0.6303 | 95.5128 ± 1.5863 |
| CUST-Iris | ResNet-18 | q05_left_iris | 1.7872 ± 0.4639 | 0.9982 ± 0.0009 | 97.2611 ± 0.8075 | 94.4639 ± 1.8364 |
| CUST-Iris | ResNet-18 | q05_left_periocular | 1.4774 ± 0.2218 | 0.9985 ± 0.0009 | 98.1352 ± 0.6140 | 95.5128 ± 0.8799 |
| CUST-Iris | ResNet-18 | q05_right_iris | 1.8648 ± 0.3639 | 0.9981 ± 0.0009 | 97.4942 ± 0.5620 | 94.1725 ± 2.2547 |
| CUST-Iris | ResNet-18 | q05_right_periocular | 1.4996 ± 0.2166 | 0.9983 ± 0.0010 | 97.9604 ± 0.4037 | 95.1049 ± 1.3199 |
| CUST-Iris | ResNet-18 | q10_left_iris | 1.7326 ± 0.8120 | 0.9983 ± 0.0010 | 97.6107 ± 1.4022 | 94.1142 ± 1.6616 |
| CUST-Iris | ResNet-18 | q10_left_periocular | 1.5351 ± 0.2347 | 0.9986 ± 0.0009 | 98.1352 ± 0.5341 | 95.5128 ± 1.0538 |
| CUST-Iris | ResNet-18 | q10_right_iris | 1.8172 ± 0.2533 | 0.9980 ± 0.0010 | 97.4942 ± 0.5620 | 93.5897 ± 2.0710 |
| CUST-Iris | ResNet-18 | q10_right_periocular | 1.5152 ± 0.2019 | 0.9983 ± 0.0010 | 98.0769 ± 0.5245 | 95.1632 ± 1.7512 |
| CUST-Iris | SwinV2-Tiny | baseline | 1.9242 ± 0.4030 | 0.9985 ± 0.0007 | 96.8531 ± 1.4310 | 91.7249 ± 2.3800 |
| CUST-Iris | SwinV2-Tiny | q05_left_iris | 2.0879 ± 0.6541 | 0.9981 ± 0.0011 | 96.8531 ± 1.4310 | 91.2005 ± 2.1364 |
| CUST-Iris | SwinV2-Tiny | q05_left_periocular | 1.8655 ± 0.4388 | 0.9986 ± 0.0007 | 96.7949 ± 1.5274 | 91.9580 ± 2.1483 |
| CUST-Iris | SwinV2-Tiny | q05_right_iris | 1.9641 ± 0.5902 | 0.9985 ± 0.0008 | 96.7949 ± 1.6524 | 91.3170 ± 2.8045 |
| CUST-Iris | SwinV2-Tiny | q05_right_periocular | 2.0638 ± 0.3350 | 0.9985 ± 0.0007 | 96.7949 ± 1.6980 | 91.4336 ± 2.6914 |
| CUST-Iris | SwinV2-Tiny | q10_left_iris | 2.2727 ± 0.8011 | 0.9977 ± 0.0015 | 96.2121 ± 1.5863 | 90.2098 ± 2.8886 |
| CUST-Iris | SwinV2-Tiny | q10_left_periocular | 1.8776 ± 0.4579 | 0.9985 ± 0.0007 | 96.8531 ± 1.7218 | 92.0163 ± 1.9494 |
| CUST-Iris | SwinV2-Tiny | q10_right_iris | 1.9814 ± 0.5341 | 0.9983 ± 0.0008 | 96.9114 ± 1.3352 | 90.9091 ± 2.1906 |
| CUST-Iris | SwinV2-Tiny | q10_right_periocular | 1.9635 ± 0.3914 | 0.9985 ± 0.0007 | 96.7949 ± 1.5274 | 91.3170 ± 2.8477 |

Paired iris-occluded minus periocular-occluded effects:

| dataset | architecture | area_fraction | side | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | 0.05 | left | 0.3097 ± 0.3112 | -0.0003 ± 0.0003 | -0.8741 ± 0.4625 | -1.0490 ± 0.9734 |
| CUST-Iris | ResNet-18 | 0.05 | right | 0.3652 ± 0.1521 | -0.0003 ± 0.0001 | -0.4662 ± 0.4400 | -0.9324 ± 1.1240 |
| CUST-Iris | ResNet-18 | 0.1 | left | 0.1975 ± 0.5931 | -0.0003 ± 0.0005 | -0.5245 ± 0.8741 | -1.3986 ± 0.6303 |
| CUST-Iris | ResNet-18 | 0.1 | right | 0.3021 ± 0.0824 | -0.0003 ± 0.0002 | -0.5828 ± 0.3639 | -1.5734 ± 1.6677 |
| CUST-Iris | SwinV2-Tiny | 0.05 | left | 0.2224 ± 0.2603 | -0.0004 ± 0.0004 | 0.0583 ± 0.1009 | -0.7576 ± 0.3639 |
| CUST-Iris | SwinV2-Tiny | 0.05 | right | -0.0997 ± 0.2859 | -0.0000 ± 0.0001 | 0.0000 ± 0.1748 | -0.1166 ± 0.4400 |
| CUST-Iris | SwinV2-Tiny | 0.1 | left | 0.3951 ± 0.3816 | -0.0008 ± 0.0009 | -0.6410 ± 0.2019 | -1.8065 ± 1.1640 |
| CUST-Iris | SwinV2-Tiny | 0.1 | right | 0.0179 ± 0.1684 | -0.0002 ± 0.0001 | 0.1166 ± 0.2019 | -0.4079 ± 1.0538 |