> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-D: explanatory matched raw-region partial occlusion

Only original E1-A frozen checkpoints and original eligible held-out test/external images were used. Sizes5% and10% of annulus area, image-coordinate left/right placements and frozen-mean fill were fixed before perturbed recognition. Every compared iris/periocular disk has exactly equal pixel count, stencil shape and center y, lies on the same horizontal side and touches neither padding nor the other ROI. The unperturbed baseline uses the same available images/pairs. All eight variants must be feasible for image inclusion; no relaxed fallback is used. Raw input/normalization and all unoccluded tensor pixels remain unchanged.

| dataset | original_images | eligible_images | unavailable_images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 432 | 398 | 34 | 53 | 106 | 572 | 77670 | 761 |
| CASIA-Interval | 396 | 147 | 249 | 29 | 45 | 260 | 10226 | 245 |
| IITD | 319 | 151 | 168 | 28 | 43 | 236 | 10911 | 178 |
| AMF | 524 | 479 | 45 | 52 | 104 | 906 | 112442 | 1133 |
| UTIRIS_NIR | 793 | 542 | 251 | 78 | 147 | 873 | 144715 | 1023 |

Excluded here means unavailable for this matched perturbation analysis only; no E1 exclusion, split, label or result was changed. Every unavailable image/reason is in the per-domain roi_inventory. Mask geometry was built and committed before its recognition scoring. Left/right placements are fixed spatial controls, not anatomical temporal/nasal claims. EER/TAR percent; AUC [0,1]; all3 seeds and sample SD.

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

This experiment measures local partial-occlusion sensitivity, not removal of an entire anatomical region. Equal mask area/fill does not equalize removed texture or intensity energy; those measurements are saved. Different x locations, segmentation error, feasible-population selection, artificial edges and test-time distribution mismatch remain confounds. A larger effect is not proof of an identity shortcut, and a small effect does not prove a region is unused. Full individual results, baseline changes, image/subject sensitivities and genuine/impostor-tail distributions are retained without selecting favorable conditions.