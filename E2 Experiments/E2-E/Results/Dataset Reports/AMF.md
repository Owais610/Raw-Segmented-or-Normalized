# AMF: separate E2-E analysis

## Absolute metrics

EER/TAR percent; AUC[0,1]. Mean ± sample SD over all3 seeds.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | A_A | 1.0244 ± 0.4541 | 0.9992 ± 0.0005 | 98.9163 ± 0.8418 | 96.0263 ± 1.5050 |
| AMF | ResNet-18 | A_B1_black | 4.1026 ± 0.4670 | 0.9924 ± 0.0019 | 88.8670 ± 1.6807 | 72.1839 ± 4.7191 |
| AMF | ResNet-18 | A_B1_mean | 5.5682 ± 0.5214 | 0.9891 ± 0.0024 | 87.0936 ± 1.3687 | 73.6946 ± 2.0572 |
| AMF | ResNet-18 | A_B2_black | 5.3055 ± 0.3158 | 0.9879 ± 0.0015 | 85.6814 ± 2.1184 | 67.9803 ± 2.9077 |
| AMF | ResNet-18 | A_B2_mean | 5.6409 ± 0.6393 | 0.9882 ± 0.0015 | 86.0427 ± 2.1638 | 74.0230 ± 2.9513 |
| AMF | ResNet-18 | A_nonannulus_black | 2.0591 ± 0.1873 | 0.9977 ± 0.0005 | 96.3218 ± 0.8940 | 90.9031 ± 1.6613 |
| AMF | ResNet-18 | A_nonannulus_mean | 1.8615 ± 0.5571 | 0.9982 ± 0.0006 | 97.1757 ± 0.6706 | 92.5452 ± 0.2844 |
| AMF | SwinV2-Tiny | A_A | 1.3356 ± 0.2943 | 0.9988 ± 0.0005 | 98.5878 ± 0.3167 | 95.5337 ± 1.0535 |
| AMF | SwinV2-Tiny | A_B1_black | 3.2038 ± 0.5831 | 0.9955 ± 0.0014 | 91.9540 ± 1.8857 | 74.5484 ± 3.5032 |
| AMF | SwinV2-Tiny | A_B1_mean | 3.3714 ± 0.5107 | 0.9953 ± 0.0011 | 90.3448 ± 1.5856 | 77.4056 ± 1.6378 |
| AMF | SwinV2-Tiny | A_B2_black | 3.4171 ± 0.5745 | 0.9950 ± 0.0015 | 90.7718 ± 2.3978 | 72.0854 ± 3.7983 |
| AMF | SwinV2-Tiny | A_B2_mean | 3.1541 ± 0.6007 | 0.9954 ± 0.0012 | 91.3629 ± 2.5698 | 77.8982 ± 1.8309 |
| AMF | SwinV2-Tiny | A_nonannulus_black | 2.1041 ± 0.2475 | 0.9966 ± 0.0003 | 96.8801 ± 0.5056 | 90.8046 ± 2.7059 |
| AMF | SwinV2-Tiny | A_nonannulus_mean | 1.9090 ± 0.2421 | 0.9966 ± 0.0003 | 97.1100 ± 0.5056 | 90.1806 ± 1.8624 |

## Paired intervention minus raw baseline

All differences use the SAME checkpoint and exact pairs. EER/TAR differences are percentage points; AUC differences are on[0,1]. Negative EER differences indicate lower EER.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | A_B1_black | 3.0781 ± 0.7356 | -0.0068 ± 0.0016 | -10.0493 ± 2.1336 | -23.8424 ± 5.9775 |
| AMF | ResNet-18 | A_B1_mean | 4.5438 ± 0.8058 | -0.0100 ± 0.0027 | -11.8227 ± 0.6461 | -22.3317 ± 0.9312 |
| AMF | ResNet-18 | A_B2_black | 4.2810 ± 0.5722 | -0.0113 ± 0.0014 | -13.2348 ± 2.1138 | -28.0460 ± 4.0314 |
| AMF | ResNet-18 | A_B2_mean | 4.6165 ± 0.6392 | -0.0110 ± 0.0015 | -12.8736 ± 1.4152 | -22.0033 ± 1.4524 |
| AMF | ResNet-18 | A_nonannulus_black | 1.0347 ± 0.3121 | -0.0015 ± 0.0007 | -2.5944 ± 0.6920 | -5.1232 ± 1.8719 |
| AMF | ResNet-18 | A_nonannulus_mean | 0.8371 ± 0.3928 | -0.0010 ± 0.0007 | -1.7406 ± 0.8940 | -3.4811 ± 1.5835 |
| AMF | SwinV2-Tiny | A_B1_black | 1.8682 ± 0.6090 | -0.0033 ± 0.0012 | -6.6338 ± 1.9440 | -20.9852 ± 4.5320 |
| AMF | SwinV2-Tiny | A_B1_mean | 2.0358 ± 0.4396 | -0.0035 ± 0.0009 | -8.2430 ± 1.4255 | -18.1281 ± 1.7514 |
| AMF | SwinV2-Tiny | A_B2_black | 2.0815 ± 0.5640 | -0.0037 ± 0.0013 | -7.8161 ± 2.4220 | -23.4483 ± 4.8276 |
| AMF | SwinV2-Tiny | A_B2_mean | 1.8185 ± 0.4789 | -0.0033 ± 0.0009 | -7.2250 ± 2.3836 | -17.6355 ± 2.4866 |
| AMF | SwinV2-Tiny | A_nonannulus_black | 0.7685 ± 0.5203 | -0.0022 ± 0.0003 | -1.7077 ± 0.8204 | -4.7291 ± 1.7761 |
| AMF | SwinV2-Tiny | A_nonannulus_mean | 0.5734 ± 0.4146 | -0.0022 ± 0.0003 | -1.4778 ± 0.7438 | -5.3530 ± 1.1074 |

## Predefined mean-minus-black and B2-minus-B1 controls

| dataset | architecture | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | B1_mean_minus_black | 1.4656 ± 0.9370 | -0.0032 ± 0.0043 | -1.7734 ± 2.7797 | 1.5107 ± 6.7373 |
| AMF | ResNet-18 | B2_mean_minus_black | 0.3354 ± 0.9463 | 0.0003 ± 0.0029 | 0.3612 ± 3.2755 | 6.0427 ± 5.3695 |
| AMF | ResNet-18 | B2_minus_B1_black | 1.2029 ± 0.1703 | -0.0045 ± 0.0008 | -3.1856 ± 1.1546 | -4.2036 ± 1.9909 |
| AMF | ResNet-18 | B2_minus_B1_mean | 0.0727 ± 0.4303 | -0.0010 ± 0.0016 | -1.0509 ± 0.7963 | 0.3284 ± 1.2668 |
| AMF | ResNet-18 | nonannulus_mean_minus_black | -0.1976 ± 0.3760 | 0.0005 ± 0.0002 | 0.8539 ± 0.3982 | 1.6420 ± 1.9440 |
| AMF | SwinV2-Tiny | B1_mean_minus_black | 0.1676 ± 1.0275 | -0.0002 ± 0.0021 | -1.6092 ± 3.3575 | 2.8571 ± 4.4760 |
| AMF | SwinV2-Tiny | B2_mean_minus_black | -0.2629 ± 1.0423 | 0.0004 ± 0.0021 | 0.5911 ± 4.6930 | 5.8128 ± 3.8398 |
| AMF | SwinV2-Tiny | B2_minus_B1_black | 0.2133 ± 0.0773 | -0.0004 ± 0.0001 | -1.1823 ± 0.5485 | -2.4631 ± 0.2956 |
| AMF | SwinV2-Tiny | B2_minus_B1_mean | -0.2172 ± 0.1139 | 0.0002 ± 0.0003 | 1.0181 ± 0.9918 | 0.4926 ± 1.1616 |
| AMF | SwinV2-Tiny | nonannulus_mean_minus_black | -0.1951 ± 0.1941 | 0.0000 ± 0.0001 | 0.2299 ± 0.5056 | -0.6240 ± 0.9154 |

## Changes in genuine similarity and high-similarity impostor tails

Cosine differences from raw baseline, mean ± sample SD across3 seeds; full per-seed values/distributions are saved.

| architecture | variant | kind | mean | p10 | p50 | p99 | p999 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_B1_black | genuine | +0.05200 ± 0.01125 | +0.10446 ± 0.02095 | +0.03879 ± 0.00975 |  |  |  |
| ResNet-18 | A_B1_black | impostor |  |  |  | +0.22005 ± 0.03684 | +0.16188 ± 0.03304 | +0.10134 ± 0.02836 |
| ResNet-18 | A_B1_mean | genuine | +0.03971 ± 0.01025 | +0.07612 ± 0.02178 | +0.03124 ± 0.00730 |  |  |  |
| ResNet-18 | A_B1_mean | impostor |  |  |  | +0.19806 ± 0.03238 | +0.14717 ± 0.02913 | +0.09334 ± 0.02476 |
| ResNet-18 | A_B2_black | genuine | +0.04865 ± 0.01278 | +0.09726 ± 0.02535 | +0.03681 ± 0.01027 |  |  |  |
| ResNet-18 | A_B2_black | impostor |  |  |  | +0.21627 ± 0.03871 | +0.15981 ± 0.03370 | +0.10097 ± 0.02835 |
| ResNet-18 | A_B2_mean | genuine | +0.03570 ± 0.01221 | +0.06595 ± 0.02693 | +0.02875 ± 0.00862 |  |  |  |
| ResNet-18 | A_B2_mean | impostor |  |  |  | +0.19149 ± 0.03449 | +0.14252 ± 0.03026 | +0.09021 ± 0.02811 |
| ResNet-18 | A_nonannulus_black | genuine | +0.00819 ± 0.00114 | +0.01446 ± 0.00079 | +0.00583 ± 0.00072 |  |  |  |
| ResNet-18 | A_nonannulus_black | impostor |  |  |  | +0.08328 ± 0.01590 | +0.05994 ± 0.01594 | +0.03325 ± 0.02509 |
| ResNet-18 | A_nonannulus_mean | genuine | +0.00508 ± 0.00391 | +0.00775 ± 0.00857 | +0.00403 ± 0.00233 |  |  |  |
| ResNet-18 | A_nonannulus_mean | impostor |  |  |  | +0.05946 ± 0.02815 | +0.04454 ± 0.02322 | +0.02842 ± 0.01189 |
| SwinV2-Tiny | A_B1_black | genuine | +0.02518 ± 0.00338 | +0.06334 ± 0.01786 | +0.01219 ± 0.00120 |  |  |  |
| SwinV2-Tiny | A_B1_black | impostor |  |  |  | +0.18204 ± 0.01438 | +0.12176 ± 0.01191 | +0.05377 ± 0.01350 |
| SwinV2-Tiny | A_B1_mean | genuine | +0.02220 ± 0.00598 | +0.05143 ± 0.02182 | +0.01154 ± 0.00342 |  |  |  |
| SwinV2-Tiny | A_B1_mean | impostor |  |  |  | +0.17326 ± 0.01666 | +0.11603 ± 0.01385 | +0.05117 ± 0.01459 |
| SwinV2-Tiny | A_B2_black | genuine | +0.02325 ± 0.00303 | +0.05922 ± 0.01699 | +0.01081 ± 0.00104 |  |  |  |
| SwinV2-Tiny | A_B2_black | impostor |  |  |  | +0.18018 ± 0.01399 | +0.12080 ± 0.01187 | +0.05260 ± 0.01264 |
| SwinV2-Tiny | A_B2_mean | genuine | +0.02179 ± 0.00573 | +0.05136 ± 0.02267 | +0.01066 ± 0.00302 |  |  |  |
| SwinV2-Tiny | A_B2_mean | impostor |  |  |  | +0.17139 ± 0.01599 | +0.11591 ± 0.01271 | +0.05105 ± 0.01404 |
| SwinV2-Tiny | A_nonannulus_black | genuine | +0.00585 ± 0.00654 | +0.01453 ± 0.01518 | +0.00451 ± 0.00432 |  |  |  |
| SwinV2-Tiny | A_nonannulus_black | impostor |  |  |  | +0.07246 ± 0.03989 | +0.05336 ± 0.02247 | +0.01879 ± 0.01680 |
| SwinV2-Tiny | A_nonannulus_mean | genuine | +0.00201 ± 0.00185 | +0.00248 ± 0.00327 | +0.00299 ± 0.00162 |  |  |  |
| SwinV2-Tiny | A_nonannulus_mean | impostor |  |  |  | +0.05596 ± 0.02247 | +0.04412 ± 0.00841 | +0.01498 ± 0.01008 |

## Subject influence

Remove each subject and all incident comparisons, recompute all4 metrics, and pair against the same raw baseline removal. Table summarizes the mean EER effect across3 seeds. Complete per-seed/four-metric effects and subject identifiers are saved.

| dataset | architecture | variant | full_mean_eer_effect_pp | loo_min_mean_effect_pp | loo_max_mean_effect_pp | sign_reversals | reversing_subjects | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | A_B1_black | 3.07815 | 2.91674 | 3.16482 | 0 |  | rasha | 0.1614 |
| AMF | ResNet-18 | A_B1_mean | 4.54379 | 4.02056 | 4.66317 | 0 |  | rasha | 0.52323 |
| AMF | ResNet-18 | A_B2_black | 4.28105 | 3.86077 | 4.39984 | 0 |  | ali | 0.42028 |
| AMF | ResNet-18 | A_B2_mean | 4.61649 | 4.02657 | 4.77617 | 0 |  | ali | 0.58992 |
| AMF | ResNet-18 | A_nonannulus_black | 1.03474 | 0.95433 | 1.09259 | 0 |  | wisam | 0.08042 |
| AMF | ResNet-18 | A_nonannulus_mean | 0.83711 | 0.69233 | 0.88458 | 0 |  | zafer | 0.14478 |
| AMF | SwinV2-Tiny | A_B1_black | 1.8682 | 1.69727 | 2.23575 | 0 |  | ahmed | 0.36756 |
| AMF | SwinV2-Tiny | A_B1_mean | 2.03576 | 1.79401 | 2.44053 | 0 |  | zafer | 0.40476 |
| AMF | SwinV2-Tiny | A_B2_black | 2.08146 | 1.94898 | 2.46489 | 0 |  | ahmed | 0.38343 |
| AMF | SwinV2-Tiny | A_B2_mean | 1.81853 | 1.59552 | 2.22135 | 0 |  | zafer | 0.40282 |
| AMF | SwinV2-Tiny | A_nonannulus_black | 0.76848 | 0.6327 | 0.82022 | 0 |  | ahmed | 0.13578 |
| AMF | SwinV2-Tiny | A_nonannulus_mean | 0.5734 | 0.43465 | 0.62796 | 0 |  | ahmed | 0.13875 |

## Individual seed results

| architecture | variant | seed | selected_epoch | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 42 | 64 | 0.591133 | 0.999796 | 99.704433 | 97.339901 |
| ResNet-18 | A_B1_black | 42 | 64 | 3.933271 | 0.993482 | 89.359606 | 71.133005 |
| ResNet-18 | A_B2_black | 42 | 64 | 5.123153 | 0.98809 | 87.487685 | 68.078818 |
| ResNet-18 | A_B1_mean | 42 | 64 | 6.064196 | 0.988298 | 87.980296 | 74.679803 |
| ResNet-18 | A_B2_mean | 42 | 64 | 5.812808 | 0.988917 | 87.389163 | 76.453202 |
| ResNet-18 | A_nonannulus_black | 42 | 64 | 1.972969 | 0.99788 | 96.453202 | 90.147783 |
| ResNet-18 | A_nonannulus_mean | 42 | 64 | 1.733798 | 0.998517 | 96.945813 | 92.70936 |
| ResNet-18 | A_A | 123 | 110 | 1.496863 | 0.998995 | 98.029557 | 94.384236 |
| ResNet-18 | A_B1_black | 123 | 110 | 3.743842 | 0.993496 | 90.246305 | 77.339901 |
| ResNet-18 | A_B2_black | 123 | 110 | 5.123153 | 0.989202 | 86.206897 | 70.837438 |
| ResNet-18 | A_B1_mean | 123 | 110 | 5.615764 | 0.987307 | 85.517241 | 71.330049 |
| ResNet-18 | A_B2_mean | 123 | 110 | 6.176703 | 0.986399 | 83.546798 | 70.738916 |
| ResNet-18 | A_nonannulus_black | 123 | 110 | 2.27398 | 0.997131 | 95.369458 | 89.753695 |
| ResNet-18 | A_nonannulus_mean | 123 | 110 | 2.471426 | 0.997466 | 96.650246 | 92.70936 |
| ResNet-18 | A_A | 2025 | 114 | 0.985222 | 0.998793 | 99.014778 | 96.35468 |
| ResNet-18 | A_B1_black | 2025 | 114 | 4.630542 | 0.990172 | 86.995074 | 68.078818 |
| ResNet-18 | A_B2_black | 2025 | 114 | 5.670049 | 0.986297 | 83.349754 | 65.024631 |
| ResNet-18 | A_B1_mean | 2025 | 114 | 5.024631 | 0.991833 | 87.783251 | 75.073892 |
| ResNet-18 | A_B2_mean | 2025 | 114 | 4.933166 | 0.989173 | 87.192118 | 74.876847 |
| ResNet-18 | A_nonannulus_black | 2025 | 114 | 1.930499 | 0.998164 | 97.142857 | 92.807882 |
| ResNet-18 | A_nonannulus_mean | 2025 | 114 | 1.37931 | 0.998545 | 97.931034 | 92.216749 |
| SwinV2-Tiny | A_A | 42 | 35 | 1.149657 | 0.999184 | 98.719212 | 96.453202 |
| SwinV2-Tiny | A_B1_black | 42 | 35 | 3.700061 | 0.994959 | 89.852217 | 70.935961 |
| SwinV2-Tiny | A_B2_black | 42 | 35 | 3.842365 | 0.994436 | 88.17734 | 68.17734 |
| SwinV2-Tiny | A_B1_mean | 42 | 35 | 2.782124 | 0.996501 | 92.118227 | 78.916256 |
| SwinV2-Tiny | A_B2_mean | 42 | 35 | 2.463054 | 0.996824 | 94.187192 | 78.423645 |
| SwinV2-Tiny | A_nonannulus_black | 42 | 35 | 2.364532 | 0.996774 | 96.748768 | 92.216749 |
| SwinV2-Tiny | A_nonannulus_mean | 42 | 35 | 2.167488 | 0.996856 | 96.551724 | 90.837438 |
| SwinV2-Tiny | A_A | 123 | 31 | 1.182266 | 0.998937 | 98.817734 | 94.384236 |
| SwinV2-Tiny | A_B1_black | 123 | 31 | 2.561576 | 0.997042 | 93.497537 | 77.931034 |
| SwinV2-Tiny | A_B2_black | 123 | 31 | 2.763497 | 0.996741 | 92.906404 | 75.763547 |
| SwinV2-Tiny | A_B1_mean | 123 | 31 | 3.68665 | 0.994546 | 89.852217 | 77.635468 |
| SwinV2-Tiny | A_B2_mean | 123 | 31 | 3.448276 | 0.994896 | 90.738916 | 79.408867 |
| SwinV2-Tiny | A_nonannulus_black | 123 | 31 | 2.075789 | 0.996731 | 96.453202 | 87.684729 |
| SwinV2-Tiny | A_nonannulus_mean | 123 | 31 | 1.687603 | 0.996585 | 97.241379 | 88.078818 |
| SwinV2-Tiny | A_A | 2025 | 23 | 1.674877 | 0.998134 | 98.226601 | 95.763547 |
| SwinV2-Tiny | A_B1_black | 2025 | 23 | 3.349754 | 0.99443 | 92.512315 | 74.778325 |
| SwinV2-Tiny | A_B2_black | 2025 | 23 | 3.64532 | 0.993945 | 91.231527 | 72.315271 |
| SwinV2-Tiny | A_B1_mean | 2025 | 23 | 3.64532 | 0.994783 | 89.064039 | 75.665025 |
| SwinV2-Tiny | A_B2_mean | 2025 | 23 | 3.551045 | 0.99461 | 89.162562 | 75.862069 |
| SwinV2-Tiny | A_nonannulus_black | 2025 | 23 | 1.871921 | 0.996221 | 97.438424 | 92.512315 |
| SwinV2-Tiny | A_nonannulus_mean | 2025 | 23 | 1.871921 | 0.996297 | 97.536946 | 91.625616 |

## Input statistics and QC examples

| dataset | variant | images | replaced_pixels_median | retained_pixels_median | padding_pixels_median | replaced_intensity_l1_median | content_mean_median | content_std_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | A_A | 523 | 0.0 | 76800.0 | 25600.0 | 0.0 | 0.56615 | 0.240783 |
| AMF | A_B1_black | 523 | 65798.0 | 11002.0 | 25600.0 | 0.599736 | 0.051195 | 0.124922 |
| AMF | A_B1_mean | 523 | 65798.0 | 11002.0 | 25600.0 | 0.229116 | 0.463399 | 0.052938 |
| AMF | A_B2_black | 523 | 66057.0 | 10743.0 | 25600.0 | 0.597411 | 0.050264 | 0.124314 |
| AMF | A_B2_mean | 523 | 66057.0 | 10743.0 | 25600.0 | 0.229488 | 0.465666 | 0.048505 |
| AMF | A_nonannulus_black | 523 | 11002.0 | 65798.0 | 25600.0 | 0.347881 | 0.515265 | 0.30638 |
| AMF | A_nonannulus_mean | 523 | 11002.0 | 65798.0 | 25600.0 | 0.137448 | 0.583223 | 0.227018 |

Examples were chosen as the first3 common subjects by image ID, before recognition scoring.









