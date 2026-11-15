# E2-B: Image quality and eyelash-mask footprints

Publication summary of saved findings. Complete numerical records and interpretation are in [the detailed report](Results/DETAILED_REPORT.md) and [result index](Results/README.md).

Native quality measurements include the original evaluation inventory, including geometry failures as missing measurements.
Recognition associations in this publication view use the common matched population only. Radius/center/segmentation proxies, invalid-neighbor-eroded texture measures, four radial/eight angular mask bins and minimum eight-subject Spearman rules are unchanged.
Subject summaries are descriptive; dependent captures, segmentation error and acquisition differences do not establish a mechanism.

## Fixed measurement panel

| dataset | feature | n | missing | p10 | p50 | p90 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | pupil_iris_radius_ratio | 523 | 1 | 0.309718 | 0.400587 | 0.479097 |
| AMF | native_robust_contrast | 524 | 0 | 0.098039 | 0.121569 | 0.156863 |
| AMF | polar_gradient_mean | 523 | 1 | 0.008436 | 0.010425 | 0.012976 |
| AMF | removed_fraction | 523 | 1 | 0.0 | 0.015556 | 0.101039 |
| UTIRIS_NIR | pupil_iris_radius_ratio | 770 | 23 | 0.335761 | 0.418023 | 0.508717 |
| UTIRIS_NIR | native_robust_contrast | 792 | 1 | 0.117647 | 0.168627 | 0.231373 |
| UTIRIS_NIR | polar_gradient_mean | 770 | 23 | 0.005959 | 0.007399 | 0.009948 |
| UTIRIS_NIR | removed_fraction | 770 | 23 | 0.003857 | 0.059564 | 0.189571 |
| CUST-Iris | pupil_iris_radius_ratio | 427 | 5 | 0.289225 | 0.359636 | 0.440259 |
| CUST-Iris | native_robust_contrast | 432 | 0 | 0.054902 | 0.07451 | 0.101569 |
| CUST-Iris | polar_gradient_mean | 427 | 5 | 0.00453 | 0.006274 | 0.00847 |
| CUST-Iris | removed_fraction | 427 | 5 | 0.0 | 0.004853 | 0.048527 |
| CASIA-Interval | pupil_iris_radius_ratio | 395 | 1 | 0.322417 | 0.393986 | 0.48428 |
| CASIA-Interval | native_robust_contrast | 396 | 0 | 0.113725 | 0.145098 | 0.176471 |
| CASIA-Interval | polar_gradient_mean | 395 | 1 | 0.012145 | 0.015864 | 0.020827 |
| CASIA-Interval | removed_fraction | 395 | 1 | 0.002068 | 0.082549 | 0.247712 |
| IITD | pupil_iris_radius_ratio | 308 | 11 | 0.326218 | 0.403097 | 0.480698 |
| IITD | native_robust_contrast | 319 | 0 | 0.172549 | 0.211765 | 0.283137 |
| IITD | polar_gradient_mean | 308 | 11 | 0.025173 | 0.036321 | 0.04777 |
| IITD | removed_fraction | 308 | 11 | 0.004057 | 0.049863 | 0.133196 |

All 23 features, native missing-data counts, geometry support proxies, spatial mask bins and the fixed subject-association panel remain in Results. Recognition associations use the common matched population only. Native geometry/quality coverage is reported over the original evaluation inventory, so failures are not hidden.

## Reproduce and inspect

Open [E2-B.ipynb](E2-B.ipynb); configure direct external assets and enable `RUN_ANALYSIS`. No preceding notebook is required. [METHOD.md](METHOD.md) states exact definitions and interpretation limits. New outputs never overwrite recorded results.
