# E3 validation and publication checks

Completed on 21 November 2026 with Python 3.11 and the pinned project environment. This records performed checks; packaging did not retrain models or run new recognition inference.

## Completed experimental audit

The original completed [evaluation audit](Results/EVALUATION_VERIFICATION.json) verifies:

- All twelve validation-selected best checkpoints, their hashes and selected validation scores. All 919 training-history epochs were replayed through the original early-stopping rule. Selection and completed epochs agree; original E1/E2 records remain intact.
- All **60** E3 checkpoint–dataset evaluations, **240** seed metric values and **29,076** matched image embeddings. Membership/order, embedding normalization and frozen pair counts agree.
- **720** E1/E2/E3 comparison metric values and **3,000** summary values. Maximum summary discrepancy is 1.11e-16; seed metrics agree exactly. Means and sample SD use all three seeds.
- **Zero** train/validation subject or iris overlap with internal test members. The same E2-A matched images and exhaustive pairs are used by E1, E2-G and E3. Datasets remain independent.
- **258** sealed output files and all twelve best-checkpoint identities. The original audit hashes are retained in [source provenance](SOURCE_PROVENANCE.json).

[Original preflight](PREFLIGHT.json) passed four real-cache B24 optimizer smoke steps and complete validation-loader checks, one per architecture/support condition. Gradients were finite, no update was skipped, and peak allocated training VRAM was approximately **0.694 GiB for ResNet-18** and **6.051 GiB for SwinV2-Tiny**. The 6,527 train/validation support pairs satisfy B2⊆B1. No grayscale decoder or test-image access occurred during training preparation.

## Publication implementation

The four standalone E3 training notebooks copy the existing verified E1 publication definitions. The mask-only dataset and approved augmentation switch are the input adaptations. Function-level AST comparisons confirm all retained scientific model, sampler, objective, optimizer, epoch, validation and checkpoint definitions are identical to E1. The evaluation notebook reuses E2-G's exact binary conversion, dataset, membership/pair assertions, inference precision/batch order, cosine scoring, metrics and seed-summary functions.

Six CPU-only unit tests pass, including all twelve configuration subcases, exact E2-G tensor equality, rejection of nonbinary masks, removal of grayscale paths from dataset records, train/test boundary checks, scientific-code comparisons, imports at the top and opt-in execution switches. A complete 60-cell synthetic saved-embedding evaluation exercises the orchestration, exhaustive-pair assertions and metric writing without GPU/model/image access. These synthetic outputs are temporary software fixtures, not experimental results.

All **five notebooks execute successfully in separate fresh kernels** in default inspection mode. Definitions, software checks and saved-record loading run; training, real-cache access and new recognition inference remain disabled. Published outputs are cleared. The original twelve history JSONL and curve PNG pairs are byte-identical copies.

## Numerical tables

The portable [table builder](Manuscript%20Tables/build_tables.py) independently checks **720** metric values against the public E1/E2-G/E3 seed records and recomputes **1,200** summary fields. Seed values agree exactly; maximum summary discrepancy is 1.11e-16. Both 12-row tables retain all five datasets, both supports, both architectures and all three regimes. EER/TAR are displayed as percentages to two decimals. The original IEEEtran PDF fits both tables on one two-column page and was visually inspected; its 120 displayed cells and architecture-bold decisions were checked against the numerical support.

## Limits and preservation

This publication update executes only bounded CPU checks, notebook inspection and numerical replay from saved records. It does not repeat the twelve full training runs, the original GPU preflight, or the complete frozen-checkpoint inference grid. The experimental audit and preflight describe their original execution. Checkpoints, image/mask caches and large embeddings are external assets, not Git uploads. Frozen splits, exclusions, validation pairs, the E1 checkpoint index and every existing E1/E2 result file are preserved.
