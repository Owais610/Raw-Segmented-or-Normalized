# Quality and masking-footprint definitions

Native measurements use the original evaluation inventory, never training/validation images. Failed geometry remains missing rather than receiving invented estimates. Recognition associations use the fixed common population.

The 23 notebook features include pupil/iris fitted-radius ratio; 1−ratio² fitted annulus fraction; center displacement divided by iris radius; native segmented-annulus/iris area; iris/frame area; sqrt(pupil-mask/iris-mask area); native unoccluded-annulus p90−p10 contrast, median intensity and fraction ≥250/255. Fitted circle-equivalent proxies remain distinct from mask-area proxies; pupil ellipses retain the frozen V2 interpretation.

Normalized texture uses C1 / 255, a 3×3 eroded valid interior and at least 32 interior samples. Local contrast is mean sqrt(max(E[I²]−E[I]²,0)) in a 3×3 window. Sobel derivatives use ksize=3, scale=1/8; report mean and p90 gradient magnitude. Laplacian variance uses ksize=3. Gradients at/above the within-image valid-interior p75 define high-gradient samples. Removed fractions use C1-valid minus C2-valid; overlap fractions explicitly state their denominator.

Geometry support/inlier fractions, supported arcs and median absolute residual divided by radius are fitting-quality proxies, not independent segmentation ground truth. Four radial and eight angular bins record support and removed samples. Validity-subset and exact common texture/coordinate checks are explicit.

Per-image outcomes are incident genuine mean, incident impostor p99/p99.9 and their difficulty margin (genuine mean minus impostor p99). Subject summaries first average within subject. Spearman uses pairwise nonmissing observations, at least eight observations and nonconstant variables. No p-values or independent-pair claims are made. The fixed short panel includes removed fraction, polar gradient, native contrast, pupil/iris radius ratio and iris supported arc; complete associations remain saved.

The numerical implementations are `features_one`, `polar_measures`, `associations` and the complete driver in the notebook. Native quantile examples select nearest p10/p50/p90 with image-ID tie breaks, independently of recognition. Biometric examples can be generated locally with permission; the release includes statistical distributions instead.
