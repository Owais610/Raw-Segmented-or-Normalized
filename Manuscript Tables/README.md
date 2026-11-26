# Manuscript and supplementary tables

The main tables reproduce **Table III (EER), IV (TAR@0.1% FAR), V (paired EER changes) and VI (paired TAR@0.1% changes)**, including all E3 binary-training and E4 complement-training rows. The supplement gives absolute **TAR@1% FAR** performance first (S1), then paired changes (S2).

- [main_tables.pdf](main_tables.pdf): IEEEtran preview of Tables III–VI.
- [main_tables.tex](main_tables.tex): the four insertable table environments.
- [supplementary_tar1.pdf](supplementary_tar1.pdf): Tables S1–S2.
- [supplementary_tar1_tables.tex](supplementary_tar1_tables.tex): insertable supplementary tables.
- [all_metrics_summary.csv](all_metrics_summary.csv): all four metrics, including full ROC-AUC and TAR@1% support.
- [all_metrics_seed_values.csv](all_metrics_seed_values.csv): each baseline, after/input condition and per-seed value.
- [displayed_cells.csv](displayed_cells.csv): the exact 660 displayed mean/SD cells and bolding.
- [verification.json](verification.json): numerical sources, hashes and conventions.
- [build_tables.py](build_tables.py): portable generation from this repository's public seed records only.

Run from the repository root:

```powershell
python "Manuscript Tables/build_tables.py" --output reproduced_outputs/paper_tables
```

Compile `main_tables_preview.tex` and `supplementary_tar1.tex` in that new directory twice with `pdflatex` and an installed IEEEtran class. Packages required are `booktabs` and `multirow`. No author workspace, native images, weights, training or inference are needed. `table_templates.json` retains the submitted table structure and verified numerical reference; the generator recomputes every mean and sample SD from the seed CSVs before rendering. All seeds 42/123/2025 are retained.

## Subtraction direction

For regional occlusion, values are **iris-occluded minus periocular-occluded**, at the same area target and image-coordinate side on the separately matched feasible cohort. They are not changes from the unoccluded baseline. The section heading explicitly states **Matched Occlusions: Iris Minus Periocular**. Positive EER or negative TAR indicates greater impairment from iris occlusion.

Frozen raw/binary interventions use input-after minus original input for the same checkpoint. Polar swaps use the indicated input direction within the trained checkpoint. Binary and complement training rows compare independent trained checkpoints with their corresponding original grayscale/raw baseline, paired by seed.

Stored EER/TAR metrics and deltas are ratios; published cells are percentages or percentage points. ROC-AUC remains unitless. SD is the sample SD of the three per-seed values, including per-seed differences for deltas. It is not a participant confidence interval.
