# CASIA-Interval: separate E2-E analysis

## Absolute metrics

EER/TAR percent; AUC[0,1]. Mean ± sample SD over all3 seeds.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | A_A | 2.1015 ± 0.6675 | 0.9969 ± 0.0006 | 95.8364 ± 2.0765 | 84.9470 ± 6.8503 |
| CASIA-Interval | ResNet-18 | A_B1_black | 9.3980 ± 1.4853 | 0.9672 ± 0.0085 | 67.9901 ± 5.7032 | 41.6851 ± 10.8678 |
| CASIA-Interval | ResNet-18 | A_B1_mean | 6.7959 ± 0.7185 | 0.9792 ± 0.0028 | 76.6199 ± 3.3646 | 56.3686 ± 6.4273 |
| CASIA-Interval | ResNet-18 | A_B2_black | 10.9834 ± 1.0742 | 0.9562 ± 0.0063 | 58.2902 ± 3.0736 | 28.8741 ± 5.1042 |
| CASIA-Interval | ResNet-18 | A_B2_mean | 7.1600 ± 0.5932 | 0.9779 ± 0.0048 | 78.7140 ± 2.6975 | 57.7729 ± 3.1878 |
| CASIA-Interval | ResNet-18 | A_nonannulus_black | 7.5388 ± 0.5174 | 0.9776 ± 0.0018 | 78.8125 ± 0.4071 | 58.4873 ± 0.9646 |
| CASIA-Interval | ResNet-18 | A_nonannulus_mean | 7.0572 ± 0.7352 | 0.9781 ± 0.0042 | 81.2023 ± 2.2664 | 61.5176 ± 0.4921 |
| CASIA-Interval | SwinV2-Tiny | A_A | 3.3059 ± 0.3567 | 0.9953 ± 0.0003 | 93.1017 ± 1.2915 | 81.1530 ± 4.9154 |
| CASIA-Interval | SwinV2-Tiny | A_B1_black | 6.1501 ± 0.3981 | 0.9839 ± 0.0028 | 71.1752 ± 8.0195 | 44.7401 ± 11.5792 |
| CASIA-Interval | SwinV2-Tiny | A_B1_mean | 6.7191 ± 0.7797 | 0.9836 ± 0.0041 | 70.7563 ± 7.3026 | 41.0446 ± 11.0337 |
| CASIA-Interval | SwinV2-Tiny | A_B2_black | 6.5254 ± 0.4408 | 0.9809 ± 0.0037 | 71.0027 ± 9.7231 | 44.7401 ± 12.5247 |
| CASIA-Interval | SwinV2-Tiny | A_B2_mean | 6.5985 ± 0.3379 | 0.9830 ± 0.0019 | 71.2737 ± 5.9060 | 42.8431 ± 10.2775 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_black | 6.1838 ± 0.8941 | 0.9837 ± 0.0048 | 80.5371 ± 3.9000 | 56.7135 ± 3.3238 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_mean | 5.8069 ± 0.3087 | 0.9863 ± 0.0022 | 83.0007 ± 3.0483 | 62.7248 ± 4.7165 |

## Paired intervention minus raw baseline

All differences use the SAME checkpoint and exact pairs. EER/TAR differences are percentage points; AUC differences are on[0,1]. Negative EER differences indicate lower EER.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | A_B1_black | 7.2965 ± 1.9010 | -0.0297 ± 0.0091 | -27.8463 ± 7.1811 | -43.2619 ± 13.3571 |
| CASIA-Interval | ResNet-18 | A_B1_mean | 4.6944 ± 1.0254 | -0.0177 ± 0.0023 | -19.2166 ± 2.7045 | -28.5785 ± 9.7161 |
| CASIA-Interval | ResNet-18 | A_B2_black | 8.8819 ± 1.4953 | -0.0406 ± 0.0069 | -37.5462 ± 3.5569 | -56.0729 ± 7.1933 |
| CASIA-Interval | ResNet-18 | A_B2_mean | 5.0585 ± 0.7956 | -0.0190 ± 0.0049 | -17.1224 ± 1.3735 | -27.1742 ± 3.7580 |
| CASIA-Interval | ResNet-18 | A_nonannulus_black | 5.4373 ± 0.3088 | -0.0193 ± 0.0012 | -17.0239 ± 1.7836 | -26.4597 ± 6.3200 |
| CASIA-Interval | ResNet-18 | A_nonannulus_mean | 4.9557 ± 1.0439 | -0.0188 ± 0.0048 | -14.6341 ± 3.2913 | -23.4294 ± 6.3678 |
| CASIA-Interval | SwinV2-Tiny | A_B1_black | 2.8443 ± 0.4275 | -0.0114 ± 0.0027 | -21.9266 ± 8.9490 | -36.4129 ± 14.5556 |
| CASIA-Interval | SwinV2-Tiny | A_B1_mean | 3.4133 ± 0.7901 | -0.0117 ± 0.0042 | -22.3454 ± 7.8052 | -40.1084 ± 12.7499 |
| CASIA-Interval | SwinV2-Tiny | A_B2_black | 3.2195 ± 0.7455 | -0.0144 ± 0.0035 | -22.0990 ± 10.8944 | -36.4129 ± 16.1026 |
| CASIA-Interval | SwinV2-Tiny | A_B2_mean | 3.2926 ± 0.6217 | -0.0123 ± 0.0017 | -21.8280 ± 7.0433 | -38.3099 ± 13.7473 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_black | 2.8779 ± 0.5406 | -0.0116 ± 0.0050 | -12.5647 ± 2.8520 | -24.4395 ± 2.9054 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_mean | 2.5011 ± 0.1828 | -0.0090 ± 0.0025 | -10.1010 ± 2.1374 | -18.4282 ± 3.5953 |

## Predefined mean-minus-black and B2-minus-B1 controls

| dataset | architecture | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | B1_mean_minus_black | -2.6021 ± 2.1176 | 0.0120 ± 0.0107 | 8.6297 ± 9.0666 | 14.6834 ± 17.2434 |
| CASIA-Interval | ResNet-18 | B2_mean_minus_black | -3.8234 ± 0.7114 | 0.0217 ± 0.0057 | 20.4237 ± 2.6866 | 28.8987 ± 5.6622 |
| CASIA-Interval | ResNet-18 | B2_minus_B1_black | 1.5854 ± 0.4153 | -0.0110 ± 0.0023 | -9.6999 ± 4.0638 | -12.8110 ± 6.4739 |
| CASIA-Interval | ResNet-18 | B2_minus_B1_mean | 0.3641 ± 1.3096 | -0.0013 ± 0.0046 | 2.0941 ± 4.0659 | 1.4043 ± 6.8525 |
| CASIA-Interval | ResNet-18 | nonannulus_mean_minus_black | -0.4816 ± 0.7361 | 0.0005 ± 0.0060 | 2.3898 ± 2.0831 | 3.0303 ± 0.8714 |
| CASIA-Interval | SwinV2-Tiny | B1_mean_minus_black | 0.5690 ± 0.3932 | -0.0003 ± 0.0021 | -0.4188 ± 3.3393 | -3.6955 ± 3.8234 |
| CASIA-Interval | SwinV2-Tiny | B2_mean_minus_black | 0.0731 ± 0.5778 | 0.0021 ± 0.0019 | 0.2710 ± 3.8662 | -1.8970 ± 2.3574 |
| CASIA-Interval | SwinV2-Tiny | B2_minus_B1_black | 0.3752 ± 0.4787 | -0.0029 ± 0.0019 | -0.1725 ± 3.5893 | -0.0000 ± 2.5646 |
| CASIA-Interval | SwinV2-Tiny | B2_minus_B1_mean | -0.1206 ± 1.0944 | -0.0006 ± 0.0034 | 0.5174 ± 4.7630 | 1.7985 ± 5.0353 |
| CASIA-Interval | SwinV2-Tiny | nonannulus_mean_minus_black | -0.3769 ± 0.6274 | 0.0025 ± 0.0025 | 2.4637 ± 0.9241 | 6.0113 ± 1.5189 |

## Changes in genuine similarity and high-similarity impostor tails

Cosine differences from raw baseline, mean ± sample SD across3 seeds; full per-seed values/distributions are saved.

| architecture | variant | kind | mean | p10 | p50 | p99 | p999 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_B1_black | genuine | +0.13516 ± 0.03070 | +0.24136 ± 0.06906 | +0.11536 ± 0.02191 |  |  |  |
| ResNet-18 | A_B1_black | impostor |  |  |  | +0.37568 ± 0.01280 | +0.25424 ± 0.02194 | +0.13871 ± 0.02046 |
| ResNet-18 | A_B1_mean | genuine | +0.08260 ± 0.03532 | +0.14776 ± 0.07444 | +0.07083 ± 0.02633 |  |  |  |
| ResNet-18 | A_B1_mean | impostor |  |  |  | +0.29313 ± 0.02755 | +0.19488 ± 0.02591 | +0.10476 ± 0.03336 |
| ResNet-18 | A_B2_black | genuine | +0.10905 ± 0.03724 | +0.19365 ± 0.08300 | +0.09326 ± 0.02548 |  |  |  |
| ResNet-18 | A_B2_black | impostor |  |  |  | +0.35620 ± 0.01760 | +0.24517 ± 0.02190 | +0.13705 ± 0.01866 |
| ResNet-18 | A_B2_mean | genuine | +0.07785 ± 0.03645 | +0.13919 ± 0.08033 | +0.06615 ± 0.02680 |  |  |  |
| ResNet-18 | A_B2_mean | impostor |  |  |  | +0.28544 ± 0.02943 | +0.18827 ± 0.01933 | +0.10130 ± 0.03509 |
| ResNet-18 | A_nonannulus_black | genuine | +0.09511 ± 0.02057 | +0.17493 ± 0.04422 | +0.07791 ± 0.01674 |  |  |  |
| ResNet-18 | A_nonannulus_black | impostor |  |  |  | +0.30877 ± 0.01630 | +0.20174 ± 0.02568 | +0.10179 ± 0.03095 |
| ResNet-18 | A_nonannulus_mean | genuine | +0.07344 ± 0.01032 | +0.13139 ± 0.02448 | +0.06252 ± 0.00453 |  |  |  |
| ResNet-18 | A_nonannulus_mean | impostor |  |  |  | +0.27011 ± 0.01598 | +0.17688 ± 0.02527 | +0.09243 ± 0.02053 |
| SwinV2-Tiny | A_B1_black | genuine | +0.07392 ± 0.00665 | +0.15462 ± 0.01979 | +0.05200 ± 0.00358 |  |  |  |
| SwinV2-Tiny | A_B1_black | impostor |  |  |  | +0.26318 ± 0.04512 | +0.17383 ± 0.04354 | +0.09318 ± 0.02261 |
| SwinV2-Tiny | A_B1_mean | genuine | +0.05948 ± 0.00475 | +0.12383 ± 0.02189 | +0.03937 ± 0.00241 |  |  |  |
| SwinV2-Tiny | A_B1_mean | impostor |  |  |  | +0.24703 ± 0.03850 | +0.16722 ± 0.03925 | +0.09456 ± 0.02268 |
| SwinV2-Tiny | A_B2_black | genuine | +0.05378 ± 0.00275 | +0.12319 ± 0.00814 | +0.03601 ± 0.00528 |  |  |  |
| SwinV2-Tiny | A_B2_black | impostor |  |  |  | +0.24000 ± 0.04844 | +0.15983 ± 0.04590 | +0.09063 ± 0.02420 |
| SwinV2-Tiny | A_B2_mean | genuine | +0.06463 ± 0.00600 | +0.14261 ± 0.01528 | +0.04133 ± 0.00744 |  |  |  |
| SwinV2-Tiny | A_B2_mean | impostor |  |  |  | +0.25299 ± 0.03197 | +0.16645 ± 0.03684 | +0.09561 ± 0.02456 |
| SwinV2-Tiny | A_nonannulus_black | genuine | +0.04278 ± 0.02077 | +0.09455 ± 0.04832 | +0.02596 ± 0.01349 |  |  |  |
| SwinV2-Tiny | A_nonannulus_black | impostor |  |  |  | +0.19995 ± 0.05200 | +0.13321 ± 0.04801 | +0.08228 ± 0.02316 |
| SwinV2-Tiny | A_nonannulus_mean | genuine | +0.01714 ± 0.01586 | +0.03666 ± 0.03070 | +0.00991 ± 0.01079 |  |  |  |
| SwinV2-Tiny | A_nonannulus_mean | impostor |  |  |  | +0.14492 ± 0.04718 | +0.09850 ± 0.04170 | +0.05575 ± 0.02652 |

## Subject influence

Remove each subject and all incident comparisons, recompute all4 metrics, and pair against the same raw baseline removal. Table summarizes the mean EER effect across3 seeds. Complete per-seed/four-metric effects and subject identifiers are saved.

| dataset | architecture | variant | full_mean_eer_effect_pp | loo_min_mean_effect_pp | loo_max_mean_effect_pp | sign_reversals | reversing_subjects | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | A_B1_black | 7.2965 | 6.52466 | 7.59801 | 0 |  | 218 | 0.77184 |
| CASIA-Interval | ResNet-18 | A_B1_mean | 4.69443 | 4.2826 | 5.0861 | 0 |  | 096 | 0.41183 |
| CASIA-Interval | ResNet-18 | A_B2_black | 8.88191 | 8.32973 | 9.43397 | 0 |  | 125 | 0.55218 |
| CASIA-Interval | ResNet-18 | A_B2_mean | 5.05853 | 4.59694 | 5.45837 | 0 |  | 028 | 0.4616 |
| CASIA-Interval | ResNet-18 | A_nonannulus_black | 5.43733 | 4.74897 | 5.59618 | 0 |  | 125 | 0.68835 |
| CASIA-Interval | ResNet-18 | A_nonannulus_mean | 4.95568 | 4.07363 | 5.23814 | 0 |  | 218 | 0.88205 |
| CASIA-Interval | SwinV2-Tiny | A_B1_black | 2.84427 | 2.54744 | 3.3186 | 0 |  | 182 | 0.47432 |
| CASIA-Interval | SwinV2-Tiny | A_B1_mean | 3.41328 | 3.02268 | 3.89527 | 0 |  | 188 | 0.48198 |
| CASIA-Interval | SwinV2-Tiny | A_B2_black | 3.2195 | 2.94876 | 3.69868 | 0 |  | 188 | 0.47918 |
| CASIA-Interval | SwinV2-Tiny | A_B2_mean | 3.29264 | 3.08505 | 3.80295 | 0 |  | 188 | 0.51031 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_black | 2.87792 | 2.48857 | 3.17852 | 0 |  | 028 | 0.38935 |
| CASIA-Interval | SwinV2-Tiny | A_nonannulus_mean | 2.50106 | 2.11382 | 2.65992 | 0 |  | 028 | 0.38725 |

## Individual seed results

| architecture | variant | seed | selected_epoch | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 42 | 64 | 2.734664 | 0.996769 | 93.865484 | 77.087953 |
| ResNet-18 | A_B1_black | 42 | 64 | 9.569295 | 0.966721 | 68.419808 | 41.389505 |
| ResNet-18 | A_B2_black | 42 | 64 | 11.164842 | 0.954889 | 56.023651 | 26.459719 |
| ResNet-18 | A_B1_mean | 42 | 64 | 6.261292 | 0.977102 | 76.496674 | 57.723577 |
| ResNet-18 | A_B2_mean | 42 | 64 | 7.65889 | 0.972727 | 75.609756 | 54.249815 |
| ResNet-18 | A_nonannulus_black | 42 | 64 | 8.130081 | 0.976788 | 78.34442 | 57.723577 |
| ResNet-18 | A_nonannulus_mean | 42 | 64 | 7.464893 | 0.980179 | 80.044346 | 60.97561 |
| ResNet-18 | A_A | 123 | 110 | 1.404287 | 0.997519 | 98.004435 | 89.652624 |
| ResNet-18 | A_B1_black | 123 | 110 | 10.790201 | 0.95899 | 62.084257 | 30.968219 |
| ResNet-18 | A_B2_black | 123 | 110 | 11.955309 | 0.950688 | 57.058389 | 25.424982 |
| ResNet-18 | A_B1_mean | 123 | 110 | 6.51371 | 0.982383 | 80.044346 | 62.010347 |
| ResNet-18 | A_B2_mean | 123 | 110 | 7.317073 | 0.978921 | 80.487805 | 60.458241 |
| ResNet-18 | A_nonannulus_black | 123 | 110 | 7.169254 | 0.979611 | 79.009608 | 58.167036 |
| ResNet-18 | A_nonannulus_mean | 123 | 110 | 7.49814 | 0.973186 | 79.748707 | 61.936438 |
| ResNet-18 | A_A | 2025 | 114 | 2.16548 | 0.996328 | 95.63932 | 88.100517 |
| ResNet-18 | A_B1_black | 2025 | 114 | 7.834442 | 0.975903 | 73.466371 | 52.697709 |
| ResNet-18 | A_B2_black | 2025 | 114 | 9.830007 | 0.963163 | 61.788618 | 34.73762 |
| ResNet-18 | A_B1_mean | 2025 | 114 | 7.612712 | 0.978087 | 73.318551 | 49.371766 |
| ResNet-18 | A_B2_mean | 2025 | 114 | 6.504065 | 0.982104 | 80.044346 | 58.610495 |
| ResNet-18 | A_nonannulus_black | 2025 | 114 | 7.317073 | 0.976254 | 79.083518 | 59.571323 |
| ResNet-18 | A_nonannulus_mean | 2025 | 114 | 6.208426 | 0.980827 | 83.813747 | 61.640798 |
| SwinV2-Tiny | A_A | 42 | 35 | 2.896163 | 0.994989 | 94.530673 | 86.104952 |
| SwinV2-Tiny | A_B1_black | 42 | 35 | 6.028802 | 0.981489 | 63.192905 | 33.481153 |
| SwinV2-Tiny | A_B2_black | 42 | 35 | 6.937507 | 0.976744 | 59.940872 | 31.263858 |
| SwinV2-Tiny | A_B1_mean | 42 | 35 | 6.631948 | 0.981952 | 65.927568 | 33.185514 |
| SwinV2-Tiny | A_B2_mean | 42 | 35 | 6.799704 | 0.980908 | 64.671101 | 32.076866 |
| SwinV2-Tiny | A_nonannulus_black | 42 | 35 | 5.173688 | 0.988774 | 84.922395 | 60.532151 |
| SwinV2-Tiny | A_nonannulus_mean | 42 | 35 | 5.521309 | 0.988533 | 86.326681 | 67.997044 |
| SwinV2-Tiny | A_A | 123 | 31 | 3.473762 | 0.995346 | 92.756837 | 81.079084 |
| SwinV2-Tiny | A_B1_black | 123 | 31 | 5.826868 | 0.986902 | 79.231338 | 56.61493 |
| SwinV2-Tiny | A_B2_black | 123 | 31 | 6.060606 | 0.983891 | 78.1966 | 56.023651 |
| SwinV2-Tiny | A_B1_mean | 123 | 31 | 5.986696 | 0.988271 | 79.157428 | 53.658537 |
| SwinV2-Tiny | A_B2_mean | 123 | 31 | 6.787384 | 0.984601 | 76.053215 | 52.549889 |
| SwinV2-Tiny | A_nonannulus_black | 123 | 31 | 6.504065 | 0.983081 | 77.457502 | 54.471545 |
| SwinV2-Tiny | A_nonannulus_mean | 123 | 31 | 5.764967 | 0.986174 | 80.339985 | 58.906135 |
| SwinV2-Tiny | A_A | 2025 | 23 | 3.547672 | 0.995565 | 92.017738 | 76.274945 |
| SwinV2-Tiny | A_B1_black | 2025 | 23 | 6.59475 | 0.983177 | 71.101256 | 44.124169 |
| SwinV2-Tiny | A_B2_black | 2025 | 23 | 6.577975 | 0.982186 | 74.870658 | 46.932742 |
| SwinV2-Tiny | A_B1_mean | 2025 | 23 | 7.538803 | 0.980481 | 67.184035 | 36.289727 |
| SwinV2-Tiny | A_B2_mean | 2025 | 23 | 6.208426 | 0.98347 | 73.096822 | 43.902439 |
| SwinV2-Tiny | A_nonannulus_black | 2025 | 23 | 6.873614 | 0.979332 | 79.231338 | 55.136733 |
| SwinV2-Tiny | A_nonannulus_mean | 2025 | 23 | 6.134516 | 0.984053 | 82.335551 | 61.271249 |

## Input statistics and QC examples

| dataset | variant | images | replaced_pixels_median | retained_pixels_median | padding_pixels_median | replaced_intensity_l1_median | content_mean_median | content_std_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | A_A | 395 | 0.0 | 89600.0 | 12800.0 | 0.0 | 0.694781 | 0.190991 |
| CASIA-Interval | A_B1_black | 395 | 63991.0 | 25609.0 | 12800.0 | 0.732122 | 0.169065 | 0.266714 |
| CASIA-Interval | A_B1_mean | 395 | 63991.0 | 25609.0 | 12800.0 | 0.301175 | 0.5127 | 0.062402 |
| CASIA-Interval | A_B2_black | 395 | 66926.0 | 22674.0 | 12800.0 | 0.722795 | 0.151788 | 0.262016 |
| CASIA-Interval | A_B2_mean | 395 | 66926.0 | 22674.0 | 12800.0 | 0.295348 | 0.512657 | 0.060637 |
| CASIA-Interval | A_nonannulus_black | 395 | 25609.0 | 63991.0 | 12800.0 | 0.593437 | 0.52368 | 0.375374 |
| CASIA-Interval | A_nonannulus_mean | 395 | 25609.0 | 63991.0 | 12800.0 | 0.119651 | 0.666207 | 0.213706 |

Examples were chosen as the first3 common subjects by image ID, before recognition scoring.









