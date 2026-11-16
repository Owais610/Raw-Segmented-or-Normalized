# E2-G: method and interpretation

This experiment was requested after completion of E1 and E2-A to E2-F. It is an inference-only input intervention; its method is fixed before new recognition scores are calculated. No models are trained or selected using these results.

## Question and exact scope

Do the twelve existing E1-B1/E1-B2 best checkpoints (ResNet-18 and SwinV2-Tiny, seeds 42, 123, 2025) retain verification discrimination when the original grayscale iris samples are replaced entirely with their binary support masks? B1 checkpoints receive their own B1 supports; B2 checkpoints receive their own B2 supports. Cross-feeding B1/B2 supports, new masks, threshold/polarity sweeps, and raw/polar-trained checkpoints are outside this experiment.

Evaluate CUST-Iris, CASIA-Interval, and IITD using only their original frozen test subjects, and AMF and UTIRIS NIR using the existing external populations. For each dataset reuse the exact E2-A intersection across all five representations, all genuine comparisons, and all eligible different-subject impostors. Same-subject opposite-eye comparisons remain a separate diagnostic. No pair is removed because its binary masks are identical: distinct captures with identical geometry are valid outcomes, not identical source images.

## Deterministic input

Read the original hash-verified 320x320 binary support PNGs. B1 = iris AND NOT pupil; B2 = B1 AND NOT predicted eyelashes. Audit that each equals the native mask formula transformed with the original nearest-exact, aspect-preserving letterbox geometry. The support is white (uint8 255), and every other pixel, including pupil, background, and padding, is black (0). No raw grayscale values, mask probabilities, soft interpolation, recentering, crop, resize, enhancement, or augmentation enter binary inputs.

Convert uint8 to float32 by division by 255 and apply the unchanged training normalization: mean 0.48287347719744544, standard deviation 0.2741831329802273. The normalized input contains exactly two possible intensities: (0-mean)/std and (1-mean)/std. Do not renormalize each image or estimate new statistics. For every image audit exact binary values, cached/native mask equivalence, support area, pupil exclusion, B2 subset of B1, and black padding. Preserve identity/QC flags and all membership.

Load original best checkpoints strictly through the visible notebook encoder/inference definitions: original 256-D unit-norm embeddings, network shapes, AMP, Swin dynamic masks and float32 attention. Models remain in eval mode with gradients disabled; optimizer and checkpoint creation are absent. Execute the twelve checkpoints sequentially with batch 24, and preserve checkpoint hashes. Store the binary-input embeddings, exact cosine pair scores, full ROCs, metrics, and runtime/VRAM provenance. Reuse original matched grayscale-baseline scores and leave-one-subject-out metrics rather than recomputing baseline inference.

## Analysis fixed in advance

For all 60 dataset/checkpoint cells report baseline and geometry EER, ROC-AUC, ROC-interpolated TAR@1% FAR and TAR@0.1% FAR, all three seeds, mean and sample SD (ddof=1), and paired geometry-minus-baseline differences. Use the existing verified metric functions without a new operating-threshold selection. Save genuine/impostor/opposite-eye distributions, genuine mean changes, high-similarity impostor p99/p99.9 changes, per-image and subject-averaged sensitivities, and leave-one-subject-out metrics and changes. Report matched-seed architecture contrasts descriptively. Keep datasets independent: do not pool scores or select the strongest seed/domain/condition.

Audit identical-mask collisions separately for genuine, impostor, and opposite-eye pairs. Select preview examples by low, median, and high predicted lash-occlusion fractions with distinct subjects before inspecting recognition outcomes. Save black/white input previews alongside the unchanged grayscale baselines. Plot per-dataset EER summaries, complete ROC views, and score distributions for every architecture/B1/B2 condition, preserving individual seeds.

Unit tests must reject soft, nonbinary, malformed, and hash-mismatched masks; verify exact normalization and absence of grayscale-path access in binary loading; enforce subject/eye/source pair rules; and verify constant-score chance metrics/ties. A real-cache GPU smoke pass for each architecture and B1/B2 input must confirm finite, unit-norm outputs without a backward pass. Verify original checkpoints, frozen protocol, original E1 results, external artifacts, and completed E2-A to E2-F remain unchanged.

## Interpretation

This measures information available to a frozen grayscale-trained encoder under a substantial binary-input distribution shift. Geometry includes iris/pupil boundaries, image-relative position, scale, shape, fragmentation, occlusion boundaries, and predicted eyelash footprints for B2. It does not isolate clean anatomical geometry from acquisition conditions, segmentation artifacts, or subject-correlated capture effects. Non-chance discrimination is descriptive evidence that these inputs are sufficient for that checkpoint on these populations; it does not prove the model relied on geometry in its ordinary grayscale condition. Chance-like performance does not prove geometry contains no identity information or that a geometry-trained model could not exploit it. Existing predicted masks are not anatomical ground truth.

Repeated captures and pairs are dependent. Three-seed SD reflects training-seed variability on the same evaluated subjects, not participant confidence intervals. EER and AUC chance references (50% and 0.5) are descriptive; no significance test or causal claim is planned. LOO is an influence diagnostic, not independent-subject confidence estimation. Existing E1/E2 results are preserved; this independent experiment is not a replacement baseline.

## Publication assets and execution order

Use `Assets/Matched Population/` and `Assets/checkpoints.json` directly. Do not regenerate eligibility or pairs. For grayscale baselines, preserve the original full-population embedding inference order before selecting matched pairs. For binary E2-G inputs, use the exact matched membership order within each dataset, as in the completed experiment. The existing private support files may carry hash fields, but no author-machine integrity index is required to execute the standalone notebook. Native binary formulas, two-valued normalized inputs, membership, source exclusion and model configuration remain asserted. Biometric previews are opt-in and remain local. Shared implementation definitions are written in this notebook; another notebook is not a prerequisite.
