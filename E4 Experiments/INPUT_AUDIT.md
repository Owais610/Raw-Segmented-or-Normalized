> Historical **preparation** audit, before training and evaluation. Its no-test-access and future-tense statements refer to that preparation stage. For completed results see [REPORT.md](REPORT.md). The original private-plan hashes are preserved in [SOURCE_PROVENANCE.json](SOURCE_PROVENANCE.json).

# Complement-only training: input and implementation audit

23 November 2026. One condition, two architectures and seeds 42/123/2025. Six independent runs are authorized; this report describes checks completed before their launch.

## Located and reused implementation

| Component | Existing implementation | Reuse |
| --- | --- | --- |
| Train/validation partitions, sources and normalization | `experiment_1/resnet18_metric/e1a/inputs.py`, frozen `e1a_protocol` | Original resolver, inventory fingerprints, exclusions and validation pairs |
| Training / stopping / checkpoints | `experiment_1/resnet18_metric/e1a/training.py`, `state.py` | Same function code objects and helper objects, bound to the new input/model factories and new output directory |
| ResNet model | `experiment_1/resnet18_metric/e1_metric/model.py` | Original pretrained grayscale ResNet-18, 512→512→256 projection and unit normalization; fully fine-tuned |
| Swin model and pretrained verification | `experiment_1/swinv2_tiny_metric/swin_metric/model.py`, `pretrained.py` | Original pretrained SwinV2-Tiny, dynamic masks and FP32 attention; fully fine-tuned |
| Exact E2 complement and fill | `experiment_2_explanations/e2_e/e2e_inputs.py` | Original `intervene` normalized-zero mean-fill operation and image geometry |
| Native-to-320 transform | `export_e1_raw_320.py`; `e1a/representations.py` | Original area-resized raw image and nearest-exact B1 annulus support |
| Later evaluation and export | `experiment_2_explanations/common.py`, `scope.py`, `inference.py` | Existing matched-pair, cosine, EER/AUC/TAR and metric-artifact functions identified; no test/external evaluation is part of this queue |

Completed E1/E2/E3 source files were not edited. `PLAN.json` pins the consumed sources/configuration/protocol and input manifests. All **252** monitored completed-run artifact files retain their original size and modification time.

## Important correction approved before training

The exact E2 mask deletes nearest-neighbor annulus support after area-resizing the raw image. Its saved audit recorded interpolation-mixed retained boundary pixels. Exact E2 matching and zero retained native-annulus contribution therefore conflict. The researcher chose: **“Remove every native-annulus contribution; approve a stricter footprint mask.”**

The frozen new mask is the union of the original B1 support and every output sample with a positive native predicted-annulus contribution under the same area resize. There is no arbitrary dilation or fitted anatomy. Removed samples receive the same E2 normalized float32 value **0**, equivalent to the original training mean **0.48287347719744544** before division by the original SD **0.2741831329802273**. No mean-fill quantization is introduced.

The stricter representation is consequently **not claimed to be pixel-identical to E2**. It agrees exactly outside the approved added boundary pixels. CASIA-Interval and IITD do not require extra pixels; all their unaugmented inputs match the E2 complement exactly.

## All-image audit

| Dataset | Partition | Images | Images needing extra removal | Added pixels, min / median / max | Remaining predicted-annulus contributions |
| --- | --- | ---: | ---: | --- | ---: |
| CUST-Iris | Train | 2,016 | 2,016 | 238 / 330 / 440 | 0 |
| CUST-Iris | Validation | 432 | 432 | 260 / 332 / 420 | 0 |
| CASIA-Interval | Train | 1,847 | 0 | 0 / 0 / 0 | 0 |
| CASIA-Interval | Validation | 396 | 0 | 0 / 0 / 0 | 0 |
| IITD | Train | 1,509 | 0 | 0 / 0 / 0 | 0 |
| IITD | Validation | 327 | 0 | 0 / 0 / 0 | 0 |

All 6,527 active inputs retain their original dimensions, content geometry and unaugmented padding. Every filled output sample is exactly normalized zero; all other output samples are bit-identical to E2. Every pure predicted-pupil sample is retained. Mixed pupil/annulus boundary samples are removed when required to meet the strict rule.

One retained training capture, **`IITD:069_02_L`**, has the existing `empty_pupil` mask flag. It remains in the frozen inventory without an invented pupil or new exclusion. Anatomical pupil retention cannot be verified for that capture. There are no empty native-annulus masks. This is a segmentation-defined intervention: errors or undercoverage in original predicted masks remain a limitation; the checks do not establish perfect anatomical ground truth or prove that all retained information is periocular.

The input cache contains removal masks only; images are formed lazily from the existing standardized A cache without another resize or lossy quantization. Per-image masks, hashes, geometry, additions and flags are in `inputs/manifest.parquet`; coverage is in `inputs/AUDIT_SUMMARY.csv`; the anomalous capture is explicit in `inputs/EXISTING_MASK_ANOMALIES.csv`.

## Augmentation and previews

Original E1 photometric settings are unchanged. Removal occurs before augmentation so discarded iris intensity cannot alter the contrast mean. Fill is restored afterward so every filled sample remains constant. Validation is unaugmented. Synthetic counterfactuals changing discarded input pixels produce exactly the same augmented tensors with the same RNG state.

Three training subjects per dataset were selected by low/median/high existing eyelash-occlusion fraction, without recognition scores. The nine examples show original A, actual binary removal mask and mean-filled complement. All three contact sheets were inspected. Setting each example's entire native predicted annulus to zero or 255 and repeating the original image resize changes **zero retained output pixels**. These are input checks, not model-selection experiments. Selection and checks are in `previews/selection_and_counterfactual_checks.csv`.

## Preflight

Six synthetic unit tests passed, including exact E2 fill, native-footprint isolation, pure pupil retention, augmentation isolation, train/test access, six frozen configurations and original-loop delegation.

Both architectures passed a real-cache **B24** optimizer step and the complete **1,155-image validation loader**, with finite nonzero backbone/projection gradients, unit-normalized embeddings and no skipped update:

| Architecture | Peak training VRAM | Batch | Result |
| --- | ---: | ---: | --- |
| ResNet-18 | 0.694 GiB | 24 | PASS |
| SwinV2-Tiny | 6.051 GiB | 24 | PASS |

All six runs retain **5,372** training inventory images, **5,356 PK-eligible images / 1,060 iris IDs**, 224 batches/epoch, P=12/K=2 and four distinct subjects per domain. The 16 CASIA singleton captures remain retained and unsampled. No normalization or validation pairs were regenerated. Macro-validation EER alone selects checkpoints, with max/min epochs 150/30 and patience 25. No test/external image was preprocessed, visualized or scored in this work.

See `PREFLIGHT.json`, `PLAN.json` and `TRAIN_VALIDATION_COUNTS.csv` for exact machine-readable settings and checks. Each of the six new run directories will retain its own best/last checkpoints, resolved configuration, input provenance, complete history and curves.
