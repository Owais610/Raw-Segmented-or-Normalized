# Raw-model input interventions

Use the six original frozen E1-A checkpoints, never B-trained replacements. Evaluate A_A plus existing A_B1_black/A_B2_black, predefined A_B1_mean/A_B2_mean and A_nonannulus_black/A_nonannulus_mean.

For iris-only controls, fill nonpadding content outside the B1/B2 support. For complementary controls, fill exactly the B1 annulus. Mean fill uses the original raw-training mean (normalized zero); black fill is (0−mean)/SD. Preserve original black padding and every unmasked tensor pixel. Complementary support retains the pupil and additional ocular information; it is not strictly periocular-only.

The native annulus and visible-iris masks are transformed with the original nearest-exact support resize. Check existing B outputs against interventions, retained-pixel equality, C1/C2 availability and anatomical nonempty support. Native area-resize footprint measures quantify boundary mixing using epsilon=1e−6. This mixing is documented rather than assumed absent. Complementary conditions require every common image in a dataset to pass the original geometry checks; otherwise retain the original population and mark that condition unavailable.

Use the exact common members/pairs across all seven inputs. Reuse the A_A original scores; crossed inputs retain original domain-specific matched inference order, batch size, normalization and AMP. Report EER/AUC/TAR, genuine means, impostor p99/p99.9/max, paired baseline differences, mean-versus-black and B2-versus-B1 contrasts, per-image/subject sensitivity and leave-one-subject-out effects for all seeds.

Degraded performance can reflect distribution shift, artificial boundaries, altered statistics or segmentation error; it is not proof of periocular identity reliance. Preserved performance indicates iris-only sufficiency under this intervention, not that raw inference ignores other information.
