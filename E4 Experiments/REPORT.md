# Independent complement-only training: matched evaluation

All six validation-selected best checkpoints are evaluated independently on the original five E2-A matched populations and exhaustive genuine/different-subject impostor pairs. Seeds 42, 123 and 2025 are retained. No scores are pooled between datasets, no best seed is selected, and no training or checkpoint selection uses these results.

The input uses the frozen, researcher-approved strict native-annulus sampling footprint, mean fill, original 320×320 geometry and E1-A normalization. It differs from the older E2 complement at interpolation-mixed boundary pixels. Pure predicted-pupil samples and other retained ocular samples remain. Original segmentation errors are not repaired; this is not a pure periocular-only or anatomical-ground-truth claim.

Absolute EER/TAR values below are percentages; ROC-AUC is on [0,1]. Mean ± sample SD uses all three seeds. Paired changes are complement-trained/complement-tested minus raw-A-trained/raw-A-tested, matched by numerical seed. These compare independent checkpoints; SD over three seeds is not a participant confidence interval.

## Matched populations

| dataset | images | subjects | iris_ids | genuine | impostor | opposite_eye_diagnostic | extra_removal_images | added_pixels_median | remaining_native_annulus_contributions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 427 | 54 | 108 | 634 | 89473 | 844 | 427 | 332.0 | 0 |
| CASIA-Interval | 395 | 37 | 59 | 1353 | 75272 | 1190 | 0 | 0.0 | 0 |
| IITD | 308 | 32 | 63 | 628 | 45936 | 714 | 0 | 0.0 | 0 |
| AMF | 523 | 54 | 108 | 1015 | 134214 | 1274 | 523 | 194.0 | 0 |
| UTIRIS_NIR | 770 | 79 | 158 | 1544 | 292613 | 1908 | 770 | 451.0 | 0 |

## Validation-selected checkpoints

| name | architecture | seed | selected_epoch | completed_epoch | best_macro_validation_eer |
| --- | --- | --- | --- | --- | --- |
| complement_mean_resnet18_seed42 | ResNet-18 | 42 | 66 | 91 | 0.019984628504472735 |
| complement_mean_resnet18_seed123 | ResNet-18 | 123 | 72 | 97 | 0.018971168587043043 |
| complement_mean_resnet18_seed2025 | ResNet-18 | 2025 | 12 | 37 | 0.026874405454538546 |
| complement_mean_swinv2_tiny_seed42 | SwinV2-Tiny | 42 | 27 | 52 | 0.020359835805083232 |
| complement_mean_swinv2_tiny_seed123 | SwinV2-Tiny | 123 | 61 | 86 | 0.015962483029040065 |
| complement_mean_swinv2_tiny_seed2025 | SwinV2-Tiny | 2025 | 21 | 46 | 0.024551250873953667 |

## CUST-Iris

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | A-complement-mean-strict | 3.0053 ± 0.5654 | 0.9946 ± 0.0028 | 95.0053 ± 1.2047 | 87.5394 ± 2.6346 |
| CUST-Iris | SwinV2-Tiny | A-complement-mean-strict | 2.5840 ± 0.3323 | 0.9960 ± 0.0007 | 95.4784 ± 0.7454 | 87.0662 ± 1.1908 |

## CASIA-Interval

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | A-complement-mean-strict | 4.0427 ± 0.7442 | 0.9939 ± 0.0023 | 89.8990 ± 3.1569 | 74.5750 ± 9.0801 |
| CASIA-Interval | SwinV2-Tiny | A-complement-mean-strict | 4.0407 ± 1.1596 | 0.9920 ± 0.0039 | 87.4107 ± 6.0196 | 69.7955 ± 11.1244 |

## IITD

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | A-complement-mean-strict | 1.6266 ± 0.3352 | 0.9991 ± 0.0004 | 97.8238 ± 0.6029 | 95.0637 ± 2.9188 |
| IITD | SwinV2-Tiny | A-complement-mean-strict | 0.7804 ± 0.1616 | 0.9997 ± 0.0002 | 99.3631 ± 0.3185 | 94.0021 ± 4.0732 |

## AMF

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | A-complement-mean-strict | 1.7734 ± 0.4294 | 0.9978 ± 0.0004 | 97.4384 ± 0.9703 | 93.2348 ± 2.6240 |
| AMF | SwinV2-Tiny | A-complement-mean-strict | 1.8068 ± 0.1498 | 0.9979 ± 0.0007 | 97.3727 ± 0.6990 | 94.2200 ± 2.4220 |

## UTIRIS_NIR

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | A-complement-mean-strict | 9.2149 ± 0.4806 | 0.9676 ± 0.0016 | 69.3869 ± 2.6871 | 45.9197 ± 0.9408 |
| UTIRIS_NIR | SwinV2-Tiny | A-complement-mean-strict | 9.0458 ± 0.9722 | 0.9702 ± 0.0053 | 68.9551 ± 5.6856 | 46.3299 ± 7.5119 |

## Changes relative to the original raw A baseline

EER/TAR deltas are percentage points; ROC-AUC differences are unitless. Negative EER or positive TAR differences favor complement training. The same fixed matched population and pair policy is used on both sides.

| dataset | architecture | condition | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | A-complement-mean-strict | 0.7490 ± 0.6813 | -0.0013 ± 0.0004 | -1.4778 ± 1.4909 | -2.7915 ± 2.8713 |
| AMF | SwinV2-Tiny | A-complement-mean-strict | 0.4712 ± 0.4226 | -0.0009 ± 0.0004 | -1.2151 ± 0.9869 | -1.3136 ± 2.8713 |
| CASIA-Interval | ResNet-18 | A-complement-mean-strict | 1.9412 ± 0.8497 | -0.0030 ± 0.0018 | -5.9374 ± 3.9776 | -10.3720 ± 13.8277 |
| CASIA-Interval | SwinV2-Tiny | A-complement-mean-strict | 0.7348 ± 1.4033 | -0.0033 ± 0.0040 | -5.6911 ± 6.2941 | -11.3575 ± 10.5234 |
| CUST-Iris | ResNet-18 | A-complement-mean-strict | 1.6049 ± 0.5353 | -0.0039 ± 0.0021 | -3.2072 ± 1.0502 | -8.1493 ± 2.7561 |
| CUST-Iris | SwinV2-Tiny | A-complement-mean-strict | 0.7123 ± 0.3810 | -0.0026 ± 0.0006 | -1.4721 ± 2.2984 | -4.2587 ± 1.9124 |
| IITD | ResNet-18 | A-complement-mean-strict | 0.8669 ± 0.6367 | -0.0005 ± 0.0006 | -1.5393 ± 1.0361 | -1.8047 ± 2.8677 |
| IITD | SwinV2-Tiny | A-complement-mean-strict | -0.8316 ± 0.6665 | 0.0010 ± 0.0009 | 1.2739 ± 0.9944 | -1.1146 ± 6.1321 |
| UTIRIS_NIR | ResNet-18 | A-complement-mean-strict | 2.2417 ± 0.7099 | -0.0128 ± 0.0007 | -10.8808 ± 2.1324 | -13.7090 ± 0.0989 |
| UTIRIS_NIR | SwinV2-Tiny | A-complement-mean-strict | -0.9104 ± 2.8946 | 0.0059 ± 0.0187 | 1.7703 ± 9.4578 | 1.3601 ± 8.6584 |

## Reproducibility and preservation

EVALUATION_PLAN.json pins checkpoints, source hashes and existing population/pair artifacts before inference. evaluation/inputs records every strict support and pixel/geometry check. All embeddings, scores, ROC curves, four metrics and full-precision seed changes are saved separately. No completed E1/E2/E3/E4 training artifact or frozen assignment was modified.
