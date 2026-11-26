# E4 completed matched results

All six best checkpoints are selected only by original macro-validation EER. They produce 30 model–dataset cells on the same five E2-A populations and exhaustive pairs. No domains or seeds are pooled.

- [individual_metrics.csv](individual_metrics.csv): 30 seed records with EER, ROC-AUC, TAR@1% FAR and TAR@0.1% FAR.
- [three_seed_summary.csv](three_seed_summary.csv): mean, sample SD (ddof=1) and all three seed values.
- [paired_changes_vs_raw_A.csv](paired_changes_vs_raw_A.csv): complement-trained/tested minus original raw-A-trained/tested, paired by seed.
- [paired_changes_vs_raw_A_summary.csv](paired_changes_vs_raw_A_summary.csv): paired mean/sample SD for all four metrics.
- [selected_validation_results.csv](selected_validation_results.csv): selected epochs and validation metrics.
- [matched_population_counts.csv](matched_population_counts.csv): unchanged memberships/pair counts and strict-footprint coverage.
- [EVALUATION_VERIFICATION.json](EVALUATION_VERIFICATION.json): original completed score/embedding replay audit.

EER and TAR are stored as ratios in CSV; multiply by 100 for percentages or delta percentage points. ROC-AUC is unitless. The [report](../REPORT.md) displays EER/TAR as percentages. Saved recognition arrays and model weights are external assets.
