# E4 validation and publication checks

Publication checks completed on 26 November 2026 using Python 3.11. No new training or recognition inference was performed while publishing.

## Original completed experiment

The original [preflight](PREFLIGHT.json) checked both architectures on a real-cache B24 optimizer step and the full 1,155-image validation loader, with finite backbone/projection gradients and no skipped updates. Peak allocated training VRAM was approximately 0.694 GiB for ResNet-18 and 6.051 GiB for SwinV2-Tiny. The [historical input audit](INPUT_AUDIT.md) documents native-footprint removal, pupil-retention limits, augmentation isolation and the explicit boundary difference from E2-E.

All six independent runs completed. The [evaluation verification](Results/EVALUATION_VERIFICATION.json) checked all six selected checkpoint hashes and selected epochs; 30 model–dataset evaluations; 14,538 matched image embeddings; 31,044 genuine and 3,825,048 primary impostor scores; 120 metric values; 400 summary fields; and zero train/validation subject, iris or image overlap with internal test members. Original score replay differed by zero; maximum summary roundoff was 1.11e-16. Test/external recognition was authorized only after training finished and never selected checkpoints.

## Published implementation

- The two standalone training notebooks preserve **136 original E1 function/class definitions** across the backbones, model construction, metrics, loss masks, sampler, optimizer, RNG, training, validation and checkpoint logic. Only strict complement input binding and the separate output scope are added. Both models are fully fine-tuned and initialize from the original pretrained sources independently.
- Five CPU-only input tests pass: strict positive native footprint, exact normalized-zero fill, unchanged retained samples, discarded-texture isolation before contrast augmentation, wrong-cache-shape rejection and frozen train/validation mask-manifest joining. No biometric images or models are used by these unit tests.
- All three new notebooks execute successfully in separate fresh kernels in default inspection mode, including saved-record loading. Training, real-asset access, GPU smoke checks and new analysis remain disabled. Imports are at the top; notebook outputs are cleared for publication.
- The **complete public evaluation orchestration** was executed in saved-embedding mode on all six original checkpoints and five published matched populations. Its **120 metric values match the original frozen results exactly**. No model, GPU inference or native image was loaded in this numerical replay. Published pair-population assertions also pass.
- All six history JSONL/curve PNG pairs are byte-identical copies. All six best checkpoint hashes and selected epochs agree with the original completed plan. The 409 history epochs reproduce the original selection and stopping records.
- The [portable paper-table builder](../Manuscript%20Tables/build_tables.py) recomputes 220 logical comparison groups from 660 seed records, retaining all four metrics. All **660 displayed mean/SD cells** in Tables III–VI and S1–S2 match the **actual submitted PDF**, including the 30 E4 cells across its EER, TAR@0.1% and supplementary TAR@1% comparisons. PDF proofs compile at IEEE two-column width without LaTeX warnings.

See [PUBLICATION_VERIFICATION.json](PUBLICATION_VERIFICATION.json) for executed publication checks and [SOURCE_PROVENANCE.json](SOURCE_PROVENANCE.json) for the original implementation/plan/result hashes. The original E1/E2/E3 code, frozen memberships, exclusions, validation pairs, results and histories were preserved. Original experimental artifacts were not edited.

## Limits

Publication does not repeat 48 complete training runs or fresh recognition inference. The original six-run GPU preflight and completed evaluation audit are historical execution records, distinct from the CPU-only publication checks above. Licensed image/mask assets, learned weights and large arrays are external assets described in [ASSETS.md](../ASSETS.md).
