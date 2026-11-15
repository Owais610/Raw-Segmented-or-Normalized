# UTIRIS_NIR: separate E2-E analysis

## Absolute metrics

EER/TAR percent; AUC[0,1]. Mean ± sample SD over all3 seeds.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | A_A | 6.9732 ± 0.3567 | 0.9803 ± 0.0022 | 80.2677 ± 0.9808 | 59.6287 ± 1.0390 |
| UTIRIS_NIR | ResNet-18 | A_B1_black | 13.3851 ± 0.0989 | 0.9420 ± 0.0005 | 50.1079 ± 1.1017 | 24.7841 ± 1.0288 |
| UTIRIS_NIR | ResNet-18 | A_B1_mean | 14.3901 ± 1.7204 | 0.9339 ± 0.0143 | 46.2867 ± 3.5393 | 23.4024 ± 2.8152 |
| UTIRIS_NIR | ResNet-18 | A_B2_black | 13.5402 ± 0.5951 | 0.9357 ± 0.0046 | 50.6908 ± 2.5600 | 24.9784 ± 1.2959 |
| UTIRIS_NIR | ResNet-18 | A_B2_mean | 13.3382 ± 1.1858 | 0.9408 ± 0.0109 | 49.7409 ± 3.9006 | 24.9136 ± 0.6122 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_black | 13.3308 ± 1.0901 | 0.9362 ± 0.0060 | 59.3912 ± 2.7577 | 37.3057 ± 4.4736 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_mean | 12.0462 ± 1.4591 | 0.9478 ± 0.0088 | 63.4715 ± 4.6203 | 40.8679 ± 4.1405 |
| UTIRIS_NIR | SwinV2-Tiny | A_A | 9.9562 ± 2.9443 | 0.9643 ± 0.0181 | 67.1848 ± 8.1494 | 44.9698 ± 5.1015 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_black | 12.9369 ± 3.8428 | 0.9445 ± 0.0278 | 46.3731 ± 13.0418 | 20.1425 ± 7.8949 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_mean | 12.9201 ± 3.6992 | 0.9439 ± 0.0264 | 51.4033 ± 14.1121 | 24.3739 ± 8.7697 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_black | 12.8713 ± 3.6081 | 0.9452 ± 0.0261 | 47.1071 ± 12.0338 | 19.9698 ± 7.9408 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_mean | 12.9191 ± 3.1816 | 0.9448 ± 0.0216 | 50.8204 ± 11.4813 | 22.7116 ± 7.7478 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_black | 14.4862 ± 1.6567 | 0.9346 ± 0.0119 | 53.5622 ± 2.8652 | 31.6494 ± 0.8098 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_mean | 13.0149 ± 2.4185 | 0.9441 ± 0.0129 | 57.8152 ± 3.6834 | 35.2979 ± 2.6124 |

## Paired intervention minus raw baseline

All differences use the SAME checkpoint and exact pairs. EER/TAR differences are percentage points; AUC differences are on[0,1]. Negative EER differences indicate lower EER.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | A_B1_black | 6.4119 ± 0.2968 | -0.0383 ± 0.0018 | -30.1598 ± 1.3104 | -34.8446 ± 0.5757 |
| UTIRIS_NIR | ResNet-18 | A_B1_mean | 7.4169 ± 1.9953 | -0.0464 ± 0.0126 | -33.9810 ± 3.1426 | -36.2263 ± 2.3897 |
| UTIRIS_NIR | ResNet-18 | A_B2_black | 6.5669 ± 0.8773 | -0.0447 ± 0.0067 | -29.5769 ± 3.0477 | -34.6503 ± 0.2823 |
| UTIRIS_NIR | ResNet-18 | A_B2_mean | 6.3649 ± 1.4741 | -0.0395 ± 0.0092 | -30.5268 ± 3.5215 | -34.7150 ± 1.1292 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_black | 6.3576 ± 0.7764 | -0.0441 ± 0.0074 | -20.8765 ± 3.5559 | -22.3230 ± 5.2912 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_mean | 5.0730 ± 1.1657 | -0.0326 ± 0.0100 | -16.7962 ± 4.8650 | -18.7608 ± 5.1376 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_black | 2.9807 ± 1.1861 | -0.0198 ± 0.0101 | -20.8117 ± 5.0228 | -24.8273 ± 4.0989 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_mean | 2.9639 ± 3.1897 | -0.0203 ± 0.0210 | -15.7815 ± 9.3691 | -20.5959 ± 4.9854 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_black | 2.9151 ± 0.9592 | -0.0190 ± 0.0087 | -20.0777 ± 3.8866 | -25.0000 ± 4.2406 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_mean | 2.9629 ± 2.9987 | -0.0194 ± 0.0186 | -16.3644 ± 6.2346 | -22.2582 ± 3.9568 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_black | 4.5300 ± 1.4961 | -0.0297 ± 0.0089 | -13.6226 ± 5.6348 | -13.3204 ± 4.5638 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_mean | 3.0588 ± 0.5459 | -0.0201 ± 0.0053 | -9.3696 ± 4.4742 | -9.6718 ± 2.5220 |

## Predefined mean-minus-black and B2-minus-B1 controls

| dataset | architecture | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | B1_mean_minus_black | 1.0050 ± 1.7244 | -0.0081 ± 0.0138 | -3.8212 ± 2.5242 | -1.3817 ± 1.9151 |
| UTIRIS_NIR | ResNet-18 | B2_mean_minus_black | -0.2020 ± 1.3091 | 0.0052 ± 0.0147 | -0.9499 ± 2.9992 | -0.0648 ± 1.2937 |
| UTIRIS_NIR | ResNet-18 | B2_minus_B1_black | 0.1550 ± 0.6940 | -0.0064 ± 0.0049 | 0.5829 ± 1.7415 | 0.1943 ± 0.5936 |
| UTIRIS_NIR | ResNet-18 | B2_minus_B1_mean | -1.0520 ± 0.5378 | 0.0069 ± 0.0034 | 3.4542 ± 0.3795 | 1.5112 ± 2.2819 |
| UTIRIS_NIR | ResNet-18 | nonannulus_mean_minus_black | -1.2845 ± 0.3989 | 0.0115 ± 0.0030 | 4.0803 ± 3.0844 | 3.5622 ± 1.8054 |
| UTIRIS_NIR | SwinV2-Tiny | B1_mean_minus_black | -0.0168 ± 2.7546 | -0.0005 ± 0.0204 | 5.0302 ± 10.5914 | 4.2314 ± 7.9350 |
| UTIRIS_NIR | SwinV2-Tiny | B2_mean_minus_black | 0.0478 ± 2.6963 | -0.0004 ± 0.0192 | 3.7133 ± 6.5739 | 2.7418 ± 7.3325 |
| UTIRIS_NIR | SwinV2-Tiny | B2_minus_B1_black | -0.0656 ± 0.2439 | 0.0007 ± 0.0016 | 0.7340 ± 1.5816 | -0.1727 ± 0.1870 |
| UTIRIS_NIR | SwinV2-Tiny | B2_minus_B1_mean | -0.0010 ± 0.5381 | 0.0009 ± 0.0049 | -0.5829 ± 3.1457 | -1.6623 ± 1.0688 |
| UTIRIS_NIR | SwinV2-Tiny | nonannulus_mean_minus_black | -1.4713 ± 0.9585 | 0.0096 ± 0.0050 | 4.2530 ± 1.6844 | 3.6485 ± 2.1986 |

## Changes in genuine similarity and high-similarity impostor tails

Cosine differences from raw baseline, mean ± sample SD across3 seeds; full per-seed values/distributions are saved.

| architecture | variant | kind | mean | p10 | p50 | p99 | p999 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_B1_black | genuine | +0.18035 ± 0.02089 | +0.31544 ± 0.03690 | +0.16299 ± 0.01803 |  |  |  |
| ResNet-18 | A_B1_black | impostor |  |  |  | +0.27065 ± 0.02791 | +0.19855 ± 0.01854 | +0.10542 ± 0.01905 |
| ResNet-18 | A_B1_mean | genuine | +0.14717 ± 0.02024 | +0.25166 ± 0.03724 | +0.13687 ± 0.01588 |  |  |  |
| ResNet-18 | A_B1_mean | impostor |  |  |  | +0.24848 ± 0.02469 | +0.18443 ± 0.01648 | +0.09800 ± 0.01531 |
| ResNet-18 | A_B2_black | genuine | +0.16883 ± 0.02466 | +0.29523 ± 0.04363 | +0.15459 ± 0.02084 |  |  |  |
| ResNet-18 | A_B2_black | impostor |  |  |  | +0.26164 ± 0.03129 | +0.19263 ± 0.02042 | +0.10393 ± 0.01683 |
| ResNet-18 | A_B2_mean | genuine | +0.13392 ± 0.02182 | +0.22834 ± 0.03872 | +0.12524 ± 0.01743 |  |  |  |
| ResNet-18 | A_B2_mean | impostor |  |  |  | +0.23337 ± 0.02660 | +0.17475 ± 0.01739 | +0.09314 ± 0.01743 |
| ResNet-18 | A_nonannulus_black | genuine | +0.06544 ± 0.02335 | +0.11180 ± 0.03949 | +0.06389 ± 0.02260 |  |  |  |
| ResNet-18 | A_nonannulus_black | impostor |  |  |  | +0.15303 ± 0.03384 | +0.11237 ± 0.02718 | +0.06143 ± 0.02284 |
| ResNet-18 | A_nonannulus_mean | genuine | +0.05354 ± 0.02243 | +0.08941 ± 0.03619 | +0.05401 ± 0.01997 |  |  |  |
| ResNet-18 | A_nonannulus_mean | impostor |  |  |  | +0.12892 ± 0.03249 | +0.09736 ± 0.02587 | +0.05265 ± 0.03028 |
| SwinV2-Tiny | A_B1_black | genuine | +0.14537 ± 0.02447 | +0.28970 ± 0.06148 | +0.11997 ± 0.01620 |  |  |  |
| SwinV2-Tiny | A_B1_black | impostor |  |  |  | +0.18691 ± 0.00112 | +0.12032 ± 0.00430 | +0.05341 ± 0.00832 |
| SwinV2-Tiny | A_B1_mean | genuine | +0.13850 ± 0.02290 | +0.26907 ± 0.05860 | +0.11695 ± 0.01326 |  |  |  |
| SwinV2-Tiny | A_B1_mean | impostor |  |  |  | +0.17905 ± 0.01850 | +0.11593 ± 0.00655 | +0.05440 ± 0.00933 |
| SwinV2-Tiny | A_B2_black | genuine | +0.13833 ± 0.02586 | +0.27558 ± 0.06211 | +0.11386 ± 0.01770 |  |  |  |
| SwinV2-Tiny | A_B2_black | impostor |  |  |  | +0.18012 ± 0.00205 | +0.11649 ± 0.00503 | +0.05189 ± 0.00640 |
| SwinV2-Tiny | A_B2_mean | genuine | +0.13356 ± 0.02328 | +0.26321 ± 0.06054 | +0.11166 ± 0.01368 |  |  |  |
| SwinV2-Tiny | A_B2_mean | impostor |  |  |  | +0.17487 ± 0.01535 | +0.11335 ± 0.00552 | +0.05065 ± 0.01051 |
| SwinV2-Tiny | A_nonannulus_black | genuine | +0.01435 ± 0.03649 | +0.01174 ± 0.07280 | +0.01682 ± 0.02989 |  |  |  |
| SwinV2-Tiny | A_nonannulus_black | impostor |  |  |  | +0.07095 ± 0.04795 | +0.04971 ± 0.03035 | +0.03019 ± 0.01400 |
| SwinV2-Tiny | A_nonannulus_mean | genuine | -0.01127 ± 0.01388 | -0.03867 ± 0.03132 | -0.00289 ± 0.01189 |  |  |  |
| SwinV2-Tiny | A_nonannulus_mean | impostor |  |  |  | +0.03306 ± 0.02719 | +0.02643 ± 0.01690 | +0.02339 ± 0.02416 |

## Subject influence

Remove each subject and all incident comparisons, recompute all4 metrics, and pair against the same raw baseline removal. Table summarizes the mean EER effect across3 seeds. Complete per-seed/four-metric effects and subject identifiers are saved.

| dataset | architecture | variant | full_mean_eer_effect_pp | loo_min_mean_effect_pp | loo_max_mean_effect_pp | sign_reversals | reversing_subjects | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | A_B1_black | 6.41192 | 6.13566 | 6.72193 | 0 |  | 077 | 0.31001 |
| UTIRIS_NIR | ResNet-18 | A_B1_mean | 7.41688 | 7.08348 | 7.72248 | 0 |  | 041 | 0.33341 |
| UTIRIS_NIR | ResNet-18 | A_B2_black | 6.56692 | 6.29531 | 6.8875 | 0 |  | 077 | 0.32058 |
| UTIRIS_NIR | ResNet-18 | A_B2_mean | 6.36492 | 6.07906 | 6.71267 | 0 |  | 077 | 0.34775 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_black | 6.35756 | 6.16787 | 6.57564 | 0 |  | 061 | 0.21808 |
| UTIRIS_NIR | ResNet-18 | A_nonannulus_mean | 5.07301 | 4.87913 | 5.18919 | 0 |  | 043 | 0.19388 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_black | 2.98071 | 2.62145 | 3.36485 | 0 |  | 077 | 0.38414 |
| UTIRIS_NIR | SwinV2-Tiny | A_B1_mean | 2.9639 | 2.68679 | 3.21867 | 0 |  | 007 | 0.27711 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_black | 2.91511 | 2.6054 | 3.34268 | 0 |  | 077 | 0.42757 |
| UTIRIS_NIR | SwinV2-Tiny | A_B2_mean | 2.96293 | 2.6716 | 3.20304 | 0 |  | 007 | 0.29133 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_black | 4.53003 | 4.28862 | 4.6813 | 0 |  | 029 | 0.24141 |
| UTIRIS_NIR | SwinV2-Tiny | A_nonannulus_mean | 3.05878 | 2.93046 | 3.2272 | 0 |  | 026 | 0.16842 |

## Individual seed results

| architecture | variant | seed | selected_epoch | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 42 | 64 | 7.318653 | 0.981766 | 80.699482 | 60.621762 |
| ResNet-18 | A_B1_black | 42 | 64 | 13.406736 | 0.942575 | 51.360104 | 25.971503 |
| ResNet-18 | A_B2_black | 42 | 64 | 13.423444 | 0.932963 | 52.849741 | 26.295337 |
| ResNet-18 | A_B1_mean | 42 | 64 | 12.435233 | 0.949426 | 50.323834 | 26.42487 |
| ResNet-18 | A_B2_mean | 42 | 64 | 11.981865 | 0.952756 | 54.209845 | 25.388601 |
| ResNet-18 | A_nonannulus_black | 42 | 64 | 14.572539 | 0.929353 | 56.541451 | 32.189119 |
| ResNet-18 | A_nonannulus_mean | 42 | 64 | 13.729397 | 0.937659 | 58.290155 | 36.26943 |
| ResNet-18 | A_A | 123 | 110 | 6.994819 | 0.977839 | 79.145078 | 59.715026 |
| ResNet-18 | A_B1_black | 123 | 110 | 13.471503 | 0.941666 | 49.676166 | 24.222798 |
| ResNet-18 | A_B2_black | 123 | 110 | 13.012067 | 0.940943 | 51.360104 | 24.935233 |
| ResNet-18 | A_B1_mean | 123 | 110 | 15.673575 | 0.921226 | 43.717617 | 20.854922 |
| ResNet-18 | A_B2_mean | 123 | 110 | 14.179138 | 0.931403 | 47.020725 | 24.222798 |
| ResNet-18 | A_nonannulus_black | 123 | 110 | 12.888601 | 0.939692 | 62.046632 | 40.479275 |
| ResNet-18 | A_nonannulus_mean | 123 | 110 | 11.26943 | 0.951854 | 64.96114 | 42.033679 |
| ResNet-18 | A_A | 2025 | 114 | 6.606218 | 0.981419 | 80.958549 | 58.549223 |
| ResNet-18 | A_B1_black | 2025 | 114 | 13.277202 | 0.941888 | 49.287565 | 24.158031 |
| ResNet-18 | A_B2_black | 2025 | 114 | 14.184947 | 0.933159 | 47.862694 | 23.704663 |
| ResNet-18 | A_B1_mean | 2025 | 114 | 15.061532 | 0.931073 | 44.818653 | 22.927461 |
| ResNet-18 | A_B2_mean | 2025 | 114 | 13.853451 | 0.938358 | 47.992228 | 25.129534 |
| ResNet-18 | A_nonannulus_black | 2025 | 114 | 12.531227 | 0.939684 | 59.585492 | 39.248705 |
| ResNet-18 | A_nonannulus_mean | 2025 | 114 | 11.139896 | 0.953808 | 67.163212 | 44.300518 |
| SwinV2-Tiny | A_A | 42 | 35 | 9.057014 | 0.970059 | 68.782383 | 46.373057 |
| SwinV2-Tiny | A_B1_black | 42 | 35 | 10.816062 | 0.957638 | 47.279793 | 18.005181 |
| SwinV2-Tiny | A_B2_black | 42 | 35 | 10.945596 | 0.957829 | 49.287565 | 17.61658 |
| SwinV2-Tiny | A_B1_mean | 42 | 35 | 8.873057 | 0.972328 | 63.73057 | 31.282383 |
| SwinV2-Tiny | A_B2_mean | 42 | 35 | 9.391192 | 0.96842 | 59.585492 | 28.562176 |
| SwinV2-Tiny | A_nonannulus_black | 42 | 35 | 14.637306 | 0.932344 | 52.784974 | 32.448187 |
| SwinV2-Tiny | A_nonannulus_mean | 42 | 35 | 12.425627 | 0.947615 | 58.743523 | 35.686528 |
| SwinV2-Tiny | A_A | 123 | 31 | 7.566308 | 0.978777 | 74.417098 | 49.222798 |
| SwinV2-Tiny | A_B1_black | 123 | 31 | 10.621762 | 0.963197 | 58.937824 | 28.88601 |
| SwinV2-Tiny | A_B2_black | 123 | 31 | 10.634524 | 0.962656 | 57.901554 | 28.821244 |
| SwinV2-Tiny | A_B1_mean | 123 | 31 | 13.760154 | 0.939492 | 54.468912 | 27.331606 |
| SwinV2-Tiny | A_B2_mean | 123 | 31 | 13.795337 | 0.940109 | 55.051813 | 25.647668 |
| SwinV2-Tiny | A_nonannulus_black | 123 | 31 | 12.759067 | 0.947421 | 56.735751 | 31.670984 |
| SwinV2-Tiny | A_nonannulus_mean | 123 | 31 | 10.945596 | 0.954949 | 60.945596 | 37.694301 |
| SwinV2-Tiny | A_A | 2025 | 23 | 13.245139 | 0.943951 | 58.354922 | 39.313472 |
| SwinV2-Tiny | A_B1_black | 2025 | 23 | 17.372776 | 0.912591 | 32.901554 | 13.536269 |
| SwinV2-Tiny | A_B2_black | 2025 | 23 | 17.033679 | 0.915175 | 34.132124 | 13.471503 |
| SwinV2-Tiny | A_B1_mean | 2025 | 23 | 16.126943 | 0.920017 | 36.010363 | 14.507772 |
| SwinV2-Tiny | A_B2_mean | 2025 | 23 | 15.570737 | 0.925934 | 37.823834 | 13.92487 |
| SwinV2-Tiny | A_nonannulus_black | 2025 | 23 | 16.062176 | 0.923907 | 51.165803 | 30.829016 |
| SwinV2-Tiny | A_nonannulus_mean | 2025 | 23 | 15.673575 | 0.929866 | 53.756477 | 32.512953 |

## Input statistics and QC examples

| dataset | variant | images | replaced_pixels_median | retained_pixels_median | padding_pixels_median | replaced_intensity_l1_median | content_mean_median | content_std_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | A_A | 770 | 0.0 | 79360.0 | 23040.0 | 0.0 | 0.460499 | 0.173797 |
| UTIRIS_NIR | A_B1_black | 770 | 62646.0 | 16919.0 | 23040.0 | 0.484325 | 0.073535 | 0.145041 |
| UTIRIS_NIR | A_B1_mean | 770 | 62646.0 | 16919.0 | 23040.0 | 0.157105 | 0.454716 | 0.067599 |
| UTIRIS_NIR | A_B2_black | 770 | 63709.0 | 15797.0 | 23040.0 | 0.481411 | 0.070571 | 0.144056 |
| UTIRIS_NIR | A_B2_mean | 770 | 63709.0 | 15797.0 | 23040.0 | 0.160939 | 0.460949 | 0.055131 |
| UTIRIS_NIR | A_nonannulus_black | 770 | 16919.0 | 62646.0 | 23040.0 | 0.345399 | 0.381033 | 0.255858 |
| UTIRIS_NIR | A_nonannulus_mean | 770 | 16919.0 | 62646.0 | 23040.0 | 0.139214 | 0.484 | 0.161535 |

Examples were chosen as the first3 common subjects by image ID, before recognition scoring.









