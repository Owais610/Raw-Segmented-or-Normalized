# IITD: E2-C

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| IITD | 308 | 628 | 45936 | 714 |

| dataset | architecture | condition | input_condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-C1 | E1-C1 | 2.2858 ± 1.0662 | 0.9969 ± 0.0010 | 96.3376 ± 2.7764 | 90.0743 ± 6.8533 |
| IITD | ResNet-18 | E1-C1 | E1-C2 | 2.3760 ± 1.0615 | 0.9962 ± 0.0011 | 96.2314 ± 1.9459 | 91.5074 ± 4.1656 |
| IITD | ResNet-18 | E1-C2 | E1-C1 | 2.0913 ± 0.8787 | 0.9968 ± 0.0008 | 96.1253 ± 2.2312 | 90.4459 ± 3.7547 |
| IITD | ResNet-18 | E1-C2 | E1-C2 | 2.1570 ± 0.4551 | 0.9968 ± 0.0008 | 96.7091 ± 0.8770 | 92.4098 ± 1.6108 |
| IITD | SwinV2-Tiny | E1-C1 | E1-C1 | 0.6192 ± 0.1865 | 0.9996 ± 0.0004 | 99.4692 ± 0.2432 | 98.5138 ± 0.1839 |
| IITD | SwinV2-Tiny | E1-C1 | E1-C2 | 0.7018 ± 0.1949 | 0.9995 ± 0.0004 | 99.4692 ± 0.2432 | 97.7707 ± 0.3185 |
| IITD | SwinV2-Tiny | E1-C2 | E1-C1 | 0.6217 ± 0.2078 | 0.9995 ± 0.0004 | 99.6285 ± 0.3315 | 96.9745 ± 2.3885 |
| IITD | SwinV2-Tiny | E1-C2 | E1-C2 | 0.9422 ± 0.4233 | 0.9994 ± 0.0005 | 98.9384 ± 0.8770 | 96.2845 ± 2.1619 |

Within-checkpoint C2-input minus C1-input effects:

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-C1 | 0.0901 ± 0.3484 | -0.0007 ± 0.0002 | -0.1062 ± 0.9729 | 1.4331 ± 3.3553 |
| IITD | ResNet-18 | E1-C2 | 0.0657 ± 0.4378 | 0.0000 ± 0.0001 | 0.5839 ± 1.4272 | 1.9639 ± 2.7226 |
| IITD | SwinV2-Tiny | E1-C1 | 0.0826 ± 0.0669 | -0.0001 ± 0.0001 | 0.0000 ± 0.0000 | -0.7431 ± 0.3677 |
| IITD | SwinV2-Tiny | E1-C2 | 0.3205 ± 0.2156 | -0.0001 ± 0.0001 | -0.6900 ± 0.5592 | -0.6900 ± 0.3315 |

Leave-one-subject-out influence:

| dataset | architecture | condition | full_eer_effect_pp | loo_min_pp | loo_max_pp | mean_sign_reversals | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-C1 | 0.09012 | 0.01198 | 0.16694 | 0 | 32 |
| IITD | ResNet-18 | E1-C2 | 0.06573 | -0.21672 | 0.18251 | 3 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | 0.08262 | -0.00306 | 0.10965 | 1 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | 0.32052 | 0.26248 | 0.38671 | 0 | 32 |