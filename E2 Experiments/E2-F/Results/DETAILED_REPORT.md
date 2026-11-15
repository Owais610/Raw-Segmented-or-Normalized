> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-F: explanatory pair-conditioned Grad-CAM for raw-ocular verification

Only the six original validation-selected E1-A raw checkpoints were used, all3 training seeds. Same encoder processes both images; target is positive cosine of complete normalized embeddings, including projection head. No classification logit, arbitrary embedding coordinate, B/C model input, training, fine-tuning or new recognition checkpoint. Domains and sampling categories remain separate. This diagnostic complements E2-D/E2-E interventions; it cannot establish causal reliance or identity shortcuts.

## Frozen layers and actual layouts

| architecture | layer | layout | activation_shape | spatial_grid |
| --- | --- | --- | --- | --- |
| ResNet-18 | backbone.layer4 | NCHW | [2, 512, 10, 10] | [10, 10] |
| SwinV2-Tiny | backbone.model.norm | NHWC | [2, 10, 10, 768] | [10, 10] |

Both selected grids are actually10x10 at320x320: ResNet channels512, Swin channels768 with verified NHWC->NCHW permutation. They differ in feature semantics/Grad-CAM behavior even though grid sizes match. Installed timm forward_features/head source and SHA256 are recorded in STRUCTURAL_PREFLIGHT.json. The chosen layers precede final pooling and were frozen before real-image maps, without selection by appearance.

## Target, precision, normalization and regions

Float32 forward/VJP prevents unequal half-precision gradient underflow; weights/input/network remain unchanged. Every original-model comparison is checked against saved AMP scores, a fresh original-AMP batch2 score and a no-grad FP32 score. Fixed saved-score tolerance0.001 and grad/no-grad tolerance1e-6 are numerical checks, not recognition thresholds. Exact errors are saved. Inputs require gradients, frozen parameters do not; inference_mode is explicitly prohibited for attribution.

Grad-CAM uses channel-average ds/dA weights and ReLU of their weighted spatial activations. Signed/native positive grids and channel weights are preserved. Positive maps are bilinearly upsampled with align_cornersFalse, padding removed from anatomical statistics, and L1 normalized over valid content. Zero maps have undefined fractions and remain in coverage/galleries. Raw intensity is not compared across architectures. Display uses a fixed0..4 positive-density scale relative to uniform valid-image attribution, not per-map stretching; display clipping does not modify saved quantitative maps.

A=existing annulus, P=original pupil, D=iris union pupil, O=valid content outside D, N=P union O. All three A/P/O regions are a checked disjoint partition. Nonannulus attribution includes pupil; outside-disc pixels are not automatically eyelashes/skin/periocular identity cues. Masks/contours are frozen predictions, not anatomical ground truth. Area fractions, normalized mean attribution per pixel, area enrichment and density ratios are recorded; zero-denominator ratios remain undefined with explicit counts/status.

## Selected pairs and scope

| dataset | common_images | genuine | high_similarity_impostor | ordinary_impostor | partner_anchors |
| --- | --- | --- | --- | --- | --- |
| AMF | 523 | 12 | 6 | 12 | 3 |
| CASIA-Interval | 395 | 12 | 6 | 12 | 3 |
| CUST-Iris | 427 | 12 | 6 | 12 | 3 |
| IITD | 308 | 12 | 6 | 12 | 3 |
| UTIRIS_NIR | 770 | 12 | 6 | 12 | 3 |

Selection seed42: genuine sampling balances subjects; ordinary impostors are random valid different-subject pairs without subject reuse within category. High-similarity impostors use one equal-six-model mean percentile ranking with average-rank ties and subject-aware selection. High-similarity sampling is outcome-conditioned exploratory; these selected pairs are not an EER benchmark. No selection uses heatmaps. Same pairs/images/partners are used across architectures and all seeds. Full IDs, hashes, raw scores/ranks, source paths and region masks are retained. No training/validation subjects are evaluated.

## Paired architecture result

Positive differences mean greater ResNet normalized nonannulus positive-mass fraction; negative means greater Swin. Values are percentage points, averaged within numerical seed on exact matched pair/branch images, then mean/sampleSD across3 seeds. Only mutually nonzero, finite, score-consistent maps contribute to numerical differences; every unsupported/zero map remains recorded and visualized. Valid counts are reported, with undefined results preserved. This is descriptive spatial mass, not stronger causal reliance.

| dataset | category | valid_seeds | mean_resnet_minus_swin_nonannulus_pp | sample_sd_pp | seed42_pp | seed123_pp | seed2025_pp | resnet_greater_seeds | swin_greater_seeds | equal_seeds | exploratory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | genuine | 3 | -2.91623 | 2.01669 | -5.03084 | -2.70353 | -1.01433 | 0 | 3 | 0 | False |
| AMF | high_similarity_impostor | 3 | -2.81879 | 0.51602 | -3.41396 | -2.49636 | -2.54606 | 0 | 3 | 0 | True |
| AMF | ordinary_impostor | 3 | -7.86116 | 3.45947 | -10.09494 | -9.6123 | -3.87625 | 0 | 3 | 0 | False |
| CASIA-Interval | genuine | 3 | -1.372 | 2.25591 | -2.93842 | -2.39126 | 1.21367 | 1 | 2 | 0 | False |
| CASIA-Interval | high_similarity_impostor | 3 | -7.70346 | 3.21543 | -9.0372 | -4.03578 | -10.03739 | 0 | 3 | 0 | True |
| CASIA-Interval | ordinary_impostor | 3 | -5.08328 | 2.07888 | -2.74507 | -6.72281 | -5.78196 | 0 | 3 | 0 | False |
| CUST-Iris | genuine | 3 | -4.34214 | 1.17088 | -4.14325 | -5.59973 | -3.28346 | 0 | 3 | 0 | False |
| CUST-Iris | high_similarity_impostor | 3 | -4.113 | 5.57006 | 1.54209 | -9.59395 | -4.28715 | 1 | 2 | 0 | True |
| CUST-Iris | ordinary_impostor | 3 | -4.84082 | 7.0984 | 2.62519 | -5.64445 | -11.50321 | 1 | 2 | 0 | False |
| IITD | genuine | 3 | -1.85077 | 3.33206 | 1.96383 | -4.19308 | -3.32306 | 1 | 2 | 0 | False |
| IITD | high_similarity_impostor | 3 | -6.15607 | 9.68384 | -10.56191 | -12.85361 | 4.94731 | 1 | 2 | 0 | True |
| IITD | ordinary_impostor | 3 | -4.16344 | 2.58629 | -2.22785 | -3.1617 | -7.10076 | 0 | 3 | 0 | False |
| UTIRIS_NIR | genuine | 3 | -3.36128 | 4.59921 | -3.11743 | -8.07756 | 1.11115 | 1 | 2 | 0 | False |
| UTIRIS_NIR | high_similarity_impostor | 3 | -0.60188 | 6.38376 | 4.92907 | -7.58741 | 0.85269 | 2 | 1 | 0 | True |
| UTIRIS_NIR | ordinary_impostor | 3 | -2.93009 | 6.07368 | -7.87281 | -4.76764 | 3.85019 | 1 | 2 | 0 | False |

## Numerical consistency

| dataset | architecture | seed | branches | score_consistent_branches | finite_activation_branches | finite_gradient_branches | zero_gradients | max_saved_fp32_error | max_saved_amp_batch2_error | max_grad_nograd_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 42 | 60 | 58 | 60 | 60 | 0 | 0.00101458 | 0.00023646 | 0.0 |
| AMF | ResNet-18 | 123 | 60 | 58 | 60 | 60 | 0 | 0.00119741 | 0.00031306 | 0.0 |
| AMF | ResNet-18 | 2025 | 60 | 60 | 60 | 60 | 0 | 0.00084613 | 0.00023845 | 0.0 |
| AMF | SwinV2-Tiny | 42 | 60 | 60 | 60 | 60 | 0 | 0.00026047 | 0.00022672 | 0.0 |
| AMF | SwinV2-Tiny | 123 | 60 | 60 | 60 | 60 | 0 | 0.00027086 | 0.00010759 | 0.0 |
| AMF | SwinV2-Tiny | 2025 | 60 | 60 | 60 | 60 | 0 | 0.00031393 | 0.0001024 | 0.0 |
| CASIA-Interval | ResNet-18 | 42 | 60 | 58 | 60 | 60 | 0 | 0.00148129 | 0.00033706 | 0.0 |
| CASIA-Interval | ResNet-18 | 123 | 60 | 60 | 60 | 60 | 0 | 0.00088365 | 0.00021076 | 0.0 |
| CASIA-Interval | ResNet-18 | 2025 | 60 | 58 | 60 | 60 | 0 | 0.00116521 | 0.00035888 | 0.0 |
| CASIA-Interval | SwinV2-Tiny | 42 | 60 | 60 | 60 | 60 | 0 | 0.00040233 | 0.00013474 | 0.0 |
| CASIA-Interval | SwinV2-Tiny | 123 | 60 | 60 | 60 | 60 | 0 | 0.00043766 | 0.00015524 | 0.0 |
| CASIA-Interval | SwinV2-Tiny | 2025 | 60 | 60 | 60 | 60 | 0 | 0.00053129 | 0.00014848 | 0.0 |
| CUST-Iris | ResNet-18 | 42 | 60 | 52 | 60 | 60 | 0 | 0.00141951 | 0.00023735 | 0.0 |
| CUST-Iris | ResNet-18 | 123 | 60 | 58 | 60 | 60 | 0 | 0.00100772 | 0.00033545 | 0.0 |
| CUST-Iris | ResNet-18 | 2025 | 60 | 58 | 60 | 60 | 0 | 0.00122398 | 0.00039407 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 42 | 60 | 60 | 60 | 60 | 0 | 0.00048485 | 0.00018115 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 123 | 60 | 60 | 60 | 60 | 0 | 0.00080535 | 0.0001387 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 2025 | 60 | 60 | 60 | 60 | 0 | 0.0005812 | 0.00010493 | 0.0 |
| IITD | ResNet-18 | 42 | 60 | 58 | 60 | 60 | 0 | 0.00138092 | 0.00070497 | 0.0 |
| IITD | ResNet-18 | 123 | 60 | 58 | 60 | 60 | 0 | 0.00105512 | 0.00062677 | 0.0 |
| IITD | ResNet-18 | 2025 | 60 | 58 | 60 | 60 | 0 | 0.00107393 | 0.00028539 | 0.0 |
| IITD | SwinV2-Tiny | 42 | 60 | 60 | 60 | 60 | 0 | 0.00045413 | 0.00017166 | 0.0 |
| IITD | SwinV2-Tiny | 123 | 60 | 60 | 60 | 60 | 0 | 0.00031912 | 0.00024128 | 0.0 |
| IITD | SwinV2-Tiny | 2025 | 60 | 60 | 60 | 60 | 0 | 0.00026169 | 0.00014468 | 0.0 |
| UTIRIS_NIR | ResNet-18 | 42 | 60 | 60 | 60 | 60 | 0 | 0.00086588 | 0.00049654 | 0.0 |
| UTIRIS_NIR | ResNet-18 | 123 | 60 | 58 | 60 | 60 | 0 | 0.00103909 | 0.00027779 | 0.0 |
| UTIRIS_NIR | ResNet-18 | 2025 | 60 | 58 | 60 | 60 | 0 | 0.00102079 | 0.00033435 | 0.0 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | 60 | 60 | 60 | 60 | 0 | 0.00050096 | 0.00013393 | 0.0 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | 60 | 60 | 60 | 60 | 0 | 0.00028449 | 0.0001695 | 0.0 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | 60 | 60 | 60 | 60 | 0 | 0.0003795 | 0.00015104 | 0.0 |

## Complete valid/zero/failure coverage

| dataset | architecture | seed | category | all_maps | supported_maps | zero_maps | computation_failures | nonfinite_maps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | ResNet-18 | 42 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| AMF | ResNet-18 | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | ResNet-18 | 123 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| AMF | ResNet-18 | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | ResNet-18 | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| AMF | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 42 | genuine | 24 | 22 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 2025 | genuine | 24 | 22 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | ResNet-18 | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CASIA-Interval | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 42 | genuine | 24 | 22 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 42 | high_similarity_impostor | 12 | 10 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 42 | ordinary_impostor | 24 | 20 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 123 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CUST-Iris | ResNet-18 | 2025 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| CUST-Iris | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| IITD | ResNet-18 | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | ResNet-18 | 42 | high_similarity_impostor | 12 | 10 | 0 | 0 | 0 |
| IITD | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| IITD | ResNet-18 | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| IITD | ResNet-18 | 123 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| IITD | ResNet-18 | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| IITD | ResNet-18 | 2025 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| IITD | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 123 | genuine | 24 | 22 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | ResNet-18 | 2025 | ordinary_impostor | 24 | 22 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | genuine | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | genuine | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | genuine | 24 | 24 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0 | 0 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0 | 0 | 0 |

## Per-dataset supplementary galleries and manuscript pages

# CUST-Iris: separate E2-F spatial analysis

| dataset | seed | category | all_branch_comparisons | supported_branch_comparisons | supported_images | nonannulus_effect | annulus_effect | pupil_effect | outside_disc_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 42 | genuine | 24 | 22 | 22 | -0.041432 | 0.041432 | 0.009473 | -0.050905 |
| CUST-Iris | 42 | high_similarity_impostor | 12 | 10 | 10 | 0.015421 | -0.015421 | -0.009843 | 0.025264 |
| CUST-Iris | 42 | ordinary_impostor | 24 | 20 | 20 | 0.026252 | -0.026252 | 0.034732 | -0.00848 |
| CUST-Iris | 123 | genuine | 24 | 24 | 24 | -0.055997 | 0.055997 | 0.020812 | -0.076809 |
| CUST-Iris | 123 | high_similarity_impostor | 12 | 12 | 12 | -0.095939 | 0.095939 | 0.013676 | -0.109616 |
| CUST-Iris | 123 | ordinary_impostor | 24 | 22 | 22 | -0.056445 | 0.056445 | 0.029856 | -0.0863 |
| CUST-Iris | 2025 | genuine | 24 | 24 | 24 | -0.032835 | 0.032835 | 0.010237 | -0.043072 |
| CUST-Iris | 2025 | high_similarity_impostor | 12 | 12 | 12 | -0.042872 | 0.042872 | 0.002849 | -0.04572 |
| CUST-Iris | 2025 | ordinary_impostor | 24 | 22 | 22 | -0.115032 | 0.115032 | 0.035842 | -0.150874 |

Per-architecture/seed/category normalized mass and concentration. Fractions are0..1; undefined density ratios are retained as missing with finite counts in the data.

| dataset | architecture | seed | category | images | subjects | annulus_mass_fraction_mean | pupil_mass_fraction_mean | outside_disc_mass_fraction_mean | nonannulus_mass_fraction_mean | annulus_area_fraction_mean | iris_vs_outside_density_ratio_p50 | nonannulus_vs_iris_density_ratio_p50 | padding_positive_mass_fraction_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | 42 | genuine | 22 | 11 | 0.25536 | 0.043639 | 0.701001 | 0.74464 | 0.199062 | 1.067783 | 0.918977 | 0.0 |
| CUST-Iris | ResNet-18 | 42 | high_similarity_impostor | 10 | 10 | 0.231136 | 0.031052 | 0.737811 | 0.768864 | 0.19179 | 1.186594 | 0.966178 | 0.0 |
| CUST-Iris | ResNet-18 | 42 | ordinary_impostor | 20 | 20 | 0.195045 | 0.070576 | 0.734379 | 0.804955 | 0.187199 | 0.675052 | 1.494862 | 0.0 |
| CUST-Iris | ResNet-18 | 123 | genuine | 24 | 12 | 0.276108 | 0.03993 | 0.683962 | 0.723892 | 0.202311 | 1.637601 | 0.604607 | 0.0 |
| CUST-Iris | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0.297018 | 0.028611 | 0.67437 | 0.702982 | 0.189324 | 1.779179 | 0.583014 | 0.0 |
| CUST-Iris | ResNet-18 | 123 | ordinary_impostor | 22 | 22 | 0.269325 | 0.04627 | 0.684405 | 0.730675 | 0.188605 | 1.81143 | 0.575011 | 0.0 |
| CUST-Iris | ResNet-18 | 2025 | genuine | 24 | 12 | 0.221442 | 0.032806 | 0.745752 | 0.778558 | 0.202311 | 0.904539 | 1.081366 | 0.0 |
| CUST-Iris | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0.23835 | 0.026633 | 0.735017 | 0.76165 | 0.189324 | 0.989783 | 1.006964 | 0.0 |
| CUST-Iris | ResNet-18 | 2025 | ordinary_impostor | 22 | 22 | 0.231202 | 0.054597 | 0.714201 | 0.768798 | 0.188605 | 1.23167 | 0.850181 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 42 | genuine | 24 | 12 | 0.228695 | 0.034432 | 0.736873 | 0.771305 | 0.202311 | 0.986905 | 1.024162 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0.252511 | 0.039164 | 0.708324 | 0.747489 | 0.189324 | 0.889596 | 1.115605 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0.203194 | 0.03017 | 0.766636 | 0.796806 | 0.187825 | 0.75873 | 1.290672 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 123 | genuine | 24 | 12 | 0.220111 | 0.019118 | 0.760771 | 0.779889 | 0.202311 | 0.873274 | 1.138295 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0.201079 | 0.014935 | 0.783986 | 0.798921 | 0.189324 | 0.702428 | 1.41562 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0.225885 | 0.016557 | 0.757557 | 0.774115 | 0.187825 | 0.80002 | 1.228739 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 2025 | genuine | 24 | 12 | 0.188607 | 0.022569 | 0.788824 | 0.811393 | 0.202311 | 0.882826 | 1.109387 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0.195478 | 0.023784 | 0.780737 | 0.804522 | 0.189324 | 0.58777 | 2.368079 | 0.0 |
| CUST-Iris | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0.133066 | 0.021223 | 0.845711 | 0.866934 | 0.187825 | 0.474991 | 2.056575 | 0.0 |

Complete gallery, every pair and seed (external recorded asset).



# CASIA-Interval: separate E2-F spatial analysis

| dataset | seed | category | all_branch_comparisons | supported_branch_comparisons | supported_images | nonannulus_effect | annulus_effect | pupil_effect | outside_disc_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | 42 | genuine | 24 | 22 | 22 | -0.029384 | 0.029384 | 0.007336 | -0.03672 |
| CASIA-Interval | 42 | high_similarity_impostor | 12 | 12 | 12 | -0.090372 | 0.090372 | -0.046233 | -0.044139 |
| CASIA-Interval | 42 | ordinary_impostor | 24 | 24 | 24 | -0.027451 | 0.027451 | 0.011922 | -0.039372 |
| CASIA-Interval | 123 | genuine | 24 | 24 | 24 | -0.023913 | 0.023913 | 0.05013 | -0.074042 |
| CASIA-Interval | 123 | high_similarity_impostor | 12 | 12 | 12 | -0.040358 | 0.040358 | -0.015688 | -0.02467 |
| CASIA-Interval | 123 | ordinary_impostor | 24 | 24 | 24 | -0.067228 | 0.067228 | 0.06162 | -0.128848 |
| CASIA-Interval | 2025 | genuine | 24 | 22 | 22 | 0.012137 | -0.012137 | 0.035415 | -0.023278 |
| CASIA-Interval | 2025 | high_similarity_impostor | 12 | 12 | 12 | -0.100374 | 0.100374 | 0.036136 | -0.13651 |
| CASIA-Interval | 2025 | ordinary_impostor | 24 | 24 | 24 | -0.05782 | 0.05782 | 0.005189 | -0.063008 |

Per-architecture/seed/category normalized mass and concentration. Fractions are0..1; undefined density ratios are retained as missing with finite counts in the data.

| dataset | architecture | seed | category | images | subjects | annulus_mass_fraction_mean | pupil_mass_fraction_mean | outside_disc_mass_fraction_mean | nonannulus_mass_fraction_mean | annulus_area_fraction_mean | iris_vs_outside_density_ratio_p50 | nonannulus_vs_iris_density_ratio_p50 | padding_positive_mass_fraction_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | 42 | genuine | 22 | 11 | 0.403458 | 0.117842 | 0.4787 | 0.596542 | 0.268235 | 2.30008 | 0.468199 | 0.032069 |
| CASIA-Interval | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0.485286 | 0.075705 | 0.439009 | 0.514714 | 0.30003 | 2.520667 | 0.446701 | 0.027129 |
| CASIA-Interval | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0.350085 | 0.104379 | 0.545536 | 0.649915 | 0.282468 | 1.355191 | 0.73643 | 0.033797 |
| CASIA-Interval | ResNet-18 | 123 | genuine | 24 | 12 | 0.433763 | 0.131759 | 0.434478 | 0.566237 | 0.264772 | 2.300856 | 0.461395 | 0.022674 |
| CASIA-Interval | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0.467133 | 0.090803 | 0.442064 | 0.532867 | 0.30003 | 2.303355 | 0.561544 | 0.021734 |
| CASIA-Interval | ResNet-18 | 123 | ordinary_impostor | 24 | 24 | 0.422749 | 0.137853 | 0.439397 | 0.577251 | 0.282468 | 2.359202 | 0.578417 | 0.026661 |
| CASIA-Interval | ResNet-18 | 2025 | genuine | 22 | 11 | 0.379263 | 0.119695 | 0.501042 | 0.620737 | 0.262079 | 1.757 | 0.594923 | 0.027043 |
| CASIA-Interval | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0.456305 | 0.123516 | 0.420179 | 0.543695 | 0.30003 | 2.628408 | 0.435407 | 0.020999 |
| CASIA-Interval | ResNet-18 | 2025 | ordinary_impostor | 24 | 24 | 0.410671 | 0.090218 | 0.499111 | 0.589329 | 0.282468 | 2.084883 | 0.514515 | 0.02973 |
| CASIA-Interval | SwinV2-Tiny | 42 | genuine | 24 | 12 | 0.381058 | 0.11158 | 0.507362 | 0.618942 | 0.264772 | 1.895024 | 0.651853 | 0.006036 |
| CASIA-Interval | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0.394914 | 0.121938 | 0.483148 | 0.605086 | 0.30003 | 1.709794 | 0.738378 | 0.008476 |
| CASIA-Interval | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0.322635 | 0.092457 | 0.584908 | 0.677365 | 0.282468 | 1.617823 | 0.709517 | 0.005662 |
| CASIA-Interval | SwinV2-Tiny | 123 | genuine | 24 | 12 | 0.40985 | 0.081629 | 0.508521 | 0.59015 | 0.264772 | 1.688395 | 0.70956 | 0.010519 |
| CASIA-Interval | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0.426775 | 0.106491 | 0.466734 | 0.573225 | 0.30003 | 3.009492 | 0.609887 | 0.01538 |
| CASIA-Interval | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0.355521 | 0.076233 | 0.568246 | 0.644479 | 0.282468 | 1.420953 | 0.729003 | 0.017725 |
| CASIA-Interval | SwinV2-Tiny | 2025 | genuine | 24 | 12 | 0.397451 | 0.082764 | 0.519786 | 0.602549 | 0.264772 | 1.887245 | 0.500942 | 0.023199 |
| CASIA-Interval | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0.355931 | 0.08738 | 0.556689 | 0.644069 | 0.30003 | 1.599295 | 0.739609 | 0.013729 |
| CASIA-Interval | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0.352851 | 0.08503 | 0.56212 | 0.647149 | 0.282468 | 1.503175 | 0.736927 | 0.022989 |

Complete gallery, every pair and seed (external recorded asset).



# IITD: separate E2-F spatial analysis

| dataset | seed | category | all_branch_comparisons | supported_branch_comparisons | supported_images | nonannulus_effect | annulus_effect | pupil_effect | outside_disc_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | 42 | genuine | 24 | 24 | 24 | 0.019638 | -0.019638 | 0.032484 | -0.012846 |
| IITD | 42 | high_similarity_impostor | 12 | 10 | 10 | -0.105619 | 0.105619 | 0.063971 | -0.16959 |
| IITD | 42 | ordinary_impostor | 24 | 24 | 24 | -0.022279 | 0.022279 | 0.068484 | -0.090763 |
| IITD | 123 | genuine | 24 | 24 | 24 | -0.041931 | 0.041931 | 0.058397 | -0.100328 |
| IITD | 123 | high_similarity_impostor | 12 | 12 | 12 | -0.128536 | 0.128536 | 0.105363 | -0.233899 |
| IITD | 123 | ordinary_impostor | 24 | 22 | 22 | -0.031617 | 0.031617 | 0.096736 | -0.128353 |
| IITD | 2025 | genuine | 24 | 24 | 24 | -0.033231 | 0.033231 | 0.026444 | -0.059675 |
| IITD | 2025 | high_similarity_impostor | 12 | 12 | 12 | 0.049473 | -0.049473 | 0.04189 | 0.007583 |
| IITD | 2025 | ordinary_impostor | 24 | 22 | 22 | -0.071008 | 0.071008 | 0.08372 | -0.154728 |

Per-architecture/seed/category normalized mass and concentration. Fractions are0..1; undefined density ratios are retained as missing with finite counts in the data.

| dataset | architecture | seed | category | images | subjects | annulus_mass_fraction_mean | pupil_mass_fraction_mean | outside_disc_mass_fraction_mean | nonannulus_mass_fraction_mean | annulus_area_fraction_mean | iris_vs_outside_density_ratio_p50 | nonannulus_vs_iris_density_ratio_p50 | padding_positive_mass_fraction_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | 42 | genuine | 24 | 12 | 0.363852 | 0.100423 | 0.535724 | 0.636148 | 0.318746 | 1.195769 | 0.852062 | 0.076364 |
| IITD | ResNet-18 | 42 | high_similarity_impostor | 10 | 10 | 0.484152 | 0.109904 | 0.405945 | 0.515848 | 0.323341 | 2.441946 | 0.510827 | 0.067547 |
| IITD | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0.31321 | 0.119154 | 0.567637 | 0.68679 | 0.299592 | 1.060983 | 1.132702 | 0.097592 |
| IITD | ResNet-18 | 123 | genuine | 24 | 12 | 0.406375 | 0.092271 | 0.501354 | 0.593625 | 0.318746 | 1.83414 | 0.686474 | 0.067369 |
| IITD | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0.481472 | 0.150479 | 0.368049 | 0.518528 | 0.319363 | 2.860704 | 0.497966 | 0.066561 |
| IITD | ResNet-18 | 123 | ordinary_impostor | 22 | 22 | 0.366855 | 0.142823 | 0.490322 | 0.633145 | 0.302024 | 1.502367 | 0.849293 | 0.077848 |
| IITD | ResNet-18 | 2025 | genuine | 24 | 12 | 0.413161 | 0.081638 | 0.505201 | 0.586839 | 0.318746 | 1.886365 | 0.644309 | 0.071957 |
| IITD | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0.390745 | 0.107459 | 0.501796 | 0.609255 | 0.319363 | 1.516058 | 0.691754 | 0.069576 |
| IITD | ResNet-18 | 2025 | ordinary_impostor | 22 | 22 | 0.369849 | 0.123461 | 0.50669 | 0.630151 | 0.294221 | 1.341184 | 0.852192 | 0.077641 |
| IITD | SwinV2-Tiny | 42 | genuine | 24 | 12 | 0.383491 | 0.067939 | 0.54857 | 0.616509 | 0.318746 | 1.185216 | 0.833705 | 0.072019 |
| IITD | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0.377167 | 0.055528 | 0.567305 | 0.622833 | 0.319363 | 1.395954 | 0.763249 | 0.075306 |
| IITD | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0.290931 | 0.050669 | 0.658399 | 0.709069 | 0.299592 | 0.828601 | 1.175983 | 0.069946 |
| IITD | SwinV2-Tiny | 123 | genuine | 24 | 12 | 0.364444 | 0.033874 | 0.601682 | 0.635556 | 0.318746 | 1.278705 | 0.714328 | 0.077462 |
| IITD | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0.352936 | 0.045115 | 0.601948 | 0.647064 | 0.319363 | 0.846953 | 1.091418 | 0.086325 |
| IITD | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0.349789 | 0.055549 | 0.594662 | 0.650211 | 0.299592 | 1.123089 | 0.842486 | 0.063231 |
| IITD | SwinV2-Tiny | 2025 | genuine | 24 | 12 | 0.379931 | 0.055194 | 0.564876 | 0.620069 | 0.318746 | 1.366696 | 0.700756 | 0.084243 |
| IITD | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0.440218 | 0.065569 | 0.494213 | 0.559782 | 0.319363 | 2.074129 | 0.517669 | 0.069948 |
| IITD | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0.310327 | 0.045118 | 0.644555 | 0.689673 | 0.299592 | 0.978763 | 1.047856 | 0.077266 |

Complete gallery, every pair and seed (external recorded asset).



# AMF: separate E2-F spatial analysis

| dataset | seed | category | all_branch_comparisons | supported_branch_comparisons | supported_images | nonannulus_effect | annulus_effect | pupil_effect | outside_disc_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | 42 | genuine | 24 | 24 | 24 | -0.050308 | 0.050308 | 0.021153 | -0.071462 |
| AMF | 42 | high_similarity_impostor | 12 | 12 | 12 | -0.03414 | 0.03414 | 0.024284 | -0.058424 |
| AMF | 42 | ordinary_impostor | 24 | 22 | 22 | -0.100949 | 0.100949 | 0.03529 | -0.13624 |
| AMF | 123 | genuine | 24 | 24 | 24 | -0.027035 | 0.027035 | 0.018718 | -0.045753 |
| AMF | 123 | high_similarity_impostor | 12 | 12 | 12 | -0.024964 | 0.024964 | 0.013864 | -0.038828 |
| AMF | 123 | ordinary_impostor | 24 | 22 | 22 | -0.096123 | 0.096123 | 0.021262 | -0.117385 |
| AMF | 2025 | genuine | 24 | 24 | 24 | -0.010143 | 0.010143 | 0.009672 | -0.019816 |
| AMF | 2025 | high_similarity_impostor | 12 | 12 | 12 | -0.025461 | 0.025461 | -0.001321 | -0.02414 |
| AMF | 2025 | ordinary_impostor | 24 | 24 | 24 | -0.038762 | 0.038762 | 0.008329 | -0.047092 |

Per-architecture/seed/category normalized mass and concentration. Fractions are0..1; undefined density ratios are retained as missing with finite counts in the data.

| dataset | architecture | seed | category | images | subjects | annulus_mass_fraction_mean | pupil_mass_fraction_mean | outside_disc_mass_fraction_mean | nonannulus_mass_fraction_mean | annulus_area_fraction_mean | iris_vs_outside_density_ratio_p50 | nonannulus_vs_iris_density_ratio_p50 | padding_positive_mass_fraction_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 42 | genuine | 24 | 12 | 0.221459 | 0.042214 | 0.736328 | 0.778541 | 0.147998 | 1.284087 | 0.773054 | 0.109389 |
| AMF | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0.140997 | 0.034964 | 0.82404 | 0.859003 | 0.141123 | 1.007388 | 1.013562 | 0.123541 |
| AMF | ResNet-18 | 42 | ordinary_impostor | 22 | 22 | 0.19093 | 0.046662 | 0.762409 | 0.80907 | 0.142622 | 1.641037 | 0.627002 | 0.150627 |
| AMF | ResNet-18 | 123 | genuine | 24 | 12 | 0.198725 | 0.039619 | 0.761655 | 0.801275 | 0.147998 | 1.384358 | 0.735074 | 0.075334 |
| AMF | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0.164676 | 0.035376 | 0.799948 | 0.835324 | 0.141123 | 0.744408 | 1.386411 | 0.076862 |
| AMF | ResNet-18 | 123 | ordinary_impostor | 22 | 22 | 0.20473 | 0.038229 | 0.75704 | 0.79527 | 0.148248 | 1.252572 | 0.829962 | 0.113369 |
| AMF | ResNet-18 | 2025 | genuine | 24 | 12 | 0.175205 | 0.023435 | 0.80136 | 0.824795 | 0.147998 | 1.188193 | 0.817605 | 0.074151 |
| AMF | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0.155464 | 0.016876 | 0.82766 | 0.844536 | 0.141123 | 0.860137 | 1.155333 | 0.088408 |
| AMF | ResNet-18 | 2025 | ordinary_impostor | 24 | 24 | 0.188931 | 0.024231 | 0.786837 | 0.811069 | 0.144576 | 1.343386 | 0.739722 | 0.103771 |
| AMF | SwinV2-Tiny | 42 | genuine | 24 | 12 | 0.17115 | 0.02106 | 0.807789 | 0.82885 | 0.147998 | 0.570885 | 1.720234 | 0.056285 |
| AMF | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0.106857 | 0.010679 | 0.882464 | 0.893143 | 0.141123 | 0.3841 | 2.801569 | 0.056697 |
| AMF | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0.098012 | 0.012525 | 0.889462 | 0.901988 | 0.144576 | 0.348192 | 2.795569 | 0.064496 |
| AMF | SwinV2-Tiny | 123 | genuine | 24 | 12 | 0.17169 | 0.020902 | 0.807408 | 0.82831 | 0.147998 | 0.981774 | 1.006127 | 0.049373 |
| AMF | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0.139712 | 0.021512 | 0.838776 | 0.860288 | 0.141123 | 0.738443 | 1.322985 | 0.040105 |
| AMF | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0.110131 | 0.016987 | 0.872882 | 0.889869 | 0.144576 | 0.7975 | 1.258904 | 0.035039 |
| AMF | SwinV2-Tiny | 2025 | genuine | 24 | 12 | 0.165062 | 0.013762 | 0.821176 | 0.834938 | 0.147998 | 0.693912 | 1.41995 | 0.064951 |
| AMF | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0.130003 | 0.018197 | 0.8518 | 0.869997 | 0.141123 | 0.539538 | 1.823587 | 0.045556 |
| AMF | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0.150169 | 0.015902 | 0.833929 | 0.849831 | 0.144576 | 0.582896 | 1.673377 | 0.050177 |

Complete gallery, every pair and seed (external recorded asset).



# UTIRIS_NIR: separate E2-F spatial analysis

| dataset | seed | category | all_branch_comparisons | supported_branch_comparisons | supported_images | nonannulus_effect | annulus_effect | pupil_effect | outside_disc_effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | 42 | genuine | 24 | 24 | 24 | -0.031174 | 0.031174 | 0.060435 | -0.091609 |
| UTIRIS_NIR | 42 | high_similarity_impostor | 12 | 12 | 12 | 0.049291 | -0.049291 | 0.114336 | -0.065045 |
| UTIRIS_NIR | 42 | ordinary_impostor | 24 | 24 | 24 | -0.078728 | 0.078728 | 0.137981 | -0.216709 |
| UTIRIS_NIR | 123 | genuine | 24 | 22 | 22 | -0.080776 | 0.080776 | 0.04808 | -0.128856 |
| UTIRIS_NIR | 123 | high_similarity_impostor | 12 | 12 | 12 | -0.075874 | 0.075874 | 0.096938 | -0.172812 |
| UTIRIS_NIR | 123 | ordinary_impostor | 24 | 24 | 24 | -0.047676 | 0.047676 | 0.088549 | -0.136226 |
| UTIRIS_NIR | 2025 | genuine | 24 | 24 | 24 | 0.011111 | -0.011111 | -0.000791 | 0.011903 |
| UTIRIS_NIR | 2025 | high_similarity_impostor | 12 | 12 | 12 | 0.008527 | -0.008527 | 0.015454 | -0.006927 |
| UTIRIS_NIR | 2025 | ordinary_impostor | 24 | 22 | 22 | 0.038502 | -0.038502 | 0.020554 | 0.017948 |

Per-architecture/seed/category normalized mass and concentration. Fractions are0..1; undefined density ratios are retained as missing with finite counts in the data.

| dataset | architecture | seed | category | images | subjects | annulus_mass_fraction_mean | pupil_mass_fraction_mean | outside_disc_mass_fraction_mean | nonannulus_mass_fraction_mean | annulus_area_fraction_mean | iris_vs_outside_density_ratio_p50 | nonannulus_vs_iris_density_ratio_p50 | padding_positive_mass_fraction_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | 42 | genuine | 24 | 12 | 0.31366 | 0.10755 | 0.57879 | 0.68634 | 0.214804 | 1.26379 | 0.841185 | 0.115787 |
| UTIRIS_NIR | ResNet-18 | 42 | high_similarity_impostor | 12 | 12 | 0.277019 | 0.203873 | 0.519107 | 0.722981 | 0.202897 | 1.464408 | 0.776396 | 0.135272 |
| UTIRIS_NIR | ResNet-18 | 42 | ordinary_impostor | 24 | 24 | 0.322063 | 0.197199 | 0.480738 | 0.677937 | 0.209154 | 2.871107 | 0.491278 | 0.101418 |
| UTIRIS_NIR | ResNet-18 | 123 | genuine | 22 | 11 | 0.363303 | 0.092031 | 0.544666 | 0.636697 | 0.216044 | 2.392665 | 0.502119 | 0.072643 |
| UTIRIS_NIR | ResNet-18 | 123 | high_similarity_impostor | 12 | 12 | 0.316657 | 0.141601 | 0.541743 | 0.683343 | 0.202897 | 2.723222 | 0.618035 | 0.065885 |
| UTIRIS_NIR | ResNet-18 | 123 | ordinary_impostor | 24 | 24 | 0.274434 | 0.131837 | 0.59373 | 0.725566 | 0.209154 | 1.42055 | 0.799054 | 0.083074 |
| UTIRIS_NIR | ResNet-18 | 2025 | genuine | 24 | 12 | 0.296197 | 0.055454 | 0.64835 | 0.703803 | 0.214804 | 1.429943 | 0.682653 | 0.088819 |
| UTIRIS_NIR | ResNet-18 | 2025 | high_similarity_impostor | 12 | 12 | 0.279955 | 0.085327 | 0.634718 | 0.720045 | 0.202897 | 1.393184 | 0.733228 | 0.100101 |
| UTIRIS_NIR | ResNet-18 | 2025 | ordinary_impostor | 22 | 22 | 0.263636 | 0.0839 | 0.652464 | 0.736364 | 0.213735 | 1.390429 | 0.81433 | 0.09512 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | genuine | 24 | 12 | 0.282486 | 0.047116 | 0.670399 | 0.717514 | 0.214804 | 1.315674 | 0.732823 | 0.059292 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | high_similarity_impostor | 12 | 12 | 0.32631 | 0.089537 | 0.584153 | 0.67369 | 0.202897 | 2.173676 | 0.585259 | 0.054674 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | ordinary_impostor | 24 | 24 | 0.243335 | 0.059218 | 0.697447 | 0.756665 | 0.209154 | 1.301433 | 0.845098 | 0.066239 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | genuine | 24 | 12 | 0.278463 | 0.042261 | 0.679276 | 0.721537 | 0.214804 | 0.99707 | 1.010147 | 0.056757 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | high_similarity_impostor | 12 | 12 | 0.240783 | 0.044663 | 0.714554 | 0.759217 | 0.202897 | 0.894407 | 1.102513 | 0.060611 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | ordinary_impostor | 24 | 24 | 0.226757 | 0.043287 | 0.729956 | 0.773243 | 0.209154 | 1.010788 | 0.9567 | 0.06138 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | genuine | 24 | 12 | 0.307308 | 0.056245 | 0.636447 | 0.692692 | 0.214804 | 1.74613 | 0.603858 | 0.051674 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | high_similarity_impostor | 12 | 12 | 0.288482 | 0.069873 | 0.641645 | 0.711518 | 0.202897 | 1.163925 | 0.836808 | 0.056722 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | ordinary_impostor | 24 | 24 | 0.324148 | 0.06764 | 0.608211 | 0.675852 | 0.209154 | 1.756348 | 0.589526 | 0.065707 |

Complete gallery, every pair and seed (external recorded asset).



## Interpretation limits

Positive attribution for an impostor pair describes increasing its similarity, not correct identity evidence. L1 normalization can amplify tiny positive signals; gradient/mass magnitudes, zero maps and parameter/partner checks are retained. Coarse features, upsampling, network-specific normalization and ROI prediction errors limit spatial interpretation. Suppressive signed evidence is not summarized as positive mass. Different attribution fractions are not evidence of necessary or sufficient identity cues. No saliency-based model/seed selection occurs.

The original Grad-CAM method motivates gradient-weighted localization ([Selvaraju et al.](https://arxiv.org/abs/1610.02391)); parameter-dependence checks address misleading visual explanations ([Adebayo et al.](https://arxiv.org/abs/1810.03292)). These references do not establish validity for this specific verification task. Full sanity findings are in E2_F_SANITY_CHECKS.md and final limits in E2_F_FINAL_INTERPRETATION.md.


## Final numerical and descriptive clarification

All10 primary dataset/category three-seed means show lower normalized nonannulus positive mass for ResNet than Swin (10/10 negative ResNet-minus-Swin means). At the individual-seed level, 25/30 differences favor greater Swin mass and 5/30 greater ResNet mass. These are direction counts of separate results, not a pooled mass estimate or significance test. The proposed universal ResNet-greater-outside-annulus explanation is not supported by this sample.

All3060 generated branch maps have finite activations/gradients and nonzero positive mass. The locked original-score fidelity check flags 15 primary pair/checkpoint cases (30 branch maps), all ResNet, because FP32 attribution scores exceed the predefined0.001 agreement tolerance. They remain visible but unsupported in the primary paired summaries. No maps, thresholds, feature layers, selected pairs or support flags were changed.

Original AMP batch24 inference scores were replayed for every numerical exception, with maximum error 0 against the saved cache. FP32 batch24 versus FP32 attribution-batch2 differs by at most 0.000126391649. The replay isolates precision/batch-kernel numerical effects rather than changed weights, targets or stale image provenance. It does not waive the frozen tolerance. See [all numerical exceptions](NUMERICAL_DIAGNOSTIC_REPORT.md).

Parameter and partner controls show that the spatial distributions respond to learned parameters and the comparison partner. These response diagnostics are necessary checks, not causal validation. Their exact per-dataset/seed values and zeros/undefined cases remain in the sanity report; no single correlation cutoff is used.

| dataset | architecture | seed | pearson_mean | cosine_mean | total_variation_mean |
| --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 42 | -0.124969 | 0.269005 | 0.732432 |
| AMF | ResNet-18 | 123 | -0.097202 | 0.298995 | 0.694067 |
| AMF | ResNet-18 | 2025 | 0.043342 | 0.377825 | 0.643771 |
| AMF | SwinV2-Tiny | 42 | -0.20797 | 0.209689 | 0.77142 |
| AMF | SwinV2-Tiny | 123 | -0.157202 | 0.244464 | 0.768221 |
| AMF | SwinV2-Tiny | 2025 | 0.168529 | 0.422637 | 0.639253 |
| CASIA-Interval | ResNet-18 | 42 | -0.072029 | 0.282398 | 0.704517 |
| CASIA-Interval | ResNet-18 | 123 | 0.002952 | 0.329522 | 0.696111 |
| CASIA-Interval | ResNet-18 | 2025 | -0.013783 | 0.325835 | 0.693025 |
| CASIA-Interval | SwinV2-Tiny | 42 | -0.086093 | 0.248235 | 0.761108 |
| CASIA-Interval | SwinV2-Tiny | 123 | -0.034664 | 0.283477 | 0.734775 |
| CASIA-Interval | SwinV2-Tiny | 2025 | -0.014559 | 0.315756 | 0.704336 |
| CUST-Iris | ResNet-18 | 42 | -0.036764 | 0.331341 | 0.673868 |
| CUST-Iris | ResNet-18 | 123 | 0.02621 | 0.369228 | 0.678476 |
| CUST-Iris | ResNet-18 | 2025 | 0.065308 | 0.381936 | 0.650958 |
| CUST-Iris | SwinV2-Tiny | 42 | -0.008158 | 0.315723 | 0.718171 |
| CUST-Iris | SwinV2-Tiny | 123 | -0.123249 | 0.270015 | 0.715935 |
| CUST-Iris | SwinV2-Tiny | 2025 | -0.036877 | 0.273987 | 0.737395 |
| IITD | ResNet-18 | 42 | 0.023479 | 0.365636 | 0.657917 |
| IITD | ResNet-18 | 123 | 0.065985 | 0.408115 | 0.622734 |
| IITD | ResNet-18 | 2025 | 0.046141 | 0.399962 | 0.626558 |
| IITD | SwinV2-Tiny | 42 | -0.01472 | 0.323175 | 0.705652 |
| IITD | SwinV2-Tiny | 123 | -0.071969 | 0.294969 | 0.717938 |
| IITD | SwinV2-Tiny | 2025 | -0.029015 | 0.300701 | 0.702615 |
| UTIRIS_NIR | ResNet-18 | 42 | 0.16745 | 0.43465 | 0.611221 |
| UTIRIS_NIR | ResNet-18 | 123 | 0.007068 | 0.323656 | 0.684907 |
| UTIRIS_NIR | ResNet-18 | 2025 | 0.014812 | 0.333044 | 0.686941 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | 0.130546 | 0.391906 | 0.65987 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | -0.129457 | 0.243064 | 0.767431 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | -0.055128 | 0.295638 | 0.720704 |

| dataset | architecture | seed | pearson_mean | cosine_mean | total_variation_mean | unchanged_anchor_activation_checks |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 42 | -0.114949 | 0.304998 | 0.671212 | 3 |
| AMF | ResNet-18 | 123 | 0.258961 | 0.563059 | 0.486676 | 3 |
| AMF | ResNet-18 | 2025 | 0.252668 | 0.504145 | 0.58243 | 3 |
| AMF | SwinV2-Tiny | 42 | 0.126926 | 0.383508 | 0.618256 | 3 |
| AMF | SwinV2-Tiny | 123 | -0.054263 | 0.32051 | 0.680537 | 3 |
| AMF | SwinV2-Tiny | 2025 | -0.148793 | 0.209448 | 0.785834 | 3 |
| CASIA-Interval | ResNet-18 | 42 | -0.007534 | 0.296146 | 0.685116 | 3 |
| CASIA-Interval | ResNet-18 | 123 | 0.037368 | 0.289032 | 0.681071 | 3 |
| CASIA-Interval | ResNet-18 | 2025 | -0.070801 | 0.266158 | 0.669971 | 3 |
| CASIA-Interval | SwinV2-Tiny | 42 | 0.38837 | 0.556835 | 0.52405 | 3 |
| CASIA-Interval | SwinV2-Tiny | 123 | 0.505649 | 0.655176 | 0.457271 | 3 |
| CASIA-Interval | SwinV2-Tiny | 2025 | 0.453847 | 0.589059 | 0.498504 | 3 |
| CUST-Iris | ResNet-18 | 42 | -0.066908 | 0.260841 | 0.734621 | 3 |
| CUST-Iris | ResNet-18 | 123 | 0.221724 | 0.523852 | 0.525037 | 3 |
| CUST-Iris | ResNet-18 | 2025 | 0.055347 | 0.338157 | 0.647955 | 3 |
| CUST-Iris | SwinV2-Tiny | 42 | -0.128526 | 0.251846 | 0.750423 | 3 |
| CUST-Iris | SwinV2-Tiny | 123 | -0.205574 | 0.146416 | 0.795172 | 3 |
| CUST-Iris | SwinV2-Tiny | 2025 | 0.149628 | 0.36954 | 0.685755 | 3 |
| IITD | ResNet-18 | 42 | 0.205751 | 0.438535 | 0.587253 | 3 |
| IITD | ResNet-18 | 123 | -0.043361 | 0.357124 | 0.662082 | 3 |
| IITD | ResNet-18 | 2025 | -0.124959 | 0.222812 | 0.712057 | 3 |
| IITD | SwinV2-Tiny | 42 | 0.492541 | 0.677854 | 0.432542 | 3 |
| IITD | SwinV2-Tiny | 123 | -0.07467 | 0.314311 | 0.653675 | 3 |
| IITD | SwinV2-Tiny | 2025 | 0.03959 | 0.313097 | 0.654318 | 3 |
| UTIRIS_NIR | ResNet-18 | 42 | 0.293179 | 0.477928 | 0.538767 | 3 |
| UTIRIS_NIR | ResNet-18 | 123 | 0.049643 | 0.306064 | 0.657305 | 3 |
| UTIRIS_NIR | ResNet-18 | 2025 | 0.297074 | 0.504686 | 0.556772 | 3 |
| UTIRIS_NIR | SwinV2-Tiny | 42 | 0.031805 | 0.331943 | 0.685604 | 3 |
| UTIRIS_NIR | SwinV2-Tiny | 123 | -0.135919 | 0.215215 | 0.747025 | 3 |
| UTIRIS_NIR | SwinV2-Tiny | 2025 | 0.093665 | 0.365384 | 0.661407 | 3 |

The result does not establish that Swin learned more periocular identity information, nor that ResNet ignores it. Pupil/outside-disc regions, predicted-mask uncertainty, coarse grid/feature semantics, positive-only normalization and limited selected pairs constrain interpretation. E2-D/E2-E intervention findings are not replaced. The causal source of the architecture–representation interaction remains unresolved; no additional experiments or methods are proposed.