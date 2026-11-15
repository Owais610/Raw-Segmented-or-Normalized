> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-E: raw-ocular-trained checkpoints on iris-only and complementary inputs

**Independent explanatory frozen-model input intervention.** Only the original six E1-A best checkpoints were used: ResNet-18/SwinV2-Tiny and seeds42/123/2025. B1/B2-trained checkpoints are never substituted. All models stay frozen, in original eval/AMP/input configuration. No training, normalization estimation, threshold fitting or preprocessing/seed selection occurred. Every evaluated cell within a dataset uses exactly its existing E2-A common images and exhaustive pairs. The original raw baseline scores are reused and remain untouched.

## Exact populations

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic | complement_available | complement_unreliable_images | existing_b1_b2_tensors_bit_exact | retained_iris_pixels_bit_exact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 | True | 0 | True | True |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 | True | 0 | True | True |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 | True | 0 | True | True |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 | True | 0 | True | True |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 | True | 0 | True | True |

Original test datasets remain separate from external zero-shot domains. Same-subject opposite eyes are a separate diagnostic, not primary impostors. The fixed normalization is mean0.48287347719744544/std0.2741831329802273 on unchanged320x320 coordinates; no extra resize or crop.

## Input conditions and pixel audit

`A_A` is the original raw input. `A_B1_black` and `A_B2_black` use the literal existing Cartesian loaders/outputs with predicted eyelashes retained/removed. Mean controls retain identical supports and fill only masked nonpadding content with the frozen training mean. Original black padding remains unchanged. `A_nonannulus_*` masks exactly the B1 annulus and retains every other raw pixel, including the pupil; it is not a pure periocular-only representation or removal of the entire iris disc.

Black fill corresponds to normalized value -1.761134863; mean fill corresponds to normalized0. These differ materially in image statistics. Fill alpha1. Every unmasked tensor pixel remains bit-identical.

| dataset | images | b1_max_tensor_error | b2_max_tensor_error | b1_mixed_native_fraction_median | b2_mixed_native_fraction_median | complement_mixed_native_fraction_median | complement_reliable_images |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | 523 | 0.0 | 0.0 | 0.0177454 | 0.018656 | 0.0029491 | 523 |
| CASIA-Interval | 395 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 395 |
| CUST-Iris | 427 | 0.0 | 0.0 | 0.0164897 | 0.0181463 | 0.0040154 | 427 |
| IITD | 308 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 308 |
| UTIRIS_NIR | 770 | 0.0 | 0.0 | 0.0270527 | 0.0313922 | 0.0071087 | 770 |

A/B1/B2 retained output pixels, zero-fill semantics and coordinate grids were checked for every image. Native images were resized before binary masking, so some retained boundary pixels can mix native tissues across a mask boundary. The table records median fractions of supported/retained output pixels with such native support mixtures using an INTER_AREA mask-footprint proxy. This does not change or repair any input, and it prevents assuming perfect isolation of native anatomical texture. All per-image discrepancy counts, mask/source hashes, dimensions, warning flags and input-statistic changes are retained.

Complement reliability is conditional on existing accepted pure-V2 geometry, original nonempty/consistent iris/pupil/annulus supports, exact cached mask transforms and nonempty retained content. It is not manual anatomical ground truth. Existing border/occlusion and UTIRIS folder/filename conflict flags remain. If any common image failed those checks the complement would be unavailable for that whole dataset, preserving identical membership; see UNAVAILABLE.json.

## Main descriptive results

| dataset | architecture | A_A EER (%) | A_B1_black EER (%) | A_B2_black EER (%) | A_B1_mean EER (%) | A_B2_mean EER (%) | A_nonannulus_black EER (%) | A_nonannulus_mean EER (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | 1.400 ± 0.287 | 8.240 ± 0.720 | 9.213 ± 0.744 | 7.639 ± 0.533 | 7.438 ± 0.294 | 2.734 ± 0.364 | 2.734 ± 0.778 |
| CUST-Iris | SwinV2-Tiny | 1.872 ± 0.318 | 7.261 ± 0.561 | 7.137 ± 0.429 | 5.591 ± 0.489 | 5.589 ± 0.348 | 2.995 ± 0.458 | 3.511 ± 0.648 |
| CASIA-Interval | ResNet-18 | 2.101 ± 0.667 | 9.398 ± 1.485 | 10.983 ± 1.074 | 6.796 ± 0.719 | 7.160 ± 0.593 | 7.539 ± 0.517 | 7.057 ± 0.735 |
| CASIA-Interval | SwinV2-Tiny | 3.306 ± 0.357 | 6.150 ± 0.398 | 6.525 ± 0.441 | 6.719 ± 0.780 | 6.599 ± 0.338 | 6.184 ± 0.894 | 5.807 ± 0.309 |
| IITD | ResNet-18 | 0.760 ± 0.360 | 3.220 ± 0.233 | 3.435 ± 0.380 | 3.698 ± 0.721 | 3.571 ± 0.969 | 3.185 ± 0.637 | 2.866 ± 0.730 |
| IITD | SwinV2-Tiny | 1.612 ± 0.507 | 2.683 ± 0.544 | 2.990 ± 0.847 | 2.533 ± 0.363 | 2.972 ± 0.092 | 2.645 ± 1.097 | 2.825 ± 0.716 |
| AMF | ResNet-18 | 1.024 ± 0.454 | 4.103 ± 0.467 | 5.305 ± 0.316 | 5.568 ± 0.521 | 5.641 ± 0.639 | 2.059 ± 0.187 | 1.862 ± 0.557 |
| AMF | SwinV2-Tiny | 1.336 ± 0.294 | 3.204 ± 0.583 | 3.417 ± 0.575 | 3.371 ± 0.511 | 3.154 ± 0.601 | 2.104 ± 0.248 | 1.909 ± 0.242 |
| UTIRIS_NIR | ResNet-18 | 6.973 ± 0.357 | 13.385 ± 0.099 | 13.540 ± 0.595 | 14.390 ± 1.720 | 13.338 ± 1.186 | 13.331 ± 1.090 | 12.046 ± 1.459 |
| UTIRIS_NIR | SwinV2-Tiny | 9.956 ± 2.944 | 12.937 ± 3.843 | 12.871 ± 3.608 | 12.920 ± 3.699 | 12.919 ± 3.182 | 14.486 ± 1.657 | 13.015 ± 2.418 |

Cells are EER percent mean ± sample SD across the same three numerical seeds. Lower EER is better. The question is performance change within each frozen raw checkpoint, not whether an independently trained B1/B2 model is stronger. Full EER/AUC/TAR results and all individual seeds follow below. No fill or seed is selected as a new pipeline.

## Interpretation safeguards

Lower performance after iris-only masking does not prove a periocular identity shortcut. Test-time distribution mismatch, artificial boundaries, changed area/intensity statistics, residual native interpolation mixtures and segmentation errors remain confounds. Mean-fill controls address one fill-statistics intervention, not all these confounds. Preserved performance indicates sufficient information under this tested transformation, not that the raw model originally ignored non-iris information. Complement performance can use retained pupil information and cannot establish a pure periocular identity channel. Iris-only and complement masks remove unequal amounts and content; input-statistic tables expose those differences.

ROC-interpolated TAR is not an observed fixed-threshold operating point. No threshold was fitted on these datasets. Repeated captures/pairs are dependent; sample SD across3 seeds measures training-seed variation on the same subjects, not participant confidence or causal significance. Subject-removal analyses assess influence rather than pairwise-independent uncertainty.

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











## Reproducibility and preservation