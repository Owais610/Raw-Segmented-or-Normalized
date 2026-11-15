> Publication view: recognition comparisons use the matched population. Table values are preserved; old workspace paths and file-integrity infrastructure are omitted. Saved tables are in Results (external recorded asset). New notebook outputs remain separate.

# E2-B: all five datasets, fixed quality and masking definitions

This extends the preserved external audit with original frozen held-out test images only. Every formula and quantile-selection rule is unchanged from ANALYSIS_PLAN.md. No tuning or refitting. Saturation >=250 is a proxy, not a validated specular-reflection measure; sampled polar gradients are resolution-standardized proxies. Missing geometry stays missing. Correlations are descriptive and cannot establish causes of domain differences.

# CUST-Iris: E2-B quality/masking

Unique source captures: 432

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | pupil_iris_radius_ratio | 427 | 5 | 0.289225 | 0.359636 | 0.440259 |
| CUST-Iris | relative_fitted_annulus_area | 427 | 5 | 0.806172 | 0.870662 | 0.916345 |
| CUST-Iris | center_displacement_iris_radii | 427 | 5 | 0.024369 | 0.041929 | 0.06761 |
| CUST-Iris | relative_segmented_annulus_area | 432 | 0 | 0.797172 | 0.865012 | 0.91525 |
| CUST-Iris | iris_native_frame_fraction | 432 | 0 | 0.198013 | 0.223587 | 0.259358 |
| CUST-Iris | mask_equivalent_pupil_iris_ratio | 432 | 0 | 0.291119 | 0.367407 | 0.450364 |
| CUST-Iris | native_robust_contrast | 432 | 0 | 0.054902 | 0.07451 | 0.101569 |
| CUST-Iris | native_median_intensity | 432 | 0 | 0.317647 | 0.34902 | 0.392157 |
| CUST-Iris | bright_proxy_fraction | 432 | 0 | 0.0 | 4.1e-05 | 0.000544 |
| CUST-Iris | polar_local_contrast | 427 | 5 | 0.004143 | 0.005759 | 0.007834 |
| CUST-Iris | polar_gradient_mean | 427 | 5 | 0.00453 | 0.006274 | 0.00847 |
| CUST-Iris | polar_gradient_p90 | 427 | 5 | 0.008686 | 0.011765 | 0.016452 |
| CUST-Iris | polar_laplacian_variance | 427 | 5 | 0.00055 | 0.002001 | 0.005813 |
| CUST-Iris | iris_inlier_fraction | 427 | 5 | 0.73913 | 0.882353 | 1.0 |
| CUST-Iris | iris_supported_arc_degrees | 427 | 5 | 263.106367 | 298.322218 | 344.81878 |
| CUST-Iris | iris_relative_residual | 427 | 5 | 0.004314 | 0.007198 | 0.01174 |
| CUST-Iris | pupil_inlier_fraction | 427 | 5 | 1.0 | 1.0 | 1.0 |
| CUST-Iris | pupil_supported_arc_degrees | 427 | 5 | 331.88332 | 338.43426 | 342.776803 |
| CUST-Iris | pupil_relative_residual | 427 | 5 | 0.002537 | 0.00404 | 0.007242 |
| CUST-Iris | c1_valid_fraction | 427 | 5 | 0.912042 | 0.962311 | 0.979797 |
| CUST-Iris | removed_fraction | 427 | 5 | 0.0 | 0.004853 | 0.048527 |
| CUST-Iris | removed_high_gradient_fraction | 427 | 5 | 0.0 | 0.009867 | 0.130438 |
| CUST-Iris | high_gradient_fraction_of_removed | 332 | 100 | 0.500704 | 0.722944 | 0.877511 |

Acquisition/QC strata:

| dataset | native_dimensions | folder_filename_conflict | images | polar_successes | removed_fraction_mean | gradient_mean | native_contrast_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | 480x480 | False | 432 | 427 | 0.015381 | 0.006432 | 0.075281 |

Existing warning/failure counts:

| dataset | type | reason | images |
| --- | --- | --- | --- |
| CUST-Iris | existing_qc | relative_low_sharpness_dataset_p01 | 4 |
| CUST-Iris | polar_failure | ambiguous_multiple_pupil_components | 1 |
| CUST-Iris | polar_failure | iris_boundary_outside_fit | 3 |
| CUST-Iris | polar_failure | pupil_boundary_outside_fit | 1 |

Fixed subject-level association panel, rho across subjects and range across3 seeds:

| dataset | architecture | condition | feature | rho_mean | rho_min | rho_max | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | E1-A | iris_supported_arc_degrees | 0.1974 | 0.0895 | 0.2993 | 54 |
| CUST-Iris | ResNet-18 | E1-A | native_robust_contrast | -0.0007 | -0.09 | 0.1247 | 54 |
| CUST-Iris | ResNet-18 | E1-A | polar_gradient_mean | -0.08 | -0.1254 | -0.0457 | 54 |
| CUST-Iris | ResNet-18 | E1-A | pupil_iris_radius_ratio | -0.2735 | -0.3375 | -0.1944 | 54 |
| CUST-Iris | ResNet-18 | E1-A | removed_fraction | -0.1038 | -0.185 | -0.0093 | 54 |
| CUST-Iris | ResNet-18 | E1-C1 | iris_supported_arc_degrees | -0.0497 | -0.1463 | 0.0484 | 54 |
| CUST-Iris | ResNet-18 | E1-C1 | native_robust_contrast | -0.0784 | -0.1419 | -0.0251 | 54 |
| CUST-Iris | ResNet-18 | E1-C1 | polar_gradient_mean | 0.0226 | -0.127 | 0.1221 | 54 |
| CUST-Iris | ResNet-18 | E1-C1 | pupil_iris_radius_ratio | -0.1474 | -0.248 | -0.0522 | 54 |
| CUST-Iris | ResNet-18 | E1-C1 | removed_fraction | 0.1271 | 0.1097 | 0.1504 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | iris_supported_arc_degrees | -0.0437 | -0.1471 | 0.1081 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | native_robust_contrast | -0.1823 | -0.3455 | -0.0983 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | polar_gradient_mean | -0.1226 | -0.3352 | 0.0606 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | pupil_iris_radius_ratio | -0.1319 | -0.184 | -0.0287 | 54 |
| CUST-Iris | ResNet-18 | E1-C2 | removed_fraction | 0.0121 | -0.0506 | 0.1023 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-A | iris_supported_arc_degrees | 0.0035 | -0.1214 | 0.1911 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-A | native_robust_contrast | 0.0097 | -0.0946 | 0.0812 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-A | polar_gradient_mean | 0.0052 | -0.0453 | 0.0377 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-A | pupil_iris_radius_ratio | -0.3612 | -0.4228 | -0.3082 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-A | removed_fraction | -0.1015 | -0.1411 | -0.0603 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | iris_supported_arc_degrees | -0.1508 | -0.1601 | -0.1362 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | native_robust_contrast | -0.1297 | -0.202 | -0.0729 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | polar_gradient_mean | 0.0477 | -0.0746 | 0.1606 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | pupil_iris_radius_ratio | -0.1164 | -0.2329 | -0.0067 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C1 | removed_fraction | -0.0824 | -0.1039 | -0.0568 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | iris_supported_arc_degrees | -0.1435 | -0.2019 | -0.0575 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | native_robust_contrast | 0.0035 | -0.0351 | 0.031 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | polar_gradient_mean | 0.1909 | 0.1078 | 0.2601 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | pupil_iris_radius_ratio | -0.115 | -0.3395 | 0.0203 | 54 |
| CUST-Iris | SwinV2-Tiny | E1-C2 | removed_fraction | 0.105 | 0.0792 | 0.1469 | 54 |


# CASIA-Interval: E2-B quality/masking

Unique source captures: 396

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | pupil_iris_radius_ratio | 395 | 1 | 0.322417 | 0.393986 | 0.48428 |
| CASIA-Interval | relative_fitted_annulus_area | 395 | 1 | 0.765473 | 0.844775 | 0.896046 |
| CASIA-Interval | center_displacement_iris_radii | 395 | 1 | 0.01983 | 0.041538 | 0.060464 |
| CASIA-Interval | relative_segmented_annulus_area | 396 | 0 | 0.732879 | 0.817094 | 0.885635 |
| CASIA-Interval | iris_native_frame_fraction | 396 | 0 | 0.295725 | 0.353214 | 0.400167 |
| CASIA-Interval | mask_equivalent_pupil_iris_ratio | 396 | 0 | 0.338179 | 0.427675 | 0.516838 |
| CASIA-Interval | native_robust_contrast | 396 | 0 | 0.113725 | 0.145098 | 0.176471 |
| CASIA-Interval | native_median_intensity | 396 | 0 | 0.531373 | 0.605882 | 0.694118 |
| CASIA-Interval | bright_proxy_fraction | 396 | 0 | 0.0 | 0.000145 | 0.001616 |
| CASIA-Interval | polar_local_contrast | 395 | 1 | 0.011645 | 0.015421 | 0.020164 |
| CASIA-Interval | polar_gradient_mean | 395 | 1 | 0.012145 | 0.015864 | 0.020827 |
| CASIA-Interval | polar_gradient_p90 | 395 | 1 | 0.022119 | 0.030785 | 0.043318 |
| CASIA-Interval | polar_laplacian_variance | 395 | 1 | 0.008383 | 0.014994 | 0.029503 |
| CASIA-Interval | iris_inlier_fraction | 395 | 1 | 0.583962 | 0.75 | 0.916667 |
| CASIA-Interval | iris_supported_arc_degrees | 395 | 1 | 228.012664 | 259.495149 | 304.835598 |
| CASIA-Interval | iris_relative_residual | 395 | 1 | 0.004437 | 0.008594 | 0.014432 |
| CASIA-Interval | pupil_inlier_fraction | 395 | 1 | 1.0 | 1.0 | 1.0 |
| CASIA-Interval | pupil_supported_arc_degrees | 395 | 1 | 332.25106 | 337.149108 | 341.322829 |
| CASIA-Interval | pupil_relative_residual | 395 | 1 | 0.002044 | 0.00312 | 0.004629 |
| CASIA-Interval | c1_valid_fraction | 395 | 1 | 0.771558 | 0.887695 | 0.961969 |
| CASIA-Interval | removed_fraction | 395 | 1 | 0.002068 | 0.082549 | 0.247712 |
| CASIA-Interval | removed_high_gradient_fraction | 395 | 1 | 0.003598 | 0.169387 | 0.552984 |
| CASIA-Interval | high_gradient_fraction_of_removed | 372 | 24 | 0.377109 | 0.581967 | 0.686952 |

Acquisition/QC strata:

| dataset | native_dimensions | folder_filename_conflict | images | polar_successes | removed_fraction_mean | gradient_mean | native_contrast_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | 320x280 | False | 396 | 395 | 0.108156 | 0.016224 | 0.145407 |

Existing warning/failure counts:

| dataset | type | reason | images |
| --- | --- | --- | --- |
| CASIA-Interval | existing_qc | eyelash_occlusion_review | 18 |
| CASIA-Interval | existing_qc | iris_touches_image_border | 22 |
| CASIA-Interval | existing_qc | relative_low_sharpness_dataset_p01 | 4 |
| CASIA-Interval | polar_failure | insufficient_iris_angular_support | 1 |

Fixed subject-level association panel, rho across subjects and range across3 seeds:

| dataset | architecture | condition | feature | rho_mean | rho_min | rho_max | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | E1-A | iris_supported_arc_degrees | -0.1185 | -0.1944 | -0.065 | 37 |
| CASIA-Interval | ResNet-18 | E1-A | native_robust_contrast | -0.1369 | -0.1769 | -0.0823 | 37 |
| CASIA-Interval | ResNet-18 | E1-A | polar_gradient_mean | -0.074 | -0.1451 | 0.005 | 37 |
| CASIA-Interval | ResNet-18 | E1-A | pupil_iris_radius_ratio | 0.0824 | -0.0605 | 0.2032 | 37 |
| CASIA-Interval | ResNet-18 | E1-A | removed_fraction | -0.0309 | -0.1091 | 0.0548 | 37 |
| CASIA-Interval | ResNet-18 | E1-C1 | iris_supported_arc_degrees | -0.111 | -0.119 | -0.1015 | 37 |
| CASIA-Interval | ResNet-18 | E1-C1 | native_robust_contrast | -0.0432 | -0.2115 | 0.096 | 37 |
| CASIA-Interval | ResNet-18 | E1-C1 | polar_gradient_mean | 0.1115 | -0.0372 | 0.2866 | 37 |
| CASIA-Interval | ResNet-18 | E1-C1 | pupil_iris_radius_ratio | -0.0153 | -0.0849 | 0.0199 | 37 |
| CASIA-Interval | ResNet-18 | E1-C1 | removed_fraction | 0.0732 | -0.0801 | 0.23 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | iris_supported_arc_degrees | -0.1091 | -0.2788 | -0.0166 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | native_robust_contrast | 0.0357 | -0.0605 | 0.11 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | polar_gradient_mean | -0.1046 | -0.2717 | 0.045 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | pupil_iris_radius_ratio | -0.0737 | -0.1316 | 0.0066 | 37 |
| CASIA-Interval | ResNet-18 | E1-C2 | removed_fraction | -0.1421 | -0.3483 | 0.0683 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-A | iris_supported_arc_degrees | -0.2379 | -0.2705 | -0.1821 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-A | native_robust_contrast | -0.2073 | -0.3739 | -0.1062 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-A | polar_gradient_mean | -0.0541 | -0.1605 | 0.0263 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-A | pupil_iris_radius_ratio | -0.0477 | -0.1996 | 0.1088 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-A | removed_fraction | 0.0633 | 0.0168 | 0.1524 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | iris_supported_arc_degrees | -0.2225 | -0.3108 | -0.1631 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | native_robust_contrast | -0.0136 | -0.0756 | 0.0775 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | polar_gradient_mean | -0.063 | -0.1057 | 0.0211 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | pupil_iris_radius_ratio | 0.1611 | 0.0889 | 0.2442 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C1 | removed_fraction | -0.1831 | -0.2354 | -0.1278 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | iris_supported_arc_degrees | -0.2613 | -0.3243 | -0.1799 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | native_robust_contrast | 0.1476 | -0.0202 | 0.2805 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | polar_gradient_mean | -0.1192 | -0.2041 | -0.0531 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | pupil_iris_radius_ratio | 0.0842 | 0.0595 | 0.1012 | 37 |
| CASIA-Interval | SwinV2-Tiny | E1-C2 | removed_fraction | -0.293 | -0.3438 | -0.2477 | 37 |


# IITD: E2-B quality/masking

Unique source captures: 319

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| IITD | pupil_iris_radius_ratio | 308 | 11 | 0.326218 | 0.403097 | 0.480698 |
| IITD | relative_fitted_annulus_area | 308 | 11 | 0.768929 | 0.837513 | 0.893581 |
| IITD | center_displacement_iris_radii | 308 | 11 | 0.029493 | 0.046573 | 0.066708 |
| IITD | relative_segmented_annulus_area | 319 | 0 | 0.728243 | 0.810009 | 0.884775 |
| IITD | iris_native_frame_fraction | 319 | 0 | 0.312263 | 0.396419 | 0.453042 |
| IITD | mask_equivalent_pupil_iris_ratio | 319 | 0 | 0.339449 | 0.43588 | 0.521303 |
| IITD | native_robust_contrast | 319 | 0 | 0.172549 | 0.211765 | 0.283137 |
| IITD | native_median_intensity | 319 | 0 | 0.333333 | 0.415686 | 0.470588 |
| IITD | bright_proxy_fraction | 319 | 0 | 5.7e-05 | 0.001051 | 0.002042 |
| IITD | polar_local_contrast | 308 | 11 | 0.024406 | 0.035515 | 0.046551 |
| IITD | polar_gradient_mean | 308 | 11 | 0.025173 | 0.036321 | 0.04777 |
| IITD | polar_gradient_p90 | 308 | 11 | 0.055868 | 0.08267 | 0.112259 |
| IITD | polar_laplacian_variance | 308 | 11 | 0.047696 | 0.099778 | 0.151646 |
| IITD | iris_inlier_fraction | 308 | 11 | 0.60853 | 0.758343 | 0.898986 |
| IITD | iris_supported_arc_degrees | 308 | 11 | 208.361141 | 236.878808 | 289.542338 |
| IITD | iris_relative_residual | 308 | 11 | 0.003839 | 0.007698 | 0.01387 |
| IITD | pupil_inlier_fraction | 308 | 11 | 1.0 | 1.0 | 1.0 |
| IITD | pupil_supported_arc_degrees | 308 | 11 | 331.118659 | 336.379739 | 340.953361 |
| IITD | pupil_relative_residual | 308 | 11 | 0.002624 | 0.003722 | 0.005008 |
| IITD | c1_valid_fraction | 308 | 11 | 0.683936 | 0.844559 | 0.944687 |
| IITD | removed_fraction | 308 | 11 | 0.004057 | 0.049863 | 0.133196 |
| IITD | removed_high_gradient_fraction | 308 | 11 | 0.006119 | 0.086426 | 0.257681 |
| IITD | high_gradient_fraction_of_removed | 295 | 24 | 0.250935 | 0.50332 | 0.769716 |

Acquisition/QC strata:

| dataset | native_dimensions | folder_filename_conflict | images | polar_successes | removed_fraction_mean | gradient_mean | native_contrast_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | 320x240 | False | 319 | 308 | 0.063045 | 0.036217 | 0.220151 |

Existing warning/failure counts:

| dataset | type | reason | images |
| --- | --- | --- | --- |
| IITD | existing_qc | exact_file_duplicate | 1 |
| IITD | existing_qc | exact_pixel_duplicate | 1 |
| IITD | existing_qc | eyelash_occlusion_review | 1 |
| IITD | existing_qc | grayscale_duplicate | 1 |
| IITD | existing_qc | iris_touches_image_border | 37 |
| IITD | existing_qc | relative_low_sharpness_dataset_p01 | 3 |
| IITD | polar_failure | insufficient_iris_angular_support | 7 |
| IITD | polar_failure | iris_boundary_outside_fit | 4 |

Fixed subject-level association panel, rho across subjects and range across3 seeds:

| dataset | architecture | condition | feature | rho_mean | rho_min | rho_max | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | E1-A | iris_supported_arc_degrees | -0.3344 | -0.4861 | -0.0407 | 32 |
| IITD | ResNet-18 | E1-A | native_robust_contrast | -0.2401 | -0.3595 | -0.1045 | 32 |
| IITD | ResNet-18 | E1-A | polar_gradient_mean | -0.2236 | -0.3262 | -0.0612 | 32 |
| IITD | ResNet-18 | E1-A | pupil_iris_radius_ratio | -0.2231 | -0.4633 | -0.0693 | 32 |
| IITD | ResNet-18 | E1-A | removed_fraction | 0.1719 | 0.1177 | 0.2115 | 32 |
| IITD | ResNet-18 | E1-C1 | iris_supported_arc_degrees | -0.0276 | -0.1503 | 0.0623 | 32 |
| IITD | ResNet-18 | E1-C1 | native_robust_contrast | -0.0878 | -0.1195 | -0.0612 | 32 |
| IITD | ResNet-18 | E1-C1 | polar_gradient_mean | -0.1926 | -0.243 | -0.1074 | 32 |
| IITD | ResNet-18 | E1-C1 | pupil_iris_radius_ratio | -0.2468 | -0.3497 | -0.1789 | 32 |
| IITD | ResNet-18 | E1-C1 | removed_fraction | -0.0382 | -0.2108 | 0.1096 | 32 |
| IITD | ResNet-18 | E1-C2 | iris_supported_arc_degrees | 0.0747 | -0.092 | 0.2705 | 32 |
| IITD | ResNet-18 | E1-C2 | native_robust_contrast | 0.0003 | -0.1807 | 0.1707 | 32 |
| IITD | ResNet-18 | E1-C2 | polar_gradient_mean | 0.0114 | -0.1584 | 0.1015 | 32 |
| IITD | ResNet-18 | E1-C2 | pupil_iris_radius_ratio | -0.2214 | -0.4197 | -0.0931 | 32 |
| IITD | ResNet-18 | E1-C2 | removed_fraction | -0.1327 | -0.2496 | -0.0246 | 32 |
| IITD | SwinV2-Tiny | E1-A | iris_supported_arc_degrees | -0.178 | -0.3798 | 0.0704 | 32 |
| IITD | SwinV2-Tiny | E1-A | native_robust_contrast | 0.146 | 0.0002 | 0.2662 | 32 |
| IITD | SwinV2-Tiny | E1-A | polar_gradient_mean | 0.0897 | 0.0301 | 0.1851 | 32 |
| IITD | SwinV2-Tiny | E1-A | pupil_iris_radius_ratio | -0.0485 | -0.1089 | 0.0312 | 32 |
| IITD | SwinV2-Tiny | E1-A | removed_fraction | -0.1724 | -0.3328 | 0.0205 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | iris_supported_arc_degrees | -0.0467 | -0.1488 | 0.0579 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | native_robust_contrast | 0.108 | 0.0275 | 0.2557 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | polar_gradient_mean | 0.0484 | -0.0495 | 0.2174 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | pupil_iris_radius_ratio | 0.1489 | 0.0685 | 0.2511 | 32 |
| IITD | SwinV2-Tiny | E1-C1 | removed_fraction | -0.0336 | -0.1217 | 0.0235 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | iris_supported_arc_degrees | -0.1307 | -0.2339 | 0.0062 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | native_robust_contrast | 0.0752 | -0.129 | 0.266 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | polar_gradient_mean | 0.0384 | -0.2482 | 0.1943 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | pupil_iris_radius_ratio | -0.0762 | -0.114 | -0.0165 | 32 |
| IITD | SwinV2-Tiny | E1-C2 | removed_fraction | -0.0415 | -0.1902 | 0.077 | 32 |


# AMF: E2-B quality/masking

Unique source captures: 524

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | pupil_iris_radius_ratio | 523 | 1 | 0.309718 | 0.400587 | 0.479097 |
| AMF | relative_fitted_annulus_area | 523 | 1 | 0.770466 | 0.83953 | 0.904075 |
| AMF | center_displacement_iris_radii | 523 | 1 | 0.017827 | 0.04071 | 0.061702 |
| AMF | relative_segmented_annulus_area | 524 | 0 | 0.745237 | 0.828198 | 0.896339 |
| AMF | iris_native_frame_fraction | 524 | 0 | 0.149568 | 0.175202 | 0.197973 |
| AMF | mask_equivalent_pupil_iris_ratio | 524 | 0 | 0.321964 | 0.414491 | 0.50474 |
| AMF | native_robust_contrast | 524 | 0 | 0.098039 | 0.121569 | 0.156863 |
| AMF | native_median_intensity | 524 | 0 | 0.301961 | 0.352941 | 0.411765 |
| AMF | bright_proxy_fraction | 524 | 0 | 0.0 | 0.000564 | 0.002348 |
| AMF | polar_local_contrast | 523 | 1 | 0.009307 | 0.011096 | 0.014104 |
| AMF | polar_gradient_mean | 523 | 1 | 0.008436 | 0.010425 | 0.012976 |
| AMF | polar_gradient_p90 | 523 | 1 | 0.014946 | 0.018769 | 0.023678 |
| AMF | polar_laplacian_variance | 523 | 1 | 0.005101 | 0.008483 | 0.015198 |
| AMF | iris_inlier_fraction | 523 | 1 | 0.636364 | 0.802817 | 0.988786 |
| AMF | iris_supported_arc_degrees | 523 | 1 | 231.510791 | 268.574376 | 342.39862 |
| AMF | iris_relative_residual | 523 | 1 | 0.003664 | 0.007 | 0.012456 |
| AMF | pupil_inlier_fraction | 523 | 1 | 1.0 | 1.0 | 1.0 |
| AMF | pupil_supported_arc_degrees | 523 | 1 | 335.127861 | 340.228471 | 344.06015 |
| AMF | pupil_relative_residual | 523 | 1 | 0.002548 | 0.004578 | 0.007894 |
| AMF | c1_valid_fraction | 523 | 1 | 0.801843 | 0.92392 | 0.97688 |
| AMF | removed_fraction | 523 | 1 | 0.0 | 0.015556 | 0.101039 |
| AMF | removed_high_gradient_fraction | 523 | 1 | 0.0 | 0.03458 | 0.18725 |
| AMF | high_gradient_fraction_of_removed | 453 | 71 | 0.372187 | 0.650633 | 0.87328 |

Acquisition/QC strata:

| dataset | native_dimensions | folder_filename_conflict | images | polar_successes | removed_fraction_mean | gradient_mean | native_contrast_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | 640x480 | False | 524 | 523 | 0.033029 | 0.010566 | 0.126405 |

Existing warning/failure counts:

| dataset | type | reason | images |
| --- | --- | --- | --- |
| AMF | polar_failure | iris_boundary_outside_fit | 1 |

Fixed subject-level association panel, rho across subjects and range across3 seeds:

| dataset | architecture | condition | feature | rho_mean | rho_min | rho_max | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | E1-A | iris_supported_arc_degrees | -0.105 | -0.1304 | -0.0827 | 54 |
| AMF | ResNet-18 | E1-A | native_robust_contrast | -0.1726 | -0.2488 | -0.0433 | 54 |
| AMF | ResNet-18 | E1-A | polar_gradient_mean | -0.1329 | -0.2062 | -0.0416 | 54 |
| AMF | ResNet-18 | E1-A | pupil_iris_radius_ratio | 0.0469 | -0.0046 | 0.0914 | 54 |
| AMF | ResNet-18 | E1-A | removed_fraction | -0.2798 | -0.3435 | -0.2403 | 54 |
| AMF | ResNet-18 | E1-C1 | iris_supported_arc_degrees | -0.0543 | -0.1136 | 0.0231 | 54 |
| AMF | ResNet-18 | E1-C1 | native_robust_contrast | -0.105 | -0.1792 | 0.0374 | 54 |
| AMF | ResNet-18 | E1-C1 | polar_gradient_mean | -0.0372 | -0.1476 | 0.0442 | 54 |
| AMF | ResNet-18 | E1-C1 | pupil_iris_radius_ratio | 0.082 | 0.0507 | 0.1098 | 54 |
| AMF | ResNet-18 | E1-C1 | removed_fraction | 0.0253 | 0.0018 | 0.0704 | 54 |
| AMF | ResNet-18 | E1-C2 | iris_supported_arc_degrees | 0.0617 | 0.014 | 0.0925 | 54 |
| AMF | ResNet-18 | E1-C2 | native_robust_contrast | -0.2084 | -0.3394 | -0.1355 | 54 |
| AMF | ResNet-18 | E1-C2 | polar_gradient_mean | -0.3134 | -0.4752 | -0.2002 | 54 |
| AMF | ResNet-18 | E1-C2 | pupil_iris_radius_ratio | -0.0807 | -0.2117 | -0.0132 | 54 |
| AMF | ResNet-18 | E1-C2 | removed_fraction | -0.0159 | -0.1267 | 0.0651 | 54 |
| AMF | SwinV2-Tiny | E1-A | iris_supported_arc_degrees | 0.0092 | -0.1915 | 0.1703 | 54 |
| AMF | SwinV2-Tiny | E1-A | native_robust_contrast | -0.154 | -0.2697 | -0.0346 | 54 |
| AMF | SwinV2-Tiny | E1-A | polar_gradient_mean | -0.1551 | -0.2622 | -0.0933 | 54 |
| AMF | SwinV2-Tiny | E1-A | pupil_iris_radius_ratio | 0.0773 | -0.1094 | 0.303 | 54 |
| AMF | SwinV2-Tiny | E1-A | removed_fraction | -0.1397 | -0.201 | -0.0587 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | iris_supported_arc_degrees | -0.1611 | -0.2226 | -0.0839 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | native_robust_contrast | -0.1053 | -0.2424 | 0.013 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | polar_gradient_mean | -0.0133 | -0.1273 | 0.0953 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | pupil_iris_radius_ratio | 0.0189 | -0.0106 | 0.0409 | 54 |
| AMF | SwinV2-Tiny | E1-C1 | removed_fraction | 0.2411 | 0.2048 | 0.2957 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | iris_supported_arc_degrees | -0.1099 | -0.2104 | -0.0125 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | native_robust_contrast | -0.0555 | -0.1652 | 0.0642 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | polar_gradient_mean | -0.0166 | -0.062 | 0.0199 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | pupil_iris_radius_ratio | -0.0145 | -0.0493 | 0.0347 | 54 |
| AMF | SwinV2-Tiny | E1-C2 | removed_fraction | 0.15 | 0.0303 | 0.2566 | 54 |


# UTIRIS_NIR: E2-B quality/masking

Unique source captures: 793

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | pupil_iris_radius_ratio | 770 | 23 | 0.335761 | 0.418023 | 0.508717 |
| UTIRIS_NIR | relative_fitted_annulus_area | 770 | 23 | 0.741207 | 0.825257 | 0.887264 |
| UTIRIS_NIR | center_displacement_iris_radii | 770 | 23 | 0.015103 | 0.035717 | 0.06155 |
| UTIRIS_NIR | relative_segmented_annulus_area | 792 | 1 | 0.707747 | 0.800035 | 0.87284 |
| UTIRIS_NIR | iris_native_frame_fraction | 793 | 0 | 0.219766 | 0.269486 | 0.304658 |
| UTIRIS_NIR | mask_equivalent_pupil_iris_ratio | 792 | 1 | 0.356594 | 0.447174 | 0.540625 |
| UTIRIS_NIR | native_robust_contrast | 792 | 1 | 0.117647 | 0.168627 | 0.231373 |
| UTIRIS_NIR | native_median_intensity | 792 | 1 | 0.309804 | 0.376471 | 0.458431 |
| UTIRIS_NIR | bright_proxy_fraction | 792 | 1 | 0.0 | 0.0 | 0.0 |
| UTIRIS_NIR | polar_local_contrast | 770 | 23 | 0.005923 | 0.007153 | 0.009344 |
| UTIRIS_NIR | polar_gradient_mean | 770 | 23 | 0.005959 | 0.007399 | 0.009948 |
| UTIRIS_NIR | polar_gradient_p90 | 770 | 23 | 0.010762 | 0.013335 | 0.018424 |
| UTIRIS_NIR | polar_laplacian_variance | 770 | 23 | 0.001434 | 0.002504 | 0.005366 |
| UTIRIS_NIR | iris_inlier_fraction | 770 | 23 | 0.698925 | 0.810326 | 0.895437 |
| UTIRIS_NIR | iris_supported_arc_degrees | 770 | 23 | 216.459294 | 247.535585 | 284.916636 |
| UTIRIS_NIR | iris_relative_residual | 770 | 23 | 0.003449 | 0.005993 | 0.010901 |
| UTIRIS_NIR | pupil_inlier_fraction | 770 | 23 | 0.948276 | 1.0 | 1.0 |
| UTIRIS_NIR | pupil_supported_arc_degrees | 770 | 23 | 326.228831 | 339.163403 | 344.848162 |
| UTIRIS_NIR | pupil_relative_residual | 770 | 23 | 0.002138 | 0.003865 | 0.00711 |
| UTIRIS_NIR | c1_valid_fraction | 770 | 23 | 0.748788 | 0.877197 | 0.955704 |
| UTIRIS_NIR | removed_fraction | 770 | 23 | 0.003857 | 0.059564 | 0.189571 |
| UTIRIS_NIR | removed_high_gradient_fraction | 770 | 23 | 0.002264 | 0.048094 | 0.187815 |
| UTIRIS_NIR | high_gradient_fraction_of_removed | 734 | 59 | 0.127668 | 0.249716 | 0.436171 |

Acquisition/QC strata:

| dataset | native_dimensions | folder_filename_conflict | images | polar_successes | removed_fraction_mean | gradient_mean | native_contrast_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | 1000x776 | False | 612 | 594 | 0.08695 | 0.007526 | 0.17133 |
| UTIRIS_NIR | 1000x776 | True | 11 | 10 | 0.072519 | 0.008703 | 0.221034 |
| UTIRIS_NIR | 960x752 | False | 166 | 162 | 0.066174 | 0.008313 | 0.176851 |
| UTIRIS_NIR | 960x752 | True | 4 | 4 | 0.004425 | 0.009358 | 0.126471 |

Existing warning/failure counts:

| dataset | type | reason | images |
| --- | --- | --- | --- |
| UTIRIS_NIR | existing_qc | empty_annulus_mask | 1 |
| UTIRIS_NIR | existing_qc | empty_iris_mask | 1 |
| UTIRIS_NIR | existing_qc | empty_pupil_mask | 1 |
| UTIRIS_NIR | existing_qc | empty_visible_iris_mask | 1 |
| UTIRIS_NIR | existing_qc | filename_eye_disagrees_with_authoritative_folder | 15 |
| UTIRIS_NIR | polar_failure | empty_iris_mask | 1 |
| UTIRIS_NIR | polar_failure | insufficient_iris_angular_support | 12 |
| UTIRIS_NIR | polar_failure | pupil_boundary_outside_fit | 5 |
| UTIRIS_NIR | polar_failure | weak_iris_curved_support | 2 |
| UTIRIS_NIR | polar_failure | weak_pupil_curved_support | 3 |

Fixed subject-level association panel, rho across subjects and range across3 seeds:

| dataset | architecture | condition | feature | rho_mean | rho_min | rho_max | subjects |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | E1-A | iris_supported_arc_degrees | -0.1052 | -0.1614 | -0.0248 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-A | native_robust_contrast | 0.0278 | -0.0521 | 0.141 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-A | polar_gradient_mean | 0.113 | -0.0376 | 0.2207 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-A | pupil_iris_radius_ratio | -0.1455 | -0.221 | -0.0337 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-A | removed_fraction | -0.1578 | -0.2046 | -0.1116 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | iris_supported_arc_degrees | -0.0107 | -0.1073 | 0.0759 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | native_robust_contrast | -0.0142 | -0.107 | 0.0622 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | polar_gradient_mean | 0.3232 | 0.1736 | 0.4146 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | pupil_iris_radius_ratio | 0.0764 | 0.032 | 0.1023 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C1 | removed_fraction | -0.1776 | -0.242 | -0.1414 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | iris_supported_arc_degrees | 0.0815 | 0.005 | 0.1949 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | native_robust_contrast | 0.0472 | -0.011 | 0.1218 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | polar_gradient_mean | 0.2642 | 0.2287 | 0.3208 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | pupil_iris_radius_ratio | 0.1242 | 0.0797 | 0.1635 | 79 |
| UTIRIS_NIR | ResNet-18 | E1-C2 | removed_fraction | -0.2827 | -0.3297 | -0.2139 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | iris_supported_arc_degrees | -0.1509 | -0.216 | -0.0209 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | native_robust_contrast | 0.1302 | 0.0786 | 0.2034 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | polar_gradient_mean | 0.0975 | 0.0143 | 0.1543 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | pupil_iris_radius_ratio | -0.1893 | -0.2728 | -0.0813 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-A | removed_fraction | -0.013 | -0.0486 | 0.055 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | iris_supported_arc_degrees | 0.0252 | -0.1159 | 0.1158 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | native_robust_contrast | 0.1427 | 0.0436 | 0.2059 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | polar_gradient_mean | 0.3802 | 0.354 | 0.4168 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | pupil_iris_radius_ratio | 0.0606 | 0.0006 | 0.0911 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C1 | removed_fraction | -0.1324 | -0.2109 | -0.0583 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | iris_supported_arc_degrees | 0.0708 | 0.0194 | 0.1019 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | native_robust_contrast | 0.1383 | 0.1152 | 0.1827 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | polar_gradient_mean | 0.4638 | 0.4042 | 0.5443 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | pupil_iris_radius_ratio | -0.0203 | -0.086 | 0.0767 | 79 |
| UTIRIS_NIR | SwinV2-Tiny | E1-C2 | removed_fraction | -0.1819 | -0.2988 | -0.1013 | 79 |