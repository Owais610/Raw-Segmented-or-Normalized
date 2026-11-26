# E4 — Independent complement-only training

Can each architecture learn iris-verification identities after the predicted iris annulus and every positive native-annulus interpolation contribution are removed?

This section contains the **six completed independent runs**: ResNet-18 and SwinV2-Tiny, each using seeds 42, 123 and 2025. It completes the paper's 48-run inventory alongside 30 E1 and 12 E3 runs. E4 is an internal repository identifier for the paper's **Complement Only Training** rows.

| Start here | Contents |
| --- | --- |
| [ResNet-18 training notebook](Training%20Codes/ResNet-18_Complement.ipynb) | Full original E1-A training definitions with strict complement inputs |
| [SwinV2-Tiny training notebook](Training%20Codes/SwinV2-Tiny_Complement.ipynb) | Same protocol, approved dynamic windows and FP32 window attention |
| [Evaluation notebook](Evaluation.ipynb) | Six frozen best checkpoints; five common populations; exhaustive pairs |
| [Completed results report](REPORT.md) | Absolute metrics, coverage, selected epochs and paired changes |
| [Results](Results/README.md) | All four seed-level metrics, mean/sample SD and raw-A comparisons |
| [Training histories](Training%20Histories) | Six original JSONL histories, curves, selected epochs and configurations |
| [Validation](VALIDATION.md) | Original experimental checks and publication checks |
| [Paper tables](../Manuscript%20Tables/README.md) | Portable code, full manuscript tables and TAR@1% supplement |

## Exact input and approved difference from E2-E

The removal support is `original_B1_support OR (INTER_AREA(native_annulus) > 0)`, with native annulus `iris AND NOT pupil`. It uses the original letterbox geometry. There is no new segmentation, arbitrary dilation, fit, crop, enhancement or additional raw-image resize.

Removal is the **exact frozen training mean**, represented as float32 zero **after** normalization. The mean is never rounded to an 8-bit pixel value. Pupil and other unremoved ocular samples remain; mixed boundary samples are removed when they include any predicted annulus contribution. This is a predicted-mask intervention, not an anatomical-ground-truth or pure-periocular representation.

The strict footprint was approved to prevent residual interpolated iris texture. It is **different from E2-E's original mean-filled complement boundary**. The old E2 result is preserved. Median additional removal is 332 / 0 / 0 / 194 / 451 pixels for CUST-Iris / CASIA-Interval / IITD / AMF / UTIRIS-NIR. The completed E4 audit finds zero remaining predicted native-annulus contributions.

For training, removal precedes the existing brightness/contrast augmentation so discarded texture cannot affect the contrast mean. Fill is reapplied after augmentation. The code in [complement_inputs.py](Code/complement_inputs.py) is embedded in both training notebooks and the evaluation notebook; none requires importing the module or running another notebook.

## Frozen protocol

Original E1 subject partitions, exclusions, validation pairs and normalization are retained. Normalization is mean 0.48287347719744544 and SD 0.2741831329802273, from the original 5,356 PK-eligible raw training images. The retained inventory has 5,372 training and 1,155 validation images; 16 singleton CASIA training captures stay retained but cannot enter K=2 batches.

Models independently initialize from the original pretrained backbone. Both backbone and 512-hidden/256-output projection are fine-tuned. P=12, K=2, batch 24; four distinct subjects per dataset. AdamW 1e-4/weight decay 1e-4; triplet margin 0.3; SupCon temperature 0.07/weight 0.5; original pair masks; 224 batches per epoch; max/min completed epochs 150/30; patience 25 and improvement tolerance 1e-4. Early best epochs remain valid; minimum completed epochs is not a checkpoint-selection floor.

## Evaluation

Use the original E2-A common populations independently: CUST-Iris 427, CASIA-Interval 395, IITD 308, AMF 523 and UTIRIS-NIR 770 images. Genuine and different-subject impostor pairs are exhaustive. The same-person opposite-eye pairs remain a separate diagnostic. All three seeds are reported without selecting a favorable seed.

The training notebooks default to **no training, real-asset access or GPU smoke run**. The evaluation notebook defaults to **no inference or score recomputation** and displays the completed records. Supply licensed assets as described in [ASSETS.md](../ASSETS.md). Outputs go to fresh `reproduced_outputs/` locations. The original completed experiments are never overwritten.

E4-to-raw deltas compare independently trained complement and original A checkpoints, paired by numerical seed. They are not frozen-checkpoint input swaps. Performance demonstrates sufficiency under this representation and protocol, not a causal explanation of the original raw model's mechanism.
