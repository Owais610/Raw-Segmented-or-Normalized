# Matched evaluation method

Use the original frozen test subjects for CUST-Iris, CASIA-Interval and IITD and the approved unique-source inventories for AMF and UTIRIS NIR. Within each dataset, intersect availability across A/B1/B2/C1/C2 and retain the published exact memberships and pair tables.

Genuine comparisons are distinct captures of the same physical eye. Primary impostors are different subjects within the same dataset. Opposite eyes of one subject remain diagnostic only. Self/identical-source comparisons are excluded. No scores or images are merged between datasets.

Reuse the saved full-population float32 embedding arrays, retain their original inference order, and calculate the original float32 cosine scores on the matched pairs. Optional fresh inference must reproduce the original full order and batch size before matching. Every validation-selected checkpoint and all seeds 42/123/2025 are retained.

Metrics use the complete ROC with tied scores moving together: EER linearly interpolates the crossing of FNR−FPR; ROC-AUC is trapezoidal; TAR@1% and @0.1% FAR preserves vertical ROC jumps during interpolation. These are ROC summaries, not selected test operating thresholds.

Report individual seeds and mean ± sample SD, ddof=1. Architecture contrasts are Swin−ResNet for the same numerical seed. C2−C1 contrasts compare independently trained models; raw-to-polar interaction contrasts subtract the architecture effects. Leave-one-subject-out sensitivity removes every incident pair before recomputing metrics, without treating pairs as independent samples.

These comparisons were developed after the initial architecture–representation results. Common eligibility controls capture coverage for the observed cohort, not every acquisition or optimization confound. No causal or significance claim follows from a descriptive seed/subject pattern.
