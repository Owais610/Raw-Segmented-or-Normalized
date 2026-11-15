# Strict matched-area partial occlusion

Use only original E1-A checkpoints. Iris ROI is the existing Cartesian annulus support. Periocular ROI is nonpadding content outside the transformed iris/pupil disc dilated by a two-pixel guard. Region placement uses mask centroid and equivalent radius only, with no anatomical refit.

For each 5%/10% target fraction of annulus area, use the largest integer-radius discrete circular stencil whose pixel count does not exceed the target. Candidate centers require the entire stencil to fit the ROI. Both disks lie on the same image-coordinate side of the centroid and share center y. Choose minimum squared distance to targets x=cx±0.7r for iris and cx±1.5r for periocular, plus 2(y−cy)², with original deterministic tie breaks. Left/right are spatial controls, not temporal/nasal labels.

All eight area/side/region combinations must be feasible for image inclusion; no relaxed fallback is allowed. The published original strict feasible cohort and frozen pair tables are supplied directly. Constructed geometry must reproduce them, or execution stops. The same cohort/pairs supports every variant and its baseline.

Replace occluded pixels with the frozen training mean before normalization, equivalent to normalized zero. Every unoccluded tensor pixel is unchanged. Preserve disk area, shape, y coordinate and measured removed-intensity energy. No new enhancement or data augmentation.

Report original metrics for all variants, baseline changes, iris-minus-periocular paired effects, distributions and per-image/subject sensitivity. Coverage/failures are analysis-specific, never new E1 exclusions. Matched area does not equalize removed texture/intensity energy; x position, segmentation, feasible-population selection and artificial boundaries remain confounds. This is partial-occlusion sensitivity, not removal of a whole region or proof of an identity shortcut.
