# AMF: E2-C

| dataset | images | genuine | impostor | opposite_eye_diagnostic |
| --- | --- | --- | --- | --- |
| AMF | 523 | 1015 | 134214 | 1274 |

| dataset | architecture | condition | input_condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-C1 | E1-C1 | 2.2215 ± 0.9520 | 0.9977 ± 0.0021 | 95.1396 ± 4.1535 | 81.4450 ± 11.3092 |
| AMF | ResNet-18 | E1-C1 | E1-C2 | 1.8664 ± 0.7237 | 0.9983 ± 0.0013 | 96.1248 ± 3.3877 | 82.3317 ± 10.7612 |
| AMF | ResNet-18 | E1-C2 | E1-C1 | 2.0919 ± 0.3346 | 0.9979 ± 0.0006 | 95.3038 ± 0.6257 | 80.6568 ± 3.0212 |
| AMF | ResNet-18 | E1-C2 | E1-C2 | 1.9784 ± 0.7141 | 0.9981 ± 0.0010 | 96.3218 ± 1.9315 | 81.2808 ± 4.3540 |
| AMF | SwinV2-Tiny | E1-C1 | E1-C1 | 1.0458 ± 0.1491 | 0.9995 ± 0.0000 | 98.9163 ± 0.2956 | 91.3629 ± 1.5712 |
| AMF | SwinV2-Tiny | E1-C1 | E1-C2 | 1.0760 ± 0.2664 | 0.9995 ± 0.0001 | 98.9819 ± 0.5056 | 91.4286 ± 1.5167 |
| AMF | SwinV2-Tiny | E1-C2 | E1-C1 | 0.8314 ± 0.2426 | 0.9996 ± 0.0002 | 99.1461 ± 0.6334 | 92.4466 ± 1.7879 |
| AMF | SwinV2-Tiny | E1-C2 | E1-C2 | 0.7534 ± 0.1686 | 0.9997 ± 0.0001 | 99.4745 ± 0.1505 | 94.1544 ± 2.0884 |

Within-checkpoint C2-input minus C1-input effects:

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-C1 | -0.3551 ± 0.2300 | 0.0006 ± 0.0008 | 0.9852 ± 0.7695 | 0.8867 ± 0.5485 |
| AMF | ResNet-18 | E1-C2 | -0.1134 ± 0.3816 | 0.0002 ± 0.0004 | 1.0181 ± 1.3840 | 0.6240 ± 4.4774 |
| AMF | SwinV2-Tiny | E1-C1 | 0.0301 ± 0.1518 | 0.0000 ± 0.0001 | 0.0657 ± 0.2275 | 0.0657 ± 1.5305 |
| AMF | SwinV2-Tiny | E1-C2 | -0.0780 ± 0.0741 | 0.0002 ± 0.0001 | 0.3284 ± 0.5056 | 1.7077 ± 1.5050 |

Leave-one-subject-out influence:

| dataset | architecture | condition | full_eer_effect_pp | loo_min_pp | loo_max_pp | mean_sign_reversals | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-C1 | -0.35511 | -0.41071 | -0.271 | 0 | 54 |
| AMF | ResNet-18 | E1-C2 | -0.11344 | -0.25461 | -0.02353 | 0 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | 0.03015 | -0.02663 | 0.067 | 8 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | -0.07802 | -0.13048 | -0.05035 | 0 | 54 |