# Assets and execution

Scientific implementations are visible inside the 22 notebooks; E3 also includes a CPU-only numerical/table verification script and unit tests. Real data, pretrained weights, learned checkpoints and large saved embeddings are external assets, bound by editable paths in each notebook. Missing required assets cause explicit errors; there is no random-weight, substitute-data or relaxed-eligibility fallback.

E3 uses the existing frozen Cartesian binary-support caches and the same metadata, partitions and pair files. Its twelve independently trained checkpoints have a separate [index](Assets/e3_checkpoints.json); their expected paths and embedding-cache layout are documented in the [E3 asset instructions](E3%20Experiments/README.md#asset-setup). The original E1 index and assets are unchanged. E3 reads no ocular grayscale intensities and performs no mask regeneration.

## Dataset access

| Dataset | Access / authority |
| --- | --- |
| CUST-Iris | [Original dataset release](https://data.mendeley.com/datasets/3j6skjpsng/3); follow its stated terms. Eye 1 = left, Eye 2 = right was explicitly confirmed by the researcher. |
| CASIA-Interval | [CASIA-Iris V4](https://nlpr-sir.github.io/dataset/casia-irisv4/); request/use according to the provider's terms. CASIA-Lamp is excluded. |
| IITD | [IIT Delhi iris database](https://www4.comp.polyu.edu.hk/~csajaykr/IITD/Database_Iris.htm); obtain access from the provider. Subject 001 remains quarantined; supplied labels for 205–218 were confirmed, with QC flags retained. |
| UTIRIS NIR | [UTIRIS project](https://utiris.wordpress.com/); use the original infrared collection, not a renamed mirror. Original subject/eye folders are authoritative for the 15 folder/filename conflicts. |
| AMF | Researcher's external collection; obtain the original approved inventory and permission from the author. The reviewed filename containing both Left/Right is labelled Right. No public download URL is asserted here. |

Do not infer replacement labels from filenames. Use the existing audited metadata and exact duplicate exclusions. Biometric source images, masks, strip images, contact sheets and Grad-CAM galleries are intentionally not redistributed.

## Public protocol data

`Assets/subject_splits.json` and `image_exclusions.json` are the original frozen subject allocation and explicit exclusions. `Assets/Validation Pairs/` contains the original three validation pair tables; polar validation uses their unchanged common-availability subset.

`Assets/Matched Population/<dataset>/` contains exact common membership and genuine/impostor/opposite-eye tables. `Assets/Occlusion Population/` contains the original strict feasible E2-D membership/pairs; no placement constraints are relaxed. `Assets/Attribution Pairs/` contains the exact E2-F primary and partner selections, including all six saved raw-model scores. These are direct metadata inputs, independent of notebook execution order.

`Assets/checkpoints.json` lists the 30 original model/condition/seed combinations and validation-selected epochs. File-integrity manifests and private audit seals are not required.

## Suggested private bundle

```text
data/
  image_manifest.parquet
  evaluation_inventory.parquet
  native/                       # licensed original images
  masks/                        # native binary masks
  cartesian/                    # unchanged raw/support caches
  polar_v2/                     # C1/C2, validity, geometry, coordinates
  pretrained/
    resnet18.a1_in1k.safetensors
    swinv2_tiny_window8_256.ms_in1k.safetensors
  checkpoints/<architecture>/<E1-condition>/seed_<seed>/best.pt
  original_embeddings/<internal|AMF|UTIRIS_NIR>/<job-name>.npz
  intervention_embeddings/<E2-C|E2-D|E2-E|E2-G>/<dataset>/<job-name>/<variant>.npz
```

Actual files can be stored elsewhere; edit each notebook's paths or explicit `PATH_REMAP`. Paths inside the portable metadata may be relative to `DATA_ROOT`.
Obtain the author's completed-study cache/metadata/checkpoint bundle through permitted access. It is not downloaded silently or reconstructed from private machine directories. The repository currently provides the code, protocol metadata, histories and results, not unrestricted public access to every underlying asset.

## Metadata fields

E1 `image_manifest.parquet` is the existing frozen inventory expressed with portable paths. Required labels: `image_id`, `dataset`, string `subject_id` (retain leading zeros), `eye_side` (L/R), `iris_id` (`dataset:subject:eye`), canonical exact-source `source_id`, `split` and `quality_flags`. Include `width`, `height`; `native_path`, `raw_path`, `b1_support_path`, `b2_support_path`, `c1_path`, `c2_path`, `c1_validity_path`, `c2_validity_path`; and native `iris_mask_path`, `pupil_mask_path`, `eyelashes_mask_path` when native reconstruction is desired.

Statuses are `b1_status`, `b2_status`, `c1_status`, `c2_status`, `failure_reason`, `geometry_version='v2'` and original false fallback/obsolete-method flags. These flags reject substitutions; no unused geometry algorithms are included. Retain unavailable images in metadata instead of making blank inputs. Full retained primary inventory: 7,674 rows, plus 524 AMF and 793 UTIRIS NIR unique sources if supplied together.

E2 `evaluation_inventory.parquet` contains **evaluation-only** original test/external rows (2,464 before common-availability filtering). It uses the same labels/source IDs, plus `source_path`, `cached_path`, `b1_support_path`, `b2_support_path`, C1/C2 image/validity paths, `geometry_path`, `coordinates_path`, `eyelash_footprint_path`, `c1_status`, `c2_status`, `polar_failure_reason`, `segmentation_status`, `quality_flags` as JSON, native dimensions and `raw_geometry_json` (the original whole-frame letterbox geometry). `mask_paths` is a JSON object with native `iris`, `pupil`, `annulus`, `eyelashes`, `visible_iris` paths. External rows must retain their original zero-based `inference_order`. No train/validation image is loaded by E2.

## Exact preprocessing

Native Worldcoin masks use [iris-semantic-segmentation](https://huggingface.co/Worldcoin/iris-semantic-segmentation), independent probability channels in order eyeball/iris/pupil/eyelashes, linear probability interpolation to native dimensions, then threshold >0.5. Annulus = iris AND NOT pupil; visible iris also removes eyelashes. The notebooks load the original masks directly; supplying a newer model or refitting masks would change the experiment.

All imports are collected in the first code cell of each notebook. The segmented/polar and E2 notebooks also contain the original native-mask input preparation, probability thresholding and explicit ONNX session implementation. It is never invoked silently. Optional regeneration requires the original `iris_semseg_upp_scse_mobilenetv2.onnx` asset and original ONNX Runtime environment (`onnxruntime-gpu==1.26.0`, installed separately). The imports cell treats ONNX Runtime as optional; cached-mask workflows run without it, and explicit native-mask generation stops with an actionable error if it is unavailable. Keep original provider settings and compare regenerated outputs to the frozen masks before using any new cache.

Cartesian preprocessing is whole-frame, aspect-preserving 320×320, `INTER_AREA` image resizing, Python-rounded content dimensions, centered black padding, and `INTER_NEAREST_EXACT` binary support resizing. B1/B2 preserve these coordinates. There is no iris-centered crop or second cache resize.

Polar preprocessing is the frozen native V2 estimator and 64×512 rubber sheet defined in the C notebooks. Independent pupil/iris centers are preserved. Radial cell midpoints, clockwise angle from +x, linear grayscale remapping, original anatomical validity and active bilinear footprint checks are unchanged. The unique geometrically supported pupil-component rule is included. C2 reuses C1's exact coordinates and common samples; it removes the active eyelash footprint, with no refit, enhancement or invented geometry. Save `x`, `y` coordinates and geometry with reconstructed caches. Any failure stops that image's normalization and remains recorded as unavailable; do not silently replace the frozen eligibility manifest.

All conditions normalize by the original 5,356 PK-eligible raw-training images' frozen mean **0.48287347719744544**, SD **0.2741831329802273**. Never recompute normalization from test/external or segmented pixels.

## Weights and inference cache order

Original timm backbones are [resnet18.a1_in1k](https://huggingface.co/timm/resnet18.a1_in1k) and [swinv2_tiny_window8_256.ms_in1k](https://huggingface.co/timm/swinv2_tiny_window8_256.ms_in1k). Supply their original `model.safetensors` under the documented names, or explicitly opt into standard timm download. Each seed initializes independently; timm's grayscale adaptation sums the original RGB first-convolution weights. Swin uses the approved dynamic window masks and FP32 window attention, AMP elsewhere.

Recognition uses original validation-selected **best.pt**, never last checkpoints or newly initialized models. All states load strictly. Checkpoint files are not included due to size; their expected paths/selected epochs are public metadata.

Each embedding NPZ contains `image_ids` and float32 unit-normalized `embeddings` [N,256]. Original internal caches preserve the entire condition's frozen test inference order across all three internal datasets; external caches preserve each original manifest's order. Score matched pairs only **after** this original full-batch inference. Running inference only on the common subset can change AMP batch-kernel scores, so it is not an exact substitute for the original cache.

For E2-C/E2-D/E2-E, optional intervention embeddings are direct external assets from the completed study, not required outputs of another notebook. Their IDs/order must match the original intervention cohort. If absent, explicitly select `INTERVENTION_SOURCE='recompute'`; it uses the original checkpoint, fixed inputs, batch size 24 and AMP policy. E2-F differentiates the frozen raw encoders in FP32 and separately checks agreement with saved AMP pair scores at the unchanged tolerance.

## Installation and execution

Use Python 3.11. Install a PyTorch/torchvision CUDA build appropriate for the machine, then `python -m pip install -r requirements.txt`. Select that environment as the Jupyter kernel. No notebook installs packages or silently changes precision/device.
Open any notebook, run its imports cell, and edit the configuration cell that follows. Run subsequent cells top-to-bottom within that notebook. You need not execute any other notebook. Default switches display completed records; explicit opt-in starts the selected reproduction workload.

New outputs must be outside recorded `Training Histories` and `Results`. `.gitignore` excludes private data, model files, embedding arrays and reproduction directories. Do not commit executed biometric displays.

## E2-G binary-input assets

E2-G uses the existing B1/B2 320×320 binary support files and matched populations; no new image preprocessing asset is required. Optional completed binary embeddings use `intervention_embeddings/E2-G/<dataset>/<job-name>/binary_geometry.npz`, with `image_ids` in the exact published matched-membership order and float32 unit-normalized `embeddings` [N,256]. The private original output is `<dataset>/runs/<job-name>/binary_geometry/embeddings.npz`; copy it explicitly to the configured asset location if desired. These caches are not outputs required from another notebook. Original grayscale baselines reuse the unchanged full-population E1 embedding assets, whose inference order differs from the matched-only binary inference order. Masks, grayscale previews, checkpoints, embeddings and pair scores are not committed.


## E4 strict complement assets

E4 uses the same original 320?320 raw caches, frozen normalization and native segmentation masks. Its checkpoint index is `Assets/e4_checkpoints.json`; supply original selected weights under `checkpoints/E4/<architecture>/seed_<seed>/best.pt`. Pretrained initialization remains the E1 backbone, never an E1-trained model.

For training, supply `data/e4_train_validation_masks.parquet` with `image_id`, `split` and `removal_mask_path`, matching all 5,372 retained training and 1,155 validation rows exactly. Mask paths are resolved relative to `data/e4_masks/train_validation/`, with optional explicit PATH_REMAP. These are the original audited strict masks, not the old E2 annulus supports. They contain `B1 OR (INTER_AREA(native_annulus)>0)` in original letterbox coordinates. The input helper demonstrates the frozen construction. Test/external masks are not included in this training asset.

Evaluation uses the same `evaluation_inventory.parquet` and published common population/pairs as E2-A. Native mask paths, `raw_geometry_json`, original B1 support and raw cache are used to reproduce the same strict footprint without fitting or tuning. Optional original embeddings go under `e4_embeddings/<dataset>/<job-name>/embeddings.npz`, with `image_ids` in exact matched-membership order and float32 normalized `[N,256]` embeddings. Explicitly select saved-embedding replay or fresh inference; no automatic fallback is used. Model weights, native images, masks and large embedding arrays remain external assets.
