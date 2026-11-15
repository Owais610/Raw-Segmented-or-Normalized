# CASIA-Interval: E2-C

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| CASIA-Interval | 395 | 1353 | 75272 | 1190 |

| dataset | architecture | condition | input_condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-C1 | E1-C1 | 3.7777 ± 0.6965 | 0.9940 ± 0.0020 | 89.1599 ± 4.2098 | 61.0495 ± 10.5665 |
| CASIA-Interval | ResNet-18 | E1-C1 | E1-C2 | 4.6541 ± 0.7072 | 0.9902 ± 0.0023 | 87.4353 ± 1.2992 | 57.9946 ± 7.4471 |
| CASIA-Interval | ResNet-18 | E1-C2 | E1-C1 | 4.7228 ± 1.4701 | 0.9906 ± 0.0050 | 86.5238 ± 5.8132 | 62.7002 ± 13.2882 |
| CASIA-Interval | ResNet-18 | E1-C2 | E1-C2 | 5.0570 ± 1.0126 | 0.9889 ± 0.0048 | 85.3412 ± 3.3953 | 54.5947 ± 15.2806 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | E1-C1 | 1.8609 ± 0.7750 | 0.9980 ± 0.0012 | 95.8118 ± 2.6826 | 75.9300 ± 3.2799 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | E1-C2 | 2.3651 ± 1.1185 | 0.9973 ± 0.0020 | 94.9249 ± 3.0152 | 75.1170 ± 3.2151 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | E1-C1 | 2.1796 ± 0.5989 | 0.9975 ± 0.0011 | 94.6785 ± 2.6267 | 75.4127 ± 6.5918 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | E1-C2 | 2.3010 ± 0.3970 | 0.9971 ± 0.0014 | 94.6539 ± 2.1979 | 75.9547 ± 5.6879 |

Within-checkpoint C2-input minus C1-input effects:

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-C1 | 0.8764 ± 0.3326 | -0.0038 ± 0.0018 | -1.7246 ± 3.4591 | -3.0549 ± 8.0539 |
| CASIA-Interval | ResNet-18 | E1-C2 | 0.3342 ± 0.4732 | -0.0017 ± 0.0007 | -1.1826 ± 2.4966 | -8.1054 ± 2.1438 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | 0.5042 ± 0.3437 | -0.0007 ± 0.0008 | -0.8869 ± 0.7501 | -0.8130 ± 1.9928 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | 0.1214 ± 0.4596 | -0.0003 ± 0.0003 | -0.0246 ± 0.9503 | 0.5420 ± 2.2103 |

Leave-one-subject-out influence:

| dataset | architecture | condition | full_eer_effect_pp | loo_min_pp | loo_max_pp | mean_sign_reversals | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-C1 | 0.87635 | 0.60804 | 1.02066 | 0 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | 0.3342 | 0.0885 | 0.47923 | 0 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | 0.50422 | 0.27447 | 0.66588 | 0 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | 0.12141 | -0.26357 | 0.26637 | 2 | 37 |