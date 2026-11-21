"""Compact EER/TAR tables from the completed, matched E1/E2/E3 records."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import statistics

import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO
E3 = HERE.parent
E2 = REPO / 'E2 Experiments'
OUT = REPO / 'reproduced_outputs/E3-tables'
DATASETS = ("CUST-Iris", "CASIA-Interval", "IITD", "AMF", "UTIRIS_NIR")
ARCHITECTURES = ("ResNet-18", "SwinV2-Tiny")
CONDITIONS = ("B1-binary", "B2-binary")
SEEDS = (42, 123, 2025)
SCENARIOS = (
    ("E1_gray_train_gray_test", "G", "G"),
    ("E2_gray_train_binary_test", "G", "M"),
    ("E3_binary_train_binary_test", "M", "M"),
)
METRICS = ("eer", "roc_auc", "tar_at_far_1pct", "tar_at_far_0_1pct")
KEYS = ["dataset", "architecture", "condition", "seed"]
SOURCES = {}
CHECKS = Counter()
MAX_ERROR = Counter()


def require(ok, message):
    if not bool(ok):
        raise AssertionError(message)


def sha(path):
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def track(path):
    h = sha(path)
    SOURCES[path.relative_to(WORKSPACE).as_posix()] = h
    return h


def close(a, b, category):
    error = abs(float(a) - float(b))
    require(error <= 3e-15, f"{category}: {a} vs {b}")
    CHECKS[category] += 1
    MAX_ERROR[category] = max(MAX_ERROR[category], error)


def table(stats, metric, caption, label):
    lines = [
        r"\begin{table*}[!t]", r"\centering", r"\caption{" + caption + "}",
        r"\label{" + label + "}", r"\begingroup", r"\small",
        r"\setlength{\tabcolsep}{2.5pt}", r"\renewcommand{\arraystretch}{1.08}",
        r"\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lllccccc@{}}",
        r"\toprule",
        r"& & & \multicolumn{3}{c}{Internal held-out test} & \multicolumn{2}{c}{External zero-shot} \\",
        r"\cmidrule(lr){4-6}\cmidrule(l){7-8}",
        r"Support & Architecture & Train $\to$ test & CUST-Iris & CASIA-Interval & IITD & AMF & UTIRIS-NIR \\",
        r"\midrule",
    ]
    cells = []
    for ci, condition in enumerate(CONDITIONS):
        for ai, architecture in enumerate(ARCHITECTURES):
            other_arch = ARCHITECTURES[1-ai]
            for si, (scenario, train, test) in enumerate(SCENARIOS):
                first = r"\multirow{6}{*}{" + condition[:2] + "}" if ai == 0 and si == 0 else ""
                arch_label = r"\multirow{3}{*}{" + architecture + "}" if si == 0 else ""
                direction = train + r"$\to$" + test
                values = []
                for dataset in DATASETS:
                    row = stats[(dataset, architecture, condition, scenario)]
                    other = stats[(dataset, other_arch, condition, scenario)]
                    mean, sd = row[metric + "_mean"], row[metric + "_sample_sd"]
                    better = mean <= other[metric + "_mean"] if metric == "eer" else mean >= other[metric + "_mean"]
                    a, b = f"{100*mean:.2f}", f"{100*sd:.2f}"
                    pair = a + r"\pm" + b
                    values.append(r"{\boldmath $" + pair + "$}" if better else "$" + pair + "$")
                    cells.append(dict(metric=metric, dataset=dataset, support=condition[:2], architecture=architecture,
                        train=train, test=test, mean_pct=100*mean, sample_sd_pct=100*sd,
                        display_mean=a, display_sample_sd=b, bold=better,
                        **{f"seed{s}_pct": 100*row[metric + f"_seed{s}"] for s in SEEDS}))
                lines.append(" & ".join([first, arch_label, direction, *values]) + r" \\")
            if ai == 0:
                lines.append(r"\cmidrule(lr){2-8}")
        if ci == 0:
            lines.append(r"\midrule")
    lines += [r"\bottomrule", r"\end{tabular*}", r"\par\vspace{3pt}",
        r"\begin{minipage}{\textwidth}\footnotesize",
        r"Mean $\pm$ sample SD over seeds 42, 123, and 2025. G: grayscale segmented input; M: corresponding binary support.",
        r"G$\to$M reuses the G$\to$G checkpoint; M$\to$M is separately trained with photometric augmentation disabled to preserve binary inputs.",
        r"All rows use identical matched images and exhaustive pairs within each dataset. Bold compares architectures within the same support, train$\to$test case, and dataset.",
        r"\end{minipage}", r"\endgroup", r"\end{table*}"]
    return "\n".join(lines), cells


def main():
    OUT.mkdir(parents=True,exist_ok=False)
    audit_path=E3/'Results/EVALUATION_VERIFICATION.json'
    track(audit_path)
    audit=json.loads(audit_path.read_text())
    require(audit['status']=='passed' and audit['same_images_and_pairs_as_e1_e2_matched_populations'],'Original evaluation audit')
    individual_path=E3/'Results/Comparisons/all_conditions_individual.csv'
    summary_path=E3/'Results/Comparisons/all_conditions_three_seed.csv'
    track(individual_path);track(summary_path)
    individual=pd.read_csv(individual_path,float_precision='round_trip')
    saved=pd.read_csv(summary_path,float_precision='round_trip')
    require(len(individual) == 180 and len(saved) == 60, "Expected all three regimes, two supports, two architectures, five datasets and three seeds")
    full_keys = KEYS + ["scenario"]
    require(not individual.duplicated(full_keys).any(), "Repeated seed record")
    require(set(individual[full_keys].itertuples(index=False, name=None)) == set(itertools.product(DATASETS, ARCHITECTURES, CONDITIONS, SEEDS, [s[0] for s in SCENARIOS])), "Missing/extra result combination")
    paths = {
        "E1_gray_train_gray_test": E2 / "E2-A/Results/individual_metrics.csv",
        "E2_gray_train_binary_test": E2 / "E2-G/Results/individual_metrics.csv",
        "E3_binary_train_binary_test": E3 / "Results/individual_metrics.csv",
    }
    frames = {}
    for name, path in paths.items():
        track(path)
        frame = pd.read_csv(path,float_precision='round_trip')
        if name.startswith("E2"):
            frame = frame[frame.variant.eq("binary_geometry")]
        frames[name] = frame
    for row in individual.to_dict("records"):
        frame = frames[row["scenario"]]
        condition = row["condition"] if row["scenario"].startswith("E3") else "E1-" + row["condition"][:2]
        selected = frame[frame.dataset.eq(row["dataset"]) & frame.architecture.eq(row["architecture"]) & frame.condition.eq(condition) & frame.seed.eq(row["seed"])]
        require(len(selected) == 1, "Ambiguous canonical metric source")
        require(int(selected.iloc[0].selected_epoch)==int(row['selected_epoch']), 'Selected epoch differs')
        if 'checkpoint_sha256' in selected:
            require(selected.iloc[0].checkpoint_sha256 == row['checkpoint_sha256'],'Checkpoint identity differs')
        for metric in METRICS:
            close(row[metric], selected.iloc[0][metric], "canonical_seed_metric_values")
    indexed = saved.set_index(["dataset", "architecture", "condition", "scenario"])
    stats = {}
    for key, group in individual.groupby(["dataset", "architecture", "condition", "scenario"]):
        by_seed = group.set_index("seed")
        require(set(by_seed.index) == set(SEEDS), "Three seeds required")
        row = {}
        for metric in METRICS:
            values = [float(by_seed.loc[s, metric]) for s in SEEDS]
            fields = {"mean": statistics.mean(values), "sample_sd": statistics.stdev(values),
                      **{f"seed{s}": value for s, value in zip(SEEDS, values)}}
            for suffix, value in fields.items():
                close(value, indexed.loc[key, metric + "_" + suffix], "seed_summary_values")
                row[metric + "_" + suffix] = value
        stats[key] = row
    tables, cells = [], []
    for metric, caption, label in (
        ("eer", r"Grayscale and binary-mask training/test comparison: EER (\%, lower is better).", "tab:e3-gray-mask-eer"),
        ("tar_at_far_0_1pct", r"Grayscale and binary-mask training/test comparison: TAR at 0.1\% FAR (\%, higher is better).", "tab:e3-gray-mask-tar001"),
    ):
        tex, displayed = table(stats, metric, caption, label)
        tables.append(tex)
        cells.extend(displayed)
    insert = "% Requires booktabs and multirow. G is segmented grayscale B1/B2, not raw ocular A.\n"
    insert += "% Both inserts retain ordinary manuscript numbering; preview starts at Table VII.\n\n"
    (OUT / "e3_comparison_tables.tex").write_text(insert + "\n\n".join(tables) + "\n", encoding="utf-8")
    pd.DataFrame(cells).to_csv(OUT / "table_values.csv", index=False, float_format="%.17g")
    # Full four-metric numerical support, all seeds and sample SD; original [0,1] scale.
    rows = [{"dataset": k[0], "architecture": k[1], "condition": k[2], "scenario": k[3], **v} for k,v in stats.items()]
    pd.DataFrame(rows).to_csv(OUT / "all_metrics_support.csv", index=False, float_format="%.17g")
    (OUT / "ieeetran_preview.tex").write_text(r"""\documentclass[journal,10pt]{IEEEtran}
\usepackage{booktabs,multirow}
\pagestyle{empty}
\begin{document}
\typeout{E3-TEXTWIDTH=\the\textwidth}
\setcounter{table}{6}
\input{e3_comparison_tables.tex}
\clearpage
\end{document}
""", encoding="utf-8")
    require(all(sha(WORKSPACE / p) == h for p,h in SOURCES.items()), "A source changed during publication export")
    report = dict(status="passed", seeds=list(SEEDS), sample_sd_ddof=1, checks=dict(CHECKS), maximum_absolute_differences=dict(MAX_ERROR),
        tables=2, rows_per_table=12, displayed_metric_cells=len(cells), datasets=list(DATASETS),
        source_sha256=SOURCES, support_definition="G = grayscale segmented B1/B2; M = matching binary mask",
        train_test_cases={s: a+"->"+b for s,a,b in SCENARIOS}, populations=audit["coverage"],
        no_source_or_experimental_artifacts_modified=True, no_training_or_inference=True,
        table_sha256=sha(OUT / "e3_comparison_tables.tex"))
    (OUT / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("status", "checks", "maximum_absolute_differences", "rows_per_table", "displayed_metric_cells")}, indent=2))


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-root',type=Path,default=OUT,help='Fresh directory; existing directories are refused')
    args=parser.parse_args()
    OUT=args.output_root.resolve()
    main()
