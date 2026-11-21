# Compact E1/E2/E3 manuscript tables

`e3_comparison_tables.tex` contains two IEEEtran-compatible `table*` inserts: EER (%) and TAR at 0.1% FAR (%). Each table has twelve rows, with B1/B2, ResNet/Swin, and three train→test regimes. Bold compares architectures within the same support, regime and dataset.

`ieeetran_preview.pdf` is the one-page two-column preview. Table numbers VII/VIII apply only to the preview; the inserts follow manuscript numbering. Required packages are `booktabs` and `multirow`.

`table_values.csv` retains the 120 displayed cells, exact seed values, means/sample SD, rounding and bold decisions. `all_metrics_support.csv` preserves ROC-AUC and TAR@1% FAR as well as EER and TAR@0.1%, on the original [0,1] scale.

Run `python -B "E3 Experiments/Manuscript Tables/build_tables.py"` from the repository root to verify all sources and generate the two tables and a numerical verification report in a fresh `reproduced_outputs/E3-tables/`. No training, images or inference are required. Compile the generated preview separately with LaTeX. The code never overwrites the recorded tables.
