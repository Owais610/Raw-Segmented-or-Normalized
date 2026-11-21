# E3 matched-population results

All metrics use the original E2-A common images and exhaustive genuine/different-subject impostor pairs. Same-subject opposite-eye comparisons remain a separate diagnostic. No sampled-impostor or unmatched test results are included.

| File | Contents |
| --- | --- |
| `individual_metrics.csv` | 60 E3 checkpoint–dataset results: two architectures × two supports × three seeds × five datasets; selected epoch and checkpoint hash included |
| `three_seed_summary.csv` | 20 groups, retaining every individual seed, mean and sample SD (ddof=1) for all four metrics |
| `selected_validation_results.csv` | 36 validation-domain results from the selected epochs of the twelve completed training runs |
| `matched_population_counts.csv` | Images, subjects, iris identities and verification-pair counts per dataset |
| `Comparisons/all_conditions_individual.csv` | 180 matched records for E1 grayscale→grayscale, E2 grayscale→binary and E3 binary→binary |
| `Comparisons/all_conditions_three_seed.csv` | 60 three-seed comparison groups, all four metrics |
| `Comparisons/training_condition_differences_*.csv` | Paired numerical-seed E3−E2 and E3−E1 differences and their summaries |
| `Comparisons/swin_minus_resnet_*.csv` | Swin−ResNet architecture contrasts within each dataset, support and training/testing regime |
| `EVALUATION_VERIFICATION.json` | Original completed audit, with private artifact paths omitted |

CSV metrics are on **[0,1]**; multiply EER and TAR by 100 to express percentages. ROC-AUC remains on [0,1]. EER/TAR differences become percentage points when multiplied by 100. The [report](../REPORT.md) and [manuscript tables](../Manuscript%20Tables/e3_comparison_tables.tex) display percentages. No confidence interval or significance test is implied by paired seed differences.

The existing E1/E2 public result tables remain unchanged. The three-condition comparison uses only their B1/B2 matched rows. [Evaluation.ipynb](../Evaluation.ipynb) contains the original scoring and mask-input functions; [build_tables.py](../Manuscript%20Tables/build_tables.py) recomputes and verifies means/sample SD from all three seed records against the public canonical E1/E2/E3 results.
