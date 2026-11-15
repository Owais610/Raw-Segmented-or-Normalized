# Saved results

| File | Use |
| --- | --- |
| [contrast_summary.csv](contrast_summary.csv) | Saved completed-study table / diagnostic |
| [coverage.csv](coverage.csv) | Saved completed-study table / diagnostic |
| [DETAILED_REPORT.md](DETAILED_REPORT.md) | Saved completed-study table / diagnostic |
| [Figures](Figures) | Statistical figures |
| [individual_metrics.csv](individual_metrics.csv) | Saved completed-study table / diagnostic |
| [leave_one_subject_out_contrasts.csv](leave_one_subject_out_contrasts.csv) | Saved completed-study table / diagnostic |
| [leave_one_subject_out_metrics.csv](leave_one_subject_out_metrics.csv) | Saved completed-study table / diagnostic |
| [paired_seed_contrasts.csv](paired_seed_contrasts.csv) | Saved completed-study table / diagnostic |
| [README.md](README.md) | Saved completed-study table / diagnostic |
| [subject_influence_summary.csv](subject_influence_summary.csv) | Saved completed-study table / diagnostic |
| [three_seed_summary.csv](three_seed_summary.csv) | Saved completed-study table / diagnostic |

CSV summaries can be read directly on GitHub. Larger observation tables use Parquet to avoid duplicate CSV/Parquet copies; load with `pandas.read_parquet`.
Every retained scientific value comes from the original completed analysis. Old workspace/provenance columns are omitted. E2-B recognition tables retain only the common matched population; its native quality/coverage measurements still show unavailable cases.
Figures contain statistical summaries only. Restricted biometric contact sheets, galleries, learned weights and raw embeddings are external assets.
