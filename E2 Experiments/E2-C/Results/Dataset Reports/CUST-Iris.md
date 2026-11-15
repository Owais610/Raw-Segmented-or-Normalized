# CUST-Iris: E2-C

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 634 | 89473 | 844 |

| dataset | architecture | condition | input_condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-C1 | E1-C1 | 2.3659 ± 0.2732 | 0.9972 ± 0.0011 | 94.9001 ± 0.5539 | 81.0200 ± 2.9311 |
| CUST-Iris | ResNet-18 | E1-C1 | E1-C2 | 2.4573 ± 0.2972 | 0.9972 ± 0.0010 | 94.6898 ± 1.1943 | 79.8107 ± 4.2440 |
| CUST-Iris | ResNet-18 | E1-C2 | E1-C1 | 2.6522 ± 0.9913 | 0.9968 ± 0.0016 | 93.1651 ± 4.3320 | 72.6078 ± 10.5823 |
| CUST-Iris | ResNet-18 | E1-C2 | E1-C2 | 2.6800 ± 0.8362 | 0.9966 ± 0.0017 | 93.1125 ± 4.5560 | 74.0273 ± 8.4430 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | E1-C1 | 1.6309 ± 0.3633 | 0.9988 ± 0.0002 | 97.6866 ± 0.4553 | 91.4826 ± 1.2519 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | E1-C2 | 1.6128 ± 0.2797 | 0.9989 ± 0.0001 | 97.8970 ± 0.6375 | 91.5352 ± 1.3781 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | E1-C1 | 1.8110 ± 0.4939 | 0.9983 ± 0.0008 | 97.1609 ± 0.9850 | 89.3796 ± 2.4956 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | E1-C2 | 1.8376 ± 0.6610 | 0.9983 ± 0.0008 | 97.6341 ± 1.2618 | 91.1672 ± 1.9700 |

Within-checkpoint C2-input minus C1-input effects:

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-C1 | 0.0913 ± 0.0853 | 0.0000 ± 0.0002 | -0.2103 ± 0.7454 | -1.2093 ± 1.8484 |
| CUST-Iris | ResNet-18 | E1-C2 | 0.0278 ± 0.1604 | -0.0002 ± 0.0001 | -0.0526 ± 0.4553 | 1.4196 ± 3.0093 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | -0.0181 ± 0.0923 | 0.0000 ± 0.0000 | 0.2103 ± 0.3969 | 0.0526 ± 0.7454 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | 0.0266 ± 0.3638 | -0.0000 ± 0.0001 | 0.4732 ± 0.4173 | 1.7876 ± 0.5539 |

Leave-one-subject-out influence:

| dataset | architecture | condition | full_eer_effect_pp | loo_min_pp | loo_max_pp | mean_sign_reversals | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-C1 | 0.09133 | -0.03356 | 0.12729 | 1 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | 0.02784 | -0.05595 | 0.11341 | 12 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | -0.01811 | -0.1351 | 0.02119 | 5 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | 0.02664 | -0.1478 | 0.10084 | 8 | 54 |