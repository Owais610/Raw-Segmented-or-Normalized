# Saved results

| File | Use |
| --- | --- |
| [all_regional_attribution.parquet](all_regional_attribution.parquet) | Compact per-observation audit table |
| [DETAILED_REPORT.md](DETAILED_REPORT.md) | Saved completed-study table / diagnostic |
| [E2_F_FINAL_INTERPRETATION.md](E2_F_FINAL_INTERPRETATION.md) | Saved completed-study table / diagnostic |
| [E2_F_SANITY_CHECKS.md](E2_F_SANITY_CHECKS.md) | Saved completed-study table / diagnostic |
| [feature_gradient_audit.parquet](feature_gradient_audit.parquet) | Compact per-observation audit table |
| [Figures](Figures) | Statistical figures |
| [image_attribution_summary.csv](image_attribution_summary.csv) | Saved completed-study table / diagnostic |
| [model_state_checks.csv](model_state_checks.csv) | Saved completed-study table / diagnostic |
| [NUMERICAL_DIAGNOSTIC_PLAN.md](NUMERICAL_DIAGNOSTIC_PLAN.md) | Saved completed-study table / diagnostic |
| [NUMERICAL_DIAGNOSTIC_REPORT.md](NUMERICAL_DIAGNOSTIC_REPORT.md) | Saved completed-study table / diagnostic |
| [numerical_exception_diagnosis.csv](numerical_exception_diagnosis.csv) | Saved completed-study table / diagnostic |
| [numerical_replay_batches.csv](numerical_replay_batches.csv) | Saved completed-study table / diagnostic |
| [numerical_summary.csv](numerical_summary.csv) | Saved completed-study table / diagnostic |
| [paired_architecture_observations.parquet](paired_architecture_observations.parquet) | Compact per-observation audit table |
| [paired_seed_architecture_contrasts.csv](paired_seed_architecture_contrasts.csv) | Saved completed-study table / diagnostic |
| [parameter_randomization_checks.csv](parameter_randomization_checks.csv) | Saved completed-study table / diagnostic |
| [parameter_randomization_summary.csv](parameter_randomization_summary.csv) | Saved completed-study table / diagnostic |
| [partner_pair_manifest.csv](partner_pair_manifest.csv) | Saved completed-study table / diagnostic |
| [partner_sensitivity_checks.csv](partner_sensitivity_checks.csv) | Saved completed-study table / diagnostic |
| [partner_sensitivity_summary.csv](partner_sensitivity_summary.csv) | Saved completed-study table / diagnostic |
| [primary_map_coverage.csv](primary_map_coverage.csv) | Saved completed-study table / diagnostic |
| [primary_regional_attribution.parquet](primary_regional_attribution.parquet) | Compact per-observation audit table |
| [README.md](README.md) | Saved completed-study table / diagnostic |
| [seed_category_attribution_summary.csv](seed_category_attribution_summary.csv) | Saved completed-study table / diagnostic |
| [selected_pair_manifest.csv](selected_pair_manifest.csv) | Saved completed-study table / diagnostic |
| [subject_attribution_summary.csv](subject_attribution_summary.csv) | Saved completed-study table / diagnostic |
| [three_seed_architecture_summary.csv](three_seed_architecture_summary.csv) | Saved completed-study table / diagnostic |

CSV summaries can be read directly on GitHub. Larger observation tables use Parquet to avoid duplicate CSV/Parquet copies; load with `pandas.read_parquet`.
Every retained scientific value comes from the original completed analysis. Old workspace/provenance columns are omitted. E2-B recognition tables retain only the common matched population; its native quality/coverage measurements still show unavailable cases.
Figures contain statistical summaries only. Restricted biometric contact sheets, galleries, learned weights and raw embeddings are external assets.
