# CUST-Iris: separate E2-E analysis

## Absolute metrics

EER/TAR percent; AUC[0,1]. Mean ± sample SD over all3 seeds.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | A_A | 1.4004 ± 0.2872 | 0.9986 ± 0.0009 | 98.2124 ± 0.4819 | 95.6887 ± 1.0502 |
| CUST-Iris | ResNet-18 | A_B1_black | 8.2398 ± 0.7204 | 0.9770 ± 0.0026 | 73.9222 ± 1.5956 | 49.2114 ± 3.0707 |
| CUST-Iris | ResNet-18 | A_B1_mean | 7.6387 ± 0.5329 | 0.9795 ± 0.0022 | 76.4984 ± 3.0093 | 52.9443 ± 3.7800 |
| CUST-Iris | ResNet-18 | A_B2_black | 9.2131 ± 0.7442 | 0.9704 ± 0.0014 | 67.2450 ± 0.2409 | 43.1125 ± 2.8406 |
| CUST-Iris | ResNet-18 | A_B2_mean | 7.4379 ± 0.2936 | 0.9781 ± 0.0019 | 75.0263 ± 4.2333 | 50.7886 ± 4.2703 |
| CUST-Iris | ResNet-18 | A_nonannulus_black | 2.7340 ± 0.3643 | 0.9944 ± 0.0032 | 95.3733 ± 0.9637 | 90.6414 ± 1.2252 |
| CUST-Iris | ResNet-18 | A_nonannulus_mean | 2.7340 ± 0.7781 | 0.9953 ± 0.0029 | 95.6887 ± 1.4225 | 90.9569 ± 1.4312 |
| CUST-Iris | SwinV2-Tiny | A_A | 1.8717 ± 0.3176 | 0.9986 ± 0.0007 | 96.9506 ± 1.6417 | 91.3249 ± 1.9700 |
| CUST-Iris | SwinV2-Tiny | A_B1_black | 7.2613 ± 0.5615 | 0.9809 ± 0.0023 | 69.8212 ± 2.2984 | 41.5878 ± 2.9816 |
| CUST-Iris | SwinV2-Tiny | A_B1_mean | 5.5908 ± 0.4886 | 0.9890 ± 0.0018 | 80.7571 ± 1.2911 | 57.3081 ± 6.2782 |
| CUST-Iris | SwinV2-Tiny | A_B2_black | 7.1372 ± 0.4289 | 0.9812 ± 0.0022 | 67.8233 ± 2.9212 | 39.8528 ± 0.2409 |
| CUST-Iris | SwinV2-Tiny | A_B2_mean | 5.5889 ± 0.3484 | 0.9890 ± 0.0021 | 80.7045 ± 2.3677 | 58.1493 ± 5.5325 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_black | 2.9946 ± 0.4577 | 0.9954 ± 0.0025 | 93.4805 ± 0.9507 | 83.2808 ± 3.8764 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_mean | 3.5105 ± 0.6482 | 0.9945 ± 0.0032 | 93.1651 ± 1.3781 | 83.9642 ± 3.9094 |

## Paired intervention minus raw baseline

All differences use the SAME checkpoint and exact pairs. EER/TAR differences are percentage points; AUC differences are on[0,1]. Negative EER differences indicate lower EER.

| dataset | architecture | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | A_B1_black | 6.8394 ± 0.5255 | -0.0215 ± 0.0024 | -24.2902 ± 1.2519 | -46.4774 ± 2.0342 |
| CUST-Iris | ResNet-18 | A_B1_mean | 6.2382 ± 0.2976 | -0.0190 ± 0.0017 | -21.7140 ± 2.6829 | -42.7445 ± 4.4417 |
| CUST-Iris | ResNet-18 | A_B2_black | 7.8126 ± 0.4843 | -0.0282 ± 0.0008 | -30.9674 ± 0.3283 | -52.5762 ± 2.5253 |
| CUST-Iris | ResNet-18 | A_B2_mean | 6.0375 ± 0.2866 | -0.0204 ± 0.0017 | -23.1861 ± 3.8280 | -44.9001 ± 4.8367 |
| CUST-Iris | ResNet-18 | A_nonannulus_black | 1.3335 ± 0.2008 | -0.0041 ± 0.0025 | -2.8391 ± 0.5464 | -5.0473 ± 1.7564 |
| CUST-Iris | ResNet-18 | A_nonannulus_mean | 1.3335 ± 0.5398 | -0.0033 ± 0.0024 | -2.5237 ± 1.3750 | -4.7319 ± 0.5464 |
| CUST-Iris | SwinV2-Tiny | A_B1_black | 5.3897 ± 0.8652 | -0.0177 ± 0.0029 | -27.1293 ± 3.9242 | -49.7371 ± 4.3521 |
| CUST-Iris | SwinV2-Tiny | A_B1_mean | 3.7191 ± 0.2234 | -0.0096 ± 0.0015 | -16.1935 ± 2.0585 | -34.0168 ± 7.9435 |
| CUST-Iris | SwinV2-Tiny | A_B2_black | 5.2655 ± 0.7430 | -0.0174 ± 0.0027 | -29.1272 ± 4.5066 | -51.4721 ± 2.2101 |
| CUST-Iris | SwinV2-Tiny | A_B2_mean | 3.7172 ± 0.2537 | -0.0096 ± 0.0019 | -16.2461 ± 2.4789 | -33.1756 ± 7.0120 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_black | 1.1229 ± 0.2014 | -0.0032 ± 0.0020 | -3.4700 ± 1.2519 | -8.0442 ± 1.9189 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_mean | 1.6388 ± 0.3725 | -0.0041 ± 0.0025 | -3.7855 ± 0.8346 | -7.3607 ± 2.5644 |

## Predefined mean-minus-black and B2-minus-B1 controls

| dataset | architecture | contrast | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | B1_mean_minus_black | -0.6012 ± 0.2366 | 0.0025 ± 0.0010 | 2.5762 ± 3.2028 | 3.7329 ± 6.2324 |
| CUST-Iris | ResNet-18 | B2_mean_minus_black | -1.7751 ± 0.7466 | 0.0078 ± 0.0011 | 7.7813 ± 3.9944 | 7.6761 ± 7.1106 |
| CUST-Iris | ResNet-18 | B2_minus_B1_black | 0.9732 ± 0.7119 | -0.0067 ± 0.0018 | -6.6772 ± 1.5561 | -6.0988 ± 2.7152 |
| CUST-Iris | ResNet-18 | B2_minus_B1_mean | -0.2007 ± 0.3343 | -0.0014 ± 0.0006 | -1.4721 ± 1.4655 | -2.1556 ± 0.6567 |
| CUST-Iris | ResNet-18 | nonannulus_mean_minus_black | 0.0000 ± 0.4173 | 0.0009 ± 0.0004 | 0.3155 ± 1.1374 | 0.3155 ± 1.7564 |
| CUST-Iris | SwinV2-Tiny | B1_mean_minus_black | -1.6706 ± 1.0501 | 0.0082 ± 0.0030 | 10.9359 ± 2.8624 | 15.7203 ± 7.1872 |
| CUST-Iris | SwinV2-Tiny | B2_mean_minus_black | -1.5483 ± 0.7450 | 0.0078 ± 0.0028 | 12.8812 ± 4.6958 | 18.2965 ± 5.3905 |
| CUST-Iris | SwinV2-Tiny | B2_minus_B1_black | -0.1241 ± 0.1580 | 0.0003 ± 0.0002 | -1.9979 ± 0.7285 | -1.7350 ± 2.8435 |
| CUST-Iris | SwinV2-Tiny | B2_minus_B1_mean | -0.0019 ± 0.2187 | -0.0001 ± 0.0004 | -0.0526 ± 1.1626 | 0.8412 ± 1.3415 |
| CUST-Iris | SwinV2-Tiny | nonannulus_mean_minus_black | 0.5159 ± 0.1905 | -0.0008 ± 0.0007 | -0.3155 ± 0.5687 | 0.6835 ± 2.0585 |

## Changes in genuine similarity and high-similarity impostor tails

Cosine differences from raw baseline, mean ± sample SD across3 seeds; full per-seed values/distributions are saved.

| architecture | variant | kind | mean | p10 | p50 | p99 | p999 | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_B1_black | genuine | +0.11779 ± 0.01332 | +0.23164 ± 0.02056 | +0.08976 ± 0.01729 |  |  |  |
| ResNet-18 | A_B1_black | impostor |  |  |  | +0.45100 ± 0.02318 | +0.33948 ± 0.01818 | +0.21329 ± 0.03341 |
| ResNet-18 | A_B1_mean | genuine | +0.10475 ± 0.01331 | +0.20211 ± 0.02161 | +0.08122 ± 0.01635 |  |  |  |
| ResNet-18 | A_B1_mean | impostor |  |  |  | +0.43221 ± 0.02003 | +0.32940 ± 0.01732 | +0.20922 ± 0.03249 |
| ResNet-18 | A_B2_black | genuine | +0.11122 ± 0.01459 | +0.21855 ± 0.02353 | +0.08471 ± 0.01857 |  |  |  |
| ResNet-18 | A_B2_black | impostor |  |  |  | +0.44594 ± 0.02434 | +0.33651 ± 0.01922 | +0.21310 ± 0.03298 |
| ResNet-18 | A_B2_mean | genuine | +0.09933 ± 0.01445 | +0.19251 ± 0.02360 | +0.07582 ± 0.01785 |  |  |  |
| ResNet-18 | A_B2_mean | impostor |  |  |  | +0.42677 ± 0.02119 | +0.32549 ± 0.01801 | +0.20810 ± 0.03135 |
| ResNet-18 | A_nonannulus_black | genuine | +0.03987 ± 0.01240 | +0.09069 ± 0.01362 | +0.02743 ± 0.01577 |  |  |  |
| ResNet-18 | A_nonannulus_black | impostor |  |  |  | +0.22538 ± 0.02490 | +0.17019 ± 0.02322 | +0.09992 ± 0.01782 |
| ResNet-18 | A_nonannulus_mean | genuine | +0.02799 ± 0.00680 | +0.05758 ± 0.00814 | +0.02026 ± 0.00757 |  |  |  |
| ResNet-18 | A_nonannulus_mean | impostor |  |  |  | +0.18558 ± 0.00996 | +0.13596 ± 0.00391 | +0.09426 ± 0.03976 |
| SwinV2-Tiny | A_B1_black | genuine | +0.05299 ± 0.00560 | +0.12456 ± 0.01630 | +0.03281 ± 0.00545 |  |  |  |
| SwinV2-Tiny | A_B1_black | impostor |  |  |  | +0.29305 ± 0.03210 | +0.19361 ± 0.02480 | +0.09515 ± 0.02376 |
| SwinV2-Tiny | A_B1_mean | genuine | +0.04993 ± 0.00541 | +0.11438 ± 0.01855 | +0.03042 ± 0.00351 |  |  |  |
| SwinV2-Tiny | A_B1_mean | impostor |  |  |  | +0.27396 ± 0.02886 | +0.18271 ± 0.02737 | +0.09084 ± 0.02396 |
| SwinV2-Tiny | A_B2_black | genuine | +0.04830 ± 0.00592 | +0.11429 ± 0.01647 | +0.02855 ± 0.00606 |  |  |  |
| SwinV2-Tiny | A_B2_black | impostor |  |  |  | +0.28852 ± 0.03207 | +0.19116 ± 0.02493 | +0.09465 ± 0.02384 |
| SwinV2-Tiny | A_B2_mean | genuine | +0.04794 ± 0.00646 | +0.11126 ± 0.02110 | +0.02874 ± 0.00465 |  |  |  |
| SwinV2-Tiny | A_B2_mean | impostor |  |  |  | +0.27104 ± 0.02920 | +0.18062 ± 0.02782 | +0.08857 ± 0.02298 |
| SwinV2-Tiny | A_nonannulus_black | genuine | +0.01161 ± 0.01335 | +0.02713 ± 0.04506 | +0.00731 ± 0.00596 |  |  |  |
| SwinV2-Tiny | A_nonannulus_black | impostor |  |  |  | +0.11414 ± 0.03649 | +0.08464 ± 0.02993 | +0.03937 ± 0.00362 |
| SwinV2-Tiny | A_nonannulus_mean | genuine | +0.00477 ± 0.00123 | +0.00932 ± 0.01811 | +0.00417 ± 0.00260 |  |  |  |
| SwinV2-Tiny | A_nonannulus_mean | impostor |  |  |  | +0.09688 ± 0.01137 | +0.07107 ± 0.00612 | +0.02549 ± 0.01100 |

## Subject influence

Remove each subject and all incident comparisons, recompute all4 metrics, and pair against the same raw baseline removal. Table summarizes the mean EER effect across3 seeds. Complete per-seed/four-metric effects and subject identifiers are saved.

| dataset | architecture | variant | full_mean_eer_effect_pp | loo_min_mean_effect_pp | loo_max_mean_effect_pp | sign_reversals | reversing_subjects | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | A_B1_black | 6.8394 | 6.62156 | 7.2456 | 0 |  | 359 | 0.4062 |
| CUST-Iris | ResNet-18 | A_B1_mean | 6.23823 | 5.91743 | 6.57349 | 0 |  | 359 | 0.33526 |
| CUST-Iris | ResNet-18 | A_B2_black | 7.81264 | 7.50581 | 8.164 | 0 |  | 359 | 0.35136 |
| CUST-Iris | ResNet-18 | A_B2_mean | 6.03752 | 5.69573 | 6.32369 | 0 |  | 252 | 0.34179 |
| CUST-Iris | ResNet-18 | A_nonannulus_black | 1.33354 | 1.08851 | 1.46465 | 0 |  | 143 | 0.24504 |
| CUST-Iris | ResNet-18 | A_nonannulus_mean | 1.33354 | 1.15445 | 1.39335 | 0 |  | 309 | 0.1791 |
| CUST-Iris | SwinV2-Tiny | A_B1_black | 5.38965 | 5.19335 | 5.65459 | 0 |  | 365 | 0.26494 |
| CUST-Iris | SwinV2-Tiny | A_B1_mean | 3.71909 | 3.46778 | 3.91176 | 0 |  | 147 | 0.25131 |
| CUST-Iris | SwinV2-Tiny | A_B2_black | 5.26551 | 5.07977 | 5.52923 | 0 |  | 359 | 0.26373 |
| CUST-Iris | SwinV2-Tiny | A_B2_mean | 3.71718 | 3.38882 | 3.92716 | 0 |  | 147 | 0.32836 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_black | 1.12287 | 0.90065 | 1.21212 | 0 |  | 320 | 0.22222 |
| CUST-Iris | SwinV2-Tiny | A_nonannulus_mean | 1.63881 | 1.25971 | 1.70432 | 0 |  | 320 | 0.3791 |

## Individual seed results

| architecture | variant | seed | selected_epoch | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | A_A | 42 | 64 | 1.104101 | 0.99955 | 98.73817 | 96.214511 |
| ResNet-18 | A_B1_black | 42 | 64 | 7.886435 | 0.978262 | 74.921136 | 50.315457 |
| ResNet-18 | A_B2_black | 42 | 64 | 8.359621 | 0.971874 | 67.507886 | 41.167192 |
| ResNet-18 | A_B1_mean | 42 | 64 | 7.255521 | 0.981347 | 79.652997 | 55.205047 |
| ResNet-18 | A_B2_mean | 42 | 64 | 7.413249 | 0.979241 | 79.810726 | 53.785489 |
| ResNet-18 | A_nonannulus_black | 42 | 64 | 2.523659 | 0.997296 | 96.214511 | 89.274448 |
| ResNet-18 | A_nonannulus_mean | 42 | 64 | 2.208202 | 0.997797 | 95.583596 | 91.167192 |
| ResNet-18 | A_A | 123 | 110 | 1.677601 | 0.998056 | 97.791798 | 94.479495 |
| ResNet-18 | A_B1_black | 123 | 110 | 9.068658 | 0.973993 | 72.082019 | 45.741325 |
| ResNet-18 | A_B2_black | 123 | 110 | 9.726957 | 0.969001 | 67.192429 | 41.798107 |
| ResNet-18 | A_B1_mean | 123 | 110 | 8.247181 | 0.977056 | 76.182965 | 55.047319 |
| ResNet-18 | A_B2_mean | 123 | 110 | 7.743118 | 0.975914 | 73.501577 | 52.681388 |
| ResNet-18 | A_nonannulus_black | 123 | 110 | 3.154574 | 0.991048 | 94.321767 | 91.009464 |
| ResNet-18 | A_nonannulus_mean | 123 | 110 | 3.62776 | 0.992052 | 94.321767 | 89.432177 |
| ResNet-18 | A_A | 2025 | 114 | 1.419558 | 0.998076 | 98.107256 | 96.37224 |
| ResNet-18 | A_B1_black | 2025 | 114 | 7.764353 | 0.978824 | 74.763407 | 51.577287 |
| ResNet-18 | A_B2_black | 2025 | 114 | 9.552602 | 0.970251 | 67.0347 | 46.37224 |
| ResNet-18 | A_B1_mean | 2025 | 114 | 7.413249 | 0.980199 | 73.659306 | 48.580442 |
| ResNet-18 | A_B2_mean | 2025 | 114 | 7.157466 | 0.979275 | 71.766562 | 45.899054 |
| ResNet-18 | A_nonannulus_black | 2025 | 114 | 2.523659 | 0.994897 | 95.583596 | 91.640379 |
| ResNet-18 | A_nonannulus_mean | 2025 | 114 | 2.365931 | 0.996079 | 97.160883 | 92.271293 |
| SwinV2-Tiny | A_A | 42 | 35 | 2.208202 | 0.997941 | 95.11041 | 89.747634 |
| SwinV2-Tiny | A_B1_black | 42 | 35 | 6.799817 | 0.983537 | 72.239748 | 44.952681 |
| SwinV2-Tiny | A_B2_black | 42 | 35 | 6.729404 | 0.983657 | 70.662461 | 40.063091 |
| SwinV2-Tiny | A_B1_mean | 42 | 35 | 5.993691 | 0.988893 | 81.072555 | 58.201893 |
| SwinV2-Tiny | A_B2_mean | 42 | 35 | 5.740279 | 0.989095 | 80.599369 | 57.728707 |
| SwinV2-Tiny | A_nonannulus_black | 42 | 35 | 3.52285 | 0.992445 | 92.586751 | 80.44164 |
| SwinV2-Tiny | A_nonannulus_mean | 42 | 35 | 4.258675 | 0.99095 | 91.640379 | 83.280757 |
| SwinV2-Tiny | A_A | 123 | 31 | 1.577287 | 0.999275 | 98.264984 | 90.694006 |
| SwinV2-Tiny | A_B1_black | 123 | 31 | 7.886435 | 0.979593 | 67.665615 | 39.274448 |
| SwinV2-Tiny | A_B2_black | 123 | 31 | 7.584411 | 0.980151 | 64.826498 | 39.905363 |
| SwinV2-Tiny | A_B1_mean | 123 | 31 | 5.047319 | 0.990911 | 81.861199 | 63.091483 |
| SwinV2-Tiny | A_B2_mean | 123 | 31 | 5.190393 | 0.990985 | 83.123028 | 63.880126 |
| SwinV2-Tiny | A_nonannulus_black | 123 | 31 | 2.718138 | 0.996978 | 93.375394 | 81.70347 |
| SwinV2-Tiny | A_nonannulus_mean | 123 | 31 | 3.118259 | 0.996834 | 93.533123 | 80.44164 |
| SwinV2-Tiny | A_A | 2025 | 23 | 1.829602 | 0.998568 | 97.476341 | 93.533123 |
| SwinV2-Tiny | A_B1_black | 2025 | 23 | 7.097792 | 0.979432 | 69.55836 | 40.536278 |
| SwinV2-Tiny | A_B2_black | 2025 | 23 | 7.097792 | 0.979697 | 67.981073 | 39.589905 |
| SwinV2-Tiny | A_B1_mean | 2025 | 23 | 5.731338 | 0.987304 | 79.337539 | 50.630915 |
| SwinV2-Tiny | A_B2_mean | 2025 | 23 | 5.835962 | 0.986772 | 78.391167 | 52.839117 |
| SwinV2-Tiny | A_nonannulus_black | 2025 | 23 | 2.742727 | 0.996672 | 94.479495 | 87.697161 |
| SwinV2-Tiny | A_nonannulus_mean | 2025 | 23 | 3.154574 | 0.995844 | 94.321767 | 88.170347 |

## Input statistics and QC examples

| dataset | variant | images | replaced_pixels_median | retained_pixels_median | padding_pixels_median | replaced_intensity_l1_median | content_mean_median | content_std_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | A_A | 427 | 0.0 | 102400.0 | 0.0 | 0.0 | 0.468567 | 0.145613 |
| CUST-Iris | A_B1_black | 427 | 82680.0 | 19720.0 | 0.0 | 0.500377 | 0.068332 | 0.140953 |
| CUST-Iris | A_B1_mean | 427 | 82680.0 | 19720.0 | 0.0 | 0.126112 | 0.457957 | 0.054082 |
| CUST-Iris | A_B2_black | 427 | 83069.0 | 19331.0 | 0.0 | 0.499106 | 0.067436 | 0.140187 |
| CUST-Iris | A_B2_mean | 427 | 83069.0 | 19331.0 | 0.0 | 0.126721 | 0.458693 | 0.053387 |
| CUST-Iris | A_nonannulus_black | 427 | 19720.0 | 82680.0 | 0.0 | 0.35172 | 0.402366 | 0.235778 |
| CUST-Iris | A_nonannulus_mean | 427 | 19720.0 | 82680.0 | 0.0 | 0.132209 | 0.496271 | 0.132549 |

Examples were chosen as the first3 common subjects by image ID, before recognition scoring.









