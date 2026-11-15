# E2-F numerical exception diagnosis

This is a bounded inference-reproducibility check, not another attribution experiment. All original primary maps, selections, support flags and the0.001 tolerance remain unchanged. No additional heatmaps or recognition metrics were generated.

The original saved embedding cache and original inference-batch membership were replayed under AMP and FP32. Additional batch members are only original held-out test/external images used to reproduce existing batches, never training/validation images or additional CAM subjects.

| dataset | architecture | seed | pair_id | category | saved_score | cached_embedding_recomputed_score | cached_embedding_score_error | original_amp_batch24_score | original_fp32_batch24_score | fp32_batch2_score | amp_batch2_score | replayed_amp24_vs_saved_error | fp32_batch24_vs_fp32_batch2_error | amp24_vs_fp32_batch24_difference | original_score_consistent_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | 42 | 55c1c7f11df9f2f5c2382116fade86bf73c815e7cfacb62f5474c7054e3a3ed6 | genuine | 0.501949728 | 0.501949728 | 0.0 | 0.501949728 | 0.501024187 | 0.500931025 | 0.501859069 | 0.0 | 9.3162e-05 | 0.000925541 | False |
| CUST-Iris | ResNet-18 | 42 | faac6227b25247c0afec943c4542b6574c269006e6f2b3fdfcfd796b06dcd2ab | high_similarity_impostor | 0.426431835 | 0.426431835 | 0.0 | 0.426431835 | 0.425379455 | 0.425253063 | 0.426341712 | 0.0 | 0.000126392 | 0.00105238 | False |
| CUST-Iris | ResNet-18 | 42 | dad138a0dd154cccd9986cc70b92d3cf2dc417c8969df02301631cfcd9988b14 | ordinary_impostor | -0.063067697 | -0.063067697 | 0.0 | -0.063067697 | -0.062023569 | -0.061939847 | -0.063223362 | 0.0 | 8.3722e-05 | 0.001044128 | False |
| CUST-Iris | ResNet-18 | 42 | ec8c8b09cd31ee62f324c6f63569993e99f8a7ac59660b0b28f2727a8095c356 | ordinary_impostor | 0.139507681 | 0.139507681 | 0.0 | 0.139507681 | 0.13812086 | 0.138088167 | 0.13942942 | 0.0 | 3.2693e-05 | 0.001386821 | False |
| CASIA-Interval | ResNet-18 | 42 | 889ba6622ac8b6891eba3ba49e06f61a838ce3833e8846c9c43023c4297c6021 | genuine | 0.65829742 | 0.65829742 | 0.0 | 0.65829742 | 0.656797171 | 0.656816125 | 0.65809387 | 0.0 | 1.8954e-05 | 0.001500249 | False |
| IITD | ResNet-18 | 42 | 6b21ca6a8dea011944f9a55bfc19f3343ba621582d44b191b139f294e7fbf057 | high_similarity_impostor | 0.527579308 | 0.527579308 | 0.0 | 0.527579308 | 0.526233912 | 0.526198387 | 0.527496338 | 0.0 | 3.5524e-05 | 0.001345396 | False |
| AMF | ResNet-18 | 42 | 5594122ea37f44362026171ef9f8362b9b4c34a24785832bfc4e300643e01cc5 | ordinary_impostor | 0.115055367 | 0.115055367 | 0.0 | 0.115055367 | 0.114102006 | 0.114040785 | 0.115007803 | 0.0 | 6.1221e-05 | 0.000953361 | False |
| CUST-Iris | ResNet-18 | 123 | 324bc9a18b411b246f93c82bf2ee0b6d6baf0dc71e791836816b0a430e013ca9 | ordinary_impostor | -0.156652451 | -0.156652451 | 0.0 | -0.156652451 | -0.157650739 | -0.157660171 | -0.156601921 | 0.0 | 9.432e-06 | 0.000998288 | False |
| IITD | ResNet-18 | 123 | b933708fccc293e734b5a736125986be16aacd227688589e51a98501d90a4b2e | ordinary_impostor | -0.050245162 | -0.050245162 | 0.0 | -0.050245162 | -0.051261909 | -0.05130028 | -0.05021314 | 0.0 | 3.837e-05 | 0.001016747 | False |
| AMF | ResNet-18 | 123 | e6fc6be9da18aae9ee01fec94672f0d7615626629b8ba34c256a74adb549f371 | ordinary_impostor | 0.19749184 | 0.19749184 | 0.0 | 0.19749184 | 0.198677555 | 0.198689252 | 0.197402149 | 0.0 | 1.1697e-05 | 0.001185715 | False |
| AMF | ResNet-18 | 123 | 651e5e8d714402ce65534963822daafce17dc6b702fbe04c77128cf05b9d6722 | partner_diagnostic_impostor | 0.24950172 | 0.24950172 | 0.0 | 0.24950172 | 0.250726193 | 0.250763834 | 0.249587879 | 0.0 | 3.764e-05 | 0.001224473 | False |
| UTIRIS_NIR | ResNet-18 | 123 | 3c561824070ebc2ae8cbe192e24d26ddb382a7c0c74f59e6806d26ed7823127f | genuine | 0.732260108 | 0.732260108 | 0.0 | 0.732260108 | 0.73334837 | 0.733299196 | 0.732260823 | 0.0 | 4.9174e-05 | 0.001088262 | False |
| CUST-Iris | ResNet-18 | 2025 | 324bc9a18b411b246f93c82bf2ee0b6d6baf0dc71e791836816b0a430e013ca9 | ordinary_impostor | 0.20770061 | 0.20770061 | 0.0 | 0.20770061 | 0.206559807 | 0.206476629 | 0.207660735 | 0.0 | 8.3178e-05 | 0.001140803 | False |
| CASIA-Interval | ResNet-18 | 2025 | afd3c7c0cdf7a313bfc8a59ef297ebceba2e7555d823c909d631d61bd50eb015 | genuine | 0.313192964 | 0.313192964 | 0.0 | 0.313192964 | 0.314448655 | 0.314358175 | 0.312974364 | 0.0 | 9.048e-05 | 0.001255691 | False |
| IITD | ResNet-18 | 2025 | d4cb5bb5960563850f19d12a3d4b835f4fafc4ccdf31234f81c349926b11b183 | ordinary_impostor | -0.066987768 | -0.066987768 | 0.0 | -0.066987768 | -0.065884121 | -0.065913841 | -0.067063734 | 0.0 | 2.972e-05 | 0.001103647 | False |
| UTIRIS_NIR | ResNet-18 | 2025 | 1a4921542f62cb083c521f467d41c889728698a7e6e915d833219234fd56c00f | ordinary_impostor | 0.492403209 | 0.492403209 | 0.0 | 0.492403209 | 0.493494779 | 0.493423998 | 0.492368191 | 0.0 | 7.0781e-05 | 0.00109157 | False |

Maximum cached-embedding score reconstruction error: 0. Maximum replayed original AMP-batch24 versus saved error: 0. Maximum FP32 batch24 versus attribution FP32 batch2 error: 0.000126391649.

The unchanged primary tolerance is applied regardless of this diagnosis. Failed FP32 agreement cases remain unsupported in matched primary spatial summaries; their maps/gradients stay saved and visible. AMP reproducibility and FP32 reproducibility are numerical facts, not evidence of causal identity reliance.

Reporting-label clarification: original_score_consistent_flag=False denotes the original failed numerical check. No support flag changed; all numerical values and controls remain the same.