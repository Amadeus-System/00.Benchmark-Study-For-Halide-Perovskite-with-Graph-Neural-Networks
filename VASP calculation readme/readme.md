## 데이터 정리

### noiselevel 0.01 데이터셋

* DFT Simulation with noise between -0.01 ~ 0.01 to atom coordinates

``` Python
 51%|█████     | 1830/3600 [01:32<01:01, 28.96it/s]
no element found: line 5402, column 0 ./1824_CsSnBr3_mp-27214_1x1x1_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 64%|██████▎   | 2291/3600 [01:53<00:38, 34.18it/s]
not well-formed (invalid token): line 901, column 0 ./2282_CsSnBr3_mp-27214_r2xr2x1_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [02:51<00:00, 21.00it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 2
```

* 기존 데이터셋에서 ParssingError 2개 발생
    - 1824번 폴더는 NSW: 50 -> 36으로 바꿔 다시 **계산 진행중...**
    - 2282번 폴더는 DFT 계산은 정상적으로 종료되었으나, 알 수 없는 ParsingError 발생 -> 데이터 사용 안함



### noiselevel 0.05 데이터셋

* DFT Simulation with noise between -0.05 ~ 0.05 to atom coordinates
* noiselevel 0.01 데이터셋에 비해 더 많은 비정상적인 계산종료가 발생 : 약 236개의 비정상 파일로 파싱 불가

``` Python
  1%|▏         | 45/3600 [00:01<02:06, 28.05it/s]
no element found: line 6425, column 0 ./0044_CsPbBr3_mp-600089_1x1x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
  2%|▏         | 89/3600 [00:03<02:07, 27.44it/s]
no element found: line 3056, column 0 ./0088_CsPbBr3_mp-600089_1x1x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 105/3600 [00:04<02:08, 27.17it/s]
no element found: line 1493, column 0 ./0102_CsPbBr3_mp-600089_2x1x1_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 123/3600 [00:04<02:24, 24.07it/s]
no element found: line 3715, column 0 ./0121_CsPbBr3_mp-600089_2x1x1_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 139/3600 [00:05<02:16, 25.34it/s]
no element found: line 2146, column 0 ./0138_CsPbBr3_mp-600089_2x1x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 152/3600 [00:06<02:14, 25.67it/s]
no element found: line 1391, column 0 ./0149_CsPbBr3_mp-600089_2x1x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 8340, column 0 ./0154_CsPbBr3_mp-600089_2x1x1_with_noise_57
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▍         | 175/3600 [00:07<02:24, 23.78it/s]
no element found: line 1004, column 0 ./0174_CsPbBr3_mp-600089_2x1x1_with_noise_75
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▌         | 182/3600 [00:07<02:17, 24.83it/s]
no element found: line 2027, column 0 ./0181_CsPbBr3_mp-600089_2x1x1_with_noise_81
<class 'xml.etree.ElementTree.ParseError'> 13
  6%|▌         | 216/3600 [00:08<02:48, 20.14it/s]
no element found: line 928, column 0 ./0214_CsPbBr3_mp-600089_2x2x1_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1684, column 0 ./0217_CsPbBr3_mp-600089_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3048, column 0 ./0219_CsPbBr3_mp-600089_2x2x1_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 242/3600 [00:10<02:31, 22.21it/s]
no element found: line 1063, column 0 ./0239_CsPbBr3_mp-600089_2x2x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1797, column 0 ./0240_CsPbBr3_mp-600089_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 249/3600 [00:10<02:34, 21.66it/s]
no element found: line 2692, column 0 ./0246_CsPbBr3_mp-600089_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 256/3600 [00:10<02:32, 21.92it/s]
no element found: line 1252, column 0 ./0255_CsPbBr3_mp-600089_2x2x1_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 266/3600 [00:11<02:39, 20.96it/s]
no element found: line 2098, column 0 ./0265_CsPbBr3_mp-600089_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 274/3600 [00:11<02:29, 22.31it/s]
no element found: line 2148, column 0 ./0272_CsPbBr3_mp-600089_2x2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 299/3600 [00:13<02:48, 19.62it/s]
no element found: line 2247, column 0 ./0297_CsPbBr3_mp-600089_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1509, column 0 ./0300_CsPbBr3_mp-600089_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1687, column 0 ./0302_CsPbBr3_mp-600089_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▊         | 313/3600 [00:13<02:17, 23.93it/s]
no element found: line 2343, column 0 ./0309_CsPbBr3_mp-600089_2x2x2_with_noise_16
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2338, column 0 ./0310_CsPbBr3_mp-600089_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1111, column 0 ./0311_CsPbBr3_mp-600089_2x2x2_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3521, column 0 ./0312_CsPbBr3_mp-600089_2x2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 320/3600 [00:14<02:37, 20.88it/s]
no element found: line 1520, column 0 ./0319_CsPbBr3_mp-600089_2x2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 8752, column 0 ./0321_CsPbBr3_mp-600089_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 328/3600 [00:14<02:35, 21.02it/s]
no element found: line 3134, column 0 ./0325_CsPbBr3_mp-600089_2x2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1781, column 0 ./0327_CsPbBr3_mp-600089_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 340/3600 [00:15<03:09, 17.20it/s]
no element found: line 1952, column 0 ./0339_CsPbBr3_mp-600089_2x2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 353/3600 [00:16<03:21, 16.09it/s]
no element found: line 2303, column 0 ./0351_CsPbBr3_mp-600089_2x2x2_with_noise_54
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 358/3600 [00:16<03:02, 17.72it/s]
no element found: line 1147, column 0 ./0357_CsPbBr3_mp-600089_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|█         | 371/3600 [00:17<03:18, 16.27it/s]
no element found: line 2640, column 0 ./0370_CsPbBr3_mp-600089_2x2x2_with_noise_71
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 392/3600 [00:18<03:20, 16.00it/s]
no element found: line 3418, column 0 ./0391_CsPbBr3_mp-600089_2x2x2_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3148, column 0 ./0393_CsPbBr3_mp-600089_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2640, column 0 ./0395_CsPbBr3_mp-600089_2x2x2_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 398/3600 [00:18<02:47, 19.07it/s]
no element found: line 3683, column 0 ./0397_CsPbBr3_mp-600089_2x2x2_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 403/3600 [00:18<02:38, 20.18it/s]
no element found: line 3467, column 0 ./0400_CsPbBr3_mp-600089_2x2x2_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▎        | 493/3600 [00:22<01:52, 27.68it/s]
no element found: line 1113, column 0 ./0491_CsPbBr3_mp-600089_r2xr2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▍        | 517/3600 [00:23<02:00, 25.63it/s]
no element found: line 2079, column 0 ./0514_CsPbBr3_mp-600089_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1692, column 0 ./0515_CsPbBr3_mp-600089_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2039, column 0 ./0519_CsPbBr3_mp-600089_r2xr2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2543, column 0 ./0523_CsPbBr3_mp-600089_r2xr2x2_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 530/3600 [00:23<01:59, 25.61it/s]
no element found: line 1589, column 0 ./0531_CsPbBr3_mp-600089_r2xr2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2111, column 0 ./0536_CsPbBr3_mp-600089_r2xr2x2_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
 16%|█▌        | 559/3600 [00:24<02:08, 23.65it/s]
no element found: line 1490, column 0 ./0558_CsPbBr3_mp-600089_r2xr2x2_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 16%|█▌        | 571/3600 [00:25<02:07, 23.67it/s]
no element found: line 1476, column 0 ./0569_CsPbBr3_mp-600089_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 16%|█▋        | 594/3600 [00:26<02:14, 22.37it/s]
no element found: line 1422, column 0 ./0598_CsPbBr3_mp-600089_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 684/3600 [00:29<01:51, 26.24it/s]
no element found: line 6407, column 0 ./0685_CsPbCl3_mp-23037_1x1x1_with_noise_85
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 698/3600 [00:30<01:47, 26.89it/s]
no element found: line 3339, column 0 ./0701_CsPbCl3_mp-23037_2x1x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 20%|█▉        | 718/3600 [00:31<01:50, 26.09it/s]
no element found: line 932, column 0 ./0716_CsPbCl3_mp-23037_2x1x1_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3005, column 0 ./0723_CsPbCl3_mp-23037_2x1x1_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 21%|██        | 758/3600 [00:32<01:53, 25.03it/s]
no element found: line 1439, column 0 ./0759_CsPbCl3_mp-23037_2x1x1_with_noise_61
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2010, column 0 ./0760_CsPbCl3_mp-23037_2x1x1_with_noise_62
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 817/3600 [00:35<02:19, 19.90it/s]
no element found: line 2373, column 0 ./0820_CsPbCl3_mp-23037_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 830/3600 [00:35<01:42, 27.10it/s]
no element found: line 2094, column 0 ./0825_CsPbCl3_mp-23037_2x2x1_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2998, column 0 ./0826_CsPbCl3_mp-23037_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 834/3600 [00:35<01:59, 23.08it/s]
no element found: line 2175, column 0 ./0835_CsPbCl3_mp-23037_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 844/3600 [00:36<02:13, 20.70it/s]
no element found: line 1198, column 0 ./0849_CsPbCl3_mp-23037_2x2x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 857/3600 [00:37<02:11, 20.85it/s]
no element found: line 1504, column 0 ./0858_CsPbCl3_mp-23037_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 869/3600 [00:37<01:45, 25.93it/s]
no element found: line 1779, column 0 ./0865_CsPbCl3_mp-23037_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
 25%|██▌       | 910/3600 [00:39<02:07, 21.10it/s]
no element found: line 2046, column 0 ./0906_CsPbCl3_mp-23037_2x2x2_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2316, column 0 ./0908_CsPbCl3_mp-23037_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 923/3600 [00:40<02:51, 15.58it/s]
no element found: line 1201, column 0 ./0922_CsPbCl3_mp-23037_2x2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 927/3600 [00:41<03:05, 14.40it/s]
no element found: line 1057, column 0 ./0928_CsPbCl3_mp-23037_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1174, column 0 ./0931_CsPbCl3_mp-23037_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 937/3600 [00:41<02:24, 18.43it/s]
could not convert string to float: '****************' ./0935_CsPbCl3_mp-23037_2x2x2_with_noise_4
<class 'ValueError'> 21
 26%|██▌       | 940/3600 [00:41<02:54, 15.25it/s]
no element found: line 2190, column 0 ./0942_CsPbCl3_mp-23037_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▋       | 952/3600 [00:42<02:53, 15.24it/s]
no element found: line 1138, column 0 ./0953_CsPbCl3_mp-23037_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3701, column 0 ./0955_CsPbCl3_mp-23037_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 962/3600 [00:42<02:13, 19.82it/s]
no element found: line 1488, column 0 ./0961_CsPbCl3_mp-23037_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 973/3600 [00:43<02:19, 18.82it/s]
no element found: line 2703, column 0 ./0969_CsPbCl3_mp-23037_2x2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
could not convert string to float: '****************' ./0973_CsPbCl3_mp-23037_2x2x2_with_noise_74
<class 'ValueError'> 21
 27%|██▋       | 980/3600 [00:44<02:15, 19.27it/s]
no element found: line 3112, column 0 ./0975_CsPbCl3_mp-23037_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 983/3600 [00:44<02:42, 16.07it/s]
could not convert string to float: '****************' ./0982_CsPbCl3_mp-23037_2x2x2_with_noise_82
<class 'ValueError'> 21
no element found: line 6089, column 0 ./0983_CsPbCl3_mp-23037_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1012, column 0 ./0987_CsPbCl3_mp-23037_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1137/3600 [00:50<01:28, 27.87it/s]
no element found: line 1256, column 0 ./1134_CsPbCl3_mp-23037_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1976, column 0 ./1135_CsPbCl3_mp-23037_r2xr2x2_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1148/3600 [00:51<01:24, 28.99it/s]
no element found: line 3641, column 0 ./1143_CsPbCl3_mp-23037_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 8006, column 0 ./1149_CsPbCl3_mp-23037_r2xr2x2_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1153/3600 [00:51<01:41, 24.13it/s]
no element found: line 3596, column 0 ./1152_CsPbCl3_mp-23037_r2xr2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 33%|███▎      | 1175/3600 [00:52<01:30, 26.84it/s]
no element found: line 2939, column 0 ./1169_CsPbCl3_mp-23037_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 10958, column 0 ./1176_CsPbCl3_mp-23037_r2xr2x2_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 38%|███▊      | 1351/3600 [00:59<01:31, 24.65it/s]
no element found: line 4913, column 0 ./1352_CsPbI3_mp-1069538_2x1x1_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 39%|███▉      | 1411/3600 [01:01<01:06, 32.87it/s]
no element found: line 1441, column 0 ./1405_CsPbI3_mp-1069538_2x2x1_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1207, column 0 ./1406_CsPbI3_mp-1069538_2x2x1_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1527, column 0 ./1407_CsPbI3_mp-1069538_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1486, column 0 ./1408_CsPbI3_mp-1069538_2x2x1_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|███▉      | 1428/3600 [01:02<01:23, 26.11it/s]
no element found: line 2152, column 0 ./1429_CsPbI3_mp-1069538_2x2x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|███▉      | 1438/3600 [01:02<01:22, 26.25it/s]
no element found: line 1693, column 0 ./1436_CsPbI3_mp-1069538_2x2x1_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 901, column 0 ./1440_CsPbI3_mp-1069538_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2670, column 0 ./1442_CsPbI3_mp-1069538_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|████      | 1449/3600 [01:03<01:18, 27.51it/s]
no element found: line 2949, column 0 ./1444_CsPbI3_mp-1069538_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████      | 1460/3600 [01:03<01:18, 27.10it/s]
no element found: line 4312, column 0 ./1458_CsPbI3_mp-1069538_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████      | 1475/3600 [01:04<01:45, 20.21it/s]
no element found: line 3421, column 0 ./1478_CsPbI3_mp-1069538_2x2x1_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████▏     | 1489/3600 [01:04<01:23, 25.28it/s]
no element found: line 2143, column 0 ./1488_CsPbI3_mp-1069538_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1513, column 0 ./1491_CsPbI3_mp-1069538_2x2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1500/3600 [01:05<01:18, 26.68it/s]
no element found: line 1243, column 0 ./1497_CsPbI3_mp-1069538_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3476, column 0 ./1502_CsPbI3_mp-1069538_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1509/3600 [01:05<01:26, 24.14it/s]
no element found: line 1165, column 0 ./1508_CsPbI3_mp-1069538_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1673, column 0 ./1510_CsPbI3_mp-1069538_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1519/3600 [01:06<01:23, 24.94it/s]
no element found: line 10779, column 0 ./1513_CsPbI3_mp-1069538_2x2x2_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1300, column 0 ./1515_CsPbI3_mp-1069538_2x2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1516_CsPbI3_mp-1069538_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2275, column 0 ./1517_CsPbI3_mp-1069538_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1528/3600 [01:06<01:33, 22.27it/s]
no element found: line 2851, column 0 ./1524_CsPbI3_mp-1069538_2x2x2_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1691, column 0 ./1531_CsPbI3_mp-1069538_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1550/3600 [01:07<01:32, 22.04it/s]
no element found: line 3310, column 0 ./1544_CsPbI3_mp-1069538_2x2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1057, column 0 ./1548_CsPbI3_mp-1069538_2x2x2_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1560/3600 [01:08<01:28, 23.09it/s]
no element found: line 1664, column 0 ./1552_CsPbI3_mp-1069538_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1264, column 0 ./1553_CsPbI3_mp-1069538_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2231, column 0 ./1555_CsPbI3_mp-1069538_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1557_CsPbI3_mp-1069538_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2204, column 0 ./1561_CsPbI3_mp-1069538_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 648, column 0 ./1562_CsPbI3_mp-1069538_2x2x2_with_noise_64
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1577/3600 [01:09<01:42, 19.70it/s]
no element found: line 6686, column 0 ./1573_CsPbI3_mp-1069538_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1578_CsPbI3_mp-1069538_2x2x2_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1966, column 0 ./1579_CsPbI3_mp-1069538_2x2x2_with_noise_8
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1012, column 0 ./1580_CsPbI3_mp-1069538_2x2x2_with_noise_80
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1590/3600 [01:09<01:25, 23.41it/s]
no element found: line 2671, column 0 ./1586_CsPbI3_mp-1069538_2x2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2239, column 0 ./1588_CsPbI3_mp-1069538_2x2x2_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3903, column 0 ./1593_CsPbI3_mp-1069538_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 967, column 0 ./1594_CsPbI3_mp-1069538_2x2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 46%|████▋     | 1669/3600 [01:12<00:59, 32.50it/s]
no element found: line 1518, column 0 ./1672_CsPbI3_mp-1069538_r2xr2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1722/3600 [01:14<01:06, 28.38it/s]
no element found: line 864, column 0 ./1718_CsPbI3_mp-1069538_r2xr2x2_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1215, column 0 ./1725_CsPbI3_mp-1069538_r2xr2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
 49%|████▊     | 1751/3600 [01:15<01:05, 28.34it/s]
no element found: line 855, column 0 ./1744_CsPbI3_mp-1069538_r2xr2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 49%|████▉     | 1762/3600 [01:16<01:10, 26.15it/s]
no element found: line 927, column 0 ./1764_CsPbI3_mp-1069538_r2xr2x2_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2376, column 0 ./1767_CsPbI3_mp-1069538_r2xr2x2_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
 50%|█████     | 1805/3600 [01:18<00:59, 30.41it/s]
no element found: line 909, column 0 ./1794_CsPbI3_mp-1069538_r2xr2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1980, column 0 ./1799_CsPbI3_mp-1069538_r2xr2x2_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 51%|█████     | 1832/3600 [01:18<00:55, 32.12it/s]
no element found: line 5618, column 0 ./1829_CsSnBr3_mp-27214_1x1x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
 51%|█████▏    | 1847/3600 [01:19<00:52, 33.24it/s]
no element found: line 6110, column 0 ./1839_CsSnBr3_mp-27214_1x1x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 53%|█████▎    | 1918/3600 [01:22<00:55, 30.39it/s]
no element found: line 2254, column 0 ./1911_CsSnBr3_mp-27214_2x1x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
 54%|█████▎    | 1931/3600 [01:22<00:54, 30.38it/s]
no element found: line 2139, column 0 ./1924_CsSnBr3_mp-27214_2x1x1_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 55%|█████▌    | 1986/3600 [01:24<00:53, 30.43it/s]
no element found: line 1538, column 0 ./1984_CsSnBr3_mp-27214_2x1x1_with_noise_84
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2002/3600 [01:25<00:50, 31.87it/s]
no element found: line 1196, column 0 ./1999_CsSnBr3_mp-27214_2x1x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1572, column 0 ./2001_CsSnBr3_mp-27214_2x2x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2015/3600 [01:25<00:55, 28.58it/s]
no element found: line 1554, column 0 ./2011_CsSnBr3_mp-27214_2x2x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▋    | 2033/3600 [01:26<00:50, 31.14it/s]
no element found: line 1518, column 0 ./2026_CsSnBr3_mp-27214_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2045/3600 [01:26<00:55, 28.15it/s]
no element found: line 1527, column 0 ./2035_CsSnBr3_mp-27214_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2539, column 0 ./2042_CsSnBr3_mp-27214_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3318, column 0 ./2046_CsSnBr3_mp-27214_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1518, column 0 ./2048_CsSnBr3_mp-27214_2x2x1_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2057/3600 [01:27<00:56, 27.16it/s]
[Errno 2] No such file or directory: './vasprun.xml' ./2055_CsSnBr3_mp-27214_2x2x1_with_noise_58
<class 'FileNotFoundError'> 13
no element found: line 1509, column 0 ./2061_CsSnBr3_mp-27214_2x2x1_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 58%|█████▊    | 2088/3600 [01:28<00:49, 30.76it/s]
no element found: line 3003, column 0 ./2083_CsSnBr3_mp-27214_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1284, column 0 ./2086_CsSnBr3_mp-27214_2x2x1_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2122/3600 [01:30<01:04, 22.76it/s]
no element found: line 2105, column 0 ./2114_CsSnBr3_mp-27214_2x2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1192, column 0 ./2116_CsSnBr3_mp-27214_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2130/3600 [01:31<01:19, 18.51it/s]
no element found: line 8411, column 0 ./2131_CsSnBr3_mp-27214_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2138/3600 [01:31<01:22, 17.70it/s]
no element found: line 3404, column 0 ./2135_CsSnBr3_mp-27214_2x2x2_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2204, column 0 ./2142_CsSnBr3_mp-27214_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|██████    | 2164/3600 [01:33<01:14, 19.17it/s]
no element found: line 1952, column 0 ./2161_CsSnBr3_mp-27214_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|██████    | 2176/3600 [01:33<01:10, 20.22it/s]
no element found: line 2613, column 0 ./2177_CsSnBr3_mp-27214_2x2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2188/3600 [01:34<01:07, 20.80it/s]
no element found: line 1435, column 0 ./2189_CsSnBr3_mp-27214_2x2x2_with_noise_89
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2886, column 0 ./2190_CsSnBr3_mp-27214_2x2x2_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2202/3600 [01:35<00:57, 24.11it/s]
no element found: line 2635, column 0 ./2196_CsSnBr3_mp-27214_2x2x2_with_noise_95
<class 'xml.etree.ElementTree.ParseError'> 13
 62%|██████▏   | 2236/3600 [01:36<00:44, 30.93it/s]
no element found: line 1473, column 0 ./2238_CsSnBr3_mp-27214_r2xr2x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
 64%|██████▍   | 2309/3600 [01:38<00:41, 30.89it/s]
no element found: line 2241, column 0 ./2304_CsSnBr3_mp-27214_r2xr2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5873, column 0 ./2310_CsSnBr3_mp-27214_r2xr2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 65%|██████▌   | 2341/3600 [01:40<00:44, 28.30it/s]
no element found: line 2201, column 0 ./2333_CsSnBr3_mp-27214_r2xr2x2_with_noise_38
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3434, column 0 ./2334_CsSnBr3_mp-27214_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5774, column 0 ./2339_CsSnBr3_mp-27214_r2xr2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3438, column 0 ./2343_CsSnBr3_mp-27214_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
 66%|██████▌   | 2365/3600 [01:40<00:39, 31.64it/s]
could not convert string to float: '****************' ./2354_CsSnBr3_mp-27214_r2xr2x2_with_noise_57
<class 'ValueError'> 21
no element found: line 2876, column 0 ./2357_CsSnBr3_mp-27214_r2xr2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 67%|██████▋   | 2406/3600 [01:42<00:44, 27.04it/s]
no element found: line 5855, column 0 ./2398_CsSnBr3_mp-27214_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 70%|██████▉   | 2510/3600 [01:46<00:38, 28.68it/s]
no element found: line 1383, column 0 ./2503_CsSnCl3_mp-1070375_2x1x1_with_noise_100
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████   | 2553/3600 [01:47<00:29, 35.05it/s]
no element found: line 2040, column 0 ./2546_CsSnCl3_mp-1070375_2x1x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████▏  | 2567/3600 [01:48<00:33, 30.53it/s]
no element found: line 2641, column 0 ./2564_CsSnCl3_mp-1070375_2x1x1_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5341, column 0 ./2574_CsSnCl3_mp-1070375_2x1x1_with_noise_75
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▏  | 2591/3600 [01:49<00:28, 35.87it/s]
no element found: line 1975, column 0 ./2592_CsSnCl3_mp-1070375_2x1x1_with_noise_91
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▏  | 2604/3600 [01:49<00:33, 29.36it/s]
no element found: line 1261, column 0 ./2607_CsSnCl3_mp-1070375_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
 73%|███████▎  | 2618/3600 [01:50<00:36, 26.95it/s]
no element found: line 2071, column 0 ./2612_CsSnCl3_mp-1070375_2x2x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 4461, column 0 ./2613_CsSnCl3_mp-1070375_2x2x1_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▎  | 2652/3600 [01:52<00:37, 25.09it/s]
no element found: line 1477, column 0 ./2642_CsSnCl3_mp-1070375_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1824, column 0 ./2646_CsSnCl3_mp-1070375_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▍  | 2669/3600 [01:52<00:38, 24.33it/s]
no element found: line 4254, column 0 ./2667_CsSnCl3_mp-1070375_2x2x1_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3165, column 0 ./2673_CsSnCl3_mp-1070375_2x2x1_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▍  | 2686/3600 [01:53<00:34, 26.52it/s]
no element found: line 1563, column 0 ./2688_CsSnCl3_mp-1070375_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▌  | 2702/3600 [01:54<00:33, 26.50it/s]
no element found: line 1549, column 0 ./2700_CsSnCl3_mp-1070375_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▌  | 2715/3600 [01:55<00:41, 21.50it/s]
no element found: line 5081, column 0 ./2717_CsSnCl3_mp-1070375_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▌  | 2729/3600 [01:55<00:38, 22.84it/s]
no element found: line 2374, column 0 ./2727_CsSnCl3_mp-1070375_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1723, column 0 ./2728_CsSnCl3_mp-1070375_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./2732_CsSnCl3_mp-1070375_2x2x2_with_noise_37
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▋  | 2753/3600 [01:57<00:44, 19.23it/s]
could not convert string to float: '****************' ./2748_CsSnCl3_mp-1070375_2x2x2_with_noise_51
<class 'ValueError'> 21
 77%|███████▋  | 2769/3600 [01:58<00:42, 19.60it/s]
could not convert string to float: '****************' ./2766_CsSnCl3_mp-1070375_2x2x2_with_noise_68
<class 'ValueError'> 21
 77%|███████▋  | 2778/3600 [01:58<00:46, 17.49it/s]
no element found: line 4317, column 0 ./2773_CsSnCl3_mp-1070375_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2838, column 0 ./2775_CsSnCl3_mp-1070375_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 77%|███████▋  | 2783/3600 [01:59<00:37, 21.56it/s]
no element found: line 2559, column 0 ./2782_CsSnCl3_mp-1070375_2x2x2_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1102, column 0 ./2787_CsSnCl3_mp-1070375_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 78%|███████▊  | 2821/3600 [02:00<00:23, 32.94it/s]
no element found: line 1176, column 0 ./2810_CsSnCl3_mp-1070375_r2xr2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 80%|████████  | 2888/3600 [02:02<00:18, 38.03it/s]
no element found: line 1800, column 0 ./2876_CsSnCl3_mp-1070375_r2xr2x1_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 81%|████████▏ | 2927/3600 [02:04<00:21, 31.38it/s]
no element found: line 2543, column 0 ./2922_CsSnCl3_mp-1070375_r2xr2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
could not convert string to float: '****************' ./2925_CsSnCl3_mp-1070375_r2xr2x2_with_noise_30
<class 'ValueError'> 21
 87%|████████▋ | 3115/3600 [02:11<00:13, 35.73it/s]
no element found: line 4333, column 0 ./3112_CsSnI3_mp-614013_2x1x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
 87%|████████▋ | 3136/3600 [02:12<00:13, 35.09it/s]
no element found: line 2083, column 0 ./3134_CsSnI3_mp-614013_2x1x1_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3157/3600 [02:13<00:12, 34.97it/s]
no element found: line 2394, column 0 ./3150_CsSnI3_mp-614013_2x1x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3178/3600 [02:14<00:12, 34.13it/s]
no element found: line 7073, column 0 ./3166_CsSnI3_mp-614013_2x1x1_with_noise_68
<class 'xml.etree.ElementTree.ParseError'> 13
 89%|████████▉ | 3212/3600 [02:15<00:15, 25.45it/s]
no element found: line 22857, column 0 ./3206_CsSnI3_mp-614013_2x2x1_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1374, column 0 ./3210_CsSnI3_mp-614013_2x2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2062, column 0 ./3217_CsSnI3_mp-614013_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1338, column 0 ./3218_CsSnI3_mp-614013_2x2x1_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|████████▉ | 3226/3600 [02:15<00:10, 36.36it/s]
no element found: line 1716, column 0 ./3220_CsSnI3_mp-614013_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 3245/3600 [02:16<00:11, 30.66it/s]
no element found: line 1450, column 0 ./3244_CsSnI3_mp-614013_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 3256/3600 [02:17<00:14, 23.20it/s]
no element found: line 3561, column 0 ./3250_CsSnI3_mp-614013_2x2x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 91%|█████████▏| 3285/3600 [02:18<00:09, 32.47it/s]
no element found: line 4227, column 0 ./3275_CsSnI3_mp-614013_2x2x1_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1869, column 0 ./3283_CsSnI3_mp-614013_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3297/3600 [02:19<00:12, 24.63it/s]
no element found: line 1576, column 0 ./3290_CsSnI3_mp-614013_2x2x1_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3241, column 0 ./3295_CsSnI3_mp-614013_2x2x1_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1284, column 0 ./3299_CsSnI3_mp-614013_2x2x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3303/3600 [02:19<00:10, 28.82it/s]
no element found: line 1821, column 0 ./3304_CsSnI3_mp-614013_2x2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1664, column 0 ./3305_CsSnI3_mp-614013_2x2x2_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3319/3600 [02:19<00:10, 25.78it/s]
no element found: line 7557, column 0 ./3310_CsSnI3_mp-614013_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1156, column 0 ./3314_CsSnI3_mp-614013_2x2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1439, column 0 ./3317_CsSnI3_mp-614013_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2365, column 0 ./3320_CsSnI3_mp-614013_2x2x2_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3325/3600 [02:20<00:09, 30.42it/s]
no element found: line 2325, column 0 ./3321_CsSnI3_mp-614013_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3339/3600 [02:20<00:11, 22.81it/s]
no element found: line 5760, column 0 ./3333_CsSnI3_mp-614013_2x2x2_with_noise_38
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3353/3600 [02:21<00:11, 21.36it/s]
no element found: line 2401, column 0 ./3345_CsSnI3_mp-614013_2x2x2_with_noise_49
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 976, column 0 ./3352_CsSnI3_mp-614013_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3375/3600 [02:22<00:08, 25.64it/s]
no element found: line 1057, column 0 ./3371_CsSnI3_mp-614013_2x2x2_with_noise_72
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2203, column 0 ./3373_CsSnI3_mp-614013_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 22984, column 0 ./3376_CsSnI3_mp-614013_2x2x2_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3388/3600 [02:23<00:10, 20.90it/s]
no element found: line 3341, column 0 ./3383_CsSnI3_mp-614013_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3392/3600 [02:23<00:08, 23.92it/s]
no element found: line 2640, column 0 ./3394_CsSnI3_mp-614013_2x2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3521/3600 [02:28<00:02, 38.49it/s]
no element found: line 1679, column 0 ./3512_CsSnI3_mp-614013_r2xr2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3510, column 0 ./3514_CsSnI3_mp-614013_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1467, column 0 ./3515_CsSnI3_mp-614013_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3540/3600 [02:29<00:01, 31.11it/s]
no element found: line 2750, column 0 ./3530_CsSnI3_mp-614013_r2xr2x2_with_noise_35
<class 'xml.etree.ElementTree.ParseError'> 13
100%|█████████▉| 3582/3600 [02:31<00:00, 24.17it/s]
no element found: line 1643, column 0 ./3572_CsSnI3_mp-614013_r2xr2x2_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1647, column 0 ./3577_CsSnI3_mp-614013_r2xr2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 4694, column 0 ./3583_CsSnI3_mp-614013_r2xr2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
100%|█████████▉| 3596/3600 [02:31<00:00, 35.76it/s]
no element found: line 2858, column 0 ./3586_CsSnI3_mp-614013_r2xr2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [02:31<00:00, 23.69it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 236
```

* 대부분 ParsingError, 일부는 알 수 없는 원인의 ValueError, FileNotFoundError 존재
* 다시 계산하기에는 너무 많으므로 일단 재계산은 보류한다.
* noiselevel 0.01 데이터셋을 우선 사용하고, 0.05는 어쩔 수 없는 경우에만 추가로 사용
* 데이터 불균형으로 regression 성능에 영향을 줄 가능성이 있음.



### 1st MD 데이터셋

* Ab-initio MD simulation : Defect을 최대 2개까지 주고, unitcell size도 각각 다름.
* 계산 초기의 INCAR 옵션은 다음과 같다.

``` Python
SYSTEM = NiPS3
   # PREC = high
   EDIFF  = 1E-06      # energy stopping-criterion for ELM
   LCHARG = .TRUE.     # determines whether the charge densities (CHGCAR/CHG) are written.
   ISMEAR = 1          # (-1-Fermi, 1-Methfessel/Paxton 2-Gaussian)
   SIGMA  = 0.1        # broadening in eV

   NELMIN = 12         # specifies the minimum number of electronic SCF steps.
   NELM   = 60
   # EDIFFG = -0.0001  # force (eV/A) stopping-criterion for geometry steps
   ISYM   = 0          # (1-use symmetry, 0-no symmetry)
   LORBIT = 12         # determines whether the PROCAR or PROOUT are written together with appropriate RWIGS.

   IBRION =  0       # ionic relax: 0-MD, 1-quasi-Newton, 2-CG, 3-Damped MD
   POTIM  =  8.00    # initial time step for geo-opt (increase for soft sys) / time interval[fs]
   NSW    =  4000    # Max number of Geometry steps / Number of Time Snapshot
   TEBEG  =  1000    # Start Temperature for MD (IBRION=0)
   MDALGO =  3       # specifies the MD simulation protocol / Langevin thermostat
   ISIF   =  3       # determines whether the stress tensor is calculated and which principal degrees of freedom are allowed in relaxation and MD.
   SMASS  =  1.0     # controls the velocities during MD / A canonical ensembel is simulated.

   LWAVE  = F   # determines whether the wavefunctions are written to the WAVECAR file at the end of a run.
   LCHARG = F   # determines whether the charge densities (CHGCAR, CHG) are written.

   ISPIN = 1    # specifies spin polarization / Non-spin polarized calculations are performed.

   ISTART = 1   # determines whether or not to read the WAVECAR file.
   ICHARG = 1   # determines how VASP constructs the initial charge density / Read the charge density from CHGCAR.

   NPAR = 2     # determines the number of bands that are treated in parallel / Number of cores
   KPAR = 4     # determines the number of k-points that are to be treated in parallel

```

* 파싱 결과는 다음과 같았다.

``` Python
 45%|████▌     | 27/60 [02:25<02:23,  4.35s/it]
no element found: line 1119004, column 0 ./27.CsPbI3-rm-I2
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 60/60 [05:44<00:00,  5.74s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 1
```

* ? 의외로 파싱에러가 안 된 것은 1개뿐인데, 아마 에너지가 불안정한 상태가 많아서 에너지 제한조건을 걸었을 때 많이 삭제 된것으로 기억한다. 그래서 2nd MD를 돌렸다.
* 재계산 : 기존의 INCAR에서 NSW: 4000 -> 2000으로 줄이고 다시 **계산 진행중...**



### 2nd MD 데이터셋

* Ab-initio MD simulation : Defect을 최대 2개까지 주고, unitcell size도 각각 다름.
* 1차 MD에 비해 계산 지속이 조금 더 오래되도록 INCAR 옵션 조정되었음 : POTIM=5.00, NSW=7000, TEBEG=500으로 수정
* 2nd MD INCAR 옵션은 아래와 같다.

``` Python
SYSTEM = NiPS3
   # PREC = high
   EDIFF  = 1E-06      # energy stopping-criterion for ELM
   LCHARG = .TRUE.     # determines whether the charge densities (CHGCAR/CHG) are written.
   ISMEAR = 1          # (-1-Fermi, 1-Methfessel/Paxton 2-Gaussian)
   SIGMA  = 0.1        # broadening in eV

   NELMIN = 12         # specifies the minimum number of electronic SCF steps.
   NELM   = 60
   # EDIFFG = -0.0001  # force (eV/A) stopping-criterion for geometry steps
   ISYM   = 0          # (1-use symmetry, 0-no symmetry)
   LORBIT = 12         # determines whether the PROCAR or PROOUT are written together with appropriate RWIGS.

   IBRION =  0       # ionic relax: 0-MD, 1-quasi-Newton, 2-CG, 3-Damped MD
   POTIM  =  5.00    # initial time step for geo-opt (increase for soft sys) / time interval[fs]
   NSW    =  7000    # Max number of Geometry steps / Number of Time Snapshot
   TEBEG  =  500     # Start Temperature for MD (IBRION=0)
   MDALGO =  3       # specifies the MD simulation protocol / Langevin thermostat
   ISIF   =  3       # determines whether the stress tensor is calculated and which principal degrees of freedom are allowed in relaxation and MD.
   SMASS  =  1.0     # controls the velocities during MD / A canonical ensembel is simulated.

   LWAVE  = F   # determines whether the wavefunctions are written to the WAVECAR file at the end of a run.
   LCHARG = F   # determines whether the charge densities (CHGCAR, CHG) are written.

   ISPIN = 1    # specifies spin polarization / Non-spin polarized calculations are performed.

   ISTART = 1   # determines whether or not to read the WAVECAR file.
   ICHARG = 1   # determines how VASP constructs the initial charge density / Read the charge density from CHGCAR.

   NPAR = 2     # determines the number of bands that are treated in parallel / Number of cores
   KPAR = 4     # determines the number of k-points that are to be treated in parallel

```

* 파싱 결과는 다음과 같다.

``` Python
 20%|██        | 12/60 [01:42<06:43,  8.41s/it]
no element found: line 2030, column 0 ./13.CsPbCl3-rm-Pb1
<class 'xml.etree.ElementTree.ParseError'> 13
 30%|███       | 18/60 [02:22<04:37,  6.60s/it]
no element found: line 2511749, column 0 ./18.CsPbCl3-rm-Cs1-Pb1
<class 'xml.etree.ElementTree.ParseError'> 13
 62%|██████▏   | 37/60 [05:12<02:34,  6.72s/it]
no element found: line 1653055, column 0 ./37.CsSnBr3-rm-Br2
<class 'xml.etree.ElementTree.ParseError'> 13
 77%|███████▋  | 46/60 [06:28<01:28,  6.34s/it]
no element found: line 702803, column 0 ./46.CsSnCl3-rm-Sn2
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 53/60 [07:26<00:54,  7.74s/it]
no element found: line 2384030, column 0 ./53.CsSnI3-rm-Sn1
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 54/60 [07:29<00:36,  6.11s/it]
no element found: line 2442044, column 0 ./54.CsSnI3-rm-I1
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 60/60 [08:30<00:00,  8.50s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 6
```

* 6개의 ParsingError 발생 : 모두 계산수렴이 안되서 발생하는 에러
* 재계산 : 기존의 INCAR에서 NSW: 7000 -> 4000으로 바꿔서 다시 계산 완료 -> **파싱만 다시하면 됨.**

---
