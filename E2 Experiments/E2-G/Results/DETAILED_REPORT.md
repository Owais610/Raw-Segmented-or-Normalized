# E2-G: segmentation-mask geometry in Cartesian iris verification models

This independent frozen-model input intervention was added after E1 and E2-A to E2-F. It evaluates the twelve original E1-B1/B2 best checkpoints: two architectures, two training representations, three seeds. All 60 binary-input evaluations use exactly the existing E2-A matched populations and exhaustive pairs. Original grayscale results are reused without modification. No training, fine-tuning, checkpoint selection, normalization estimation or threshold fitting occurred.

## Exact inputs

**B1 → B1 binary annulus:** white where iris AND NOT pupil, black everywhere else. **B2 → B2 binary support:** white where annulus AND NOT predicted eyelashes, black elsewhere. These are filled support masks, not outlines. Every input uses the original 320×320 coordinates and black padding. No grayscale samples, segmentation probabilities, antialiasing, additional resizing, cropping, polar conversion or image enhancement enter binary inference. B1/B2 supports are never exchanged between trained conditions. Native formulas and original nearest-exact letterbox transforms were reconstructed for every image and matched the existing cached masks exactly.

Frozen normalization: mean 0.48287347719744544, std 0.2741831329802273; binary black maps to -1.761134873 and white to 1.886062491. The original 256-D normalized embedding encoders and per-checkpoint AMP settings are unchanged, including Swin dynamic attention masks and float32 window attention. All models run in eval mode with gradients disabled; no optimizer is constructed.

## Matched populations and coverage

| dataset | images | subjects | iris_ids | left | right | genuine | impostor | opposite_eye_diagnostic | b1_empty | b2_empty | all_native_masks_exact | all_b2_subset_b1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 212 | 215 | 634 | 89473 | 844 | 0 | 0 | True | True |
| CASIA-Interval | 395 | 37 | 59 | 200 | 195 | 1353 | 75272 | 1190 | 0 | 0 | True | True |
| IITD | 308 | 32 | 63 | 164 | 144 | 628 | 45936 | 714 | 0 | 0 | True | True |
| AMF | 523 | 54 | 108 | 262 | 261 | 1015 | 134214 | 1274 | 0 | 0 | True | True |
| UTIRIS_NIR | 770 | 79 | 158 | 388 | 382 | 1544 | 292613 | 1908 | 0 | 0 | True | True |

CUST-Iris, CASIA-Interval and IITD contain only their original frozen test subjects; AMF and UTIRIS NIR remain independent external domains. There are 2,423 images total, evaluated independently within each dataset. No training/validation image is added. Same-person opposite eyes are a separate diagnostic and never primary impostors. Exact-source identical-image pairs are absent. No new subject assignments, exclusions, image eligibility or pair generation occurred.

## Main results

Values are mean ± sample SD across all three seeds (42, 123, 2025). EER is percent; AUC is [0,1]; paired changes are binary minus the SAME checkpoint’s grayscale baseline, in percentage points. No best seed is selected.

| dataset | architecture | condition | baseline_eer_percent | baseline_auc | binary_eer_percent | binary_auc | paired_eer_change_pp |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-B1 | 1.341 ± 0.209 | 0.99924 ± 0.00028 | 15.976 ± 0.374 | 0.91796 ± 0.00298 | +14.635 ± 0.256 |
| CASIA-Interval | ResNet-18 | E1-B1 | 2.782 ± 0.346 | 0.99587 ± 0.00077 | 18.566 ± 1.275 | 0.89666 ± 0.01180 | +15.784 ± 1.598 |
| IITD | ResNet-18 | E1-B1 | 1.069 ± 0.254 | 0.99926 ± 0.00040 | 5.748 ± 0.332 | 0.98442 ± 0.00072 | +4.678 ± 0.079 |
| AMF | ResNet-18 | E1-B1 | 1.642 ± 0.284 | 0.99876 ± 0.00054 | 10.143 ± 0.574 | 0.96430 ± 0.00152 | +8.501 ± 0.512 |
| UTIRIS_NIR | ResNet-18 | E1-B1 | 6.636 ± 0.349 | 0.98365 ± 0.00355 | 20.142 ± 0.847 | 0.88205 ± 0.00615 | +13.507 ± 0.750 |
| CUST-Iris | ResNet-18 | E1-B2 | 1.420 ± 0.340 | 0.99909 ± 0.00039 | 15.644 ± 0.630 | 0.91950 ± 0.00840 | +14.224 ± 0.553 |
| CASIA-Interval | ResNet-18 | E1-B2 | 3.863 ± 1.566 | 0.99023 ± 0.00221 | 13.188 ± 0.696 | 0.94264 ± 0.00585 | +9.325 ± 1.844 |
| IITD | ResNet-18 | E1-B2 | 1.324 ± 0.788 | 0.99856 ± 0.00194 | 4.134 ± 0.432 | 0.99125 ± 0.00032 | +2.810 ± 1.208 |
| AMF | ResNet-18 | E1-B2 | 1.526 ± 0.290 | 0.99888 ± 0.00049 | 9.609 ± 0.906 | 0.96517 ± 0.00804 | +8.083 ± 0.628 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | 7.303 ± 0.418 | 0.97909 ± 0.00392 | 19.244 ± 0.659 | 0.88745 ± 0.00648 | +11.940 ± 0.869 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | 1.541 ± 0.214 | 0.99871 ± 0.00037 | 31.020 ± 3.994 | 0.75599 ± 0.04674 | +29.479 ± 4.136 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | 3.231 ± 0.527 | 0.99582 ± 0.00085 | 38.630 ± 2.604 | 0.65765 ± 0.03658 | +35.400 ± 2.895 |
| IITD | SwinV2-Tiny | E1-B1 | 0.934 ± 0.515 | 0.99972 ± 0.00024 | 27.713 ± 3.870 | 0.78750 ± 0.03983 | +26.779 ± 3.620 |
| AMF | SwinV2-Tiny | E1-B1 | 1.793 ± 0.580 | 0.99838 ± 0.00078 | 25.780 ± 4.342 | 0.82325 ± 0.05044 | +23.987 ± 4.570 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | 6.717 ± 1.233 | 0.98152 ± 0.00695 | 40.404 ± 1.981 | 0.63350 ± 0.02574 | +33.687 ± 0.822 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | 2.004 ± 0.378 | 0.99830 ± 0.00043 | 23.688 ± 1.255 | 0.83849 ± 0.01464 | +21.684 ± 1.346 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | 3.302 ± 0.693 | 0.99426 ± 0.00271 | 16.449 ± 0.508 | 0.91030 ± 0.00472 | +13.148 ± 0.903 |
| IITD | SwinV2-Tiny | E1-B2 | 1.159 ± 0.144 | 0.99933 ± 0.00013 | 11.837 ± 2.432 | 0.95010 ± 0.01699 | +10.678 ± 2.376 |
| AMF | SwinV2-Tiny | E1-B2 | 1.465 ± 0.218 | 0.99892 ± 0.00049 | 16.158 ± 0.769 | 0.91754 ± 0.00551 | +14.693 ± 0.739 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | 6.292 ± 0.518 | 0.98476 ± 0.00161 | 28.092 ± 0.924 | 0.79487 ± 0.01258 | +21.799 ± 1.336 |

## Identical-mask collisions

| dataset | condition | pair_kind | pairs | identical_binary_masks | distinct_masks |
| --- | --- | --- | --- | --- | --- |
| CUST-Iris | E1-B1 | genuine | 634 | 0 | 427 |
| CUST-Iris | E1-B1 | impostor | 89473 | 0 | 427 |
| CUST-Iris | E1-B1 | opposite_eye_diagnostic | 844 | 0 | 427 |
| CUST-Iris | E1-B2 | genuine | 634 | 0 | 427 |
| CUST-Iris | E1-B2 | impostor | 89473 | 0 | 427 |
| CUST-Iris | E1-B2 | opposite_eye_diagnostic | 844 | 0 | 427 |
| CASIA-Interval | E1-B1 | genuine | 1353 | 0 | 395 |
| CASIA-Interval | E1-B1 | impostor | 75272 | 0 | 395 |
| CASIA-Interval | E1-B1 | opposite_eye_diagnostic | 1190 | 0 | 395 |
| CASIA-Interval | E1-B2 | genuine | 1353 | 0 | 395 |
| CASIA-Interval | E1-B2 | impostor | 75272 | 0 | 395 |
| CASIA-Interval | E1-B2 | opposite_eye_diagnostic | 1190 | 0 | 395 |
| IITD | E1-B1 | genuine | 628 | 0 | 308 |
| IITD | E1-B1 | impostor | 45936 | 0 | 308 |
| IITD | E1-B1 | opposite_eye_diagnostic | 714 | 0 | 308 |
| IITD | E1-B2 | genuine | 628 | 0 | 308 |
| IITD | E1-B2 | impostor | 45936 | 0 | 308 |
| IITD | E1-B2 | opposite_eye_diagnostic | 714 | 0 | 308 |
| AMF | E1-B1 | genuine | 1015 | 0 | 523 |
| AMF | E1-B1 | impostor | 134214 | 0 | 523 |
| AMF | E1-B1 | opposite_eye_diagnostic | 1274 | 0 | 523 |
| AMF | E1-B2 | genuine | 1015 | 0 | 523 |
| AMF | E1-B2 | impostor | 134214 | 0 | 523 |
| AMF | E1-B2 | opposite_eye_diagnostic | 1274 | 0 | 523 |
| UTIRIS_NIR | E1-B1 | genuine | 1544 | 0 | 770 |
| UTIRIS_NIR | E1-B1 | impostor | 292613 | 0 | 770 |
| UTIRIS_NIR | E1-B1 | opposite_eye_diagnostic | 1908 | 0 | 770 |
| UTIRIS_NIR | E1-B2 | genuine | 1544 | 0 | 770 |
| UTIRIS_NIR | E1-B2 | impostor | 292613 | 0 | 770 |
| UTIRIS_NIR | E1-B2 | opposite_eye_diagnostic | 1908 | 0 | 770 |

These are identical binary geometries from distinct, nonidentical source images. They remain in both genuine and impostor populations. High cosine similarity for such pairs is an expected consequence of discarding grayscale texture, not a reason for exclusion.

## Interpretation and practical limits

The intervention removes all grayscale iris texture. It retains image-relative boundary shape, iris/pupil position and size, visible-support fragmentation, predicted occlusion geometry, and the B2 predicted eyelash footprint. These include acquisition and segmentation effects, so the experiment is not a pure clean-anatomy identity test. Binary foreground 255 also changes input statistics and edge contrast substantially from training. Non-chance performance is descriptive evidence of discrimination available to a frozen model under this specific intervention; it does not establish that segmentation geometry caused its original grayscale accuracy. Degradation or chance-like performance does not prove geometry carries no identity information or that a model trained directly on masks would fail. Predicted masks are not anatomical ground truth.

Chance references of EER 50% and AUC 0.5 are descriptive, without a significance claim. TAR@FAR uses the original complete-ROC interpolation and is not a measured fixed-threshold operating point. Repeated pairs and captures are dependent. Sample SD across three training seeds is not a participant confidence interval. Subject-removal analyses measure influence, not independent-trial uncertainty. Comparisons do not pool any dataset score distributions or replace prior E1/E2 results.

# CUST-Iris: E2-G

## Absolute metrics

EER/TAR are percent, AUC [0,1]; mean ± sample SD over the three seeds.

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-B1 | binary_geometry | 15.9758 ± 0.3745 | 0.9180 ± 0.0030 | 39.1693 ± 2.9522 | 14.8791 ± 0.9242 |
| CUST-Iris | ResNet-18 | E1-B1 | segmented_grayscale | 1.3408 ± 0.2088 | 0.9992 ± 0.0003 | 98.2124 ± 0.6375 | 91.1672 ± 1.1041 |
| CUST-Iris | ResNet-18 | E1-B2 | binary_geometry | 15.6443 ± 0.6303 | 0.9195 ± 0.0084 | 36.6982 ± 3.4025 | 14.3533 ± 2.1912 |
| CUST-Iris | ResNet-18 | E1-B2 | segmented_grayscale | 1.4202 ± 0.3398 | 0.9991 ± 0.0004 | 97.8444 ± 0.7939 | 90.2734 ± 1.5799 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | binary_geometry | 31.0200 ± 3.9944 | 0.7560 ± 0.0467 | 14.0904 ± 2.4503 | 3.9432 ± 1.9124 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | segmented_grayscale | 1.5415 ± 0.2137 | 0.9987 ± 0.0004 | 97.4238 ± 0.5972 | 86.8034 ± 3.4061 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | binary_geometry | 23.6877 ± 1.2551 | 0.8385 ± 0.0146 | 16.9295 ± 3.5175 | 5.0473 ± 1.7350 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | segmented_grayscale | 2.0037 ± 0.3775 | 0.9983 ± 0.0004 | 96.3722 ± 1.5534 | 81.2303 ± 3.6957 |

## Paired within-checkpoint differences

EER/TAR differences are percentage points; AUC differences are on [0,1].

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-B1 | binary-minus-grayscale | 14.6349 ± 0.2562 | -0.0813 ± 0.0031 | -59.0431 ± 2.5644 | -76.2881 ± 1.9972 |
| CUST-Iris | ResNet-18 | E1-B2 | binary-minus-grayscale | 14.2242 ± 0.5529 | -0.0796 ± 0.0082 | -61.1462 ± 3.4748 | -75.9201 ± 3.7635 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | binary-minus-grayscale | 29.4785 ± 4.1358 | -0.2427 ± 0.0471 | -83.3333 ± 2.4452 | -82.8601 ± 5.2058 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | binary-minus-grayscale | 21.6840 ± 1.3459 | -0.1598 ± 0.0145 | -79.4427 ± 3.9663 | -76.1830 ± 5.2289 |

## All individual seeds

| architecture | condition | seed | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | E1-B1 | 42 | segmented_grayscale | 1.49878 | 0.99932 | 97.63407 | 92.27129 |
| ResNet-18 | E1-B1 | 42 | binary_geometry | 16.40379 | 0.91452 | 35.80442 | 14.19558 |
| ResNet-18 | E1-B1 | 123 | segmented_grayscale | 1.10410 | 0.99947 | 98.89590 | 91.16719 |
| ResNet-18 | E1-B1 | 123 | binary_geometry | 15.70865 | 0.91951 | 40.37855 | 14.51104 |
| ResNet-18 | E1-B1 | 2025 | segmented_grayscale | 1.41956 | 0.99893 | 98.10726 | 90.06309 |
| ResNet-18 | E1-B1 | 2025 | binary_geometry | 15.81483 | 0.91985 | 41.32492 | 15.93060 |
| ResNet-18 | E1-B2 | 42 | segmented_grayscale | 1.42836 | 0.99914 | 97.94953 | 91.48265 |
| ResNet-18 | E1-B2 | 42 | binary_geometry | 16.28871 | 0.91188 | 32.80757 | 12.93375 |
| ResNet-18 | E1-B2 | 123 | segmented_grayscale | 1.07630 | 0.99945 | 98.58044 | 88.48580 |
| ResNet-18 | E1-B2 | 123 | binary_geometry | 15.02911 | 0.92850 | 39.11672 | 16.87697 |
| ResNet-18 | E1-B2 | 2025 | segmented_grayscale | 1.75584 | 0.99868 | 97.00315 | 90.85174 |
| ResNet-18 | E1-B2 | 2025 | binary_geometry | 15.61514 | 0.91812 | 38.17035 | 13.24921 |
| SwinV2-Tiny | E1-B1 | 42 | segmented_grayscale | 1.31213 | 0.99892 | 98.10726 | 86.43533 |
| SwinV2-Tiny | E1-B1 | 42 | binary_geometry | 32.49211 | 0.74293 | 14.82650 | 5.04732 |
| SwinV2-Tiny | E1-B1 | 123 | segmented_grayscale | 1.73502 | 0.99828 | 97.00315 | 83.59621 |
| SwinV2-Tiny | E1-B1 | 123 | binary_geometry | 26.49842 | 0.80787 | 16.08833 | 5.04732 |
| SwinV2-Tiny | E1-B1 | 2025 | segmented_grayscale | 1.57729 | 0.99892 | 97.16088 | 90.37855 |
| SwinV2-Tiny | E1-B1 | 2025 | binary_geometry | 34.06940 | 0.71717 | 11.35647 | 1.73502 |
| SwinV2-Tiny | E1-B2 | 42 | segmented_grayscale | 1.73502 | 0.99862 | 97.63407 | 83.59621 |
| SwinV2-Tiny | E1-B2 | 42 | binary_geometry | 22.64035 | 0.85394 | 19.55836 | 5.04732 |
| SwinV2-Tiny | E1-B2 | 123 | segmented_grayscale | 2.43537 | 0.99781 | 94.63722 | 76.97161 |
| SwinV2-Tiny | E1-B2 | 123 | binary_geometry | 23.34385 | 0.83671 | 18.29653 | 6.78233 |
| SwinV2-Tiny | E1-B2 | 2025 | segmented_grayscale | 1.84078 | 0.99847 | 96.84543 | 83.12303 |
| SwinV2-Tiny | E1-B2 | 2025 | binary_geometry | 25.07886 | 0.82482 | 12.93375 | 3.31230 |

## Similarity-distribution changes

Values are binary minus grayscale, averaged within numerical seed, then mean/sample SD across seeds. Genuine mean and impostor p99/p99.9 distinguish score shifts from verification changes. Opposite-eye scores remain diagnostic.

| dataset | architecture | condition | pair_kind | mean_mean | mean_sample_sd | p99_mean | p99_sample_sd | p999_mean | p999_sample_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-B1 | genuine | 0.082982 | 0.010213 | 0.01214 | 0.001363 | 0.008517 | 0.001386 |
| CUST-Iris | ResNet-18 | E1-B1 | impostor | 0.861597 | 0.037829 | 0.363379 | 0.008933 | 0.238858 | 0.013181 |
| CUST-Iris | ResNet-18 | E1-B1 | opposite_eye_diagnostic | 0.439648 | 0.044903 | 0.109605 | 0.036212 | 0.082909 | 0.019987 |
| CUST-Iris | ResNet-18 | E1-B2 | genuine | 0.087399 | 0.004396 | 0.012208 | 0.003629 | 0.007809 | 0.001504 |
| CUST-Iris | ResNet-18 | E1-B2 | impostor | 0.861022 | 0.01068 | 0.360471 | 0.024601 | 0.22582 | 0.014876 |
| CUST-Iris | ResNet-18 | E1-B2 | opposite_eye_diagnostic | 0.423157 | 0.010865 | 0.117348 | 0.030954 | 0.096849 | 0.025764 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | genuine | 0.099697 | 0.003837 | 0.010579 | 0.002924 | 0.006914 | 0.003252 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | impostor | 0.947279 | 0.013564 | 0.342716 | 0.02536 | 0.18896 | 0.023669 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | opposite_eye_diagnostic | 0.449967 | 0.03762 | 0.08111 | 0.041321 | 0.061405 | 0.030368 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | genuine | 0.062295 | 0.009053 | 0.00747 | 0.001038 | 0.004285 | 0.001308 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | impostor | 0.799445 | 0.040511 | 0.313941 | 0.014228 | 0.167598 | 0.016403 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | opposite_eye_diagnostic | 0.338061 | 0.043386 | 0.058863 | 0.020153 | 0.04243 | 0.015425 |

## Subject influence

| dataset | architecture | condition | full_mean_eer_effect_pp | loo_min_effect_pp | loo_max_effect_pp | sign_reversals | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-B1 | 14.63494 | 14.26987 | 15.03423 | 0 | 286 | 0.39928 |
| CUST-Iris | ResNet-18 | E1-B2 | 14.22416 | 13.82762 | 14.63212 | 0 | 226 | 0.40797 |
| CUST-Iris | SwinV2-Tiny | E1-B1 | 29.4785 | 29.15253 | 29.87202 | 0 | 334 | 0.39352 |
| CUST-Iris | SwinV2-Tiny | E1-B2 | 21.68397 | 21.36709 | 22.30609 | 0 | 279 | 0.62212 |

Full per-image, subject-averaged and leave-one-subject-out values are in the corresponding CSV/Parquet tables. LOO removes all comparisons involving each omitted subject.

[CUST-Iris: previews, figures and independent report](Dataset%20Reports/CUST-Iris.md)

# CASIA-Interval: E2-G

## Absolute metrics

EER/TAR are percent, AUC [0,1]; mean ± sample SD over the three seeds.

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-B1 | binary_geometry | 18.5656 ± 1.2753 | 0.8967 ± 0.0118 | 27.9379 ± 4.9188 | 8.3518 ± 1.4101 |
| CASIA-Interval | ResNet-18 | E1-B1 | segmented_grayscale | 2.7820 ± 0.3462 | 0.9959 ± 0.0008 | 94.6046 ± 0.9665 | 83.7152 ± 2.0922 |
| CASIA-Interval | ResNet-18 | E1-B2 | binary_geometry | 13.1882 ± 0.6962 | 0.9426 ± 0.0059 | 46.4400 ± 5.0914 | 13.5009 ± 4.1293 |
| CASIA-Interval | ResNet-18 | E1-B2 | segmented_grayscale | 3.8632 ± 1.5662 | 0.9902 ± 0.0022 | 91.6482 ± 4.4976 | 76.0039 ± 10.2906 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | binary_geometry | 38.6302 ± 2.6040 | 0.6576 ± 0.0366 | 7.2185 ± 2.1792 | 2.1187 ± 1.1217 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | segmented_grayscale | 3.2307 ± 0.5268 | 0.9958 ± 0.0009 | 92.2148 ± 1.6664 | 80.0443 ± 2.8510 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | binary_geometry | 16.4492 ± 0.5081 | 0.9103 ± 0.0047 | 27.2727 ± 3.5160 | 7.9576 ± 3.2506 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | segmented_grayscale | 3.3017 ± 0.6931 | 0.9943 ± 0.0027 | 90.6874 ± 3.9505 | 72.2345 ± 11.6668 |

## Paired within-checkpoint differences

EER/TAR differences are percentage points; AUC differences are on [0,1].

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-B1 | binary-minus-grayscale | 15.7835 ± 1.5977 | -0.0992 ± 0.0125 | -66.6667 ± 5.5423 | -75.3634 ± 1.8244 |
| CASIA-Interval | ResNet-18 | E1-B2 | binary-minus-grayscale | 9.3250 ± 1.8443 | -0.0476 ± 0.0064 | -45.2082 ± 5.8600 | -62.5031 ± 12.8699 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | binary-minus-grayscale | 35.3995 ± 2.8947 | -0.3382 ± 0.0373 | -84.9963 ± 3.0750 | -77.9256 ± 3.9542 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | binary-minus-grayscale | 13.1475 ± 0.9030 | -0.0840 ± 0.0063 | -63.4146 ± 7.4513 | -64.2769 ± 13.5056 |

## All individual seeds

| architecture | condition | seed | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | E1-B1 | 42 | segmented_grayscale | 3.17812 | 0.99502 | 94.16112 | 84.84848 |
| ResNet-18 | E1-B1 | 42 | binary_geometry | 17.31321 | 0.90849 | 33.48115 | 9.97783 |
| ResNet-18 | E1-B1 | 123 | segmented_grayscale | 2.53746 | 0.99650 | 95.71323 | 84.99630 |
| ResNet-18 | E1-B1 | 123 | binary_geometry | 19.86263 | 0.88490 | 24.09460 | 7.61271 |
| ResNet-18 | E1-B1 | 2025 | segmented_grayscale | 2.63046 | 0.99609 | 93.93939 | 81.30081 |
| ResNet-18 | E1-B1 | 2025 | binary_geometry | 18.52083 | 0.89660 | 26.23799 | 7.46489 |
| ResNet-18 | E1-B2 | 42 | segmented_grayscale | 4.73023 | 0.98820 | 88.24834 | 64.81892 |
| ResNet-18 | E1-B2 | 42 | binary_geometry | 12.41685 | 0.94703 | 49.74132 | 17.14708 |
| ResNet-18 | E1-B2 | 123 | segmented_grayscale | 2.05521 | 0.99258 | 96.74797 | 85.07021 |
| ResNet-18 | E1-B2 | 123 | binary_geometry | 13.37768 | 0.94490 | 49.00222 | 14.33851 |
| ResNet-18 | E1-B2 | 2025 | segmented_grayscale | 4.80414 | 0.98990 | 89.94826 | 78.12269 |
| ResNet-18 | E1-B2 | 2025 | binary_geometry | 13.77006 | 0.93600 | 40.57650 | 9.01700 |
| SwinV2-Tiny | E1-B1 | 42 | segmented_grayscale | 3.17382 | 0.99632 | 90.61345 | 81.22690 |
| SwinV2-Tiny | E1-B1 | 42 | binary_geometry | 41.38950 | 0.61959 | 6.43016 | 1.92166 |
| SwinV2-Tiny | E1-B1 | 123 | segmented_grayscale | 3.78361 | 0.99484 | 92.09165 | 76.79231 |
| SwinV2-Tiny | E1-B1 | 123 | binary_geometry | 36.21582 | 0.69255 | 9.68219 | 3.32594 |
| SwinV2-Tiny | E1-B1 | 2025 | segmented_grayscale | 2.73466 | 0.99631 | 93.93939 | 82.11382 |
| SwinV2-Tiny | E1-B1 | 2025 | binary_geometry | 38.28529 | 0.66080 | 5.54324 | 1.10865 |
| SwinV2-Tiny | E1-B2 | 42 | segmented_grayscale | 2.53879 | 0.99737 | 94.30894 | 77.75314 |
| SwinV2-Tiny | E1-B2 | 42 | binary_geometry | 16.33407 | 0.90872 | 24.39024 | 4.21286 |
| SwinV2-Tiny | E1-B2 | 123 | segmented_grayscale | 3.89255 | 0.99238 | 86.47450 | 58.83222 |
| SwinV2-Tiny | E1-B2 | 123 | binary_geometry | 16.00861 | 0.91561 | 31.18995 | 10.05174 |
| SwinV2-Tiny | E1-B2 | 2025 | segmented_grayscale | 3.47376 | 0.99302 | 91.27864 | 80.11826 |
| SwinV2-Tiny | E1-B2 | 2025 | binary_geometry | 17.00500 | 0.90658 | 26.23799 | 9.60828 |

## Similarity-distribution changes

Values are binary minus grayscale, averaged within numerical seed, then mean/sample SD across seeds. Genuine mean and impostor p99/p99.9 distinguish score shifts from verification changes. Opposite-eye scores remain diagnostic.

| dataset | architecture | condition | pair_kind | mean_mean | mean_sample_sd | p99_mean | p99_sample_sd | p999_mean | p999_sample_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-B1 | genuine | 0.135272 | 0.005796 | 0.029388 | 0.004251 | 0.01897 | 0.002338 |
| CASIA-Interval | ResNet-18 | E1-B1 | impostor | 0.819372 | 0.060761 | 0.374915 | 0.025483 | 0.261813 | 0.02468 |
| CASIA-Interval | ResNet-18 | E1-B1 | opposite_eye_diagnostic | 0.502997 | 0.064435 | 0.151605 | 0.037755 | 0.09734 | 0.022548 |
| CASIA-Interval | ResNet-18 | E1-B2 | genuine | 0.134219 | 0.010111 | 0.025612 | 0.00543 | 0.020937 | 0.004332 |
| CASIA-Interval | ResNet-18 | E1-B2 | impostor | 0.689283 | 0.027895 | 0.346933 | 0.04491 | 0.245494 | 0.048416 |
| CASIA-Interval | ResNet-18 | E1-B2 | opposite_eye_diagnostic | 0.382426 | 0.018305 | 0.167341 | 0.034552 | 0.123682 | 0.03178 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | genuine | 0.148571 | 0.006438 | 0.020021 | 0.002424 | 0.012551 | 0.001081 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | impostor | 0.949263 | 0.006862 | 0.348832 | 0.033511 | 0.215831 | 0.02386 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | opposite_eye_diagnostic | 0.435675 | 0.03993 | 0.089584 | 0.013382 | 0.056623 | 0.01156 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | genuine | 0.09403 | 0.029714 | 0.019953 | 0.00623 | 0.011612 | 0.004165 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | impostor | 0.611189 | 0.104578 | 0.308609 | 0.07465 | 0.192721 | 0.069619 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | opposite_eye_diagnostic | 0.135519 | 0.08055 | 0.065007 | 0.020832 | 0.05004 | 0.013015 |

## Subject influence

| dataset | architecture | condition | full_mean_eer_effect_pp | loo_min_effect_pp | loo_max_effect_pp | sign_reversals | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-B1 | 15.78354 | 14.43956 | 16.36972 | 0 | 125 | 1.34398 |
| CASIA-Interval | ResNet-18 | E1-B2 | 9.325 | 7.93302 | 9.75557 | 0 | 125 | 1.39198 |
| CASIA-Interval | SwinV2-Tiny | E1-B1 | 35.39951 | 34.67791 | 35.99034 | 0 | 125 | 0.7216 |
| CASIA-Interval | SwinV2-Tiny | E1-B2 | 13.14752 | 11.68969 | 13.75189 | 0 | 125 | 1.45783 |

Full per-image, subject-averaged and leave-one-subject-out values are in the corresponding CSV/Parquet tables. LOO removes all comparisons involving each omitted subject.

[CASIA-Interval: previews, figures and independent report](Dataset%20Reports/CASIA-Interval.md)

# IITD: E2-G

## Absolute metrics

EER/TAR are percent, AUC [0,1]; mean ± sample SD over the three seeds.

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-B1 | binary_geometry | 5.7479 ± 0.3324 | 0.9844 ± 0.0007 | 79.6709 ± 0.9598 | 50.3715 ± 3.9468 |
| IITD | ResNet-18 | E1-B1 | segmented_grayscale | 1.0694 ± 0.2537 | 0.9993 ± 0.0004 | 98.8854 ± 0.3185 | 97.0276 ± 1.4795 |
| IITD | ResNet-18 | E1-B2 | binary_geometry | 4.1341 ± 0.4316 | 0.9913 ± 0.0003 | 88.3758 ± 0.5741 | 65.3397 ± 4.4652 |
| IITD | ResNet-18 | E1-B2 | segmented_grayscale | 1.3243 ± 0.7882 | 0.9986 ± 0.0019 | 98.1423 ± 1.8456 | 93.6306 ± 6.2102 |
| IITD | SwinV2-Tiny | E1-B1 | binary_geometry | 27.7130 ± 3.8701 | 0.7875 ± 0.0398 | 23.5138 ± 9.5824 | 7.8025 ± 4.2220 |
| IITD | SwinV2-Tiny | E1-B1 | segmented_grayscale | 0.9340 ± 0.5146 | 0.9997 ± 0.0002 | 99.2569 ± 0.7525 | 96.8684 ± 1.2969 |
| IITD | SwinV2-Tiny | E1-B2 | binary_geometry | 11.8365 ± 2.4324 | 0.9501 ± 0.0170 | 51.1146 ± 7.7291 | 22.5584 ± 6.1781 |
| IITD | SwinV2-Tiny | E1-B2 | segmented_grayscale | 1.1590 ± 0.1443 | 0.9993 ± 0.0001 | 98.7261 ± 0.2758 | 96.1253 ± 0.8770 |

## Paired within-checkpoint differences

EER/TAR differences are percentage points; AUC differences are on [0,1].

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-B1 | binary-minus-grayscale | 4.6785 ± 0.0788 | -0.0148 ± 0.0010 | -19.2144 ± 0.6435 | -46.6561 ± 2.7210 |
| IITD | ResNet-18 | E1-B2 | binary-minus-grayscale | 2.8098 ± 1.2080 | -0.0073 ± 0.0021 | -9.7665 ± 2.0163 | -28.2909 ± 3.9307 |
| IITD | SwinV2-Tiny | E1-B1 | binary-minus-grayscale | 26.7790 ± 3.6198 | -0.2122 ± 0.0397 | -75.7431 ± 9.8241 | -89.0658 ± 4.6050 |
| IITD | SwinV2-Tiny | E1-B2 | binary-minus-grayscale | 10.6775 ± 2.3762 | -0.0492 ± 0.0169 | -47.6115 ± 7.6648 | -73.5669 ± 6.3515 |

## All individual seeds

| architecture | condition | seed | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | E1-B1 | 42 | segmented_grayscale | 1.11465 | 0.99883 | 98.88535 | 96.33758 |
| ResNet-18 | E1-B1 | 42 | binary_geometry | 5.81243 | 0.98512 | 79.77707 | 46.81529 |
| ResNet-18 | E1-B1 | 123 | segmented_grayscale | 0.79618 | 0.99963 | 99.20382 | 98.72611 |
| ResNet-18 | E1-B1 | 123 | binary_geometry | 5.38793 | 0.98446 | 80.57325 | 54.61783 |
| ResNet-18 | E1-B1 | 2025 | segmented_grayscale | 1.29746 | 0.99932 | 98.56688 | 96.01911 |
| ResNet-18 | E1-B1 | 2025 | binary_geometry | 6.04330 | 0.98369 | 78.66242 | 49.68153 |
| ResNet-18 | E1-B2 | 42 | segmented_grayscale | 2.22930 | 0.99632 | 96.01911 | 86.46497 |
| ResNet-18 | E1-B2 | 42 | binary_geometry | 3.64420 | 0.99143 | 88.53503 | 61.46497 |
| ResNet-18 | E1-B2 | 123 | segmented_grayscale | 0.95541 | 0.99963 | 99.04459 | 96.97452 |
| ResNet-18 | E1-B2 | 123 | binary_geometry | 4.45860 | 0.99088 | 87.73885 | 64.33121 |
| ResNet-18 | E1-B2 | 2025 | segmented_grayscale | 0.78805 | 0.99973 | 99.36306 | 97.45223 |
| ResNet-18 | E1-B2 | 2025 | binary_geometry | 4.29936 | 0.99144 | 88.85350 | 70.22293 |
| SwinV2-Tiny | E1-B1 | 42 | segmented_grayscale | 1.52821 | 0.99945 | 98.40764 | 95.38217 |
| SwinV2-Tiny | E1-B1 | 42 | binary_geometry | 30.11364 | 0.76487 | 24.36306 | 7.96178 |
| SwinV2-Tiny | E1-B1 | 123 | segmented_grayscale | 0.63694 | 0.99983 | 99.52229 | 97.45223 |
| SwinV2-Tiny | E1-B1 | 123 | binary_geometry | 23.24841 | 0.83349 | 32.64331 | 11.94268 |
| SwinV2-Tiny | E1-B1 | 2025 | segmented_grayscale | 0.63694 | 0.99989 | 99.84076 | 97.77070 |
| SwinV2-Tiny | E1-B1 | 2025 | binary_geometry | 29.77707 | 0.76415 | 13.53503 | 3.50318 |
| SwinV2-Tiny | E1-B2 | 42 | segmented_grayscale | 1.27389 | 0.99921 | 98.56688 | 96.17834 |
| SwinV2-Tiny | E1-B2 | 42 | binary_geometry | 14.49045 | 0.93121 | 42.51592 | 15.44586 |
| SwinV2-Tiny | E1-B2 | 123 | segmented_grayscale | 1.20603 | 0.99933 | 98.56688 | 96.97452 |
| SwinV2-Tiny | E1-B2 | 123 | binary_geometry | 9.71338 | 0.96412 | 57.48408 | 25.63694 |
| SwinV2-Tiny | E1-B2 | 2025 | segmented_grayscale | 0.99704 | 0.99946 | 99.04459 | 95.22293 |
| SwinV2-Tiny | E1-B2 | 2025 | binary_geometry | 11.30573 | 0.95497 | 53.34395 | 26.59236 |

## Similarity-distribution changes

Values are binary minus grayscale, averaged within numerical seed, then mean/sample SD across seeds. Genuine mean and impostor p99/p99.9 distinguish score shifts from verification changes. Opposite-eye scores remain diagnostic.

| dataset | architecture | condition | pair_kind | mean_mean | mean_sample_sd | p99_mean | p99_sample_sd | p999_mean | p999_sample_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-B1 | genuine | 0.082027 | 0.010396 | 0.020783 | 0.003465 | 0.01525 | 0.003254 |
| IITD | ResNet-18 | E1-B1 | impostor | 0.811445 | 0.032152 | 0.40546 | 0.037442 | 0.29429 | 0.034509 |
| IITD | ResNet-18 | E1-B1 | opposite_eye_diagnostic | 0.437873 | 0.039842 | 0.172472 | 0.018881 | 0.160591 | 0.017862 |
| IITD | ResNet-18 | E1-B2 | genuine | 0.094615 | 0.006755 | 0.021378 | 0.00507 | 0.014035 | 0.003614 |
| IITD | ResNet-18 | E1-B2 | impostor | 0.809698 | 0.034217 | 0.391373 | 0.048114 | 0.265512 | 0.072829 |
| IITD | ResNet-18 | E1-B2 | opposite_eye_diagnostic | 0.420566 | 0.024117 | 0.171152 | 0.007424 | 0.134157 | 0.017307 |
| IITD | SwinV2-Tiny | E1-B1 | genuine | 0.064565 | 0.004745 | 0.009677 | 0.001569 | 0.007226 | 0.001017 |
| IITD | SwinV2-Tiny | E1-B1 | impostor | 0.908275 | 0.00705 | 0.342844 | 0.024897 | 0.220778 | 0.015515 |
| IITD | SwinV2-Tiny | E1-B1 | opposite_eye_diagnostic | 0.412585 | 0.030448 | 0.145336 | 0.020787 | 0.111988 | 0.024617 |
| IITD | SwinV2-Tiny | E1-B2 | genuine | 0.045087 | 0.009804 | 0.007717 | 0.000349 | 0.005563 | 0.000718 |
| IITD | SwinV2-Tiny | E1-B2 | impostor | 0.728015 | 0.038429 | 0.326674 | 0.016212 | 0.217628 | 0.009146 |
| IITD | SwinV2-Tiny | E1-B2 | opposite_eye_diagnostic | 0.286915 | 0.026489 | 0.090904 | 0.025496 | 0.074823 | 0.02509 |

## Subject influence

| dataset | architecture | condition | full_mean_eer_effect_pp | loo_min_effect_pp | loo_max_effect_pp | sign_reversals | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-B1 | 4.67846 | 4.29938 | 4.92534 | 0 | 214 | 0.37908 |
| IITD | ResNet-18 | E1-B2 | 2.8098 | 2.502 | 3.11312 | 0 | 064 | 0.3078 |
| IITD | SwinV2-Tiny | E1-B1 | 26.77901 | 26.08611 | 27.19648 | 0 | 214 | 0.6929 |
| IITD | SwinV2-Tiny | E1-B2 | 10.67753 | 10.2147 | 11.04711 | 0 | 033 | 0.46284 |

Full per-image, subject-averaged and leave-one-subject-out values are in the corresponding CSV/Parquet tables. LOO removes all comparisons involving each omitted subject.

[IITD: previews, figures and independent report](Dataset%20Reports/IITD.md)

# AMF: E2-G

## Absolute metrics

EER/TAR are percent, AUC [0,1]; mean ± sample SD over the three seeds.

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-B1 | binary_geometry | 10.1434 ± 0.5737 | 0.9643 ± 0.0015 | 59.2447 ± 1.3304 | 30.4105 ± 1.5146 |
| AMF | ResNet-18 | E1-B1 | segmented_grayscale | 1.6420 ± 0.2844 | 0.9988 ± 0.0005 | 97.7340 ± 0.6897 | 91.3957 ± 2.9905 |
| AMF | ResNet-18 | E1-B2 | binary_geometry | 9.6085 ± 0.9056 | 0.9652 ± 0.0080 | 63.6782 ± 1.3120 | 36.0920 ± 2.1949 |
| AMF | ResNet-18 | E1-B2 | segmented_grayscale | 1.5258 ± 0.2902 | 0.9989 ± 0.0005 | 97.7997 ± 0.7127 | 91.0016 ± 3.8314 |
| AMF | SwinV2-Tiny | E1-B1 | binary_geometry | 25.7800 ± 4.3421 | 0.8233 ± 0.0504 | 25.2874 ± 8.9054 | 10.3847 ± 4.4209 |
| AMF | SwinV2-Tiny | E1-B1 | segmented_grayscale | 1.7932 ± 0.5804 | 0.9984 ± 0.0008 | 96.9458 ± 1.2883 | 90.2791 ± 2.1230 |
| AMF | SwinV2-Tiny | E1-B2 | binary_geometry | 16.1576 ± 0.7695 | 0.9175 ± 0.0055 | 37.7668 ± 3.6524 | 16.9458 ± 2.5898 |
| AMF | SwinV2-Tiny | E1-B2 | segmented_grayscale | 1.4651 ± 0.2180 | 0.9989 ± 0.0005 | 97.8325 ± 0.9398 | 89.6880 ± 5.7451 |

## Paired within-checkpoint differences

EER/TAR differences are percentage points; AUC differences are on [0,1].

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-B1 | binary-minus-grayscale | 8.5013 ± 0.5121 | -0.0345 ± 0.0016 | -38.4893 ± 1.3945 | -60.9852 ± 1.7761 |
| AMF | ResNet-18 | E1-B2 | binary-minus-grayscale | 8.0827 ± 0.6280 | -0.0337 ± 0.0076 | -34.1215 ± 1.2397 | -54.9097 ± 2.3652 |
| AMF | SwinV2-Tiny | E1-B1 | binary-minus-grayscale | 23.9868 ± 4.5695 | -0.1751 ± 0.0508 | -71.6585 ± 9.6130 | -79.8944 ± 4.5756 |
| AMF | SwinV2-Tiny | E1-B2 | binary-minus-grayscale | 14.6925 ± 0.7387 | -0.0814 ± 0.0053 | -60.0657 ± 3.2592 | -72.7422 ± 7.1061 |

## All individual seeds

| architecture | condition | seed | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | E1-B1 | 42 | segmented_grayscale | 1.97044 | 0.99814 | 96.94581 | 88.17734 |
| ResNet-18 | E1-B1 | 42 | binary_geometry | 10.44335 | 0.96383 | 59.21182 | 28.66995 |
| ResNet-18 | E1-B1 | 123 | segmented_grayscale | 1.47783 | 0.99916 | 98.02956 | 94.08867 |
| ResNet-18 | E1-B1 | 123 | binary_geometry | 10.50487 | 0.96307 | 57.93103 | 31.13300 |
| ResNet-18 | E1-B1 | 2025 | segmented_grayscale | 1.47783 | 0.99897 | 98.22660 | 91.92118 |
| ResNet-18 | E1-B1 | 2025 | binary_geometry | 9.48187 | 0.96600 | 60.59113 | 31.42857 |
| ResNet-18 | E1-B2 | 42 | segmented_grayscale | 1.57635 | 0.99893 | 97.33990 | 86.89655 |
| ResNet-18 | E1-B2 | 42 | binary_geometry | 10.01162 | 0.96247 | 64.53202 | 34.67980 |
| ResNet-18 | E1-B2 | 123 | segmented_grayscale | 1.21373 | 0.99934 | 98.62069 | 94.48276 |
| ResNet-18 | E1-B2 | 123 | binary_geometry | 8.57143 | 0.97422 | 64.33498 | 38.62069 |
| ResNet-18 | E1-B2 | 2025 | segmented_grayscale | 1.78744 | 0.99837 | 97.43842 | 91.62562 |
| ResNet-18 | E1-B2 | 2025 | binary_geometry | 10.24260 | 0.95883 | 62.16749 | 34.97537 |
| SwinV2-Tiny | E1-B1 | 42 | segmented_grayscale | 2.46305 | 0.99751 | 95.46798 | 88.07882 |
| SwinV2-Tiny | E1-B1 | 42 | binary_geometry | 23.94089 | 0.84036 | 29.35961 | 11.84374 |
| SwinV2-Tiny | E1-B1 | 123 | segmented_grayscale | 1.43875 | 0.99862 | 97.53695 | 92.31527 |
| SwinV2-Tiny | E1-B1 | 123 | binary_geometry | 22.66010 | 0.86291 | 31.42857 | 13.89163 |
| SwinV2-Tiny | E1-B1 | 2025 | segmented_grayscale | 1.47783 | 0.99900 | 97.83251 | 90.44335 |
| SwinV2-Tiny | E1-B1 | 2025 | binary_geometry | 30.73892 | 0.76649 | 15.07389 | 5.41872 |
| SwinV2-Tiny | E1-B2 | 42 | segmented_grayscale | 1.30314 | 0.99941 | 98.42365 | 93.00493 |
| SwinV2-Tiny | E1-B2 | 42 | binary_geometry | 16.65025 | 0.91753 | 35.96059 | 13.99015 |
| SwinV2-Tiny | E1-B2 | 123 | segmented_grayscale | 1.37931 | 0.99892 | 98.32512 | 93.00493 |
| SwinV2-Tiny | E1-B2 | 123 | binary_geometry | 15.27094 | 0.92306 | 41.97044 | 18.81773 |
| SwinV2-Tiny | E1-B2 | 2025 | segmented_grayscale | 1.71294 | 0.99843 | 96.74877 | 83.05419 |
| SwinV2-Tiny | E1-B2 | 2025 | binary_geometry | 16.55172 | 0.91204 | 35.36946 | 18.02956 |

## Similarity-distribution changes

Values are binary minus grayscale, averaged within numerical seed, then mean/sample SD across seeds. Genuine mean and impostor p99/p99.9 distinguish score shifts from verification changes. Opposite-eye scores remain diagnostic.

| dataset | architecture | condition | pair_kind | mean_mean | mean_sample_sd | p99_mean | p99_sample_sd | p999_mean | p999_sample_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-B1 | genuine | 0.017608 | 0.003401 | 0.001542 | 0.000917 | 0.001358 | 0.000139 |
| AMF | ResNet-18 | E1-B1 | impostor | 0.239688 | 0.056809 | 0.093488 | 0.021228 | 0.060539 | 0.013949 |
| AMF | ResNet-18 | E1-B1 | opposite_eye_diagnostic | 0.111272 | 0.029672 | 0.036925 | 0.010875 | 0.031069 | 0.009496 |
| AMF | ResNet-18 | E1-B2 | genuine | 0.020395 | 0.002974 | 0.002896 | 0.001009 | 0.001649 | 0.001762 |
| AMF | ResNet-18 | E1-B2 | impostor | 0.257676 | 0.013675 | 0.09367 | 0.008957 | 0.061734 | 0.003541 |
| AMF | ResNet-18 | E1-B2 | opposite_eye_diagnostic | 0.121832 | 0.016229 | 0.035378 | 0.004057 | 0.02653 | 0.001989 |
| AMF | SwinV2-Tiny | E1-B1 | genuine | 0.050319 | 0.006057 | 0.004212 | 0.001274 | 0.002512 | 0.000617 |
| AMF | SwinV2-Tiny | E1-B1 | impostor | 0.657702 | 0.050144 | 0.190598 | 0.039787 | 0.112575 | 0.02545 |
| AMF | SwinV2-Tiny | E1-B1 | opposite_eye_diagnostic | 0.265471 | 0.030212 | 0.056648 | 0.017752 | 0.036715 | 0.012304 |
| AMF | SwinV2-Tiny | E1-B2 | genuine | 0.026999 | 0.000646 | 0.003576 | 0.000744 | 0.002286 | 0.000429 |
| AMF | SwinV2-Tiny | E1-B2 | impostor | 0.554109 | 0.005715 | 0.174825 | 0.040855 | 0.100437 | 0.032461 |
| AMF | SwinV2-Tiny | E1-B2 | opposite_eye_diagnostic | 0.186334 | 0.037235 | 0.039698 | 0.003999 | 0.02508 | 0.000626 |

## Subject influence

| dataset | architecture | condition | full_mean_eer_effect_pp | loo_min_effect_pp | loo_max_effect_pp | sign_reversals | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-B1 | 8.50133 | 8.14981 | 8.69436 | 0 | zaid | 0.35152 |
| AMF | ResNet-18 | E1-B2 | 8.08271 | 7.78655 | 8.31236 | 0 | zaid | 0.29616 |
| AMF | SwinV2-Tiny | E1-B1 | 23.98676 | 23.60551 | 24.57499 | 0 | kareem | 0.58823 |
| AMF | SwinV2-Tiny | E1-B2 | 14.69251 | 14.14957 | 15.11133 | 0 | zaid | 0.54293 |

Full per-image, subject-averaged and leave-one-subject-out values are in the corresponding CSV/Parquet tables. LOO removes all comparisons involving each omitted subject.

[AMF: previews, figures and independent report](Dataset%20Reports/AMF.md)

# UTIRIS_NIR: E2-G

## Absolute metrics

EER/TAR are percent, AUC [0,1]; mean ± sample SD over the three seeds.

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-B1 | binary_geometry | 20.1425 ± 0.8469 | 0.8820 ± 0.0061 | 22.0855 ± 2.2668 | 5.9154 ± 0.8841 |
| UTIRIS_NIR | ResNet-18 | E1-B1 | segmented_grayscale | 6.6357 ± 0.3494 | 0.9836 ± 0.0036 | 80.0302 ± 2.4793 | 56.4983 ± 3.7966 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | binary_geometry | 19.2439 ± 0.6595 | 0.8875 ± 0.0065 | 24.9568 ± 0.7507 | 7.6857 ± 0.4312 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | segmented_grayscale | 7.3034 ± 0.4180 | 0.9791 ± 0.0039 | 75.3670 ± 3.3217 | 51.7487 ± 3.6159 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | binary_geometry | 40.4043 ± 1.9808 | 0.6335 ± 0.0257 | 5.0734 ± 1.0369 | 0.9067 ± 0.5301 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | segmented_grayscale | 6.7172 ± 1.2329 | 0.9815 ± 0.0069 | 74.6114 ± 4.7611 | 46.7185 ± 9.0535 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | binary_geometry | 28.0916 ± 0.9243 | 0.7949 ± 0.0126 | 12.1762 ± 2.1559 | 2.8929 ± 0.9075 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | segmented_grayscale | 6.2924 ± 0.5181 | 0.9848 ± 0.0016 | 76.2090 ± 1.7551 | 47.9706 ± 2.8887 |

## Paired within-checkpoint differences

EER/TAR differences are percentage points; AUC differences are on [0,1].

| dataset | architecture | condition | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-B1 | binary-minus-grayscale | 13.5068 ± 0.7501 | -0.1016 ± 0.0043 | -57.9447 ± 2.1288 | -50.5829 ± 3.4345 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | binary-minus-grayscale | 11.9405 ± 0.8688 | -0.0916 ± 0.0046 | -50.4102 ± 4.0449 | -44.0630 ± 4.0016 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | binary-minus-grayscale | 33.6871 ± 0.8217 | -0.3480 ± 0.0188 | -69.5380 ± 4.4920 | -45.8117 ± 8.7270 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | binary-minus-grayscale | 21.7992 ± 1.3362 | -0.1899 ± 0.0140 | -64.0328 ± 3.7444 | -45.0777 ± 3.7648 |

## All individual seeds

| architecture | condition | seed | variant | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-18 | E1-B1 | 42 | segmented_grayscale | 6.46178 | 0.98572 | 82.31865 | 59.06736 |
| ResNet-18 | E1-B1 | 42 | binary_geometry | 20.72539 | 0.88051 | 22.08549 | 5.50518 |
| ResNet-18 | E1-B1 | 123 | segmented_grayscale | 6.40744 | 0.98568 | 80.37565 | 58.29016 |
| ResNet-18 | E1-B1 | 123 | binary_geometry | 19.17098 | 0.88882 | 24.35233 | 6.93005 |
| ResNet-18 | E1-B1 | 2025 | segmented_grayscale | 7.03796 | 0.97954 | 77.39637 | 52.13731 |
| ResNet-18 | E1-B1 | 2025 | binary_geometry | 20.53109 | 0.87682 | 19.81865 | 5.31088 |
| ResNet-18 | E1-B2 | 42 | segmented_grayscale | 6.87256 | 0.98105 | 78.30311 | 55.56995 |
| ResNet-18 | E1-B2 | 42 | binary_geometry | 19.75389 | 0.88505 | 24.15803 | 7.18912 |
| ResNet-18 | E1-B2 | 123 | segmented_grayscale | 7.33050 | 0.98164 | 76.03627 | 51.29534 |
| ResNet-18 | E1-B2 | 123 | binary_geometry | 18.49918 | 0.89479 | 25.06477 | 7.96632 |
| ResNet-18 | E1-B2 | 2025 | segmented_grayscale | 7.70725 | 0.97457 | 71.76166 | 48.38083 |
| ResNet-18 | E1-B2 | 2025 | binary_geometry | 19.47863 | 0.88251 | 25.64767 | 7.90155 |
| SwinV2-Tiny | E1-B1 | 42 | segmented_grayscale | 8.13976 | 0.97356 | 69.55959 | 40.22021 |
| SwinV2-Tiny | E1-B1 | 42 | binary_geometry | 42.61658 | 0.60450 | 5.11658 | 1.03627 |
| SwinV2-Tiny | E1-B1 | 123 | segmented_grayscale | 6.05339 | 0.98466 | 79.01554 | 57.05959 |
| SwinV2-Tiny | E1-B1 | 123 | binary_geometry | 39.80102 | 0.64232 | 6.08808 | 1.36010 |
| SwinV2-Tiny | E1-B1 | 2025 | segmented_grayscale | 5.95855 | 0.98635 | 75.25907 | 42.87565 |
| SwinV2-Tiny | E1-B1 | 2025 | binary_geometry | 38.79534 | 0.65367 | 4.01554 | 0.32383 |
| SwinV2-Tiny | E1-B2 | 42 | segmented_grayscale | 5.89379 | 0.98622 | 78.04404 | 50.12953 |
| SwinV2-Tiny | E1-B2 | 42 | binary_geometry | 29.15824 | 0.78039 | 9.71503 | 2.00777 |
| SwinV2-Tiny | E1-B2 | 123 | segmented_grayscale | 6.10533 | 0.98503 | 76.03627 | 44.68912 |
| SwinV2-Tiny | E1-B2 | 123 | binary_geometry | 27.59067 | 0.80109 | 13.73057 | 3.82124 |
| SwinV2-Tiny | E1-B2 | 2025 | segmented_grayscale | 6.87803 | 0.98303 | 74.54663 | 49.09326 |
| SwinV2-Tiny | E1-B2 | 2025 | binary_geometry | 27.52591 | 0.80313 | 13.08290 | 2.84974 |

## Similarity-distribution changes

Values are binary minus grayscale, averaged within numerical seed, then mean/sample SD across seeds. Genuine mean and impostor p99/p99.9 distinguish score shifts from verification changes. Opposite-eye scores remain diagnostic.

| dataset | architecture | condition | pair_kind | mean_mean | mean_sample_sd | p99_mean | p99_sample_sd | p999_mean | p999_sample_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-B1 | genuine | 0.097068 | 0.008765 | 0.015932 | 0.002195 | 0.008433 | 0.003117 |
| UTIRIS_NIR | ResNet-18 | E1-B1 | impostor | 0.493473 | 0.063198 | 0.179006 | 0.024441 | 0.121435 | 0.016536 |
| UTIRIS_NIR | ResNet-18 | E1-B1 | opposite_eye_diagnostic | 0.234457 | 0.023772 | 0.06591 | 0.004296 | 0.037214 | 0.006763 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | genuine | 0.099801 | 0.004666 | 0.020072 | 0.004241 | 0.012542 | 0.002361 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | impostor | 0.455321 | 0.034468 | 0.165442 | 0.019999 | 0.113181 | 0.01823 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | opposite_eye_diagnostic | 0.213735 | 0.010922 | 0.072003 | 0.009882 | 0.050903 | 0.013059 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | genuine | 0.128584 | 0.025322 | 0.01829 | 0.001586 | 0.010289 | 0.001784 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | impostor | 0.617776 | 0.099642 | 0.169745 | 0.029093 | 0.097098 | 0.011615 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | opposite_eye_diagnostic | 0.249612 | 0.044016 | 0.051542 | 0.00528 | 0.033198 | 0.004023 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | genuine | 0.069229 | 0.016547 | 0.011421 | 0.00265 | 0.007898 | 0.002684 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | impostor | 0.501323 | 0.048578 | 0.156096 | 0.022748 | 0.092134 | 0.012987 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | opposite_eye_diagnostic | 0.151117 | 0.031427 | 0.036805 | 0.005866 | 0.025701 | 0.007527 |

## Subject influence

| dataset | architecture | condition | full_mean_eer_effect_pp | loo_min_effect_pp | loo_max_effect_pp | sign_reversals | most_influential_subject | largest_absolute_shift_pp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-B1 | 13.50676 | 13.20059 | 13.77681 | 0 | 061 | 0.30617 |
| UTIRIS_NIR | ResNet-18 | E1-B2 | 11.94046 | 11.69993 | 12.22912 | 0 | 077 | 0.28866 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B1 | 33.68708 | 33.48199 | 33.96803 | 0 | 061 | 0.28095 |
| UTIRIS_NIR | SwinV2-Tiny | E1-B2 | 21.79922 | 21.58424 | 22.07107 | 0 | 068 | 0.27184 |

Full per-image, subject-averaged and leave-one-subject-out values are in the corresponding CSV/Parquet tables. LOO removes all comparisons involving each omitted subject.

[UTIRIS_NIR: previews, figures and independent report](Dataset%20Reports/UTIRIS_NIR.md)


## Reproduction and validation

The [standalone notebook](../E2-G.ipynb) contains all models, binary inputs, audits, metrics, sensitivity analyses, figures and report generation. All imports are at the top; no preceding notebook or original machine directory is required. Large per-image/subject tables are published as Parquet, summaries as CSV. Biometric previews, weights, raw embeddings and pair-score arrays remain external. The completed source experiment passed all six unit tests, reconstructed every new score set from embeddings exactly, and preserved all 32,477 protected earlier files, including 60 checkpoints. The initial diagnostic adapter assumed earlier E2-A LOO tables included B1/B2; those missing diagnostics were instead derived from unchanged saved baseline scores. The first binary result was reused unchanged. Inputs, pairs, checkpoints, normalization and metric definitions were not changed.
