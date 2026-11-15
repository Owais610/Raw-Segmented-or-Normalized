# Saved results

| File | Use |
| --- | --- |
| [acquisition_warning_strata.csv](acquisition_warning_strata.csv) | Saved completed-study table / diagnostic |
| [DETAILED_REPORT.md](DETAILED_REPORT.md) | Saved completed-study table / diagnostic |
| [example_selection.csv](example_selection.csv) | Saved completed-study table / diagnostic |
| [failure_and_warning_counts.csv](failure_and_warning_counts.csv) | Saved completed-study table / diagnostic |
| [failure_and_warning_records.csv](failure_and_warning_records.csv) | Saved completed-study table / diagnostic |
| [feature_quantiles.csv](feature_quantiles.csv) | Saved completed-study table / diagnostic |
| [Figures](Figures) | Statistical figures |
| [image_associations.parquet](image_associations.parquet) | Compact per-observation audit table |
| [image_quality_features.parquet](image_quality_features.parquet) | Compact per-observation audit table |
| [mask_location_bins.parquet](mask_location_bins.parquet) | Compact per-observation audit table |
| [mask_location_summary.csv](mask_location_summary.csv) | Saved completed-study table / diagnostic |
| [per_image_recognition_outcomes.parquet](per_image_recognition_outcomes.parquet) | Compact per-observation audit table |
| [prespecified_subject_association_panel.csv](prespecified_subject_association_panel.csv) | Saved completed-study table / diagnostic |
| [README.md](README.md) | Saved completed-study table / diagnostic |
| [subject_associations.parquet](subject_associations.parquet) | Compact per-observation audit table |
| [subject_quality_and_outcomes.parquet](subject_quality_and_outcomes.parquet) | Compact per-observation audit table |
| [subject_quality_features.csv](subject_quality_features.csv) | Saved completed-study table / diagnostic |
| [trained_model_c2_minus_c1_per_image.parquet](trained_model_c2_minus_c1_per_image.parquet) | Compact per-observation audit table |
| [trained_model_delta_subject_associations.csv](trained_model_delta_subject_associations.csv) | Saved completed-study table / diagnostic |

CSV summaries can be read directly on GitHub. Larger observation tables use Parquet to avoid duplicate CSV/Parquet copies; load with `pandas.read_parquet`.
Every retained scientific value comes from the original completed analysis. Old workspace/provenance columns are omitted. E2-B recognition tables retain only the common matched population; its native quality/coverage measurements still show unavailable cases.
Figures contain statistical summaries only. Restricted biometric contact sheets, galleries, learned weights and raw embeddings are external assets.
