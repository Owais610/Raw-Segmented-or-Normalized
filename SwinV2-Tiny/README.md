# SwinV2-Tiny

One shared, fully fine-tuned embedding encoder; a GELU/LayerNorm projection produces 256-dimensional L2-normalized embeddings. No independent two-tower parameters.

| Condition | Input | Implementation | Training / validation | Matched evaluation |
| --- | --- | --- | --- | --- |
| E1-A | Raw ocular frame | [Standalone notebook](Training%20Codes/E1-A_Raw_Ocular.ipynb) | [All three runs](Training%20Histories/E1-A) | [Individual / three-seed metrics](Results/E1-A) |
| E1-B1 | Cartesian iris annulus; eyelashes retained | [Standalone notebook](Training%20Codes/E1-B1_Cartesian_Unmasked.ipynb) | [All three runs](Training%20Histories/E1-B1) | [Individual / three-seed metrics](Results/E1-B1) |
| E1-B2 | Cartesian iris annulus; predicted eyelashes masked | [Standalone notebook](Training%20Codes/E1-B2_Cartesian_Masked.ipynb) | [All three runs](Training%20Histories/E1-B2) | [Individual / three-seed metrics](Results/E1-B2) |
| E1-C1 | Pure-V2 polar iris; eyelashes retained | [Standalone notebook](Training%20Codes/E1-C1_Polar_Unmasked.ipynb) | [All three runs](Training%20Histories/E1-C1) | [Individual / three-seed metrics](Results/E1-C1) |
| E1-C2 | Pure-V2 polar iris; predicted eyelashes masked | [Standalone notebook](Training%20Codes/E1-C2_Polar_Masked.ipynb) | [All three runs](Training%20Histories/E1-C2) | [Individual / three-seed metrics](Results/E1-C2) |

Seeds **42, 123, 2025** start independently from the same tagged pretrained backbone. Inputs are 320×320 Cartesian or 64×512 native polar. All conditions use the original global raw-training mean/SD.
Training uses P=12, K=2 (four distinct subjects per dataset), masked batch-hard triplet + 0.5 supervised contrastive loss. Cross-dataset and same-subject opposite-eye pairs enter neither objective.
Selection uses validation macro-EER only; max/min epochs 150/30, patience 25, strict improvement >0.0001. Learning rate is constant.

Each history folder contains `runs.csv`, validation metric tables, and `seed_42/`, `seed_123/`, `seed_2025/` with the original `history.jsonl`, original `curves.png` and portable `configuration.json`. Best epochs and completed epochs remain separate.
The result folders contain the agreed common-population evaluation only; [E2-A](../E2%20Experiments/E2-A/README.md) contains the complete evaluation implementation and cross-architecture comparisons.

See [asset setup](../ASSETS.md), [executed checks](../VALIDATION.md) and [project navigation](../README.md).

Frozen B1/B2 models are also tested with binary mask geometry only in **[E2-G](../E2%20Experiments/E2-G/REPORT.md)**; all three seeds and matched datasets are retained.
