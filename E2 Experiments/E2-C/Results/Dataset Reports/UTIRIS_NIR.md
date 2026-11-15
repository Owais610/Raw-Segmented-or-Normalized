# UTIRIS_NIR: E2-C

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| UTIRIS_NIR | 770 | 1544 | 292613 | 1908 |

| dataset | architecture | condition | input_condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-C1 | E1-C1 | 7.6682 ± 0.8530 | 0.9777 ± 0.0058 | 73.2945 ± 5.4088 | 47.8843 ± 8.2275 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | E1-C2 | 7.7979 ± 0.6955 | 0.9778 ± 0.0043 | 73.9853 ± 5.1184 | 49.3307 ± 6.2875 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | E1-C1 | 9.1894 ± 1.1970 | 0.9705 ± 0.0064 | 66.5371 ± 5.2845 | 41.3860 ± 7.3401 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | E1-C2 | 9.1549 ± 1.2585 | 0.9709 ± 0.0080 | 66.5803 ± 5.8301 | 40.8463 ± 8.3120 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | E1-C1 | 4.4450 ± 0.6736 | 0.9917 ± 0.0028 | 85.1468 ± 2.7935 | 61.6796 ± 3.4206 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | E1-C2 | 4.3819 ± 0.4872 | 0.9927 ± 0.0017 | 85.7297 ± 2.3817 | 62.5648 ± 3.1470 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | E1-C1 | 5.6082 ± 1.5121 | 0.9873 ± 0.0060 | 78.6701 ± 9.0373 | 54.0803 ± 12.9003 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | E1-C2 | 5.2354 ± 0.8497 | 0.9898 ± 0.0031 | 81.1744 ± 5.2322 | 57.5130 ± 7.2574 |

Within-checkpoint C2-input minus C1-input effects:

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-C1 | 0.1298 ± 0.6212 | 0.0001 ± 0.0026 | 0.6908 ± 2.2681 | 1.4465 ± 2.1425 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | -0.0345 ± 0.1430 | 0.0003 ± 0.0015 | 0.0432 ± 0.9482 | -0.5397 ± 1.1074 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | -0.0631 ± 0.3098 | 0.0010 ± 0.0014 | 0.5829 ± 1.1872 | 0.8851 ± 0.9744 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | -0.3728 ± 0.6682 | 0.0025 ± 0.0029 | 2.5043 ± 4.2120 | 3.4326 ± 6.4152 |

Leave-one-subject-out influence:

| dataset | architecture | condition | full_eer_effect_pp | loo_min_pp | loo_max_pp | mean_sign_reversals | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-C1 | 0.12979 | -0.00069 | 0.24957 | 1 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | -0.03451 | -0.16073 | 0.0915 | 15 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | -0.06313 | -0.1302 | -0.02488 | 0 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | -0.37285 | -0.4732 | -0.28046 | 0 | 79 |