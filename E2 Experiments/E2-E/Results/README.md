# Saved results

| File | Use |
| --- | --- |
| [coverage.csv](coverage.csv) | Saved completed-study table / diagnostic |
| [Dataset Reports](Dataset%20Reports) | Per-dataset reports or eligibility records |
| [DETAILED_REPORT.md](DETAILED_REPORT.md) | Saved completed-study table / diagnostic |
| [distribution_change_summary.csv](distribution_change_summary.csv) | Saved completed-study table / diagnostic |
| [distribution_changes.csv](distribution_changes.csv) | Saved completed-study table / diagnostic |
| [eer_overview.csv](eer_overview.csv) | Saved completed-study table / diagnostic |
| [Figures](Figures) | Statistical figures |
| [fill_and_lash_contrasts.csv](fill_and_lash_contrasts.csv) | Saved completed-study table / diagnostic |
| [fill_and_lash_summary.csv](fill_and_lash_summary.csv) | Saved completed-study table / diagnostic |
| [individual_metrics.csv](individual_metrics.csv) | Saved completed-study table / diagnostic |
| [input_statistic_summary.csv](input_statistic_summary.csv) | Saved completed-study table / diagnostic |
| [input_statistics.parquet](input_statistics.parquet) | Compact per-observation audit table |
| [input_verification.parquet](input_verification.parquet) | Compact per-observation audit table |
| [leave_one_subject_out_baseline_effects.csv](leave_one_subject_out_baseline_effects.csv) | Saved completed-study table / diagnostic |
| [leave_one_subject_out_metrics.csv](leave_one_subject_out_metrics.csv) | Saved completed-study table / diagnostic |
| [paired_baseline_effects.csv](paired_baseline_effects.csv) | Saved completed-study table / diagnostic |
| [paired_effect_summary.csv](paired_effect_summary.csv) | Saved completed-study table / diagnostic |
| [per_image_sensitivity.parquet](per_image_sensitivity.parquet) | Compact per-observation audit table |
| [pixel_geometry_summary.csv](pixel_geometry_summary.csv) | Saved completed-study table / diagnostic |
| [README.md](README.md) | Saved completed-study table / diagnostic |
| [score_distributions.csv](score_distributions.csv) | Saved completed-study table / diagnostic |
| [seed_subject_influence.csv](seed_subject_influence.csv) | Saved completed-study table / diagnostic |
| [subject_influence_summary.csv](subject_influence_summary.csv) | Saved completed-study table / diagnostic |
| [subject_sensitivity.csv](subject_sensitivity.csv) | Saved completed-study table / diagnostic |
| [three_seed_summary.csv](three_seed_summary.csv) | Saved completed-study table / diagnostic |

CSV summaries can be read directly on GitHub. Larger observation tables use Parquet to avoid duplicate CSV/Parquet copies; load with `pandas.read_parquet`.
Every retained scientific value comes from the original completed analysis. Old workspace/provenance columns are omitted. E2-B recognition tables retain only the common matched population; its native quality/coverage measurements still show unavailable cases.
Figures contain statistical summaries only. Restricted biometric contact sheets, galleries, learned weights and raw embeddings are external assets.
