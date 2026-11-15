> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-A: all five datasets, matched eligibility (scope V2)

The internal-dataset coverage was added after the external A/B analyses completed. The original frozen test split and exhaustive different-subject comparisons supplied the three internal datasets. Completed external results were preserved. No additional inference or training was needed for this matched score analysis; the common-population results below are the publication protocol.

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 |

# CUST-Iris: E2-A common eligibility

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 |

Metrics: mean ± sample SD over all3 seeds; EER/TAR percent, AUC [0,1].

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-A | 1.4004 ± 0.2872 | 0.9986 ± 0.0009 | 98.2124 ± 0.4819 | 95.6887 ± 1.0502 |
| CUST-Iris | ResNet-18 | E1-B1 | 1.3408 ± 0.2088 | 0.9992 ± 0.0003 | 98.2124 ± 0.6375 | 91.1672 ± 1.1041 |
| CUST-Iris | ResNet-18 | E1-B2 | 1.4202 ± 0.3398 | 0.9991 ± 0.0004 | 97.8444 ± 0.7939 | 90.2734 ± 1.5799 |
| CUST-Iris | ResNet-18 | E1-C1 | 2.3659 ± 0.2732 | 0.9972 ± 0.0011 | 94.9001 ± 0.5539 | 81.0200 ± 2.9311 |
| CUST-Iris | ResNet-18 | E1-C2 | 2.6800 ± 0.8362 | 0.9966 ± 0.0017 | 93.1125 ± 4.5560 | 74.0273 ± 8.4430 |
| CUST-Iris | SwinV2-Tiny | E1-A | 1.8717 ± 0.3176 | 0.9986 ± 0.0007 | 96.9506 ± 1.6417 | 91.3249 ± 1.9700 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | 1.5415 ± 0.2137 | 0.9987 ± 0.0004 | 97.4238 ± 0.5972 | 86.8034 ± 3.4061 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | 2.0037 ± 0.3775 | 0.9983 ± 0.0004 | 96.3722 ± 1.5534 | 81.2303 ± 3.6957 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | 1.6309 ± 0.3633 | 0.9988 ± 0.0002 | 97.6866 ± 0.4553 | 91.4826 ± 1.2519 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | 1.8376 ± 0.6610 | 0.9983 ± 0.0008 | 97.6341 ± 1.2618 | 91.1672 ± 1.9700 |

Paired numerical-seed contrasts; no significance/causal interpretation.

| dataset | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18:C2-minus-C1 | 0.3141 ± 0.9604 | -0.0006 ± 0.0019 | -1.7876 ± 4.6532 | -6.9926 ± 6.3745 |
| CUST-Iris | SwinV2-Tiny:C2-minus-C1 | 0.2067 ± 0.6611 | -0.0005 ± 0.0007 | -0.0526 ± 1.3415 | -0.3155 ± 1.7915 |
| CUST-Iris | architecture:E1-A:Swin-minus-ResNet | 0.4713 ± 0.6045 | 0.0000 ± 0.0015 | -1.2618 ± 2.1220 | -4.3638 ± 1.8818 |
| CUST-Iris | architecture:E1-B1:Swin-minus-ResNet | 0.2007 ± 0.4105 | -0.0005 ± 0.0006 | -0.7886 ± 1.1908 | -4.3638 ± 4.1442 |
| CUST-Iris | architecture:E1-B2:Swin-minus-ResNet | 0.5836 ± 0.6807 | -0.0008 ± 0.0008 | -1.4721 ± 2.1415 | -9.0431 ± 2.1415 |
| CUST-Iris | architecture:E1-C1:Swin-minus-ResNet | -0.7350 ± 0.5538 | 0.0017 ± 0.0011 | 2.7865 ± 0.7454 | 10.4627 ± 2.1874 |
| CUST-Iris | architecture:E1-C2:Swin-minus-ResNet | -0.8424 ± 0.7941 | 0.0017 ± 0.0011 | 4.5216 ± 4.7694 | 17.1399 ± 7.5732 |
| CUST-Iris | interaction:E1-C1-minus-A | -1.2063 ± 1.1543 | 0.0016 ± 0.0025 | 4.0484 ± 2.8667 | 14.8265 ± 3.9432 |
| CUST-Iris | interaction:E1-C2-minus-A | -1.3137 ± 0.1907 | 0.0017 ± 0.0009 | 5.7834 ± 3.0517 | 21.5037 ± 7.4188 |

Leave-one-subject-out principal contrasts; full per-seed/four-metric results retained.

| dataset | contrast | full_mean_eer_effect_pp | loo_min_mean_eer_effect_pp | loo_max_mean_eer_effect_pp | sign_reversing_subjects | zero_subject_effects | most_influential_subject | largest_absolute_shift_pp | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18:C2-minus-C1 | 0.31411 | 0.04037 | 0.4672 | 0 | 0 | 143 | 0.27373 | 54 |
| CUST-Iris | SwinV2-Tiny:C2-minus-C1 | 0.20667 | 0.07193 | 0.32003 | 0 | 0 | 320 | 0.13475 | 54 |
| CUST-Iris | architecture:E1-A:Swin-minus-ResNet | 0.47128 | 0.40532 | 0.52904 | 0 | 0 | 309 | 0.06595 | 54 |
| CUST-Iris | architecture:E1-C1:Swin-minus-ResNet | -0.73499 | -0.93919 | -0.60354 | 0 | 0 | 143 | 0.2042 | 54 |
| CUST-Iris | architecture:E1-C2:Swin-minus-ResNet | -0.84243 | -0.96671 | -0.63541 | 0 | 0 | 141 | 0.20702 | 54 |
| CUST-Iris | interaction:E1-C1-minus-A | -1.20627 | -1.38056 | -1.07368 | 0 | 0 | 143 | 0.17429 | 54 |
| CUST-Iris | interaction:E1-C2-minus-A | -1.31371 | -1.43105 | -1.12026 | 0 | 0 | 141 | 0.19345 | 54 |


# CASIA-Interval: E2-A common eligibility

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 |

Metrics: mean ± sample SD over all3 seeds; EER/TAR percent, AUC [0,1].

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-A | 2.1015 ± 0.6675 | 0.9969 ± 0.0006 | 95.8364 ± 2.0765 | 84.9470 ± 6.8503 |
| CASIA-Interval | ResNet-18 | E1-B1 | 2.7820 ± 0.3462 | 0.9959 ± 0.0008 | 94.6046 ± 0.9665 | 83.7152 ± 2.0922 |
| CASIA-Interval | ResNet-18 | E1-B2 | 3.8632 ± 1.5662 | 0.9902 ± 0.0022 | 91.6482 ± 4.4976 | 76.0039 ± 10.2906 |
| CASIA-Interval | ResNet-18 | E1-C1 | 3.7777 ± 0.6965 | 0.9940 ± 0.0020 | 89.1599 ± 4.2098 | 61.0495 ± 10.5665 |
| CASIA-Interval | ResNet-18 | E1-C2 | 5.0570 ± 1.0126 | 0.9889 ± 0.0048 | 85.3412 ± 3.3953 | 54.5947 ± 15.2806 |
| CASIA-Interval | SwinV2-Tiny | E1-A | 3.3059 ± 0.3567 | 0.9953 ± 0.0003 | 93.1017 ± 1.2915 | 81.1530 ± 4.9154 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | 3.2307 ± 0.5268 | 0.9958 ± 0.0009 | 92.2148 ± 1.6664 | 80.0443 ± 2.8510 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | 3.3017 ± 0.6931 | 0.9943 ± 0.0027 | 90.6874 ± 3.9505 | 72.2345 ± 11.6668 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | 1.8609 ± 0.7750 | 0.9980 ± 0.0012 | 95.8118 ± 2.6826 | 75.9300 ± 3.2799 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | 2.3010 ± 0.3970 | 0.9971 ± 0.0014 | 94.6539 ± 2.1979 | 75.9547 ± 5.6879 |

Paired numerical-seed contrasts; no significance/causal interpretation.

| dataset | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18:C2-minus-C1 | 1.2793 ± 0.8990 | -0.0051 ± 0.0046 | -3.8187 ± 2.7776 | -6.4548 ± 5.1368 |
| CASIA-Interval | SwinV2-Tiny:C2-minus-C1 | 0.4401 ± 0.8141 | -0.0009 ± 0.0023 | -1.1579 ± 3.9279 | 0.0246 ± 7.0165 |
| CASIA-Interval | architecture:E1-A:Swin-minus-ResNet | 1.2044 ± 0.9663 | -0.0016 ± 0.0007 | -2.7347 ± 3.0545 | -3.7940 ± 11.2132 |
| CASIA-Interval | architecture:E1-B1:Swin-minus-ResNet | 0.4487 ± 0.6928 | -0.0000 ± 0.0015 | -2.3898 ± 2.0699 | -3.6709 ± 4.5087 |
| CASIA-Interval | architecture:E1-B2:Swin-minus-ResNet | -0.5615 ± 2.1216 | 0.0040 ± 0.0048 | -0.9608 ± 8.4046 | -3.7694 ± 20.2124 |
| CASIA-Interval | architecture:E1-C1:Swin-minus-ResNet | -1.9168 ± 1.4411 | 0.0041 ± 0.0029 | 6.6519 ± 6.8489 | 14.8805 ± 13.7731 |
| CASIA-Interval | architecture:E1-C2:Swin-minus-ResNet | -2.7560 ± 1.3260 | 0.0083 ± 0.0048 | 9.3126 ± 4.3869 | 21.3599 ± 15.8555 |
| CASIA-Interval | interaction:E1-C1-minus-A | -3.1212 ± 1.2269 | 0.0056 ± 0.0034 | 9.3865 ± 5.8286 | 18.6746 ± 10.1556 |
| CASIA-Interval | interaction:E1-C2-minus-A | -3.9604 ± 1.9653 | 0.0098 ± 0.0055 | 12.0473 ± 6.5788 | 25.1540 ± 14.4214 |

Leave-one-subject-out principal contrasts; full per-seed/four-metric results retained.

| dataset | contrast | full_mean_eer_effect_pp | loo_min_mean_eer_effect_pp | loo_max_mean_eer_effect_pp | sign_reversing_subjects | zero_subject_effects | most_influential_subject | largest_absolute_shift_pp | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18:C2-minus-C1 | 1.2793 | 0.921 | 1.59269 | 0 | 0 | 219 | 0.35831 | 37 |
| CASIA-Interval | SwinV2-Tiny:C2-minus-C1 | 0.44009 | 0.06212 | 0.57679 | 0 | 0 | 182 | 0.37797 | 37 |
| CASIA-Interval | architecture:E1-A:Swin-minus-ResNet | 1.20439 | 0.88042 | 1.30221 | 0 | 0 | 218 | 0.32396 | 37 |
| CASIA-Interval | architecture:E1-C1:Swin-minus-ResNet | -1.91681 | -2.13777 | -1.62719 | 0 | 0 | 028 | 0.28962 | 37 |
| CASIA-Interval | architecture:E1-C2:Swin-minus-ResNet | -2.75602 | -3.07915 | -2.25605 | 0 | 0 | 219 | 0.49997 | 37 |
| CASIA-Interval | interaction:E1-C1-minus-A | -3.1212 | -3.40594 | -2.6292 | 0 | 0 | 028 | 0.492 | 37 |
| CASIA-Interval | interaction:E1-C2-minus-A | -3.96041 | -4.26798 | -3.37815 | 0 | 0 | 218 | 0.58226 | 37 |


# IITD: E2-A common eligibility

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 |

Metrics: mean ± sample SD over all3 seeds; EER/TAR percent, AUC [0,1].

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-A | 0.7598 ± 0.3596 | 0.9997 ± 0.0003 | 99.3631 ± 0.5516 | 96.8684 ± 0.6435 |
| IITD | ResNet-18 | E1-B1 | 1.0694 ± 0.2537 | 0.9993 ± 0.0004 | 98.8854 ± 0.3185 | 97.0276 ± 1.4795 |
| IITD | ResNet-18 | E1-B2 | 1.3243 ± 0.7882 | 0.9986 ± 0.0019 | 98.1423 ± 1.8456 | 93.6306 ± 6.2102 |
| IITD | ResNet-18 | E1-C1 | 2.2858 ± 1.0662 | 0.9969 ± 0.0010 | 96.3376 ± 2.7764 | 90.0743 ± 6.8533 |
| IITD | ResNet-18 | E1-C2 | 2.1570 ± 0.4551 | 0.9968 ± 0.0008 | 96.7091 ± 0.8770 | 92.4098 ± 1.6108 |
| IITD | SwinV2-Tiny | E1-A | 1.6120 ± 0.5075 | 0.9986 ± 0.0009 | 98.0892 ± 0.7962 | 95.1168 ± 2.9591 |
| IITD | SwinV2-Tiny | E1-B1 | 0.9340 ± 0.5146 | 0.9997 ± 0.0002 | 99.2569 ± 0.7525 | 96.8684 ± 1.2969 |
| IITD | SwinV2-Tiny | E1-B2 | 1.1590 ± 0.1443 | 0.9993 ± 0.0001 | 98.7261 ± 0.2758 | 96.1253 ± 0.8770 |
| IITD | SwinV2-Tiny | E1-C1 | 0.6192 ± 0.1865 | 0.9996 ± 0.0004 | 99.4692 ± 0.2432 | 98.5138 ± 0.1839 |
| IITD | SwinV2-Tiny | E1-C2 | 0.9422 ± 0.4233 | 0.9994 ± 0.0005 | 98.9384 ± 0.8770 | 96.2845 ± 2.1619 |

Paired numerical-seed contrasts; no significance/causal interpretation.

| dataset | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18:C2-minus-C1 | -0.1288 ± 1.1969 | -0.0001 ± 0.0009 | 0.3715 ± 2.7687 | 2.3355 ± 6.2292 |
| IITD | SwinV2-Tiny:C2-minus-C1 | 0.3230 ± 0.4211 | -0.0002 ± 0.0004 | -0.5308 ± 0.7525 | -2.2293 ± 2.3130 |
| IITD | architecture:E1-A:Swin-minus-ResNet | 0.8522 ± 0.8554 | -0.0010 ± 0.0010 | -1.2739 ± 1.3034 | -1.7516 ± 2.6310 |
| IITD | architecture:E1-B1:Swin-minus-ResNet | -0.1354 ± 0.5374 | 0.0005 ± 0.0002 | 0.3715 ± 0.8770 | -0.1592 ± 1.6625 |
| IITD | architecture:E1-B2:Swin-minus-ResNet | -0.1653 ± 0.6846 | 0.0008 ± 0.0018 | 0.5839 ± 1.7027 | 2.4947 ± 6.3502 |
| IITD | architecture:E1-C1:Swin-minus-ResNet | -1.6666 ± 1.2421 | 0.0027 ± 0.0013 | 3.1316 ± 2.9804 | 8.4395 ± 6.7577 |
| IITD | architecture:E1-C2:Swin-minus-ResNet | -1.2148 ± 0.8782 | 0.0026 ± 0.0012 | 2.2293 ± 1.7516 | 3.8747 ± 3.6183 |
| IITD | interaction:E1-C1-minus-A | -2.5189 ± 0.4884 | 0.0038 ± 0.0009 | 4.4055 ± 1.7027 | 10.1911 ± 5.6343 |
| IITD | interaction:E1-C2-minus-A | -2.0670 ± 1.0752 | 0.0037 ± 0.0004 | 3.5032 ± 1.8364 | 5.6263 ± 1.7540 |

Leave-one-subject-out principal contrasts; full per-seed/four-metric results retained.

| dataset | contrast | full_mean_eer_effect_pp | loo_min_mean_eer_effect_pp | loo_max_mean_eer_effect_pp | sign_reversing_subjects | zero_subject_effects | most_influential_subject | largest_absolute_shift_pp | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18:C2-minus-C1 | -0.12885 | -0.29103 | 0.09097 | 1 | 0 | 033 | 0.21982 | 32 |
| IITD | SwinV2-Tiny:C2-minus-C1 | 0.323 | 0.1896 | 0.53179 | 0 | 0 | 004 | 0.20879 | 32 |
| IITD | architecture:E1-A:Swin-minus-ResNet | 0.85225 | 0.63124 | 0.92339 | 0 | 0 | 064 | 0.22101 | 32 |
| IITD | architecture:E1-C1:Swin-minus-ResNet | -1.66664 | -1.78879 | -1.31524 | 0 | 0 | 013 | 0.3514 | 32 |
| IITD | architecture:E1-C2:Swin-minus-ResNet | -1.21479 | -1.34495 | -0.91974 | 0 | 0 | 192 | 0.29504 | 32 |
| IITD | interaction:E1-C1-minus-A | -2.51888 | -2.69405 | -2.12769 | 0 | 0 | 033 | 0.39119 | 32 |
| IITD | interaction:E1-C2-minus-A | -2.06704 | -2.21637 | -1.75583 | 0 | 0 | 192 | 0.31121 | 32 |


# AMF: E2-A common eligibility

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 |

Metrics: mean ± sample SD over all3 seeds; EER/TAR percent, AUC [0,1].

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-A | 1.0244 ± 0.4541 | 0.9992 ± 0.0005 | 98.9163 ± 0.8418 | 96.0263 ± 1.5050 |
| AMF | ResNet-18 | E1-B1 | 1.6420 ± 0.2844 | 0.9988 ± 0.0005 | 97.7340 ± 0.6897 | 91.3957 ± 2.9905 |
| AMF | ResNet-18 | E1-B2 | 1.5258 ± 0.2902 | 0.9989 ± 0.0005 | 97.7997 ± 0.7127 | 91.0016 ± 3.8314 |
| AMF | ResNet-18 | E1-C1 | 2.2215 ± 0.9520 | 0.9977 ± 0.0021 | 95.1396 ± 4.1535 | 81.4450 ± 11.3092 |
| AMF | ResNet-18 | E1-C2 | 1.9784 ± 0.7141 | 0.9981 ± 0.0010 | 96.3218 ± 1.9315 | 81.2808 ± 4.3540 |
| AMF | SwinV2-Tiny | E1-A | 1.3356 ± 0.2943 | 0.9988 ± 0.0005 | 98.5878 ± 0.3167 | 95.5337 ± 1.0535 |
| AMF | SwinV2-Tiny | E1-B1 | 1.7932 ± 0.5804 | 0.9984 ± 0.0008 | 96.9458 ± 1.2883 | 90.2791 ± 2.1230 |
| AMF | SwinV2-Tiny | E1-B2 | 1.4651 ± 0.2180 | 0.9989 ± 0.0005 | 97.8325 ± 0.9398 | 89.6880 ± 5.7451 |
| AMF | SwinV2-Tiny | E1-C1 | 1.0458 ± 0.1491 | 0.9995 ± 0.0000 | 98.9163 ± 0.2956 | 91.3629 ± 1.5712 |
| AMF | SwinV2-Tiny | E1-C2 | 0.7534 ± 0.1686 | 0.9997 ± 0.0001 | 99.4745 ± 0.1505 | 94.1544 ± 2.0884 |

Paired numerical-seed contrasts; no significance/causal interpretation.

| dataset | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18:C2-minus-C1 | -0.2431 ± 1.2223 | 0.0004 ± 0.0027 | 1.1823 ± 4.7178 | -0.1642 ± 14.9274 |
| AMF | SwinV2-Tiny:C2-minus-C1 | -0.2924 ± 0.1501 | 0.0002 ± 0.0001 | 0.5583 ± 0.3730 | 2.7915 ± 0.8494 |
| AMF | architecture:E1-A:Swin-minus-ResNet | 0.3112 ± 0.5459 | -0.0004 ± 0.0003 | -0.3284 ± 0.9720 | -0.4926 ± 0.4515 |
| AMF | architecture:E1-B1:Swin-minus-ResNet | 0.1512 ± 0.2963 | -0.0004 ± 0.0004 | -0.7882 ± 0.5993 | -1.1166 ± 0.8940 |
| AMF | architecture:E1-B2:Swin-minus-ResNet | -0.0607 ± 0.2197 | 0.0000 ± 0.0005 | 0.0328 ± 0.9312 | -1.3136 ± 7.3413 |
| AMF | architecture:E1-C1:Swin-minus-ResNet | -1.1757 ± 0.8500 | 0.0018 ± 0.0021 | 3.7767 ± 3.9042 | 9.9179 ± 12.6294 |
| AMF | architecture:E1-C2:Swin-minus-ResNet | -1.2251 ± 0.8793 | 0.0016 ± 0.0011 | 3.1527 ± 2.0215 | 12.8736 ± 5.0182 |
| AMF | interaction:E1-C1-minus-A | -1.4869 ± 0.3837 | 0.0022 ± 0.0017 | 4.1051 ± 2.9331 | 10.4105 ± 12.2558 |
| AMF | interaction:E1-C2-minus-A | -1.5363 ± 1.1395 | 0.0021 ± 0.0013 | 3.4811 ± 2.1905 | 13.3662 ± 4.9471 |

Leave-one-subject-out principal contrasts; full per-seed/four-metric results retained.

| dataset | contrast | full_mean_eer_effect_pp | loo_min_mean_eer_effect_pp | loo_max_mean_eer_effect_pp | sign_reversing_subjects | zero_subject_effects | most_influential_subject | largest_absolute_shift_pp | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18:C2-minus-C1 | -0.2431 | -0.42093 | -0.08593 | 0 | 0 | basam | 0.17783 | 54 |
| AMF | SwinV2-Tiny:C2-minus-C1 | -0.29243 | -0.34887 | -0.078 | 0 | 0 | zafer | 0.21443 | 54 |
| AMF | architecture:E1-A:Swin-minus-ResNet | 0.31119 | 0.0564 | 0.36038 | 0 | 0 | ahmed | 0.2548 | 54 |
| AMF | architecture:E1-C1:Swin-minus-ResNet | -1.17573 | -1.30609 | -1.00503 | 0 | 0 | yaseen | 0.17071 | 54 |
| AMF | architecture:E1-C2:Swin-minus-ResNet | -1.22506 | -1.31871 | -0.95758 | 0 | 0 | rasha | 0.26748 | 54 |
| AMF | interaction:E1-C1-minus-A | -1.48693 | -1.60658 | -1.23353 | 0 | 0 | ahmed | 0.2534 | 54 |
| AMF | interaction:E1-C2-minus-A | -1.53626 | -1.64003 | -1.13721 | 0 | 0 | zafer | 0.39905 | 54 |


# UTIRIS_NIR: E2-A common eligibility

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 |

Metrics: mean ± sample SD over all3 seeds; EER/TAR percent, AUC [0,1].

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-A | 6.9732 ± 0.3567 | 0.9803 ± 0.0022 | 80.2677 ± 0.9808 | 59.6287 ± 1.0390 |
| UTIRIS_NIR | ResNet-18 | E1-B1 | 6.6357 ± 0.3494 | 0.9836 ± 0.0036 | 80.0302 ± 2.4793 | 56.4983 ± 3.7966 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | 7.3034 ± 0.4180 | 0.9791 ± 0.0039 | 75.3670 ± 3.3217 | 51.7487 ± 3.6159 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | 7.6682 ± 0.8530 | 0.9777 ± 0.0058 | 73.2945 ± 5.4088 | 47.8843 ± 8.2275 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | 9.1549 ± 1.2585 | 0.9709 ± 0.0080 | 66.5803 ± 5.8301 | 40.8463 ± 8.3120 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | 9.9562 ± 2.9443 | 0.9643 ± 0.0181 | 67.1848 ± 8.1494 | 44.9698 ± 5.1015 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | 6.7172 ± 1.2329 | 0.9815 ± 0.0069 | 74.6114 ± 4.7611 | 46.7185 ± 9.0535 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | 6.2924 ± 0.5181 | 0.9848 ± 0.0016 | 76.2090 ± 1.7551 | 47.9706 ± 2.8887 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | 4.4450 ± 0.6736 | 0.9917 ± 0.0028 | 85.1468 ± 2.7935 | 61.6796 ± 3.4206 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | 5.2354 ± 0.8497 | 0.9898 ± 0.0031 | 81.1744 ± 5.2322 | 57.5130 ± 7.2574 |

Paired numerical-seed contrasts; no significance/causal interpretation.

| dataset | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18:C2-minus-C1 | 1.4868 ± 1.6618 | -0.0068 ± 0.0102 | -6.7142 ± 11.1512 | -7.0380 ± 16.4457 |
| UTIRIS_NIR | SwinV2-Tiny:C2-minus-C1 | 0.7903 ± 0.9240 | -0.0019 ± 0.0041 | -3.9724 ± 5.9506 | -4.1667 ± 6.0899 |
| UTIRIS_NIR | architecture:E1-A:Swin-minus-ResNet | 2.9829 ± 3.2195 | -0.0161 ± 0.0196 | -13.0829 ± 8.9947 | -14.6589 ± 4.3862 |
| UTIRIS_NIR | architecture:E1-B1:Swin-minus-ResNet | 0.0815 ± 1.4294 | -0.0021 ± 0.0095 | -5.4188 ± 6.3687 | -9.7798 ± 8.8197 |
| UTIRIS_NIR | architecture:E1-B2:Swin-minus-ResNet | -1.0111 ± 0.1999 | 0.0057 ± 0.0026 | 0.8420 ± 1.6877 | -3.7781 ± 3.9323 |
| UTIRIS_NIR | architecture:E1-C1:Swin-minus-ResNet | -3.2231 ± 1.5235 | 0.0140 ± 0.0083 | 11.8523 ± 8.2009 | 13.7953 ± 11.3318 |
| UTIRIS_NIR | architecture:E1-C2:Swin-minus-ResNet | -3.9196 ± 2.0104 | 0.0189 ± 0.0107 | 14.5941 ± 8.6355 | 16.6667 ± 11.7987 |
| UTIRIS_NIR | interaction:E1-C1-minus-A | -6.2061 ± 1.7760 | 0.0300 ± 0.0120 | 24.9352 ± 5.7741 | 28.4542 ± 7.6525 |
| UTIRIS_NIR | interaction:E1-C2-minus-A | -6.9025 ± 3.4022 | 0.0350 ± 0.0197 | 27.6770 ± 12.6075 | 31.3256 ± 12.9709 |

Leave-one-subject-out principal contrasts; full per-seed/four-metric results retained.

| dataset | contrast | full_mean_eer_effect_pp | loo_min_mean_eer_effect_pp | loo_max_mean_eer_effect_pp | sign_reversing_subjects | zero_subject_effects | most_influential_subject | largest_absolute_shift_pp | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18:C2-minus-C1 | 1.48677 | 1.36755 | 1.72936 | 0 | 0 | 024 | 0.24259 | 79 |
| UTIRIS_NIR | SwinV2-Tiny:C2-minus-C1 | 0.79035 | 0.70519 | 0.87609 | 0 | 0 | 001 | 0.08575 | 79 |
| UTIRIS_NIR | architecture:E1-A:Swin-minus-ResNet | 2.98292 | 2.82152 | 3.18273 | 0 | 0 | 045 | 0.19981 | 79 |
| UTIRIS_NIR | architecture:E1-C1:Swin-minus-ResNet | -3.22315 | -3.33701 | -2.98521 | 0 | 0 | 007 | 0.23794 | 79 |
| UTIRIS_NIR | architecture:E1-C2:Swin-minus-ResNet | -3.91957 | -4.0446 | -3.73527 | 0 | 0 | 030 | 0.1843 | 79 |
| UTIRIS_NIR | interaction:E1-C1-minus-A | -6.20607 | -6.42337 | -5.9474 | 0 | 0 | 077 | 0.25867 | 79 |
| UTIRIS_NIR | interaction:E1-C2-minus-A | -6.90249 | -7.15458 | -6.68389 | 0 | 0 | 045 | 0.25209 | 79 |


Original test/validation/train subject-disjointness assertions are recorded in TEST_BOUNDARY.json; no training or validation images entered evaluation. Each dataset has distinct pair/score arrays and full ROCs. No new macro/pooling replaces E1. Exact source scores and all original full-population metrics remain preserved.
