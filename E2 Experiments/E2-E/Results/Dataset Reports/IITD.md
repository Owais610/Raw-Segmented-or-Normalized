# IITD: separate E2-E analysis

## Absolute metrics

EER/TAR percent; AUC[0,1]. Mean ± sample SD over all3 seeds.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | A_A | 0.7598 ± 0.3596 | 0.9997 ± 0.0003 | 99.3631 ± 0.5516 | 96.8684 ± 0.6435 |
| IITD | ResNet-18 | A_B1_black | 3.2196 ± 0.2327 | 0.9936 ± 0.0019 | 94.2144 ± 1.0602 | 88.0042 ± 3.2724 |
| IITD | ResNet-18 | A_B1_mean | 3.6982 ± 0.7210 | 0.9914 ± 0.0003 | 94.0021 ± 1.3354 | 88.4820 ± 3.7727 |
| IITD | ResNet-18 | A_B2_black | 3.4352 ± 0.3803 | 0.9932 ± 0.0019 | 94.2144 ± 0.4597 | 87.1550 ± 1.6877 |
| IITD | ResNet-18 | A_B2_mean | 3.5707 ± 0.9685 | 0.9919 ± 0.0014 | 93.6837 ± 1.7756 | 87.5796 ± 5.1030 |
| IITD | ResNet-18 | A_nonannulus_black | 3.1847 ± 0.6369 | 0.9949 ± 0.0032 | 95.0106 ± 1.1952 | 90.1274 ± 0.5741 |
| IITD | ResNet-18 | A_nonannulus_mean | 2.8662 ± 0.7297 | 0.9944 ± 0.0041 | 95.5945 ± 0.7855 | 89.7558 ± 1.1952 |
| IITD | SwinV2-Tiny | A_A | 1.6120 ± 0.5075 | 0.9986 ± 0.0009 | 98.0892 ± 0.7962 | 95.1168 ± 2.9591 |
| IITD | SwinV2-Tiny | A_B1_black | 2.6834 ± 0.5441 | 0.9967 ± 0.0022 | 95.1699 ± 1.7027 | 88.1635 ± 5.4753 |
| IITD | SwinV2-Tiny | A_B1_mean | 2.5325 ± 0.3628 | 0.9961 ± 0.0025 | 96.4437 ± 0.6630 | 90.9236 ± 2.2965 |
| IITD | SwinV2-Tiny | A_B2_black | 2.9895 ± 0.8474 | 0.9959 ± 0.0026 | 94.2144 ± 2.2369 | 84.0764 ± 6.8026 |
| IITD | SwinV2-Tiny | A_B2_mean | 2.9724 ± 0.0919 | 0.9951 ± 0.0022 | 95.2229 ± 0.4213 | 89.4904 ± 0.9944 |
| IITD | SwinV2-Tiny | A_nonannulus_black | 2.6450 ± 1.0975 | 0.9963 ± 0.0017 | 95.0106 ± 2.4167 | 90.2866 ± 0.8866 |
| IITD | SwinV2-Tiny | A_nonannulus_mean | 2.8254 ± 0.7160 | 0.9960 ± 0.0017 | 94.4798 ± 1.5301 | 90.4989 ± 1.1519 |

## Paired intervention minus raw baseline

All differences use the SAME checkpoint and exact pairs. EER/TAR differences are percentage points; AUC differences are on[0,1]. Negative EER differences indicate lower EER.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | A_B1_black | 2.4599 ± 0.4098 | -0.0061 ± 0.0017 | -5.1486 ± 1.0839 | -8.8641 ± 3.3791 |
| IITD | ResNet-18 | A_B1_mean | 2.9385 ± 0.5324 | -0.0083 ± 0.0001 | -5.3609 ± 1.1952 | -8.3864 ± 4.1534 |
| IITD | ResNet-18 | A_B2_black | 2.6754 ± 0.1684 | -0.0064 ± 0.0017 | -5.1486 ± 0.5119 | -9.7134 ± 2.2965 |
| IITD | ResNet-18 | A_B2_mean | 2.8109 ± 0.6142 | -0.0078 ± 0.0011 | -5.6794 ± 1.4795 | -9.2887 ± 5.1088 |
| IITD | ResNet-18 | A_nonannulus_black | 2.4249 ± 0.3121 | -0.0047 ± 0.0029 | -4.3524 ± 0.7525 | -6.7410 ± 0.1839 |
| IITD | ResNet-18 | A_nonannulus_mean | 2.1065 ± 0.4459 | -0.0053 ± 0.0038 | -3.7686 ± 0.7525 | -7.1125 ± 1.3354 |
| IITD | SwinV2-Tiny | A_B1_black | 1.0714 ± 0.2194 | -0.0019 ± 0.0014 | -2.9193 ± 0.9330 | -6.9533 ± 2.5295 |
| IITD | SwinV2-Tiny | A_B1_mean | 0.9205 ± 0.3554 | -0.0025 ± 0.0016 | -1.6454 ± 0.5592 | -4.1932 ± 0.8015 |
| IITD | SwinV2-Tiny | A_B2_black | 1.3775 ± 0.3430 | -0.0027 ± 0.0018 | -3.8747 ± 1.4449 | -11.0403 ± 4.5048 |
| IITD | SwinV2-Tiny | A_B2_mean | 1.3604 ± 0.5127 | -0.0035 ± 0.0013 | -2.8662 ± 1.1483 | -5.6263 ± 3.9080 |
| IITD | SwinV2-Tiny | A_nonannulus_black | 1.0330 ± 1.2224 | -0.0024 ± 0.0012 | -3.0786 ± 2.2538 | -4.8301 ± 3.7355 |
| IITD | SwinV2-Tiny | A_nonannulus_mean | 1.2134 ± 0.6456 | -0.0027 ± 0.0009 | -3.6093 ± 1.2057 | -4.6178 ± 3.7037 |

## Predefined mean-minus-black and B2-minus-B1 controls

| dataset | architecture | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | B1_mean_minus_black | 0.4786 ± 0.5614 | -0.0022 ± 0.0016 | -0.2123 ± 0.4007 | 0.4777 ± 1.7945 |
| IITD | ResNet-18 | B2_mean_minus_black | 0.1355 ± 0.6192 | -0.0014 ± 0.0015 | -0.5308 ± 1.3259 | 0.4246 ± 4.8229 |
| IITD | ResNet-18 | B2_minus_B1_black | 0.2156 ± 0.3263 | -0.0003 ± 0.0001 | 0.0000 ± 0.6369 | -0.8493 ± 2.9462 |
| IITD | ResNet-18 | B2_minus_B1_mean | -0.1275 ± 0.5900 | 0.0004 ± 0.0011 | -0.3185 ± 0.5741 | -0.9023 ± 2.9889 |
| IITD | ResNet-18 | nonannulus_mean_minus_black | -0.3185 ± 0.1592 | -0.0005 ± 0.0010 | 0.5839 ± 0.7525 | -0.3715 ± 1.1519 |
| IITD | SwinV2-Tiny | B1_mean_minus_black | -0.1509 ± 0.5302 | -0.0007 ± 0.0006 | 1.2739 ± 1.2022 | 2.7601 ± 3.2879 |
| IITD | SwinV2-Tiny | B2_mean_minus_black | -0.0171 ± 0.8557 | -0.0008 ± 0.0012 | 1.0085 ± 2.5889 | 5.4140 ± 7.7830 |
| IITD | SwinV2-Tiny | B2_minus_B1_black | 0.3061 ± 0.3823 | -0.0008 ± 0.0005 | -0.9554 ± 0.5741 | -4.0870 ± 3.1136 |
| IITD | SwinV2-Tiny | B2_minus_B1_mean | 0.4399 ± 0.3030 | -0.0010 ± 0.0004 | -1.2208 ± 1.0839 | -1.4331 ± 3.1966 |
| IITD | SwinV2-Tiny | nonannulus_mean_minus_black | 0.1804 ± 0.6054 | -0.0003 ± 0.0004 | -0.5308 ± 1.0602 | 0.2123 ± 0.5119 |

## Changes in genuine similarity and high-similarity impostor tails

Cosine differences from raw baseline, mean ± sample SD across3 seeds; full per-seed values/distributions are saved.

| architecture | variant | kind | mean | p10 | p50 | p99 | p999 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_B1_black | genuine | +0.08063 ± 0.01875 | +0.15453 ± 0.02284 | +0.06232 ± 0.01795 |  |  |  |
| ResNet-18 | A_B1_black | impostor |  |  |  | +0.39332 ± 0.01600 | +0.27141 ± 0.03631 | +0.17297 ± 0.05491 |
| ResNet-18 | A_B1_mean | genuine | +0.04621 ± 0.02111 | +0.09465 ± 0.03499 | +0.03729 ± 0.01780 |  |  |  |
| ResNet-18 | A_B1_mean | impostor |  |  |  | +0.31215 ± 0.03897 | +0.21227 ± 0.06855 | +0.13788 ± 0.07116 |
| ResNet-18 | A_B2_black | genuine | +0.07944 ± 0.01952 | +0.15131 ± 0.02391 | +0.06227 ± 0.01867 |  |  |  |
| ResNet-18 | A_B2_black | impostor |  |  |  | +0.39200 ± 0.01667 | +0.27152 ± 0.03475 | +0.17453 ± 0.05863 |
| ResNet-18 | A_B2_mean | genuine | +0.04832 ± 0.01814 | +0.09805 ± 0.02754 | +0.03776 ± 0.01674 |  |  |  |
| ResNet-18 | A_B2_mean | impostor |  |  |  | +0.31966 ± 0.03117 | +0.21592 ± 0.06230 | +0.13819 ± 0.06012 |
| ResNet-18 | A_nonannulus_black | genuine | +0.06208 ± 0.00251 | +0.11177 ± 0.01257 | +0.04980 ± 0.00444 |  |  |  |
| ResNet-18 | A_nonannulus_black | impostor |  |  |  | +0.33236 ± 0.01520 | +0.22573 ± 0.03135 | +0.13453 ± 0.05887 |
| ResNet-18 | A_nonannulus_mean | genuine | +0.05938 ± 0.00351 | +0.10497 ± 0.01948 | +0.05063 ± 0.00391 |  |  |  |
| ResNet-18 | A_nonannulus_mean | impostor |  |  |  | +0.31391 ± 0.03167 | +0.21859 ± 0.04412 | +0.13458 ± 0.06809 |
| SwinV2-Tiny | A_B1_black | genuine | +0.02891 ± 0.01272 | +0.06775 ± 0.03577 | +0.01107 ± 0.00728 |  |  |  |
| SwinV2-Tiny | A_B1_black | impostor |  |  |  | +0.25940 ± 0.01476 | +0.17450 ± 0.00923 | +0.11440 ± 0.02838 |
| SwinV2-Tiny | A_B1_mean | genuine | +0.02533 ± 0.01292 | +0.05708 ± 0.04043 | +0.00979 ± 0.00583 |  |  |  |
| SwinV2-Tiny | A_B1_mean | impostor |  |  |  | +0.23547 ± 0.02020 | +0.15567 ± 0.01848 | +0.09775 ± 0.03704 |
| SwinV2-Tiny | A_B2_black | genuine | +0.02721 ± 0.01382 | +0.06371 ± 0.03928 | +0.00906 ± 0.00728 |  |  |  |
| SwinV2-Tiny | A_B2_black | impostor |  |  |  | +0.27006 ± 0.01445 | +0.18123 ± 0.00569 | +0.12005 ± 0.03151 |
| SwinV2-Tiny | A_B2_mean | genuine | +0.02245 ± 0.01559 | +0.05448 ± 0.04825 | +0.00750 ± 0.00724 |  |  |  |
| SwinV2-Tiny | A_B2_mean | impostor |  |  |  | +0.24681 ± 0.02634 | +0.16223 ± 0.01684 | +0.10421 ± 0.03037 |
| SwinV2-Tiny | A_nonannulus_black | genuine | +0.02104 ± 0.00493 | +0.03527 ± 0.01985 | +0.01361 ± 0.00550 |  |  |  |
| SwinV2-Tiny | A_nonannulus_black | impostor |  |  |  | +0.19235 ± 0.05782 | +0.13366 ± 0.04554 | +0.07915 ± 0.06367 |
| SwinV2-Tiny | A_nonannulus_mean | genuine | +0.01478 ± 0.00160 | +0.02346 ± 0.01902 | +0.01181 ± 0.00107 |  |  |  |
| SwinV2-Tiny | A_nonannulus_mean | impostor |  |  |  | +0.17113 ± 0.03812 | +0.11980 ± 0.03476 | +0.07198 ± 0.04956 |

## Subject influence

Remove each subject and all incident comparisons, recompute all4 metrics, and pair against the same raw baseline removal. Table summarizes the mean EER effect across3 seeds. Complete per-seed/four-metric effects and subject identifiers are saved.

| dataset | architecture | variant | full_mean_eer_effect_pp | loo_min_mean_effect_pp | loo_max_mean_effect_pp | sign_reversals | reversing_subjects | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | A_B1_black | 2.45987 | 1.99221 | 2.59846 | 0 |  | 013 | 0.46767 |
| IITD | ResNet-18 | A_B1_mean | 2.93845 | 2.42902 | 3.12505 | 0 |  | 013 | 0.50943 |
| IITD | ResNet-18 | A_B2_black | 2.67545 | 2.15481 | 2.80973 | 0 |  | 013 | 0.52064 |
| IITD | ResNet-18 | A_B2_mean | 2.81095 | 2.38969 | 3.00501 | 0 |  | 013 | 0.42126 |
| IITD | ResNet-18 | A_nonannulus_black | 2.42494 | 1.89244 | 2.53447 | 0 |  | 004 | 0.5325 |
| IITD | ResNet-18 | A_nonannulus_mean | 2.10647 | 1.78313 | 2.20767 | 0 |  | 088 | 0.32334 |
| IITD | SwinV2-Tiny | A_B1_black | 1.07143 | 0.88923 | 1.20296 | 0 |  | 088 | 0.18219 |
| IITD | SwinV2-Tiny | A_B1_mean | 0.92053 | 0.60307 | 1.1212 | 0 |  | 004 | 0.31746 |
| IITD | SwinV2-Tiny | A_B2_black | 1.37749 | 1.11405 | 1.48775 | 0 |  | 088 | 0.26344 |
| IITD | SwinV2-Tiny | A_B2_mean | 1.36038 | 1.16335 | 1.54169 | 0 |  | 088 | 0.19703 |
| IITD | SwinV2-Tiny | A_nonannulus_black | 1.03297 | 0.83166 | 1.14832 | 0 |  | 214 | 0.2013 |
| IITD | SwinV2-Tiny | A_nonannulus_mean | 1.21339 | 1.0882 | 1.34334 | 0 |  | 033 | 0.12995 |

## Individual seed results

| architecture | variant | seed | selected_epoch | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 42 | 64 | 1.164664 | 0.999328 | 98.726115 | 96.496815 |
| ResNet-18 | A_B1_black | 42 | 64 | 3.184713 | 0.991747 | 93.949045 | 84.872611 |
| ResNet-18 | A_B2_black | 42 | 64 | 3.776994 | 0.991349 | 93.949045 | 87.420382 |
| ResNet-18 | A_B1_mean | 42 | 64 | 4.140127 | 0.991051 | 93.312102 | 86.464968 |
| ResNet-18 | A_B2_mean | 42 | 64 | 4.617834 | 0.990408 | 92.356688 | 82.324841 |
| ResNet-18 | A_nonannulus_black | 42 | 64 | 3.821656 | 0.991585 | 93.789809 | 89.649682 |
| ResNet-18 | A_nonannulus_mean | 42 | 64 | 3.503185 | 0.989927 | 95.22293 | 88.535032 |
| ResNet-18 | A_A | 123 | 110 | 0.636943 | 0.999866 | 99.681529 | 97.611465 |
| ResNet-18 | A_B1_black | 123 | 110 | 3.467868 | 0.993412 | 93.312102 | 87.738854 |
| ResNet-18 | A_B2_black | 123 | 110 | 3.503185 | 0.993239 | 93.949045 | 85.350318 |
| ResNet-18 | A_B1_mean | 123 | 110 | 4.088297 | 0.991525 | 93.152866 | 86.146497 |
| ResNet-18 | A_B2_mean | 123 | 110 | 3.387321 | 0.993084 | 92.993631 | 87.898089 |
| ResNet-18 | A_nonannulus_black | 123 | 110 | 3.184713 | 0.99522 | 95.063694 | 90.764331 |
| ResNet-18 | A_nonannulus_mean | 123 | 110 | 3.025478 | 0.995233 | 95.063694 | 89.808917 |
| ResNet-18 | A_A | 2025 | 114 | 0.477707 | 0.999785 | 99.681529 | 96.496815 |
| ResNet-18 | A_B1_black | 2025 | 114 | 3.006357 | 0.995552 | 95.382166 | 91.401274 |
| ResNet-18 | A_B2_black | 2025 | 114 | 3.025478 | 0.995131 | 94.745223 | 88.694268 |
| ResNet-18 | A_B1_mean | 2025 | 114 | 2.866242 | 0.991647 | 95.541401 | 92.834395 |
| ResNet-18 | A_B2_mean | 2025 | 114 | 2.707006 | 0.99207 | 95.700637 | 92.515924 |
| ResNet-18 | A_nonannulus_black | 2025 | 114 | 2.547771 | 0.997929 | 96.178344 | 89.968153 |
| ResNet-18 | A_nonannulus_mean | 2025 | 114 | 2.070064 | 0.997956 | 96.496815 | 90.923567 |
| SwinV2-Tiny | A_A | 42 | 35 | 1.11465 | 0.998936 | 98.88535 | 96.496815 |
| SwinV2-Tiny | A_B1_black | 42 | 35 | 2.061564 | 0.998194 | 96.656051 | 91.082803 |
| SwinV2-Tiny | A_B2_black | 42 | 35 | 2.124695 | 0.997891 | 96.33758 | 90.44586 |
| SwinV2-Tiny | A_B1_mean | 42 | 35 | 2.433821 | 0.997195 | 96.656051 | 91.56051 |
| SwinV2-Tiny | A_B2_mean | 42 | 35 | 3.025478 | 0.995757 | 95.063694 | 88.694268 |
| SwinV2-Tiny | A_nonannulus_black | 42 | 35 | 3.34596 | 0.995563 | 94.585987 | 90.44586 |
| SwinV2-Tiny | A_nonannulus_mean | 42 | 35 | 2.866242 | 0.995721 | 94.745223 | 91.242038 |
| SwinV2-Tiny | A_A | 123 | 31 | 1.592357 | 0.999308 | 98.089172 | 97.133758 |
| SwinV2-Tiny | A_B1_black | 123 | 31 | 2.917102 | 0.997808 | 95.541401 | 91.56051 |
| SwinV2-Tiny | A_B2_black | 123 | 31 | 3.025478 | 0.996816 | 94.426752 | 84.872611 |
| SwinV2-Tiny | A_B1_mean | 123 | 31 | 2.229299 | 0.997777 | 96.974522 | 92.834395 |
| SwinV2-Tiny | A_B2_mean | 123 | 31 | 2.866242 | 0.996917 | 94.904459 | 89.171975 |
| SwinV2-Tiny | A_nonannulus_black | 123 | 31 | 1.380181 | 0.998203 | 97.611465 | 89.33121 |
| SwinV2-Tiny | A_nonannulus_mean | 123 | 31 | 2.089864 | 0.997719 | 95.859873 | 89.171975 |
| SwinV2-Tiny | A_A | 2025 | 23 | 2.129049 | 0.997615 | 97.292994 | 91.719745 |
| SwinV2-Tiny | A_B1_black | 2025 | 23 | 3.071665 | 0.994224 | 93.312102 | 81.847134 |
| SwinV2-Tiny | A_B2_black | 2025 | 23 | 3.818356 | 0.992991 | 91.878981 | 76.910828 |
| SwinV2-Tiny | A_B1_mean | 2025 | 23 | 2.934518 | 0.993258 | 95.700637 | 88.375796 |
| SwinV2-Tiny | A_B2_mean | 2025 | 23 | 3.025478 | 0.992641 | 95.700637 | 90.605096 |
| SwinV2-Tiny | A_nonannulus_black | 2025 | 23 | 3.208812 | 0.994985 | 92.834395 | 91.082803 |
| SwinV2-Tiny | A_nonannulus_mean | 2025 | 23 | 3.520115 | 0.994422 | 92.834395 | 91.082803 |

## Input statistics and QC examples

| dataset | variant | images | replaced_pixels_median | retained_pixels_median | padding_pixels_median | replaced_intensity_l1_median | content_mean_median | content_std_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | A_A | 308 | 0.0 | 76800.0 | 25600.0 | 0.0 | 0.494294 | 0.253363 |
| IITD | A_B1_black | 308 | 52595.0 | 24205.0 | 25600.0 | 0.523746 | 0.122041 | 0.196311 |
| IITD | A_B1_mean | 308 | 52595.0 | 24205.0 | 25600.0 | 0.252539 | 0.457866 | 0.075354 |
| IITD | A_B2_black | 308 | 54028.0 | 22772.0 | 25600.0 | 0.515151 | 0.1177 | 0.195583 |
| IITD | A_B2_mean | 308 | 54028.0 | 22772.0 | 25600.0 | 0.253993 | 0.462882 | 0.064095 |
| IITD | A_nonannulus_black | 308 | 24205.0 | 52595.0 | 25600.0 | 0.402105 | 0.361201 | 0.338433 |
| IITD | A_nonannulus_mean | 308 | 24205.0 | 52595.0 | 25600.0 | 0.10482 | 0.510732 | 0.239479 |

Examples were chosen as the first3 common subjects by image ID, before recognition scoring.









