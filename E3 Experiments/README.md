# E3 — Training directly on binary iris masks

Can the two architectures learn verification discrimination from segmentation geometry and masking patterns without grayscale iris texture?

**Read the [completed report](REPORT.md) or the [compact EER and TAR tables](Manuscript%20Tables/ieeetran_preview.pdf).** All twelve runs are complete. Results use all three seeds and the same five matched populations and exhaustive pairs as E2-A and E2-G. Each dataset is scored separately.

## Code and records

| Architecture | B1-binary training | B2-binary training | Completed histories |
| --- | --- | --- | --- |
| ResNet-18 | [Notebook](Training%20Codes/ResNet-18_B1-binary.ipynb) | [Notebook](Training%20Codes/ResNet-18_B2-binary.ipynb) | [Six runs](Training%20Histories/ResNet-18) |
| SwinV2-Tiny | [Notebook](Training%20Codes/SwinV2-Tiny_B1-binary.ipynb) | [Notebook](Training%20Codes/SwinV2-Tiny_B2-binary.ipynb) | [Six runs](Training%20Histories/SwinV2-Tiny) |

- [Evaluation notebook](Evaluation.ipynb): original mask-only conversion, frozen best-checkpoint loading, saved-embedding replay or explicit inference, and exhaustive-pair scoring.
- [Results](Results/README.md): all four metrics, individual seeds, mean/sample SD, validation-selected epochs and E1/E2/E3 contrasts.
- [Table generator](Manuscript%20Tables/build_tables.py): verifies the numerical sources and regenerates both manuscript tables without images or a GPU.
- [Validation report](VALIDATION.md): performed checks and their limits.

Each notebook is self-contained, with imports at the top. Default execution only defines the implementation and displays completed records. Training, image access and new inference require explicit switches. Fresh outputs belong in `reproduced_outputs/`; recorded histories and results are never overwritten.

## Exact inputs and preserved protocol

`B1-binary = iris_mask AND NOT pupil_mask`.

`B2-binary = B1-binary AND NOT predicted_eyelash_mask`.

Load the exact frozen 320×320 black/white supports already used by E2-G. White is 255, black is 0. Do not decode grayscale ocular images, introduce soft edges, invert polarity, resize again, or repair masks. Retain the whole-frame letterbox coordinates and original black padding. Convert uint8 to float32/255 and apply the frozen E1-A mean **0.48287347719744544** and SD **0.2741831329802273**.

**Approved difference:** brightness/contrast augmentation is disabled so inputs remain strictly binary. Both architectures otherwise retain E1's architecture, independent pretrained initialization, sampler, losses, optimizer, AMP policy, validation pairs and stopping settings. This augmentation difference accompanies the input change and must remain explicit in comparisons. There is no spatial augmentation.

| Setting | Value |
| --- | --- |
| Seeds | 42, 123, 2025; independent pretrained initialization |
| Input / embedding | 1×320×320 / 256-D, L2 normalized |
| Sampler | P=12, K=2, B=24; four distinct subjects per domain, two distinct captures per physical eye |
| Batches per epoch | 224 |
| Loss | Masked batch-hard triplet, margin 0.3, plus 0.5×SupCon, temperature 0.07 |
| Eligible negatives | Same dataset, different subject |
| Excluded from both losses | Self, identical source, cross-dataset, same-subject opposite eye |
| Optimizer | AdamW; lr=1e-4, weight decay=1e-4, betas=(0.9,0.999); gradient norm clip 5 |
| Precision | Original CUDA AMP/GradScaler; metric losses float32; Swin window attention float32 |
| Epoch ceiling / stopping minimum | 150 / 30 |
| Early stopping | Patience 25, improvement >1e-4; macro-validation EER selects best checkpoint |

Training retains **5,372 images**, of which **5,356 images / 1,060 iris identities** are PK eligible. The 16 CASIA singleton captures remain retained but are not sampled. Validation has **1,155 images**, with unchanged pair manifests. Dataset/subject partitions, physical-eye labels and existing exclusions remain frozen. See [dataset-wise counts](TRAIN_VALIDATION_COUNTS.csv).

The stopping minimum gates termination, not checkpoint eligibility: a selected epoch below 30 is permitted by the original rule. Best and completed epochs are reported separately.

## Comparisons and interpretation

The three recorded regimes are grayscale-segmented training/testing (E1), the same grayscale-trained checkpoint with binary input (E2-G), and independent binary training/testing (E3). Grayscale here means B1/B2 segmented inputs, rather than raw ocular E1-A. The E1 and E2 checkpoints are identical within each grayscale baseline/intervention pair; E3 uses newly trained checkpoints.

Original test subjects from CUST-Iris, CASIA-Interval and IITD, and the external AMF and UTIRIS-NIR populations, remain independent. Test/external results were computed after all twelve E3 training jobs finished. They do not select checkpoints or tune training settings. No participant scores are pooled and no best seed is chosen for reporting.

Binary masks contain boundary geometry, image-relative position/scale and masking footprints, including segmentation errors. Discrimination under this protocol does not establish what caused the original grayscale models' performance. Sample SD over three training seeds is not a participant confidence interval.

## Asset setup

Use the existing [asset schema](../ASSETS.md), `Assets/subject_splits.json`, exclusions, validation pairs and `Assets/Matched Population/`. Supply the frozen B1/B2 supports in the original metadata; training has no native-mask or grayscale fallback. No segmentation or eligibility regeneration is needed.

[Assets/e3_checkpoints.json](../Assets/e3_checkpoints.json) separately lists the twelve original E3 best epochs, checkpoint SHA-256 values and scientific configurations. Put those learned weights under `data/checkpoints/E3/<architecture>/<support>/seed_<seed>/best.pt`. The original E1 checkpoint index is unchanged. For numerical replay, place each completed E3 embedding cache at `data/e3_embeddings/<dataset>/<job_name>/embeddings.npz`; its order must equal the published matched-membership order. Weights, embeddings and biometric image/mask files are private assets and are not committed.

Training notebooks use the underlying E1-B1/E1-B2 configuration keys only to select unchanged model and pair logic; their experiment labels, input loaders and output roots are E3. Reproduced notebook checkpoints use the existing publication checkpoint format. The shipped evaluation index deliberately identifies the original completed author checkpoints; evaluating new reproductions requires a separate explicit checkpoint index.

From the repository root, run the CPU-only numerical/table checks with:

```powershell
python -B "E3 Experiments/Manuscript Tables/build_tables.py"
python -B -m unittest discover -s "E3 Experiments/Tests" -v
```

The table builder refuses an existing output directory; select a fresh `--output-root` for another replay. Compile its generated `ieeetran_preview.tex` with IEEEtran, booktabs and multirow installed. The shipped PDF is the inspected two-column preview. [Source provenance](SOURCE_PROVENANCE.json) records hashes without requiring the author's workstation paths.
