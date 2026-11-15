> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-C: explanatory frozen-checkpoint polar input swap, all five domains

Every checkpoint is original, frozen and validation selected. Each domain has one identical image/pair population across all four cells. Original diagonal scores are reused; only the two crossed cells required inference. C2-valid is a subset of C1-valid and common-valid grayscale pixels/coordinates were verified exactly before swaps. Normalization, cached inputs and original AMP/inference settings are unchanged.

EER/TAR percent; AUC [0,1]; all3 seeds, mean ± sample SD. Input effects are C2 input minus C1 input **within the same frozen checkpoint**. Negative EER changes indicate lower EER on C2 input. This is distinct from comparing differently trained C1 and C2 models.

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

Complete individual metrics, score distributions including impostor p99/p99.9/max, full ROCs, embeddings, per-image/per-subject sensitivity and leave-one-subject-out effects are saved under e2_c. No external or original test threshold was fitted.

Feeding C2 to a C1-trained model (or the reverse) introduces test-time distribution mismatch. Masking simultaneously removes observed tissue/intensity, changes support/boundaries and can obscure high-gradient texture. Fixed-model sensitivity cannot isolate a causal eyelash-information mechanism. No saliency is presented as causal evidence.