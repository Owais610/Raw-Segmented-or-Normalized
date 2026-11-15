# Reproducibility-package validation

Executed on **16 November 2026**, Python 3.11, the pinned package environment, NVIDIA RTX 5060 Laptop GPU (8 GB).
Scientific source: the author's [IrisCueLab implementation](https://github.com/Owais610/IrisCueLab/tree/dc1ab6d28efe78ef0447402bd00fd4e1d9b3ebc1). Its tracked files and HEAD remain unchanged.
This document reports performed checks; it does not claim that 30 new training runs or every large explanatory workload was repeated.

## Notebook execution and independence — PASS

- All **10 E1 and six E2 notebooks** are valid Jupyter notebook JSON and compile as Python.
- All **16 notebooks executed successfully in separate fresh kernels** in default inspection mode: complete definition cells, environment/software checks and actual recorded-result loading. Training and fresh full recognition analysis remained disabled.
- No project-module imports, relative Python imports, code restoration, required file-integrity gates, original-directory discovery or author-machine absolute paths remain in their code.
- Implementations are ordinary visible Python definitions. Asset paths and execution switches are at the top of each notebook. No notebook must run before another.
- Published code-cell outputs are cleared. Saved histories, metric tables and statistical figures remain directly inspectable without execution.

## Frozen training protocol and numerical functions — PASS

- All **30 seed configurations** retain the original architecture, augmentation, P/K/B, losses, optimizer, normalization, validation, epoch ceiling/minimum, tolerance and patience settings.
- Frozen primary inventory and common V2 availability were checked: raw train/validation/test **5,372 / 1,155 / 1,147**; common polar **5,320 / 1,138 / 1,130**. PK-eligible training images are **5,356 raw/Cartesian** and **5,303 polar**. C1/C2 membership is identical.
- **27 sampler batches** across all three seeds and epochs 0/1/7 match the original implementation exactly. They retain four distinct subjects per domain and two distinct captures per selected physical eye.
- Synthetic loss values match the original exactly. Self-pairs, identical sources, cross-dataset pairs and opposite eyes of one subject are excluded from both loss masks and denominators.
- Three original training images (one per internal dataset) reproduced all five representations against existing caches exactly. Native V2 geometry/sampling also matches the original implementation. No fit parameters were tuned.
- Original and notebook pretrained encoders have identical state tensors and synthetic forward outputs for both backbones and both spatial shapes. Grayscale adaptation, projection, unit normalization and Swin precision/window policies are preserved.
- Bounded real pretrained **synthetic B24 optimizer-step checks** passed, with finite backbone and projection gradients and no OOM:

| Architecture | Input | Synthetic B24 GPU peak (GiB) | Result |
| --- | --- | --- | --- |
| ResNet-18 | [1, 320, 320] | 0.694 | PASS |
| ResNet-18 | [1, 64, 512] | 0.324 | PASS |
| SwinV2-Tiny | [1, 320, 320] | 6.051 | PASS |
| SwinV2-Tiny | [1, 64, 512] | 1.801 | PASS |

These are software checks on disposable models, not experimental training runs or new research checkpoints.
The 30 original history/curve pairs were compared byte-for-byte; replaying their per-epoch stopping decisions reproduces every selected epoch and patience counter. New workflow outputs are kept separate from those records.

## Matched evaluation — PASS

- All five public common populations and strict occlusion populations pass physical-eye, subject, source, endpoint and diagnostic-pair checks. Original internal evaluation subjects remain disjoint from train/validation allocations.
- **All 150 model–dataset cells / 600 metric values** were replayed from the unchanged original full-population saved embeddings on the frozen common pairs. **Maximum absolute metric difference: 0.** No new inference or population selection was needed for this check.
- Three-seed summaries and paired architecture/representation contrasts agree with the saved tables. The main paper results use only common matched eligibility, with no pooled-domain scoring or favorable-seed selection.
- Public result curation preserves retained numerical cells. Only old workspace/provenance columns and E2-B's unmatched recognition rows are omitted. Large observation tables use Parquet instead of duplicate CSV copies. Native quality/coverage failures remain visible.

## Explanatory implementation checks — PASS

- **E2-B:** all **2,464** native evaluation records reproduced all **23 features** with **zero numerical difference**. All **29,076** spatial masking-bin rows agree.
- **E2-C:** exact validity-subset/common-texture checks are included directly, without requiring E2-B outputs. Its complete four-cell orchestration passed synthetic I/O/metric/subject-sensitivity tests.
- **E2-D:** **50** stratified real cases (25 accepted, 25 failed) reproduce original feasibility, failure reasons, placements, areas and replacement-intensity measurements; **344** attempted variant records checked. No relaxed constraint was introduced.
- **E2-E:** **25** real matched images across all five datasets reproduce all seven inputs and **175** input-statistic records, including retained-pixel equality and native interpolation-footprint measurements.
- **E2-F:** fixed pair/partner selections were reconstructed exactly for every dataset (**30 + 3 pairs per dataset**). Ten real checkpoint/pair cases across both architectures and all five datasets reproduce **20 branch maps**, native activations, gradients, embeddings and normalized maps **exactly** (maximum difference 0).
- Grad-CAM map save/load and all three parameter-randomization levels passed for both backbones. Full controls changed all **66 ResNet** or **225 Swin** parameter tensors in disposable copies, leaving original model states unchanged.
- Attribution coverage and paired summaries reproduce the original **1,770/1,800 supported primary maps** and **870/900 supported paired architecture comparisons**. Original numerical exceptions and fixed tolerances remain unchanged.
- Complete E2-A/B/C/D/E orchestration passed with explicit synthetic fixtures and synthetic scores; these outputs are not published as experimental results. Statistical-figure generation and direct asset loading were also exercised.

## Limits of this validation

No full training epoch, full 30-run retraining, hyperparameter search, test-threshold fitting or new model selection was performed. Original learned checkpoint files and frozen preprocessing caches were not modified.
The full real C/D/E intervention-inference grids, all leave-one-subject-out recomputations, all-seed Grad-CAM galleries and every numerical-replay case were not rerun end-to-end for this packaging task. Their original completed tables/reports are preserved; bounded real-cache, saved-score, source-equivalence and synthetic orchestration checks are reported above.
Optional native ONNX mask regeneration is included as visible code, but no new masks were generated or substituted. Exact reproduction uses the original frozen mask/cache bundle; its provider/runtime must be respected when regeneration is explicitly requested.
Licensed images, model weights and large embedding/map arrays remain external assets as documented in [ASSETS.md](ASSETS.md). The repository does not claim that those restricted or large assets are publicly downloadable here.

Final publication checks found no broken local links, author-machine paths or private path columns. The package includes 16 notebooks, 30 original histories and 73 statistical/history figures. Staged history/curve files and frozen allocation/exclusion records were checked byte-for-byte. `.gitattributes` preserves these records across operating systems; `.gitignore` was checked against private images, checkpoints and new output paths. The new repository's existing license is preserved.

## Imports layout — PASS

All imports, including plotting-helper imports, are now collected in the first code cell of each of the 16 notebooks. Existing effective import bindings are preserved. An AST comparison confirms that existing calculations and configurations are unchanged; the only additional function check reports a missing optional ONNX Runtime dependency before explicit native-mask generation. Cached workflows were checked without that optional dependency. All 16 notebooks executed successfully again in fresh kernels in default inspection mode, with no training or new recognition inference. Saved results, histories and protocol data are unchanged.
