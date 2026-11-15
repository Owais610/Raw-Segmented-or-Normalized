# Frozen polar input-swap method

For each C1-trained and C2-trained checkpoint (both backbones, all three seeds), score both C1 and C2 inputs on each dataset's same common images/pairs. Diagonal scores reuse original full-population embedding caches; crossed inference retains original domain-specific matched order, batch 24 and AMP policy.

C1/C2 use one saved V2 geometry and coordinate map. C2 validity is a subset of C1 validity; common-valid samples are exactly equal, and invalid pixels stay zero. No segmentation, fit, normalization or architecture is changed for the swap.

Calculate original EER/AUC/TAR metrics, full score distributions and the within-checkpoint effect C2-input minus C1-input. Report all three seeds, means/sample SD, per-image/subject score sensitivity and leave-one-subject-out input effects. Always distinguish this fixed-model effect from a C1-trained versus C2-trained model comparison.

Masking changes tissue, support boundaries and image statistics and creates test-time distribution mismatch. The swap is an input sensitivity experiment and does not isolate a causal eyelash-information effect.
