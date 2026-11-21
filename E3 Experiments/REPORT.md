# E3: training and testing directly on binary segmentation masks

All results use validation-selected best checkpoints and seeds 42, 123 and 2025. Values are mean ± sample SD. EER/TAR are percentages and ROC-AUC is on [0,1]. Each dataset has its original E2-A common images and exhaustive pairs. No dataset scores are pooled and no seed is selected as the reported result.

The new models start independently from the same pretrained encoders as E1. E3 reuses the unchanged E1 training loop, architecture, sampler, objective, optimizer, schedule, original validation pairs and frozen normalization. The user approved disabling brightness/contrast augmentation so inputs remain strictly 0/255 before normalization. This approved augmentation difference accompanies the training-representation change and must be retained in interpretation.

## CUST-Iris

| dataset | architecture | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST-Iris | ResNet-18 | B1-binary | E1_gray_train_gray_test | 1.3408 ± 0.2088 | 0.9992 ± 0.0003 | 98.2124 ± 0.6375 | 91.1672 ± 1.1041 |
| CUST-Iris | ResNet-18 | B1-binary | E2_gray_train_binary_test | 15.9758 ± 0.3745 | 0.9180 ± 0.0030 | 39.1693 ± 2.9522 | 14.8791 ± 0.9242 |
| CUST-Iris | ResNet-18 | B1-binary | E3_binary_train_binary_test | 7.4291 ± 0.6549 | 0.9768 ± 0.0028 | 70.3996 ± 0.3643 | 38.9590 ± 4.0244 |
| CUST-Iris | ResNet-18 | B2-binary | E1_gray_train_gray_test | 1.4202 ± 0.3398 | 0.9991 ± 0.0004 | 97.8444 ± 0.7939 | 90.2734 ± 1.5799 |
| CUST-Iris | ResNet-18 | B2-binary | E2_gray_train_binary_test | 15.6443 ± 0.6303 | 0.9195 ± 0.0084 | 36.6982 ± 3.4025 | 14.3533 ± 2.1912 |
| CUST-Iris | ResNet-18 | B2-binary | E3_binary_train_binary_test | 7.8864 ± 0.2732 | 0.9759 ± 0.0004 | 65.6151 ± 3.0093 | 35.8570 ± 3.7800 |
| CUST-Iris | SwinV2-Tiny | B1-binary | E1_gray_train_gray_test | 1.5415 ± 0.2137 | 0.9987 ± 0.0004 | 97.4238 ± 0.5972 | 86.8034 ± 3.4061 |
| CUST-Iris | SwinV2-Tiny | B1-binary | E2_gray_train_binary_test | 31.0200 ± 3.9944 | 0.7560 ± 0.0467 | 14.0904 ± 2.4503 | 3.9432 ± 1.9124 |
| CUST-Iris | SwinV2-Tiny | B1-binary | E3_binary_train_binary_test | 9.8089 ± 0.4294 | 0.9656 ± 0.0011 | 58.6225 ± 2.7152 | 26.6562 ± 2.0137 |
| CUST-Iris | SwinV2-Tiny | B2-binary | E1_gray_train_gray_test | 2.0037 ± 0.3775 | 0.9983 ± 0.0004 | 96.3722 ± 1.5534 | 81.2303 ± 3.6957 |
| CUST-Iris | SwinV2-Tiny | B2-binary | E2_gray_train_binary_test | 23.6877 ± 1.2551 | 0.8385 ± 0.0146 | 16.9295 ± 3.5175 | 5.0473 ± 1.7350 |
| CUST-Iris | SwinV2-Tiny | B2-binary | E3_binary_train_binary_test | 9.1410 ± 0.7172 | 0.9701 ± 0.0010 | 59.3586 ± 2.9858 | 30.9674 ± 5.0383 |

## CASIA-Interval

| dataset | architecture | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CASIA-Interval | ResNet-18 | B1-binary | E1_gray_train_gray_test | 2.7820 ± 0.3462 | 0.9959 ± 0.0008 | 94.6046 ± 0.9665 | 83.7152 ± 2.0922 |
| CASIA-Interval | ResNet-18 | B1-binary | E2_gray_train_binary_test | 18.5656 ± 1.2753 | 0.8967 ± 0.0118 | 27.9379 ± 4.9188 | 8.3518 ± 1.4101 |
| CASIA-Interval | ResNet-18 | B1-binary | E3_binary_train_binary_test | 9.8800 ± 0.4753 | 0.9657 ± 0.0038 | 58.7090 ± 2.4112 | 27.6915 ± 1.3413 |
| CASIA-Interval | ResNet-18 | B2-binary | E1_gray_train_gray_test | 3.8632 ± 1.5662 | 0.9902 ± 0.0022 | 91.6482 ± 4.4976 | 76.0039 ± 10.2906 |
| CASIA-Interval | ResNet-18 | B2-binary | E2_gray_train_binary_test | 13.1882 ± 0.6962 | 0.9426 ± 0.0059 | 46.4400 ± 5.0914 | 13.5009 ± 4.1293 |
| CASIA-Interval | ResNet-18 | B2-binary | E3_binary_train_binary_test | 8.4654 ± 0.3551 | 0.9734 ± 0.0014 | 67.9970 ± 1.6006 | 34.8115 ± 3.6306 |
| CASIA-Interval | SwinV2-Tiny | B1-binary | E1_gray_train_gray_test | 3.2307 ± 0.5268 | 0.9958 ± 0.0009 | 92.2148 ± 1.6664 | 80.0443 ± 2.8510 |
| CASIA-Interval | SwinV2-Tiny | B1-binary | E2_gray_train_binary_test | 38.6302 ± 2.6040 | 0.6576 ± 0.0366 | 7.2185 ± 2.1792 | 2.1187 ± 1.1217 |
| CASIA-Interval | SwinV2-Tiny | B1-binary | E3_binary_train_binary_test | 12.3183 ± 1.3020 | 0.9474 ± 0.0083 | 49.0022 ± 4.4364 | 18.2804 ± 2.3165 |
| CASIA-Interval | SwinV2-Tiny | B2-binary | E1_gray_train_gray_test | 3.3017 ± 0.6931 | 0.9943 ± 0.0027 | 90.6874 ± 3.9505 | 72.2345 ± 11.6668 |
| CASIA-Interval | SwinV2-Tiny | B2-binary | E2_gray_train_binary_test | 16.4492 ± 0.5081 | 0.9103 ± 0.0047 | 27.2727 ± 3.5160 | 7.9576 ± 3.2506 |
| CASIA-Interval | SwinV2-Tiny | B2-binary | E3_binary_train_binary_test | 9.5117 ± 0.7829 | 0.9658 ± 0.0044 | 62.0596 ± 2.5543 | 33.8753 ± 1.8993 |

## IITD

| dataset | architecture | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IITD | ResNet-18 | B1-binary | E1_gray_train_gray_test | 1.0694 ± 0.2537 | 0.9993 ± 0.0004 | 98.8854 ± 0.3185 | 97.0276 ± 1.4795 |
| IITD | ResNet-18 | B1-binary | E2_gray_train_binary_test | 5.7479 ± 0.3324 | 0.9844 ± 0.0007 | 79.6709 ± 0.9598 | 50.3715 ± 3.9468 |
| IITD | ResNet-18 | B1-binary | E3_binary_train_binary_test | 1.8220 ± 0.6425 | 0.9984 ± 0.0009 | 96.9214 ± 1.6108 | 84.9257 ± 0.4007 |
| IITD | ResNet-18 | B2-binary | E1_gray_train_gray_test | 1.3243 ± 0.7882 | 0.9986 ± 0.0019 | 98.1423 ± 1.8456 | 93.6306 ± 6.2102 |
| IITD | ResNet-18 | B2-binary | E2_gray_train_binary_test | 4.1341 ± 0.4316 | 0.9913 ± 0.0003 | 88.3758 ± 0.5741 | 65.3397 ± 4.4652 |
| IITD | ResNet-18 | B2-binary | E3_binary_train_binary_test | 2.3811 ± 0.3187 | 0.9975 ± 0.0007 | 96.0722 ± 1.3543 | 85.1380 ± 0.6029 |
| IITD | SwinV2-Tiny | B1-binary | E1_gray_train_gray_test | 0.9340 ± 0.5146 | 0.9997 ± 0.0002 | 99.2569 ± 0.7525 | 96.8684 ± 1.2969 |
| IITD | SwinV2-Tiny | B1-binary | E2_gray_train_binary_test | 27.7130 ± 3.8701 | 0.7875 ± 0.0398 | 23.5138 ± 9.5824 | 7.8025 ± 4.2220 |
| IITD | SwinV2-Tiny | B1-binary | E3_binary_train_binary_test | 2.4533 ± 0.6337 | 0.9967 ± 0.0015 | 94.5860 ± 1.8364 | 79.7771 ± 4.6343 |
| IITD | SwinV2-Tiny | B2-binary | E1_gray_train_gray_test | 1.1590 ± 0.1443 | 0.9993 ± 0.0001 | 98.7261 ± 0.2758 | 96.1253 ± 0.8770 |
| IITD | SwinV2-Tiny | B2-binary | E2_gray_train_binary_test | 11.8365 ± 2.4324 | 0.9501 ± 0.0170 | 51.1146 ± 7.7291 | 22.5584 ± 6.1781 |
| IITD | SwinV2-Tiny | B2-binary | E3_binary_train_binary_test | 2.6649 ± 0.3838 | 0.9936 ± 0.0027 | 94.2144 ± 2.0226 | 78.7686 ± 3.8755 |

## AMF

| dataset | architecture | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMF | ResNet-18 | B1-binary | E1_gray_train_gray_test | 1.6420 ± 0.2844 | 0.9988 ± 0.0005 | 97.7340 ± 0.6897 | 91.3957 ± 2.9905 |
| AMF | ResNet-18 | B1-binary | E2_gray_train_binary_test | 10.1434 ± 0.5737 | 0.9643 ± 0.0015 | 59.2447 ± 1.3304 | 30.4105 ± 1.5146 |
| AMF | ResNet-18 | B1-binary | E3_binary_train_binary_test | 10.8575 ± 1.0981 | 0.9585 ± 0.0056 | 56.1248 ± 2.0814 | 26.8309 ± 2.8080 |
| AMF | ResNet-18 | B2-binary | E1_gray_train_gray_test | 1.5258 ± 0.2902 | 0.9989 ± 0.0005 | 97.7997 ± 0.7127 | 91.0016 ± 3.8314 |
| AMF | ResNet-18 | B2-binary | E2_gray_train_binary_test | 9.6085 ± 0.9056 | 0.9652 ± 0.0080 | 63.6782 ± 1.3120 | 36.0920 ± 2.1949 |
| AMF | ResNet-18 | B2-binary | E3_binary_train_binary_test | 8.8694 ± 1.0038 | 0.9705 ± 0.0050 | 64.1379 ± 5.0631 | 35.7307 ± 4.8670 |
| AMF | SwinV2-Tiny | B1-binary | E1_gray_train_gray_test | 1.7932 ± 0.5804 | 0.9984 ± 0.0008 | 96.9458 ± 1.2883 | 90.2791 ± 2.1230 |
| AMF | SwinV2-Tiny | B1-binary | E2_gray_train_binary_test | 25.7800 ± 4.3421 | 0.8233 ± 0.0504 | 25.2874 ± 8.9054 | 10.3847 ± 4.4209 |
| AMF | SwinV2-Tiny | B1-binary | E3_binary_train_binary_test | 11.0939 ± 1.9720 | 0.9546 ± 0.0125 | 53.2677 ± 7.6476 | 22.6343 ± 7.8762 |
| AMF | SwinV2-Tiny | B2-binary | E1_gray_train_gray_test | 1.4651 ± 0.2180 | 0.9989 ± 0.0005 | 97.8325 ± 0.9398 | 89.6880 ± 5.7451 |
| AMF | SwinV2-Tiny | B2-binary | E2_gray_train_binary_test | 16.1576 ± 0.7695 | 0.9175 ± 0.0055 | 37.7668 ± 3.6524 | 16.9458 ± 2.5898 |
| AMF | SwinV2-Tiny | B2-binary | E3_binary_train_binary_test | 9.8653 ± 1.6669 | 0.9634 ± 0.0105 | 62.2989 ± 2.2344 | 31.7241 ± 0.7695 |

## UTIRIS_NIR

| dataset | architecture | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UTIRIS_NIR | ResNet-18 | B1-binary | E1_gray_train_gray_test | 6.6357 ± 0.3494 | 0.9836 ± 0.0036 | 80.0302 ± 2.4793 | 56.4983 ± 3.7966 |
| UTIRIS_NIR | ResNet-18 | B1-binary | E2_gray_train_binary_test | 20.1425 ± 0.8469 | 0.8820 ± 0.0061 | 22.0855 ± 2.2668 | 5.9154 ± 0.8841 |
| UTIRIS_NIR | ResNet-18 | B1-binary | E3_binary_train_binary_test | 18.0438 ± 2.6486 | 0.8999 ± 0.0226 | 33.5708 ± 4.8408 | 11.5069 ± 2.7435 |
| UTIRIS_NIR | ResNet-18 | B2-binary | E1_gray_train_gray_test | 7.3034 ± 0.4180 | 0.9791 ± 0.0039 | 75.3670 ± 3.3217 | 51.7487 ± 3.6159 |
| UTIRIS_NIR | ResNet-18 | B2-binary | E2_gray_train_binary_test | 19.2439 ± 0.6595 | 0.8875 ± 0.0065 | 24.9568 ± 0.7507 | 7.6857 ± 0.4312 |
| UTIRIS_NIR | ResNet-18 | B2-binary | E3_binary_train_binary_test | 18.0089 ± 0.4651 | 0.8980 ± 0.0036 | 33.5060 ± 2.0779 | 12.4136 ± 1.6183 |
| UTIRIS_NIR | SwinV2-Tiny | B1-binary | E1_gray_train_gray_test | 6.7172 ± 1.2329 | 0.9815 ± 0.0069 | 74.6114 ± 4.7611 | 46.7185 ± 9.0535 |
| UTIRIS_NIR | SwinV2-Tiny | B1-binary | E2_gray_train_binary_test | 40.4043 ± 1.9808 | 0.6335 ± 0.0257 | 5.0734 ± 1.0369 | 0.9067 ± 0.5301 |
| UTIRIS_NIR | SwinV2-Tiny | B1-binary | E3_binary_train_binary_test | 18.8883 ± 0.7824 | 0.8954 ± 0.0077 | 27.9793 ± 0.7853 | 7.7073 ± 0.4670 |
| UTIRIS_NIR | SwinV2-Tiny | B2-binary | E1_gray_train_gray_test | 6.2924 ± 0.5181 | 0.9848 ± 0.0016 | 76.2090 ± 1.7551 | 47.9706 ± 2.8887 |
| UTIRIS_NIR | SwinV2-Tiny | B2-binary | E2_gray_train_binary_test | 28.0916 ± 0.9243 | 0.7949 ± 0.0126 | 12.1762 ± 2.1559 | 2.8929 ± 0.9075 |
| UTIRIS_NIR | SwinV2-Tiny | B2-binary | E3_binary_train_binary_test | 19.4085 ± 0.9893 | 0.8890 ± 0.0065 | 29.3826 ± 0.5031 | 9.6287 ± 0.3567 |

## Architecture contrast

SwinV2-Tiny minus ResNet-18, paired by numerical seed. Negative EER contrast favors SwinV2-Tiny; positive TAR contrast favors SwinV2-Tiny. These descriptive seed differences are not participant confidence intervals or causal/significance tests.

| dataset | condition | scenario | eer | roc_auc | tar_at_far_1pct | tar_at_far_0_1pct |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | B1-binary | E1_gray_train_gray_test | 0.1512 ± 0.2963 | -0.0004 ± 0.0004 | -0.7882 ± 0.5993 | -1.1166 ± 0.8940 |
| AMF | B1-binary | E2_gray_train_binary_test | 15.6366 ± 4.9135 | -0.1410 ± 0.0520 | -33.9573 ± 10.1503 | -20.0258 ± 5.1865 |
| AMF | B1-binary | E3_binary_train_binary_test | 0.2364 ± 2.9725 | -0.0038 ± 0.0180 | -2.8571 ± 9.7288 | -4.1966 ± 9.6826 |
| AMF | B2-binary | E1_gray_train_gray_test | -0.0607 ± 0.2197 | 0.0000 ± 0.0005 | 0.0328 ± 0.9312 | -1.3136 ± 7.3413 |
| AMF | B2-binary | E2_gray_train_binary_test | 6.5491 ± 0.2100 | -0.0476 ± 0.0032 | -25.9113 ± 3.1970 | -19.1461 ± 1.9564 |
| AMF | B2-binary | E3_binary_train_binary_test | 0.9959 ± 2.3438 | -0.0071 ± 0.0135 | -1.8391 ± 7.0760 | -4.0066 ± 4.1124 |
| CASIA-Interval | B1-binary | E1_gray_train_gray_test | 0.4487 ± 0.6928 | -0.0000 ± 0.0015 | -2.3898 ± 2.0699 | -3.6709 ± 4.5087 |
| CASIA-Interval | B1-binary | E2_gray_train_binary_test | 20.0646 ± 3.8703 | -0.2390 ± 0.0484 | -20.7194 ± 6.3193 | -6.2331 ± 1.8877 |
| CASIA-Interval | B1-binary | E3_binary_train_binary_test | 2.4384 ± 1.7431 | -0.0183 ± 0.0114 | -9.7068 ± 6.8083 | -9.4112 ± 3.5694 |
| CASIA-Interval | B2-binary | E1_gray_train_gray_test | -0.5615 ± 2.1216 | 0.0040 ± 0.0048 | -0.9608 ± 8.4046 | -3.7694 ± 20.2124 |
| CASIA-Interval | B2-binary | E2_gray_train_binary_test | 3.2610 ± 0.6435 | -0.0323 ± 0.0052 | -19.1673 ± 5.6299 | -5.5432 ± 6.8497 |
| CASIA-Interval | B2-binary | E3_binary_train_binary_test | 1.0464 ± 0.5663 | -0.0076 ± 0.0053 | -5.9374 ± 0.9618 | -0.9362 ± 3.8556 |
| CUST-Iris | B1-binary | E1_gray_train_gray_test | 0.2007 ± 0.4105 | -0.0005 ± 0.0006 | -0.7886 ± 1.1908 | -4.3638 ± 4.1442 |
| CUST-Iris | B1-binary | E2_gray_train_binary_test | 15.0442 ± 3.8404 | -0.1620 ± 0.0463 | -25.0789 ± 4.5469 | -10.9359 ± 2.8274 |
| CUST-Iris | B1-binary | E3_binary_train_binary_test | 2.3797 ± 1.0835 | -0.0113 ± 0.0037 | -11.7771 ± 3.0760 | -12.3028 ± 5.9999 |
| CUST-Iris | B2-binary | E1_gray_train_gray_test | 0.5836 ± 0.6807 | -0.0008 ± 0.0008 | -1.4721 ± 2.1415 | -9.0431 ± 2.1415 |
| CUST-Iris | B2-binary | E2_gray_train_binary_test | 8.0434 ± 1.5737 | -0.0810 ± 0.0200 | -19.7687 ± 6.0625 | -9.3060 ± 1.2319 |
| CUST-Iris | B2-binary | E3_binary_train_binary_test | 1.2545 ± 0.8125 | -0.0058 ± 0.0011 | -6.2566 ± 4.6852 | -4.8896 ± 5.2289 |
| IITD | B1-binary | E1_gray_train_gray_test | -0.1354 ± 0.5374 | 0.0005 ± 0.0002 | 0.3715 ± 0.8770 | -0.1592 ± 1.6625 |
| IITD | B1-binary | E2_gray_train_binary_test | 21.9652 ± 3.5661 | -0.1969 ± 0.0398 | -56.1571 ± 8.6228 | -42.5690 ± 3.6636 |
| IITD | B1-binary | E3_binary_train_binary_test | 0.6313 ± 1.1585 | -0.0017 ± 0.0023 | -2.3355 ± 2.4737 | -5.1486 ± 4.3734 |
| IITD | B2-binary | E1_gray_train_gray_test | -0.1653 ± 0.6846 | 0.0008 ± 0.0018 | 0.5839 ± 1.7027 | 2.4947 ± 6.3502 |
| IITD | B2-binary | E2_gray_train_binary_test | 7.7025 ± 2.8600 | -0.0412 ± 0.0172 | -37.2611 ± 8.0268 | -42.7813 ± 3.7355 |
| IITD | B2-binary | E3_binary_train_binary_test | 0.2838 ± 0.6314 | -0.0039 ± 0.0033 | -1.8577 ± 2.3956 | -6.3694 ± 3.3553 |
| UTIRIS_NIR | B1-binary | E1_gray_train_gray_test | 0.0815 ± 1.4294 | -0.0021 ± 0.0095 | -5.4188 ± 6.3687 | -9.7798 ± 8.8197 |
| UTIRIS_NIR | B1-binary | E2_gray_train_binary_test | 20.2618 ± 1.8413 | -0.2486 ± 0.0265 | -17.0121 ± 1.2311 | -5.0086 ± 0.5508 |
| UTIRIS_NIR | B1-binary | E3_binary_train_binary_test | 0.8445 ± 2.2152 | -0.0045 ± 0.0176 | -5.5915 ± 5.0428 | -3.7997 ± 2.4885 |
| UTIRIS_NIR | B2-binary | E1_gray_train_gray_test | -1.0111 ± 0.1999 | 0.0057 ± 0.0026 | 0.8420 ± 1.6877 | -3.7781 ± 3.9323 |
| UTIRIS_NIR | B2-binary | E2_gray_train_binary_test | 8.8477 ± 0.7106 | -0.0926 ± 0.0127 | -12.7807 ± 1.5656 | -4.7927 ± 0.5646 |
| UTIRIS_NIR | B2-binary | E3_binary_train_binary_test | 1.3996 ± 1.3094 | -0.0090 ± 0.0082 | -4.1235 ± 1.5869 | -2.7850 ± 1.2758 |

## Interpretation boundaries

Binary supports contain geometry, position/scale and predicted masking footprints, including segmentation errors. They contain no grayscale source texture. Above-chance performance establishes discrimination for this mask-trained protocol; it does not establish which geometric feature is responsible or that original grayscale models used the same information. EER and TAR use the existing complete-ROC interpolation; no test-set threshold fitting or hyperparameter selection occurs.
