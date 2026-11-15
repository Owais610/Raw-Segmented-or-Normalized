# E2-F final interpretation: last planned explanatory experiment

**explanatory attribution evidence, not a causal explanation.** This analysis used only frozen raw-trained checkpoints, identical pair subsets across architectures/seeds, and the complete pair-cosine target. E2-D/E2-E interventions remain preserved independent evidence.

## 1. Do architectures differ in iris/noniris attribution?

The proposed universal ResNet-greater-nonannulus pattern is not established across all primary domains/categories/seeds. Among the10 domain/category means, 0 favor greater ResNet mass and 10 greater Swin mass; every cell and seed is reported below.

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

The primary contrast is normalized positive mass outside the annulus; pupil and outside-disc fractions plus area-adjusted densities are reported separately. A larger region can contain more mass without greater per-pixel concentration. These distributions are not directly comparable raw Grad-CAM intensities or exact learned information.

## 2. Are patterns consistent across datasets and seeds?

Use the explicit seed42/123/2025 differences and direction counts above. Genuine/ordinary categories are separate primary descriptive samples; high-similarity impostors are outcome-conditioned exploratory samples. No cross-domain average or independent-pair confidence interval is used. Any zero/failing map changes conditional valid coverage and remains disclosed.

## 3. What do the sanity checks establish?

Original parameter files/model state are unchanged, randomization covers all selected tensors, and gradients/scores/layouts have explicit numerical audits. Parameter randomization and partner sensitivity are graded spatial-response diagnostics, not binary validation from a correlation cutoff. Their complete ranges, zero cases and apparently invariant comparisons are in E2_F_SANITY_CHECKS.md. Numerical correctness alone does not make a heatmap a faithful identity explanation.

| dataset | architecture | level | valid_comparisons | pearson_mean_across_seeds | cosine_mean_across_seeds | total_variation_mean_across_seeds | randomized_zero_maps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | full | 36 | -0.05961 | 0.315275 | 0.69009 | 0 |
| AMF | ResNet-18 | late_and_projection | 36 | 0.091939 | 0.421443 | 0.60019 | 0 |
| AMF | ResNet-18 | projection | 36 | 0.53199 | 0.699126 | 0.421336 | 0 |
| AMF | SwinV2-Tiny | full | 36 | -0.065548 | 0.292263 | 0.726298 | 0 |
| AMF | SwinV2-Tiny | late_and_projection | 36 | 0.069383 | 0.381143 | 0.651537 | 0 |
| AMF | SwinV2-Tiny | projection | 36 | 0.674228 | 0.785463 | 0.338813 | 0 |
| CASIA-Interval | ResNet-18 | full | 36 | -0.02762 | 0.312585 | 0.697884 | 0 |
| CASIA-Interval | ResNet-18 | late_and_projection | 36 | 0.119548 | 0.41268 | 0.616334 | 0 |
| CASIA-Interval | ResNet-18 | projection | 36 | 0.522382 | 0.673804 | 0.436082 | 0 |
| CASIA-Interval | SwinV2-Tiny | full | 36 | -0.045105 | 0.282489 | 0.733407 | 0 |
| CASIA-Interval | SwinV2-Tiny | late_and_projection | 36 | 0.037947 | 0.351767 | 0.672786 | 0 |
| CASIA-Interval | SwinV2-Tiny | projection | 36 | 0.749103 | 0.825158 | 0.299597 | 0 |
| CUST-Iris | ResNet-18 | full | 36 | 0.018251 | 0.360835 | 0.667768 | 0 |
| CUST-Iris | ResNet-18 | late_and_projection | 36 | 0.063584 | 0.429448 | 0.597956 | 0 |
| CUST-Iris | ResNet-18 | projection | 36 | 0.413592 | 0.626218 | 0.468515 | 0 |
| CUST-Iris | SwinV2-Tiny | full | 36 | -0.056095 | 0.286575 | 0.723834 | 0 |
| CUST-Iris | SwinV2-Tiny | late_and_projection | 36 | 0.113539 | 0.416367 | 0.626623 | 0 |
| CUST-Iris | SwinV2-Tiny | projection | 36 | 0.658929 | 0.76344 | 0.366609 | 0 |
| IITD | ResNet-18 | full | 36 | 0.045202 | 0.391238 | 0.635736 | 0 |
| IITD | ResNet-18 | late_and_projection | 36 | 0.112366 | 0.44867 | 0.590764 | 0 |
| IITD | ResNet-18 | projection | 36 | 0.46556 | 0.661538 | 0.447384 | 0 |
| IITD | SwinV2-Tiny | full | 36 | -0.038568 | 0.306282 | 0.708735 | 0 |
| IITD | SwinV2-Tiny | late_and_projection | 36 | 0.07703 | 0.409939 | 0.631303 | 0 |
| IITD | SwinV2-Tiny | projection | 36 | 0.717097 | 0.810549 | 0.314713 | 0 |
| UTIRIS_NIR | ResNet-18 | full | 36 | 0.06311 | 0.363783 | 0.661023 | 0 |
| UTIRIS_NIR | ResNet-18 | late_and_projection | 36 | 0.173462 | 0.467538 | 0.582207 | 0 |
| UTIRIS_NIR | ResNet-18 | projection | 36 | 0.484522 | 0.663603 | 0.438031 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | full | 36 | -0.018013 | 0.310203 | 0.716002 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | late_and_projection | 36 | 0.137294 | 0.418691 | 0.627863 | 0 |
| UTIRIS_NIR | SwinV2-Tiny | projection | 36 | 0.763745 | 0.837296 | 0.279345 | 0 |

| dataset | architecture | anchors_across_seeds | pearson_mean_across_seeds | cosine_mean_across_seeds | total_variation_mean_across_seeds |
| --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | 9 | 0.132227 | 0.457401 | 0.580106 |
| AMF | SwinV2-Tiny | 9 | -0.025377 | 0.304489 | 0.694876 |
| CASIA-Interval | ResNet-18 | 9 | -0.013656 | 0.283779 | 0.678719 |
| CASIA-Interval | SwinV2-Tiny | 9 | 0.449289 | 0.600357 | 0.493275 |
| CUST-Iris | ResNet-18 | 9 | 0.070054 | 0.374283 | 0.635871 |
| CUST-Iris | SwinV2-Tiny | 9 | -0.061491 | 0.255934 | 0.743783 |
| IITD | ResNet-18 | 9 | 0.012477 | 0.33949 | 0.653797 |
| IITD | SwinV2-Tiny | 9 | 0.152487 | 0.435087 | 0.580178 |
| UTIRIS_NIR | ResNet-18 | 9 | 0.213298 | 0.429559 | 0.584281 |
| UTIRIS_NIR | SwinV2-Tiny | 9 | -0.003483 | 0.30418 | 0.698012 |

## 4. What conclusions are justified?

Only descriptive differences in normalized positive score-attribution location, conditional on this fixed layer/target/pair subset and its numerical support. Consistency can support compatibility with surrounding-context sensitivity, but cannot demonstrate a periocular identity shortcut. Predominantly iris-focused, inconsistent, diffuse or sanity-insensitive maps can leave the E2-D/E2-E performance effects unexplained by a simple location story. High-impostor maps promote erroneous similarity, not correct identity evidence.

## 5. What remains unresolved?

The causal information responsible for the architecture–representation interaction, the exact role of noniris/pupil/segmentation shape cues, and the faithfulness of coarse Grad-CAM as an identity mechanism remain unresolved by attribution alone. Input normalization, pooling, spatial/channel aggregation, small subject-aware samples, predicted masks and outcome-conditioned high-pair selection limit inference. No additional training, models, attribution algorithms or datasets are proposed. This completes the last planned explanatory analysis.


## Fixed-tolerance exception diagnosis

The locked FP32-versus-saved-AMP agreement check has exceptions. A separate [numerical replay report](NUMERICAL_DIAGNOSTIC_REPORT.md) records their original-batch reproduction. The tolerance and affected unsupported primary maps are unchanged; these cases are not silently reintroduced. No new CAMs or model-selection analysis was performed.


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