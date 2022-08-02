
## 데이터 관련 기록

### Noise01 Dataset

* DFT Simulation with noise between -0.01 ~ 0.01 for atom coordinates
* 3600개의 계산폴더 존재
* 초기 INCAR 구성은 다음과 같다.

``` Shell
SYSTEM = CsPbBr3
ISTART = 0       # Start option
ICHARG = 2       # Charge density file read or not

GGA = PS         # Perdew-Burke-Ernzerhof revised for solids (PBEsol)
ENCUT = 400      # Energy cutoff (eV)

ISIF = 4         # Calculation of (forces / stress tensor / positions / cell shape) / cell volume fixed
IBRION = 2       # Optimization algorithm = Conjugate Gradient (CG) algorithm

NSW = 50         # Number of SCF steps
EDIFF = 1E-6     # Energy convergence
EDIFFG = -1E-4   # Break condition of force
LREAL = Auto     # Projection done in real space, fully automatic optimization of projection operators (little to no user interference required)

NPAR = 4         # determines the number of bands that are treated in parallel
KPAR = 4         # determines the number of k-points that are to be treated in parallel (available as of VASP.5.3.2). Also, used in Laplace transformed MP2 calculations
SIGMA = 0.05     # width of smearing function
ISYM = 0         # Ignore Symmetry (by Professor)
```

* 초기 데이터(tar.gz) 파싱 결과는 다음과 같다.

``` Python
 51%|█████     | 1829/3600 [01:43<01:13, 23.95it/s]
no element found: line 5402, column 0 ./1824_CsSnBr3_mp-27214_1x1x1_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 64%|██████▎   | 2289/3600 [02:06<00:37, 35.08it/s]
not well-formed (invalid token): line 901, column 0 ./2282_CsSnBr3_mp-27214_r2xr2x1_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [03:12<00:00, 18.70it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 2
```

* 기존 데이터셋에서 ParssingError 2개 발생
    - 1824번 폴더는 NSW: 50 -> 36으로 바꿔 재계산
    - 2282번 폴더는 DFT 계산은 정상적으로 종료되었으나, 알 수 없는 ParsingError 발생 -> 데이터 사용 안함
* **이제 데이터 추출(tar.gz)하고 파싱(pickle)한다.**
* 최종 파싱 결과는 다음과 같다.

``` Python
 64%|██████▎   | 2291/3600 [02:05<00:46, 28.13it/s]
not well-formed (invalid token): line 901, column 0 ./2282_CsSnBr3_mp-27214_r2xr2x1_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [03:09<00:00, 18.98it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 1
```

* 재계산한 1824번 폴더는 NSW = 36에서 수렴된 것 같다.
* 전체 데이터포인트 수 = 28792


### Noise05 Dataset

* DFT Simulation with noise between -0.05 ~ 0.05 for atom coordinates
* Noise01 데이터셋에 비해 더 많은 비정상적인 계산종료 발생 : 약 236개의 비수렴파일에서 파싱에러
* 초기 INCAR 구성은 Noise01과 같다.

``` Shell
SYSTEM = CsPbBr3
ISTART = 0       # Start option
ICHARG = 2       # Charge density file read or not

GGA = PS         # Perdew-Burke-Ernzerhof revised for solids (PBEsol)
ENCUT = 400      # Energy cutoff (eV)

ISIF = 4         # Calculation of (forces / stress tensor / positions / cell shape) / cell volume fixed
IBRION = 2       # Optimization algorithm = Conjugate Gradient (CG) algorithm

NSW = 50         # Number of SCF steps
EDIFF = 1E-6     # Energy convergence
EDIFFG = -1E-4   # Break condition of force
LREAL = Auto     # Projection done in real space, fully automatic optimization of projection operators (little to no user interference required)

NPAR = 4         # determines the number of bands that are treated in parallel
KPAR = 4         # determines the number of k-points that are to be treated in parallel (available as of VASP.5.3.2). Also, used in Laplace transformed MP2 calculations
SIGMA = 0.05     # width of smearing function
ISYM = 0         # Ignore Symmetry (by Professor)
```

* 초기 파싱 결과는 다음과 같다.


``` Python
  1%|▏         | 47/3600 [00:02<03:21, 17.67it/s]
no element found: line 6425, column 0 ./0044_CsPbBr3_mp-600089_1x1x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 91/3600 [00:05<03:18, 17.72it/s]
no element found: line 3056, column 0 ./0088_CsPbBr3_mp-600089_1x1x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 104/3600 [00:06<03:14, 18.02it/s]
no element found: line 1493, column 0 ./0102_CsPbBr3_mp-600089_2x1x1_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 122/3600 [00:07<03:37, 15.96it/s]
no element found: line 3715, column 0 ./0121_CsPbBr3_mp-600089_2x1x1_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 139/3600 [00:08<03:16, 17.63it/s]
no element found: line 2146, column 0 ./0138_CsPbBr3_mp-600089_2x1x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 152/3600 [00:08<03:15, 17.62it/s]
no element found: line 1391, column 0 ./0149_CsPbBr3_mp-600089_2x1x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 155/3600 [00:09<03:21, 17.08it/s]
no element found: line 8340, column 0 ./0154_CsPbBr3_mp-600089_2x1x1_with_noise_57
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▍         | 175/3600 [00:10<03:34, 15.98it/s]
no element found: line 1004, column 0 ./0174_CsPbBr3_mp-600089_2x1x1_with_noise_75
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▌         | 182/3600 [00:10<03:16, 17.37it/s]
no element found: line 2027, column 0 ./0181_CsPbBr3_mp-600089_2x1x1_with_noise_81
<class 'xml.etree.ElementTree.ParseError'> 13
  6%|▌         | 215/3600 [00:13<03:56, 14.31it/s]
no element found: line 928, column 0 ./0214_CsPbBr3_mp-600089_2x2x1_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1684, column 0 ./0217_CsPbBr3_mp-600089_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
  6%|▌         | 218/3600 [00:13<03:54, 14.40it/s]
no element found: line 3048, column 0 ./0219_CsPbBr3_mp-600089_2x2x1_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 241/3600 [00:14<03:35, 15.57it/s]
no element found: line 1063, column 0 ./0239_CsPbBr3_mp-600089_2x2x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1797, column 0 ./0240_CsPbBr3_mp-600089_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 244/3600 [00:15<03:45, 14.85it/s]
no element found: line 2692, column 0 ./0246_CsPbBr3_mp-600089_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 254/3600 [00:15<03:54, 14.25it/s]
no element found: line 1252, column 0 ./0255_CsPbBr3_mp-600089_2x2x1_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 264/3600 [00:16<03:59, 13.96it/s]
no element found: line 2098, column 0 ./0265_CsPbBr3_mp-600089_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 273/3600 [00:17<03:24, 16.29it/s]
no element found: line 2148, column 0 ./0272_CsPbBr3_mp-600089_2x2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 298/3600 [00:18<03:56, 13.98it/s]
no element found: line 2247, column 0 ./0297_CsPbBr3_mp-600089_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1509, column 0 ./0300_CsPbBr3_mp-600089_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 302/3600 [00:19<03:41, 14.91it/s]
no element found: line 1687, column 0 ./0302_CsPbBr3_mp-600089_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▊         | 308/3600 [00:19<04:22, 12.56it/s]
no element found: line 2343, column 0 ./0309_CsPbBr3_mp-600089_2x2x2_with_noise_16
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2338, column 0 ./0310_CsPbBr3_mp-600089_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1111, column 0 ./0311_CsPbBr3_mp-600089_2x2x2_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3521, column 0 ./0312_CsPbBr3_mp-600089_2x2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 317/3600 [00:20<03:51, 14.19it/s]
no element found: line 1520, column 0 ./0319_CsPbBr3_mp-600089_2x2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 8752, column 0 ./0321_CsPbBr3_mp-600089_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 322/3600 [00:20<03:36, 15.13it/s]
no element found: line 3134, column 0 ./0325_CsPbBr3_mp-600089_2x2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 326/3600 [00:20<03:39, 14.90it/s]
no element found: line 1781, column 0 ./0327_CsPbBr3_mp-600089_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 338/3600 [00:21<04:33, 11.91it/s]
no element found: line 1952, column 0 ./0339_CsPbBr3_mp-600089_2x2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 348/3600 [00:22<04:41, 11.53it/s]
no element found: line 2303, column 0 ./0351_CsPbBr3_mp-600089_2x2x2_with_noise_54
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 355/3600 [00:23<04:35, 11.78it/s]
no element found: line 1147, column 0 ./0357_CsPbBr3_mp-600089_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|█         | 369/3600 [00:24<04:54, 10.97it/s]
no element found: line 2640, column 0 ./0370_CsPbBr3_mp-600089_2x2x2_with_noise_71
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 391/3600 [00:26<04:36, 11.60it/s]
no element found: line 3418, column 0 ./0391_CsPbBr3_mp-600089_2x2x2_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3148, column 0 ./0393_CsPbBr3_mp-600089_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 399/3600 [00:26<03:09, 16.92it/s]
no element found: line 2640, column 0 ./0395_CsPbBr3_mp-600089_2x2x2_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3683, column 0 ./0397_CsPbBr3_mp-600089_2x2x2_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3467, column 0 ./0400_CsPbBr3_mp-600089_2x2x2_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▎        | 489/3600 [00:31<02:50, 18.28it/s]
no element found: line 1113, column 0 ./0491_CsPbBr3_mp-600089_r2xr2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▍        | 513/3600 [00:32<03:13, 15.92it/s]
no element found: line 2079, column 0 ./0514_CsPbBr3_mp-600089_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1692, column 0 ./0515_CsPbBr3_mp-600089_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2039, column 0 ./0519_CsPbBr3_mp-600089_r2xr2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 526/3600 [00:33<02:13, 22.98it/s]
no element found: line 2543, column 0 ./0523_CsPbBr3_mp-600089_r2xr2x2_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 529/3600 [00:33<02:42, 18.92it/s]
no element found: line 1589, column 0 ./0531_CsPbBr3_mp-600089_r2xr2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 533/3600 [00:33<02:56, 17.42it/s]
no element found: line 2111, column 0 ./0536_CsPbBr3_mp-600089_r2xr2x2_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▌        | 557/3600 [00:35<02:57, 17.15it/s]
no element found: line 1490, column 0 ./0558_CsPbBr3_mp-600089_r2xr2x2_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 16%|█▌        | 569/3600 [00:35<02:54, 17.40it/s]
no element found: line 1476, column 0 ./0569_CsPbBr3_mp-600089_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 17%|█▋        | 598/3600 [00:37<03:00, 16.64it/s]
no element found: line 1422, column 0 ./0598_CsPbBr3_mp-600089_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 681/3600 [00:41<02:45, 17.59it/s]
no element found: line 6407, column 0 ./0685_CsPbCl3_mp-23037_1x1x1_with_noise_85
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 701/3600 [00:42<01:51, 26.09it/s]
no element found: line 3339, column 0 ./0701_CsPbCl3_mp-23037_2x1x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 20%|█▉        | 714/3600 [00:43<02:34, 18.63it/s]
no element found: line 932, column 0 ./0716_CsPbCl3_mp-23037_2x1x1_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
 20%|██        | 721/3600 [00:43<02:26, 19.67it/s]
no element found: line 3005, column 0 ./0723_CsPbCl3_mp-23037_2x1x1_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 21%|██        | 761/3600 [00:45<01:49, 25.93it/s]
no element found: line 1439, column 0 ./0759_CsPbCl3_mp-23037_2x1x1_with_noise_61
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2010, column 0 ./0760_CsPbCl3_mp-23037_2x1x1_with_noise_62
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 821/3600 [00:49<03:06, 14.90it/s]
no element found: line 2373, column 0 ./0820_CsPbCl3_mp-23037_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2094, column 0 ./0825_CsPbCl3_mp-23037_2x2x1_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2998, column 0 ./0826_CsPbCl3_mp-23037_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 835/3600 [00:49<02:52, 16.05it/s]
no element found: line 2175, column 0 ./0835_CsPbCl3_mp-23037_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▎       | 848/3600 [00:50<02:58, 15.45it/s]
no element found: line 1198, column 0 ./0849_CsPbCl3_mp-23037_2x2x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 857/3600 [00:51<02:31, 18.08it/s]
no element found: line 1504, column 0 ./0858_CsPbCl3_mp-23037_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 860/3600 [00:51<03:02, 15.05it/s]
no element found: line 1779, column 0 ./0865_CsPbCl3_mp-23037_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
 25%|██▌       | 905/3600 [00:54<03:04, 14.59it/s]
no element found: line 2046, column 0 ./0906_CsPbCl3_mp-23037_2x2x2_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
 25%|██▌       | 911/3600 [00:54<02:58, 15.06it/s]
no element found: line 2316, column 0 ./0908_CsPbCl3_mp-23037_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 923/3600 [00:55<03:02, 14.67it/s]
no element found: line 1201, column 0 ./0922_CsPbCl3_mp-23037_2x2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 926/3600 [00:56<03:46, 11.83it/s]
no element found: line 1057, column 0 ./0928_CsPbCl3_mp-23037_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 934/3600 [00:56<03:02, 14.59it/s]
no element found: line 1174, column 0 ./0931_CsPbCl3_mp-23037_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
could not convert string to float: '****************' ./0935_CsPbCl3_mp-23037_2x2x2_with_noise_4
<class 'ValueError'> 21
 26%|██▋       | 946/3600 [00:57<03:09, 13.99it/s]
no element found: line 2190, column 0 ./0942_CsPbCl3_mp-23037_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 957/3600 [00:58<03:00, 14.63it/s]
no element found: line 1138, column 0 ./0953_CsPbCl3_mp-23037_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3701, column 0 ./0955_CsPbCl3_mp-23037_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 964/3600 [00:59<02:53, 15.23it/s]
no element found: line 1488, column 0 ./0961_CsPbCl3_mp-23037_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 967/3600 [00:59<03:37, 12.13it/s]
no element found: line 2703, column 0 ./0969_CsPbCl3_mp-23037_2x2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 975/3600 [01:00<02:59, 14.60it/s]
could not convert string to float: '****************' ./0973_CsPbCl3_mp-23037_2x2x2_with_noise_74
<class 'ValueError'> 21
no element found: line 3112, column 0 ./0975_CsPbCl3_mp-23037_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 981/3600 [01:00<03:11, 13.68it/s]
could not convert string to float: '****************' ./0982_CsPbCl3_mp-23037_2x2x2_with_noise_82
<class 'ValueError'> 21
no element found: line 6089, column 0 ./0983_CsPbCl3_mp-23037_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 988/3600 [01:01<02:59, 14.53it/s]
no element found: line 1012, column 0 ./0987_CsPbCl3_mp-23037_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1140/3600 [01:09<01:57, 20.99it/s]
no element found: line 1256, column 0 ./1134_CsPbCl3_mp-23037_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1976, column 0 ./1135_CsPbCl3_mp-23037_r2xr2x2_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3641, column 0 ./1143_CsPbCl3_mp-23037_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1150/3600 [01:09<01:54, 21.34it/s]
no element found: line 8006, column 0 ./1149_CsPbCl3_mp-23037_r2xr2x2_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3596, column 0 ./1152_CsPbCl3_mp-23037_r2xr2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1168/3600 [01:10<02:04, 19.59it/s]
no element found: line 2939, column 0 ./1169_CsPbCl3_mp-23037_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 33%|███▎      | 1178/3600 [01:11<01:59, 20.21it/s]
no element found: line 10958, column 0 ./1176_CsPbCl3_mp-23037_r2xr2x2_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 37%|███▋      | 1349/3600 [01:20<01:42, 21.88it/s]
no element found: line 4913, column 0 ./1352_CsPbI3_mp-1069538_2x1x1_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 39%|███▉      | 1401/3600 [01:22<01:42, 21.54it/s]
no element found: line 1441, column 0 ./1405_CsPbI3_mp-1069538_2x2x1_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1207, column 0 ./1406_CsPbI3_mp-1069538_2x2x1_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1527, column 0 ./1407_CsPbI3_mp-1069538_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1486, column 0 ./1408_CsPbI3_mp-1069538_2x2x1_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|███▉      | 1432/3600 [01:24<01:51, 19.45it/s]
no element found: line 2152, column 0 ./1429_CsPbI3_mp-1069538_2x2x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1693, column 0 ./1436_CsPbI3_mp-1069538_2x2x1_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|████      | 1448/3600 [01:25<01:26, 24.88it/s]
no element found: line 901, column 0 ./1440_CsPbI3_mp-1069538_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2670, column 0 ./1442_CsPbI3_mp-1069538_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2949, column 0 ./1444_CsPbI3_mp-1069538_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|████      | 1456/3600 [01:25<01:46, 20.20it/s]
no element found: line 4312, column 0 ./1458_CsPbI3_mp-1069538_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████▏     | 1486/3600 [01:27<01:38, 21.42it/s]
no element found: line 3421, column 0 ./1478_CsPbI3_mp-1069538_2x2x1_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1495/3600 [01:28<01:44, 20.13it/s]
no element found: line 2143, column 0 ./1488_CsPbI3_mp-1069538_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1513, column 0 ./1491_CsPbI3_mp-1069538_2x2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1243, column 0 ./1497_CsPbI3_mp-1069538_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1506/3600 [01:28<01:44, 20.00it/s]
no element found: line 3476, column 0 ./1502_CsPbI3_mp-1069538_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1165, column 0 ./1508_CsPbI3_mp-1069538_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1514/3600 [01:29<01:54, 18.24it/s]
no element found: line 1673, column 0 ./1510_CsPbI3_mp-1069538_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 10779, column 0 ./1513_CsPbI3_mp-1069538_2x2x2_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1300, column 0 ./1515_CsPbI3_mp-1069538_2x2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1516_CsPbI3_mp-1069538_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2275, column 0 ./1517_CsPbI3_mp-1069538_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1527/3600 [01:29<01:41, 20.33it/s]
no element found: line 2851, column 0 ./1524_CsPbI3_mp-1069538_2x2x2_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1534/3600 [01:30<02:03, 16.70it/s]
no element found: line 1691, column 0 ./1531_CsPbI3_mp-1069538_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1546/3600 [01:31<01:49, 18.69it/s]
no element found: line 3310, column 0 ./1544_CsPbI3_mp-1069538_2x2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1554/3600 [01:31<01:55, 17.70it/s]
no element found: line 1057, column 0 ./1548_CsPbI3_mp-1069538_2x2x2_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1664, column 0 ./1552_CsPbI3_mp-1069538_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1264, column 0 ./1553_CsPbI3_mp-1069538_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2231, column 0 ./1555_CsPbI3_mp-1069538_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1557_CsPbI3_mp-1069538_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1564/3600 [01:32<01:50, 18.38it/s]
no element found: line 2204, column 0 ./1561_CsPbI3_mp-1069538_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 648, column 0 ./1562_CsPbI3_mp-1069538_2x2x2_with_noise_64
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1576/3600 [01:33<01:59, 17.00it/s]
no element found: line 6686, column 0 ./1573_CsPbI3_mp-1069538_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1583/3600 [01:33<02:06, 15.94it/s]
no element found: line 1970, column 0 ./1578_CsPbI3_mp-1069538_2x2x2_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1966, column 0 ./1579_CsPbI3_mp-1069538_2x2x2_with_noise_8
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1012, column 0 ./1580_CsPbI3_mp-1069538_2x2x2_with_noise_80
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2671, column 0 ./1586_CsPbI3_mp-1069538_2x2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1587/3600 [01:33<01:44, 19.34it/s]
no element found: line 2239, column 0 ./1588_CsPbI3_mp-1069538_2x2x2_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1599/3600 [01:34<01:41, 19.76it/s]
no element found: line 3903, column 0 ./1593_CsPbI3_mp-1069538_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 967, column 0 ./1594_CsPbI3_mp-1069538_2x2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 47%|████▋     | 1683/3600 [01:38<01:05, 29.14it/s]
no element found: line 1518, column 0 ./1672_CsPbI3_mp-1069538_r2xr2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1719/3600 [01:40<01:26, 21.68it/s]
no element found: line 864, column 0 ./1718_CsPbI3_mp-1069538_r2xr2x2_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1729/3600 [01:40<01:32, 20.13it/s]
no element found: line 1215, column 0 ./1725_CsPbI3_mp-1069538_r2xr2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
 49%|████▊     | 1749/3600 [01:41<01:13, 25.26it/s]
no element found: line 855, column 0 ./1744_CsPbI3_mp-1069538_r2xr2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 49%|████▉     | 1769/3600 [01:42<01:29, 20.57it/s]
no element found: line 927, column 0 ./1764_CsPbI3_mp-1069538_r2xr2x2_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2376, column 0 ./1767_CsPbI3_mp-1069538_r2xr2x2_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
 50%|████▉     | 1798/3600 [01:44<01:26, 20.74it/s]
no element found: line 909, column 0 ./1794_CsPbI3_mp-1069538_r2xr2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1980, column 0 ./1799_CsPbI3_mp-1069538_r2xr2x2_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 51%|█████     | 1827/3600 [01:45<01:14, 23.73it/s]
no element found: line 5618, column 0 ./1829_CsSnBr3_mp-27214_1x1x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
 51%|█████▏    | 1845/3600 [01:46<01:00, 28.90it/s]
no element found: line 6110, column 0 ./1839_CsSnBr3_mp-27214_1x1x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 53%|█████▎    | 1914/3600 [01:49<01:02, 27.03it/s]
no element found: line 2254, column 0 ./1911_CsSnBr3_mp-27214_2x1x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
 54%|█████▎    | 1926/3600 [01:50<01:09, 23.93it/s]
no element found: line 2139, column 0 ./1924_CsSnBr3_mp-27214_2x1x1_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 55%|█████▌    | 1982/3600 [01:53<01:12, 22.17it/s]
no element found: line 1538, column 0 ./1984_CsSnBr3_mp-27214_2x1x1_with_noise_84
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2002/3600 [01:53<00:55, 28.80it/s]
no element found: line 1196, column 0 ./1999_CsSnBr3_mp-27214_2x1x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1572, column 0 ./2001_CsSnBr3_mp-27214_2x2x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2012/3600 [01:54<01:11, 22.11it/s]
no element found: line 1554, column 0 ./2011_CsSnBr3_mp-27214_2x2x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▋    | 2027/3600 [01:55<01:06, 23.58it/s]
no element found: line 1518, column 0 ./2026_CsSnBr3_mp-27214_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2037/3600 [01:56<01:17, 20.12it/s]
no element found: line 1527, column 0 ./2035_CsSnBr3_mp-27214_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2539, column 0 ./2042_CsSnBr3_mp-27214_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2054/3600 [01:56<01:06, 23.37it/s]
no element found: line 3318, column 0 ./2046_CsSnBr3_mp-27214_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1518, column 0 ./2048_CsSnBr3_mp-27214_2x2x1_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
[Errno 2] No such file or directory: './vasprun.xml' ./2055_CsSnBr3_mp-27214_2x2x1_with_noise_58
<class 'FileNotFoundError'> 13
 57%|█████▋    | 2067/3600 [01:57<01:07, 22.57it/s]
no element found: line 1509, column 0 ./2061_CsSnBr3_mp-27214_2x2x1_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 58%|█████▊    | 2081/3600 [01:58<01:07, 22.34it/s]
no element found: line 3003, column 0 ./2083_CsSnBr3_mp-27214_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 58%|█████▊    | 2091/3600 [01:59<01:18, 19.32it/s]
no element found: line 1284, column 0 ./2086_CsSnBr3_mp-27214_2x2x1_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2117/3600 [02:00<01:18, 18.96it/s]
no element found: line 2105, column 0 ./2114_CsSnBr3_mp-27214_2x2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1192, column 0 ./2116_CsSnBr3_mp-27214_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2134/3600 [02:02<01:48, 13.56it/s]
no element found: line 8411, column 0 ./2131_CsSnBr3_mp-27214_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3404, column 0 ./2135_CsSnBr3_mp-27214_2x2x2_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|█████▉    | 2145/3600 [02:02<01:39, 14.66it/s]
no element found: line 2204, column 0 ./2142_CsSnBr3_mp-27214_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|██████    | 2160/3600 [02:03<01:22, 17.54it/s]
no element found: line 1952, column 0 ./2161_CsSnBr3_mp-27214_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2183/3600 [02:05<01:18, 18.02it/s]
no element found: line 2613, column 0 ./2177_CsSnBr3_mp-27214_2x2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2192/3600 [02:06<01:25, 16.54it/s]
no element found: line 1435, column 0 ./2189_CsSnBr3_mp-27214_2x2x2_with_noise_89
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2886, column 0 ./2190_CsSnBr3_mp-27214_2x2x2_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2635, column 0 ./2196_CsSnBr3_mp-27214_2x2x2_with_noise_95
<class 'xml.etree.ElementTree.ParseError'> 13
 62%|██████▏   | 2244/3600 [02:08<00:57, 23.53it/s]
no element found: line 1473, column 0 ./2238_CsSnBr3_mp-27214_r2xr2x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
 64%|██████▍   | 2308/3600 [02:11<00:47, 26.95it/s]
no element found: line 2241, column 0 ./2304_CsSnBr3_mp-27214_r2xr2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5873, column 0 ./2310_CsSnBr3_mp-27214_r2xr2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 65%|██████▍   | 2339/3600 [02:12<00:49, 25.27it/s]
no element found: line 2201, column 0 ./2333_CsSnBr3_mp-27214_r2xr2x2_with_noise_38
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3434, column 0 ./2334_CsSnBr3_mp-27214_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5774, column 0 ./2339_CsSnBr3_mp-27214_r2xr2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3438, column 0 ./2343_CsSnBr3_mp-27214_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
 66%|██████▌   | 2359/3600 [02:13<00:51, 24.10it/s]
could not convert string to float: '****************' ./2354_CsSnBr3_mp-27214_r2xr2x2_with_noise_57
<class 'ValueError'> 21
no element found: line 2876, column 0 ./2357_CsSnBr3_mp-27214_r2xr2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 67%|██████▋   | 2408/3600 [02:16<00:46, 25.67it/s]
no element found: line 5855, column 0 ./2398_CsSnBr3_mp-27214_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 70%|██████▉   | 2511/3600 [02:21<00:40, 26.75it/s]
no element found: line 1383, column 0 ./2503_CsSnCl3_mp-1070375_2x1x1_with_noise_100
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████   | 2545/3600 [02:23<00:41, 25.68it/s]
no element found: line 2040, column 0 ./2546_CsSnCl3_mp-1070375_2x1x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████   | 2562/3600 [02:23<00:41, 25.15it/s]
no element found: line 2641, column 0 ./2564_CsSnCl3_mp-1070375_2x1x1_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▏  | 2581/3600 [02:24<00:39, 25.77it/s]
no element found: line 5341, column 0 ./2574_CsSnCl3_mp-1070375_2x1x1_with_noise_75
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▏  | 2600/3600 [02:25<00:37, 26.56it/s]
no element found: line 1975, column 0 ./2592_CsSnCl3_mp-1070375_2x1x1_with_noise_91
<class 'xml.etree.ElementTree.ParseError'> 13
 73%|███████▎  | 2611/3600 [02:26<00:48, 20.34it/s]
no element found: line 1261, column 0 ./2607_CsSnCl3_mp-1070375_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2071, column 0 ./2612_CsSnCl3_mp-1070375_2x2x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 4461, column 0 ./2613_CsSnCl3_mp-1070375_2x2x1_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▎  | 2647/3600 [02:28<00:48, 19.47it/s]
no element found: line 1477, column 0 ./2642_CsSnCl3_mp-1070375_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1824, column 0 ./2646_CsSnCl3_mp-1070375_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▍  | 2670/3600 [02:29<00:37, 24.82it/s]
no element found: line 4254, column 0 ./2667_CsSnCl3_mp-1070375_2x2x1_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▍  | 2678/3600 [02:30<00:54, 16.88it/s]
no element found: line 3165, column 0 ./2673_CsSnCl3_mp-1070375_2x2x1_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▍  | 2692/3600 [02:31<00:54, 16.51it/s]
no element found: line 1563, column 0 ./2688_CsSnCl3_mp-1070375_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▌  | 2702/3600 [02:31<00:37, 23.89it/s]
no element found: line 1549, column 0 ./2700_CsSnCl3_mp-1070375_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▌  | 2719/3600 [02:33<01:08, 12.85it/s]
no element found: line 5081, column 0 ./2717_CsSnCl3_mp-1070375_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▌  | 2726/3600 [02:33<00:49, 17.65it/s]
no element found: line 2374, column 0 ./2727_CsSnCl3_mp-1070375_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1723, column 0 ./2728_CsSnCl3_mp-1070375_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▌  | 2736/3600 [02:34<00:54, 15.90it/s]
no element found: line 1970, column 0 ./2732_CsSnCl3_mp-1070375_2x2x2_with_noise_37
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▋  | 2751/3600 [02:35<00:49, 17.00it/s]
could not convert string to float: '****************' ./2748_CsSnCl3_mp-1070375_2x2x2_with_noise_51
<class 'ValueError'> 21
 77%|███████▋  | 2766/3600 [02:36<00:51, 16.19it/s]
could not convert string to float: '****************' ./2766_CsSnCl3_mp-1070375_2x2x2_with_noise_68
<class 'ValueError'> 21
 77%|███████▋  | 2777/3600 [02:37<00:50, 16.30it/s]
no element found: line 4317, column 0 ./2773_CsSnCl3_mp-1070375_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2838, column 0 ./2775_CsSnCl3_mp-1070375_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 77%|███████▋  | 2780/3600 [02:37<00:44, 18.39it/s]
no element found: line 2559, column 0 ./2782_CsSnCl3_mp-1070375_2x2x2_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
 78%|███████▊  | 2791/3600 [02:38<00:51, 15.81it/s]
no element found: line 1102, column 0 ./2787_CsSnCl3_mp-1070375_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 78%|███████▊  | 2813/3600 [02:39<00:29, 26.37it/s]
no element found: line 1176, column 0 ./2810_CsSnCl3_mp-1070375_r2xr2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 80%|████████  | 2883/3600 [02:42<00:22, 31.73it/s]
no element found: line 1800, column 0 ./2876_CsSnCl3_mp-1070375_r2xr2x1_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 81%|████████  | 2921/3600 [02:44<00:30, 22.61it/s]
no element found: line 2543, column 0 ./2922_CsSnCl3_mp-1070375_r2xr2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
could not convert string to float: '****************' ./2925_CsSnCl3_mp-1070375_r2xr2x2_with_noise_30
<class 'ValueError'> 21
 87%|████████▋ | 3121/3600 [02:54<00:23, 20.37it/s]
no element found: line 4333, column 0 ./3112_CsSnI3_mp-614013_2x1x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
 87%|████████▋ | 3132/3600 [02:54<00:15, 29.37it/s]
no element found: line 2083, column 0 ./3134_CsSnI3_mp-614013_2x1x1_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3156/3600 [02:55<00:14, 31.00it/s]
no element found: line 2394, column 0 ./3150_CsSnI3_mp-614013_2x1x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3174/3600 [02:56<00:16, 25.88it/s]
no element found: line 7073, column 0 ./3166_CsSnI3_mp-614013_2x1x1_with_noise_68
<class 'xml.etree.ElementTree.ParseError'> 13
 89%|████████▉ | 3212/3600 [02:58<00:17, 22.49it/s]
no element found: line 22857, column 0 ./3206_CsSnI3_mp-614013_2x2x1_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1374, column 0 ./3210_CsSnI3_mp-614013_2x2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 89%|████████▉ | 3218/3600 [02:59<00:13, 28.20it/s]
no element found: line 2062, column 0 ./3217_CsSnI3_mp-614013_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1338, column 0 ./3218_CsSnI3_mp-614013_2x2x1_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1716, column 0 ./3220_CsSnI3_mp-614013_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 3251/3600 [03:01<00:16, 20.99it/s]
no element found: line 1450, column 0 ./3244_CsSnI3_mp-614013_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3561, column 0 ./3250_CsSnI3_mp-614013_2x2x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 91%|█████████ | 3274/3600 [03:02<00:14, 22.45it/s]
no element found: line 4227, column 0 ./3275_CsSnI3_mp-614013_2x2x1_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 91%|█████████▏| 3289/3600 [03:03<00:15, 20.02it/s]
no element found: line 1869, column 0 ./3283_CsSnI3_mp-614013_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1576, column 0 ./3290_CsSnI3_mp-614013_2x2x1_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3300/3600 [03:03<00:09, 30.44it/s]
no element found: line 3241, column 0 ./3295_CsSnI3_mp-614013_2x2x1_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1284, column 0 ./3299_CsSnI3_mp-614013_2x2x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3309/3600 [03:04<00:17, 16.25it/s]
no element found: line 1821, column 0 ./3304_CsSnI3_mp-614013_2x2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1664, column 0 ./3305_CsSnI3_mp-614013_2x2x2_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 7557, column 0 ./3310_CsSnI3_mp-614013_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3318/3600 [03:04<00:11, 23.58it/s]
no element found: line 1156, column 0 ./3314_CsSnI3_mp-614013_2x2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1439, column 0 ./3317_CsSnI3_mp-614013_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2365, column 0 ./3320_CsSnI3_mp-614013_2x2x2_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2325, column 0 ./3321_CsSnI3_mp-614013_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3338/3600 [03:05<00:11, 22.44it/s]
no element found: line 5760, column 0 ./3333_CsSnI3_mp-614013_2x2x2_with_noise_38
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3349/3600 [03:07<00:15, 15.84it/s]
no element found: line 2401, column 0 ./3345_CsSnI3_mp-614013_2x2x2_with_noise_49
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3353/3600 [03:07<00:12, 19.32it/s]
no element found: line 976, column 0 ./3352_CsSnI3_mp-614013_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▎| 3373/3600 [03:08<00:09, 23.07it/s]
no element found: line 1057, column 0 ./3371_CsSnI3_mp-614013_2x2x2_with_noise_72
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2203, column 0 ./3373_CsSnI3_mp-614013_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3380/3600 [03:09<00:16, 12.96it/s]
no element found: line 22984, column 0 ./3376_CsSnI3_mp-614013_2x2x2_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3387/3600 [03:09<00:11, 18.26it/s]
no element found: line 3341, column 0 ./3383_CsSnI3_mp-614013_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3398/3600 [03:10<00:13, 14.65it/s]
no element found: line 2640, column 0 ./3394_CsSnI3_mp-614013_2x2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3517/3600 [03:15<00:02, 33.79it/s]
no element found: line 1679, column 0 ./3512_CsSnI3_mp-614013_r2xr2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3510, column 0 ./3514_CsSnI3_mp-614013_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1467, column 0 ./3515_CsSnI3_mp-614013_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3534/3600 [03:16<00:02, 23.52it/s]
no element found: line 2750, column 0 ./3530_CsSnI3_mp-614013_r2xr2x2_with_noise_35
<class 'xml.etree.ElementTree.ParseError'> 13
 99%|█████████▉| 3580/3600 [03:19<00:00, 22.07it/s]
no element found: line 1643, column 0 ./3572_CsSnI3_mp-614013_r2xr2x2_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1647, column 0 ./3577_CsSnI3_mp-614013_r2xr2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
100%|█████████▉| 3586/3600 [03:19<00:00, 27.74it/s]
no element found: line 4694, column 0 ./3583_CsSnI3_mp-614013_r2xr2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2858, column 0 ./3586_CsSnI3_mp-614013_r2xr2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [03:20<00:00, 17.98it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 236
```

* 대부분 ParsingError + 일부는 알 수 없는 원인의 ValueError, FileNotFoundError 발생
* 기존의 INCAR 구성에서 NSW: 50->36으로 바꿔 계산에러 폴더에서 재계산 시도 : 역순으로 2026번 폴더까지 재계산 시도 완료
* 그러나 재계산 결과를 확인해보면 대부분 여전히 수렴되지 않고 비정상적 종료하게 됨.
* 아마 노이즈레벨 0.05가 수렴에 영향을 주는 것 같다.
* 그러므로 이제 수렴이 안 된 계산폴더는 사용하지 않고, **최종 데이터 추출(tag.gz) 및 파싱(pickle) 진행하자.**

* Noise01 Dataset 우선 사용 -> Noise05 Dataset은 데이터 부족한 경우에 추가사용하기로 한다.
* 전체 데이터의 클래스 구성비율을 나중에 확인할 것! (random shuffling 이후에)
* 최종 파싱 결과는 다음과 같다. : 일부 계산이 수렴했으나, 이제 그만하고 이 데이터를 사용하기로 한다.

``` Python
  1%|          | 44/3600 [00:03<03:46, 15.73it/s]
no element found: line 6425, column 0 ./0044_CsPbBr3_mp-600089_1x1x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 91/3600 [00:06<03:32, 16.51it/s]
no element found: line 3056, column 0 ./0088_CsPbBr3_mp-600089_1x1x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 105/3600 [00:06<03:14, 17.95it/s]
no element found: line 1493, column 0 ./0102_CsPbBr3_mp-600089_2x1x1_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  3%|▎         | 123/3600 [00:07<03:29, 16.62it/s]
no element found: line 3715, column 0 ./0121_CsPbBr3_mp-600089_2x1x1_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 139/3600 [00:08<03:23, 17.01it/s]
no element found: line 2146, column 0 ./0138_CsPbBr3_mp-600089_2x1x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 152/3600 [00:09<03:21, 17.14it/s]
no element found: line 1391, column 0 ./0149_CsPbBr3_mp-600089_2x1x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
  4%|▍         | 155/3600 [00:09<03:27, 16.57it/s]
no element found: line 8340, column 0 ./0154_CsPbBr3_mp-600089_2x1x1_with_noise_57
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▍         | 175/3600 [00:11<03:32, 16.09it/s]
no element found: line 1004, column 0 ./0174_CsPbBr3_mp-600089_2x1x1_with_noise_75
<class 'xml.etree.ElementTree.ParseError'> 13
  5%|▌         | 182/3600 [00:11<03:18, 17.18it/s]
no element found: line 2027, column 0 ./0181_CsPbBr3_mp-600089_2x1x1_with_noise_81
<class 'xml.etree.ElementTree.ParseError'> 13
  6%|▌         | 215/3600 [00:13<04:01, 14.01it/s]
no element found: line 928, column 0 ./0214_CsPbBr3_mp-600089_2x2x1_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1684, column 0 ./0217_CsPbBr3_mp-600089_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
  6%|▌         | 218/3600 [00:14<03:59, 14.10it/s]
no element found: line 3048, column 0 ./0219_CsPbBr3_mp-600089_2x2x1_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 238/3600 [00:15<03:58, 14.11it/s]
no element found: line 1063, column 0 ./0239_CsPbBr3_mp-600089_2x2x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1797, column 0 ./0240_CsPbBr3_mp-600089_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 245/3600 [00:16<03:51, 14.49it/s]
no element found: line 2692, column 0 ./0246_CsPbBr3_mp-600089_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 256/3600 [00:16<03:39, 15.24it/s]
no element found: line 1252, column 0 ./0255_CsPbBr3_mp-600089_2x2x1_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
  7%|▋         | 263/3600 [00:17<03:46, 14.73it/s]
no element found: line 2098, column 0 ./0265_CsPbBr3_mp-600089_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 270/3600 [00:17<03:47, 14.66it/s]
no element found: line 2148, column 0 ./0272_CsPbBr3_mp-600089_2x2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 295/3600 [00:19<04:21, 12.62it/s]
no element found: line 2247, column 0 ./0297_CsPbBr3_mp-600089_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 299/3600 [00:19<04:01, 13.65it/s]
no element found: line 1509, column 0 ./0300_CsPbBr3_mp-600089_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1687, column 0 ./0302_CsPbBr3_mp-600089_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
  8%|▊         | 306/3600 [00:20<04:06, 13.35it/s]
no element found: line 2343, column 0 ./0309_CsPbBr3_mp-600089_2x2x2_with_noise_16
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2338, column 0 ./0310_CsPbBr3_mp-600089_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1111, column 0 ./0311_CsPbBr3_mp-600089_2x2x2_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3521, column 0 ./0312_CsPbBr3_mp-600089_2x2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 316/3600 [00:20<03:36, 15.15it/s]
no element found: line 1520, column 0 ./0319_CsPbBr3_mp-600089_2x2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 320/3600 [00:21<03:40, 14.86it/s]
no element found: line 8752, column 0 ./0321_CsPbBr3_mp-600089_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 323/3600 [00:21<03:55, 13.90it/s]
no element found: line 3134, column 0 ./0325_CsPbBr3_mp-600089_2x2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1781, column 0 ./0327_CsPbBr3_mp-600089_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
  9%|▉         | 336/3600 [00:22<04:41, 11.58it/s]
no element found: line 1952, column 0 ./0339_CsPbBr3_mp-600089_2x2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 351/3600 [00:23<04:24, 12.30it/s]
no element found: line 2303, column 0 ./0351_CsPbBr3_mp-600089_2x2x2_with_noise_54
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|▉         | 354/3600 [00:24<04:37, 11.69it/s]
no element found: line 1147, column 0 ./0357_CsPbBr3_mp-600089_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 10%|█         | 367/3600 [00:25<04:54, 10.97it/s]
no element found: line 2640, column 0 ./0370_CsPbBr3_mp-600089_2x2x2_with_noise_71
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 388/3600 [00:27<04:50, 11.07it/s]
no element found: line 3418, column 0 ./0391_CsPbBr3_mp-600089_2x2x2_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 392/3600 [00:27<04:34, 11.68it/s]
no element found: line 3148, column 0 ./0393_CsPbBr3_mp-600089_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2640, column 0 ./0395_CsPbBr3_mp-600089_2x2x2_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3683, column 0 ./0397_CsPbBr3_mp-600089_2x2x2_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
 11%|█         | 403/3600 [00:27<02:54, 18.35it/s]
no element found: line 3467, column 0 ./0400_CsPbBr3_mp-600089_2x2x2_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▎        | 487/3600 [00:32<02:56, 17.64it/s]
no element found: line 1113, column 0 ./0491_CsPbBr3_mp-600089_r2xr2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▍        | 515/3600 [00:33<02:25, 21.21it/s]
no element found: line 2079, column 0 ./0514_CsPbBr3_mp-600089_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1692, column 0 ./0515_CsPbBr3_mp-600089_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
 14%|█▍        | 519/3600 [00:33<02:45, 18.62it/s]
no element found: line 2039, column 0 ./0519_CsPbBr3_mp-600089_r2xr2x2_with_noise_25
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2543, column 0 ./0523_CsPbBr3_mp-600089_r2xr2x2_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 534/3600 [00:34<02:23, 21.38it/s]
no element found: line 1589, column 0 ./0531_CsPbBr3_mp-600089_r2xr2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▍        | 537/3600 [00:34<02:58, 17.19it/s]
no element found: line 2111, column 0 ./0536_CsPbBr3_mp-600089_r2xr2x2_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
 15%|█▌        | 557/3600 [00:36<02:39, 19.10it/s]
no element found: line 1490, column 0 ./0558_CsPbBr3_mp-600089_r2xr2x2_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 16%|█▌        | 570/3600 [00:36<02:24, 20.93it/s]
no element found: line 1476, column 0 ./0569_CsPbBr3_mp-600089_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 17%|█▋        | 600/3600 [00:38<02:26, 20.54it/s]
no element found: line 1422, column 0 ./0598_CsPbBr3_mp-600089_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 687/3600 [00:43<02:30, 19.40it/s]
no element found: line 6407, column 0 ./0685_CsPbCl3_mp-23037_1x1x1_with_noise_85
<class 'xml.etree.ElementTree.ParseError'> 13
 19%|█▉        | 701/3600 [00:44<02:28, 19.51it/s]
no element found: line 3339, column 0 ./0701_CsPbCl3_mp-23037_2x1x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 20%|█▉        | 714/3600 [00:44<02:40, 17.97it/s]
no element found: line 932, column 0 ./0716_CsPbCl3_mp-23037_2x1x1_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
 20%|██        | 725/3600 [00:45<02:05, 22.89it/s]
no element found: line 3005, column 0 ./0723_CsPbCl3_mp-23037_2x1x1_with_noise_29
<class 'xml.etree.ElementTree.ParseError'> 13
 21%|██        | 754/3600 [00:46<02:48, 16.87it/s]
no element found: line 1439, column 0 ./0759_CsPbCl3_mp-23037_2x1x1_with_noise_61
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2010, column 0 ./0760_CsPbCl3_mp-23037_2x1x1_with_noise_62
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 823/3600 [00:50<02:34, 17.95it/s]
no element found: line 2373, column 0 ./0820_CsPbCl3_mp-23037_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 831/3600 [00:51<02:21, 19.63it/s]
no element found: line 2094, column 0 ./0825_CsPbCl3_mp-23037_2x2x1_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2998, column 0 ./0826_CsPbCl3_mp-23037_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
 23%|██▎       | 834/3600 [00:51<02:59, 15.44it/s]
no element found: line 2175, column 0 ./0835_CsPbCl3_mp-23037_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▎       | 847/3600 [00:52<03:00, 15.29it/s]
no element found: line 1198, column 0 ./0849_CsPbCl3_mp-23037_2x2x1_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 864/3600 [00:53<02:23, 19.09it/s]
no element found: line 1504, column 0 ./0858_CsPbCl3_mp-23037_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 24%|██▍       | 867/3600 [00:53<02:56, 15.52it/s]
no element found: line 1779, column 0 ./0865_CsPbCl3_mp-23037_2x2x1_with_noise_67
<class 'xml.etree.ElementTree.ParseError'> 13
 25%|██▌       | 910/3600 [00:56<02:53, 15.50it/s]
no element found: line 2046, column 0 ./0906_CsPbCl3_mp-23037_2x2x2_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2316, column 0 ./0908_CsPbCl3_mp-23037_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 925/3600 [00:58<03:23, 13.16it/s]
no element found: line 1201, column 0 ./0922_CsPbCl3_mp-23037_2x2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 932/3600 [00:58<02:58, 14.93it/s]
no element found: line 1057, column 0 ./0928_CsPbCl3_mp-23037_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1174, column 0 ./0931_CsPbCl3_mp-23037_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 26%|██▌       | 938/3600 [00:58<03:09, 14.05it/s]
could not convert string to float: '****************' ./0935_CsPbCl3_mp-23037_2x2x2_with_noise_4
<class 'ValueError'> 21
 26%|██▋       | 945/3600 [00:59<03:02, 14.53it/s]
no element found: line 2190, column 0 ./0942_CsPbCl3_mp-23037_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 956/3600 [01:00<03:00, 14.66it/s]
no element found: line 1138, column 0 ./0953_CsPbCl3_mp-23037_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3701, column 0 ./0955_CsPbCl3_mp-23037_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 963/3600 [01:00<02:53, 15.18it/s]
no element found: line 1488, column 0 ./0961_CsPbCl3_mp-23037_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 966/3600 [01:01<03:39, 12.00it/s]
no element found: line 2703, column 0 ./0969_CsPbCl3_mp-23037_2x2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 973/3600 [01:01<03:16, 13.38it/s]
could not convert string to float: '****************' ./0973_CsPbCl3_mp-23037_2x2x2_with_noise_74
<class 'ValueError'> 21
no element found: line 3112, column 0 ./0975_CsPbCl3_mp-23037_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 27%|██▋       | 986/3600 [01:02<03:00, 14.48it/s]
could not convert string to float: '****************' ./0982_CsPbCl3_mp-23037_2x2x2_with_noise_82
<class 'ValueError'> 21
no element found: line 6089, column 0 ./0983_CsPbCl3_mp-23037_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1012, column 0 ./0987_CsPbCl3_mp-23037_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1138/3600 [01:10<01:52, 21.81it/s]
no element found: line 1256, column 0 ./1134_CsPbCl3_mp-23037_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1976, column 0 ./1135_CsPbCl3_mp-23037_r2xr2x2_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1148/3600 [01:11<01:53, 21.68it/s]
no element found: line 3641, column 0 ./1143_CsPbCl3_mp-23037_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 8006, column 0 ./1149_CsPbCl3_mp-23037_r2xr2x2_with_noise_52
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3596, column 0 ./1152_CsPbCl3_mp-23037_r2xr2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 32%|███▏      | 1166/3600 [01:12<02:06, 19.26it/s]
no element found: line 2939, column 0 ./1169_CsPbCl3_mp-23037_r2xr2x2_with_noise_70
<class 'xml.etree.ElementTree.ParseError'> 13
 33%|███▎      | 1175/3600 [01:12<02:05, 19.37it/s]
no element found: line 10958, column 0 ./1176_CsPbCl3_mp-23037_r2xr2x2_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 38%|███▊      | 1355/3600 [01:22<01:42, 21.86it/s]
no element found: line 4913, column 0 ./1352_CsPbI3_mp-1069538_2x1x1_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 39%|███▉      | 1410/3600 [01:25<01:30, 24.24it/s]
no element found: line 1441, column 0 ./1405_CsPbI3_mp-1069538_2x2x1_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1207, column 0 ./1406_CsPbI3_mp-1069538_2x2x1_with_noise_13
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1527, column 0 ./1407_CsPbI3_mp-1069538_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1486, column 0 ./1408_CsPbI3_mp-1069538_2x2x1_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|███▉      | 1429/3600 [01:26<01:48, 19.98it/s]
no element found: line 2152, column 0 ./1429_CsPbI3_mp-1069538_2x2x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
 40%|████      | 1445/3600 [01:26<01:23, 25.80it/s]
no element found: line 1693, column 0 ./1436_CsPbI3_mp-1069538_2x2x1_with_noise_40
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 901, column 0 ./1440_CsPbI3_mp-1069538_2x2x1_with_noise_44
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2670, column 0 ./1442_CsPbI3_mp-1069538_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2949, column 0 ./1444_CsPbI3_mp-1069538_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████      | 1460/3600 [01:28<01:54, 18.72it/s]
no element found: line 4312, column 0 ./1458_CsPbI3_mp-1069538_2x2x1_with_noise_60
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████      | 1481/3600 [01:29<01:50, 19.15it/s]
no element found: line 3421, column 0 ./1478_CsPbI3_mp-1069538_2x2x1_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
 41%|████▏     | 1490/3600 [01:29<01:52, 18.72it/s]
no element found: line 2143, column 0 ./1488_CsPbI3_mp-1069538_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1513, column 0 ./1491_CsPbI3_mp-1069538_2x2x1_with_noise_90
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1504/3600 [01:30<01:36, 21.68it/s]
no element found: line 1243, column 0 ./1497_CsPbI3_mp-1069538_2x2x1_with_noise_96
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3476, column 0 ./1502_CsPbI3_mp-1069538_2x2x2_with_noise_10
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1512/3600 [01:31<01:54, 18.19it/s]
no element found: line 1165, column 0 ./1508_CsPbI3_mp-1069538_2x2x2_with_noise_15
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1673, column 0 ./1510_CsPbI3_mp-1069538_2x2x2_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 10779, column 0 ./1513_CsPbI3_mp-1069538_2x2x2_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1300, column 0 ./1515_CsPbI3_mp-1069538_2x2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1516_CsPbI3_mp-1069538_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2275, column 0 ./1517_CsPbI3_mp-1069538_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
 42%|████▏     | 1525/3600 [01:31<01:41, 20.53it/s]
no element found: line 2851, column 0 ./1524_CsPbI3_mp-1069538_2x2x2_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1532/3600 [01:32<02:03, 16.68it/s]
no element found: line 1691, column 0 ./1531_CsPbI3_mp-1069538_2x2x2_with_noise_36
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1547/3600 [01:33<02:20, 14.57it/s]
no element found: line 3310, column 0 ./1544_CsPbI3_mp-1069538_2x2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1057, column 0 ./1548_CsPbI3_mp-1069538_2x2x2_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1551/3600 [01:33<01:54, 17.87it/s]
no element found: line 1664, column 0 ./1552_CsPbI3_mp-1069538_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1264, column 0 ./1553_CsPbI3_mp-1069538_2x2x2_with_noise_56
<class 'xml.etree.ElementTree.ParseError'> 13
 43%|████▎     | 1559/3600 [01:34<01:57, 17.39it/s]
no element found: line 2231, column 0 ./1555_CsPbI3_mp-1069538_2x2x2_with_noise_58
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1970, column 0 ./1557_CsPbI3_mp-1069538_2x2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2204, column 0 ./1561_CsPbI3_mp-1069538_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 648, column 0 ./1562_CsPbI3_mp-1069538_2x2x2_with_noise_64
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▎     | 1572/3600 [01:35<01:58, 17.05it/s]
no element found: line 6686, column 0 ./1573_CsPbI3_mp-1069538_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1581/3600 [01:35<01:54, 17.63it/s]
no element found: line 1970, column 0 ./1578_CsPbI3_mp-1069538_2x2x2_with_noise_79
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1966, column 0 ./1579_CsPbI3_mp-1069538_2x2x2_with_noise_8
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1012, column 0 ./1580_CsPbI3_mp-1069538_2x2x2_with_noise_80
<class 'xml.etree.ElementTree.ParseError'> 13
 44%|████▍     | 1590/3600 [01:36<01:58, 16.90it/s]
no element found: line 2671, column 0 ./1586_CsPbI3_mp-1069538_2x2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2239, column 0 ./1588_CsPbI3_mp-1069538_2x2x2_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3903, column 0 ./1593_CsPbI3_mp-1069538_2x2x2_with_noise_92
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 967, column 0 ./1594_CsPbI3_mp-1069538_2x2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 47%|████▋     | 1678/3600 [01:40<01:05, 29.17it/s]
no element found: line 1518, column 0 ./1672_CsPbI3_mp-1069538_r2xr2x1_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1715/3600 [01:42<01:28, 21.19it/s]
no element found: line 864, column 0 ./1718_CsPbI3_mp-1069538_r2xr2x2_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1730/3600 [01:42<01:17, 24.20it/s]
no element found: line 1215, column 0 ./1725_CsPbI3_mp-1069538_r2xr2x2_with_noise_30
<class 'xml.etree.ElementTree.ParseError'> 13
 48%|████▊     | 1739/3600 [01:43<01:33, 19.84it/s]
no element found: line 855, column 0 ./1744_CsPbI3_mp-1069538_r2xr2x2_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 49%|████▉     | 1771/3600 [01:45<01:11, 25.49it/s]
no element found: line 927, column 0 ./1764_CsPbI3_mp-1069538_r2xr2x2_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2376, column 0 ./1767_CsPbI3_mp-1069538_r2xr2x2_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
 50%|████▉     | 1794/3600 [01:46<01:20, 22.56it/s]
no element found: line 909, column 0 ./1794_CsPbI3_mp-1069538_r2xr2x2_with_noise_93
<class 'xml.etree.ElementTree.ParseError'> 13
 50%|█████     | 1805/3600 [01:47<01:24, 21.34it/s]
no element found: line 1980, column 0 ./1799_CsPbI3_mp-1069538_r2xr2x2_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 51%|█████     | 1835/3600 [01:48<01:12, 24.28it/s]
no element found: line 5618, column 0 ./1829_CsSnBr3_mp-27214_1x1x1_with_noise_34
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 6110, column 0 ./1839_CsSnBr3_mp-27214_1x1x1_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
 53%|█████▎    | 1920/3600 [01:52<01:15, 22.14it/s]
no element found: line 2254, column 0 ./1911_CsSnBr3_mp-27214_2x1x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2139, column 0 ./1924_CsSnBr3_mp-27214_2x1x1_with_noise_3
<class 'xml.etree.ElementTree.ParseError'> 13
 55%|█████▌    | 1994/3600 [01:56<01:02, 25.77it/s]
no element found: line 1538, column 0 ./1984_CsSnBr3_mp-27214_2x1x1_with_noise_84
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2005/3600 [01:56<01:11, 22.28it/s]
no element found: line 1196, column 0 ./1999_CsSnBr3_mp-27214_2x1x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1572, column 0 ./2001_CsSnBr3_mp-27214_2x2x1_with_noise_1
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▌    | 2009/3600 [01:56<01:04, 24.72it/s]
no element found: line 1554, column 0 ./2011_CsSnBr3_mp-27214_2x2x1_with_noise_18
<class 'xml.etree.ElementTree.ParseError'> 13
 56%|█████▋    | 2031/3600 [01:58<01:24, 18.66it/s]
no element found: line 1518, column 0 ./2026_CsSnBr3_mp-27214_2x2x1_with_noise_31
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1527, column 0 ./2035_CsSnBr3_mp-27214_2x2x1_with_noise_4
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2051/3600 [01:59<01:03, 24.37it/s]
no element found: line 3156, column 0 ./2046_CsSnBr3_mp-27214_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1401, column 0 ./2048_CsSnBr3_mp-27214_2x2x1_with_noise_51
<class 'xml.etree.ElementTree.ParseError'> 13
 57%|█████▋    | 2060/3600 [01:59<01:19, 19.31it/s]
[Errno 2] No such file or directory: './vasprun.xml' ./2055_CsSnBr3_mp-27214_2x2x1_with_noise_58
<class 'FileNotFoundError'> 13
no element found: line 1509, column 0 ./2061_CsSnBr3_mp-27214_2x2x1_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 58%|█████▊    | 2089/3600 [02:01<01:06, 22.65it/s]
no element found: line 3120, column 0 ./2083_CsSnBr3_mp-27214_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1284, column 0 ./2086_CsSnBr3_mp-27214_2x2x1_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
 59%|█████▉    | 2119/3600 [02:03<01:45, 13.99it/s]
no element found: line 1624, column 0 ./2116_CsSnBr3_mp-27214_2x2x2_with_noise_22
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|█████▉    | 2144/3600 [02:05<01:18, 18.47it/s]
no element found: line 2393, column 0 ./2142_CsSnBr3_mp-27214_2x2x2_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|██████    | 2164/3600 [02:07<01:25, 16.88it/s]
no element found: line 3507, column 0 ./2161_CsSnBr3_mp-27214_2x2x2_with_noise_63
<class 'xml.etree.ElementTree.ParseError'> 13
 60%|██████    | 2173/3600 [02:07<01:31, 15.57it/s]
no element found: line 2586, column 0 ./2177_CsSnBr3_mp-27214_2x2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2186/3600 [02:08<01:20, 17.48it/s]
no element found: line 1435, column 0 ./2189_CsSnBr3_mp-27214_2x2x2_with_noise_89
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2967, column 0 ./2190_CsSnBr3_mp-27214_2x2x2_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
 61%|██████    | 2199/3600 [02:09<01:13, 19.02it/s]
no element found: line 2563, column 0 ./2196_CsSnBr3_mp-27214_2x2x2_with_noise_95
<class 'xml.etree.ElementTree.ParseError'> 13
 62%|██████▏   | 2237/3600 [02:11<00:51, 26.47it/s]
no element found: line 1473, column 0 ./2238_CsSnBr3_mp-27214_r2xr2x1_with_noise_42
<class 'xml.etree.ElementTree.ParseError'> 13
 64%|██████▍   | 2311/3600 [02:14<00:52, 24.52it/s]
no element found: line 2669, column 0 ./2304_CsSnBr3_mp-27214_r2xr2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
 65%|██████▌   | 2341/3600 [02:16<00:54, 23.14it/s]
no element found: line 2498, column 0 ./2333_CsSnBr3_mp-27214_r2xr2x2_with_noise_38
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3047, column 0 ./2334_CsSnBr3_mp-27214_r2xr2x2_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 5801, column 0 ./2339_CsSnBr3_mp-27214_r2xr2x2_with_noise_43
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3609, column 0 ./2343_CsSnBr3_mp-27214_r2xr2x2_with_noise_47
<class 'xml.etree.ElementTree.ParseError'> 13
 66%|██████▌   | 2360/3600 [02:17<00:54, 22.88it/s]
could not convert string to float: '****************' ./2354_CsSnBr3_mp-27214_r2xr2x2_with_noise_57
<class 'ValueError'> 21
no element found: line 2858, column 0 ./2357_CsSnBr3_mp-27214_r2xr2x2_with_noise_6
<class 'xml.etree.ElementTree.ParseError'> 13
 67%|██████▋   | 2405/3600 [02:19<01:00, 19.74it/s]
no element found: line 6395, column 0 ./2398_CsSnBr3_mp-27214_r2xr2x2_with_noise_97
<class 'xml.etree.ElementTree.ParseError'> 13
 70%|██████▉   | 2508/3600 [02:24<00:52, 20.96it/s]
no element found: line 1383, column 0 ./2503_CsSnCl3_mp-1070375_2x1x1_with_noise_100
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████   | 2553/3600 [02:26<00:41, 25.25it/s]
no element found: line 2112, column 0 ./2546_CsSnCl3_mp-1070375_2x1x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 71%|███████▏  | 2570/3600 [02:27<00:40, 25.22it/s]
no element found: line 2128, column 0 ./2564_CsSnCl3_mp-1070375_2x1x1_with_noise_66
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▏  | 2587/3600 [02:28<00:40, 24.82it/s]
no element found: line 2056, column 0 ./2592_CsSnCl3_mp-1070375_2x1x1_with_noise_91
<class 'xml.etree.ElementTree.ParseError'> 13
 72%|███████▎  | 2610/3600 [02:29<00:35, 28.05it/s]
no element found: line 1261, column 0 ./2607_CsSnCl3_mp-1070375_2x2x1_with_noise_14
<class 'xml.etree.ElementTree.ParseError'> 13
 73%|███████▎  | 2619/3600 [02:30<00:51, 19.12it/s]
no element found: line 2044, column 0 ./2612_CsSnCl3_mp-1070375_2x2x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 4722, column 0 ./2613_CsSnCl3_mp-1070375_2x2x1_with_noise_2
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▎  | 2650/3600 [02:31<00:52, 18.26it/s]
no element found: line 1477, column 0 ./2642_CsSnCl3_mp-1070375_2x2x1_with_noise_46
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1680, column 0 ./2646_CsSnCl3_mp-1070375_2x2x1_with_noise_5
<class 'xml.etree.ElementTree.ParseError'> 13
 74%|███████▍  | 2674/3600 [02:33<00:37, 24.89it/s]
no element found: line 4209, column 0 ./2667_CsSnCl3_mp-1070375_2x2x1_with_noise_69
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3030, column 0 ./2673_CsSnCl3_mp-1070375_2x2x1_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▍  | 2687/3600 [02:34<00:45, 20.19it/s]
no element found: line 1554, column 0 ./2688_CsSnCl3_mp-1070375_2x2x1_with_noise_88
<class 'xml.etree.ElementTree.ParseError'> 13
 75%|███████▌  | 2701/3600 [02:34<00:44, 20.09it/s]
no element found: line 1567, column 0 ./2700_CsSnCl3_mp-1070375_2x2x1_with_noise_99
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▌  | 2731/3600 [02:37<00:39, 22.15it/s]
no element found: line 2788, column 0 ./2727_CsSnCl3_mp-1070375_2x2x2_with_noise_32
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1723, column 0 ./2728_CsSnCl3_mp-1070375_2x2x2_with_noise_33
<class 'xml.etree.ElementTree.ParseError'> 13
 76%|███████▋  | 2753/3600 [02:39<00:52, 16.08it/s]
could not convert string to float: '****************' ./2748_CsSnCl3_mp-1070375_2x2x2_with_noise_51
<class 'ValueError'> 21
 77%|███████▋  | 2768/3600 [02:40<00:45, 18.32it/s]
could not convert string to float: '****************' ./2766_CsSnCl3_mp-1070375_2x2x2_with_noise_68
<class 'ValueError'> 21
 77%|███████▋  | 2778/3600 [02:41<00:54, 14.98it/s]
no element found: line 2568, column 0 ./2775_CsSnCl3_mp-1070375_2x2x2_with_noise_76
<class 'xml.etree.ElementTree.ParseError'> 13
 77%|███████▋  | 2781/3600 [02:41<00:47, 17.33it/s]
no element found: line 2577, column 0 ./2782_CsSnCl3_mp-1070375_2x2x2_with_noise_82
<class 'xml.etree.ElementTree.ParseError'> 13
 78%|███████▊  | 2791/3600 [02:42<00:54, 14.92it/s]
no element found: line 1093, column 0 ./2787_CsSnCl3_mp-1070375_2x2x2_with_noise_87
<class 'xml.etree.ElementTree.ParseError'> 13
 78%|███████▊  | 2819/3600 [02:43<00:27, 28.52it/s]
no element found: line 1176, column 0 ./2810_CsSnCl3_mp-1070375_r2xr2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
 80%|████████  | 2884/3600 [02:46<00:22, 31.62it/s]
no element found: line 1800, column 0 ./2876_CsSnCl3_mp-1070375_r2xr2x1_with_noise_77
<class 'xml.etree.ElementTree.ParseError'> 13
 81%|████████▏ | 2926/3600 [02:48<00:25, 26.62it/s]
no element found: line 2435, column 0 ./2922_CsSnCl3_mp-1070375_r2xr2x2_with_noise_28
<class 'xml.etree.ElementTree.ParseError'> 13
could not convert string to float: '****************' ./2925_CsSnCl3_mp-1070375_r2xr2x2_with_noise_30
<class 'ValueError'> 21
 86%|████████▋ | 3112/3600 [02:57<00:16, 29.17it/s]
no element found: line 4288, column 0 ./3112_CsSnI3_mp-614013_2x1x1_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
 87%|████████▋ | 3136/3600 [02:59<00:15, 30.43it/s]
no element found: line 2092, column 0 ./3134_CsSnI3_mp-614013_2x1x1_with_noise_39
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3160/3600 [03:00<00:14, 30.51it/s]
no element found: line 2430, column 0 ./3150_CsSnI3_mp-614013_2x1x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 3171/3600 [03:01<00:20, 20.59it/s]
no element found: line 1547, column 0 ./3166_CsSnI3_mp-614013_2x1x1_with_noise_68
<class 'xml.etree.ElementTree.ParseError'> 13
 89%|████████▉ | 3215/3600 [03:03<00:16, 22.65it/s]
no element found: line 1464, column 0 ./3210_CsSnI3_mp-614013_2x2x1_with_noise_17
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2044, column 0 ./3217_CsSnI3_mp-614013_2x2x1_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1338, column 0 ./3218_CsSnI3_mp-614013_2x2x1_with_noise_24
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1725, column 0 ./3220_CsSnI3_mp-614013_2x2x1_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 3241/3600 [03:04<00:14, 24.39it/s]
no element found: line 1450, column 0 ./3244_CsSnI3_mp-614013_2x2x1_with_noise_48
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 3254/3600 [03:05<00:17, 19.91it/s]
no element found: line 3642, column 0 ./3250_CsSnI3_mp-614013_2x2x1_with_noise_53
<class 'xml.etree.ElementTree.ParseError'> 13
 91%|█████████ | 3281/3600 [03:06<00:13, 22.91it/s]
no element found: line 1869, column 0 ./3283_CsSnI3_mp-614013_2x2x1_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3295/3600 [03:07<00:14, 20.44it/s]
no element found: line 1558, column 0 ./3290_CsSnI3_mp-614013_2x2x1_with_noise_9
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3565, column 0 ./3295_CsSnI3_mp-614013_2x2x1_with_noise_94
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1284, column 0 ./3299_CsSnI3_mp-614013_2x2x1_with_noise_98
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3305/3600 [03:07<00:10, 28.98it/s]
no element found: line 1821, column 0 ./3304_CsSnI3_mp-614013_2x2x2_with_noise_11
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1664, column 0 ./3305_CsSnI3_mp-614013_2x2x2_with_noise_12
<class 'xml.etree.ElementTree.ParseError'> 13
 92%|█████████▏| 3318/3600 [03:08<00:14, 18.91it/s]
no element found: line 1156, column 0 ./3314_CsSnI3_mp-614013_2x2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1484, column 0 ./3317_CsSnI3_mp-614013_2x2x2_with_noise_23
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2698, column 0 ./3320_CsSnI3_mp-614013_2x2x2_with_noise_26
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2406, column 0 ./3321_CsSnI3_mp-614013_2x2x2_with_noise_27
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3349/3600 [03:11<00:17, 14.48it/s]
no element found: line 2536, column 0 ./3345_CsSnI3_mp-614013_2x2x2_with_noise_49
<class 'xml.etree.ElementTree.ParseError'> 13
 93%|█████████▎| 3356/3600 [03:11<00:12, 20.30it/s]
no element found: line 976, column 0 ./3352_CsSnI3_mp-614013_2x2x2_with_noise_55
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▎| 3372/3600 [03:12<00:11, 20.53it/s]
no element found: line 1057, column 0 ./3371_CsSnI3_mp-614013_2x2x2_with_noise_72
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2095, column 0 ./3373_CsSnI3_mp-614013_2x2x2_with_noise_74
<class 'xml.etree.ElementTree.ParseError'> 13
 94%|█████████▍| 3386/3600 [03:13<00:11, 18.21it/s]
no element found: line 2540, column 0 ./3383_CsSnI3_mp-614013_2x2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3518/3600 [03:20<00:02, 32.91it/s]
no element found: line 1661, column 0 ./3512_CsSnI3_mp-614013_r2xr2x2_with_noise_19
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 3861, column 0 ./3514_CsSnI3_mp-614013_r2xr2x2_with_noise_20
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1494, column 0 ./3515_CsSnI3_mp-614013_r2xr2x2_with_noise_21
<class 'xml.etree.ElementTree.ParseError'> 13
 98%|█████████▊| 3534/3600 [03:21<00:02, 22.61it/s]
no element found: line 2651, column 0 ./3530_CsSnI3_mp-614013_r2xr2x2_with_noise_35
<class 'xml.etree.ElementTree.ParseError'> 13
 99%|█████████▉| 3579/3600 [03:23<00:01, 20.81it/s]
no element found: line 1643, column 0 ./3572_CsSnI3_mp-614013_r2xr2x2_with_noise_73
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 1647, column 0 ./3577_CsSnI3_mp-614013_r2xr2x2_with_noise_78
<class 'xml.etree.ElementTree.ParseError'> 13
100%|█████████▉| 3591/3600 [03:23<00:00, 30.24it/s]
no element found: line 4685, column 0 ./3583_CsSnI3_mp-614013_r2xr2x2_with_noise_83
<class 'xml.etree.ElementTree.ParseError'> 13
no element found: line 2669, column 0 ./3586_CsSnI3_mp-614013_r2xr2x2_with_noise_86
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 3600/3600 [03:24<00:00, 17.57it/s]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 221
```


### 1stMD 

* Ab-initio MD Simulation : Defect를 최대 2개까지 부여하고, Unitcell Size도 각각 다르게 9 종류
* 초기 INCAR 옵션은 다음과 같다.

``` Shell
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

* 초기 tar.gz 파일을 Parsing한 결과는 다음과 같았다.

``` Python
 45%|████▌     | 27/60 [02:25<02:19,  4.22s/it]
no element found: line 1119004, column 0 ./27.CsPbI3-rm-I2
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 60/60 [05:30<00:00,  5.51s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 1
```

* 의외로 ParsingError가 발생한 것은 1개뿐 -> 하지만 실제로 Target Propety 필터를 걸어주면 에너지가 지나치게 높은 상태가 많아서 상당한 데이터가 삭제되었던 것으로 기억하고, 그래서 2ndMD를 시도했었다.
* 27번 폴더 재계산 : 초기 INCAR 구성에서 NSW: 4000 -> 2000으로 바꾸고 다시 계산 시도하였음. -> **이제 데이터 추출(tar.gz)하고 파싱(pickle)하면 된다.**
* 최종 파싱 결과는 다음과 같다. : 238000개 데이터포인트

``` Python
100%|██████████| 60/60 [04:46<00:00,  4.78s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 0
```



### 2nd MD 데이터셋

* Ab-initio MD Simulation : 1stMD와 마찬가지로 Defect를 최대 2개까지 부여 + Unitcell Size는 서로 다른 9가지
* 1stMD 데이터셋에 비해 계산이 안정적으로 진행되도록 (그래서 물성 필터조건을 걸었을 때 삭제되는 데이터포인트가 적어지도록) INCAR 옵션을 조정하였다.
* POTIM = 5.00 / NSW = 7000, TEBEG = 500으로 수정
* 2ndMD 데이터셋의 초기 INCAR 구성은 다음과 같다.

``` Shell
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

* 초기 파싱 결과는 다음과 같다.

``` Python
 20%|██        | 12/60 [01:58<08:17, 10.37s/it]
no element found: line 2030, column 0 ./13.CsPbCl3-rm-Pb1
<class 'xml.etree.ElementTree.ParseError'> 13
 30%|███       | 18/60 [02:38<05:06,  7.29s/it]
no element found: line 2511749, column 0 ./18.CsPbCl3-rm-Cs1-Pb1
<class 'xml.etree.ElementTree.ParseError'> 13
 62%|██████▏   | 37/60 [05:51<02:49,  7.39s/it]
no element found: line 1653055, column 0 ./37.CsSnBr3-rm-Br2
<class 'xml.etree.ElementTree.ParseError'> 13
 77%|███████▋  | 46/60 [07:17<01:41,  7.28s/it]
no element found: line 702803, column 0 ./46.CsSnCl3-rm-Sn2
<class 'xml.etree.ElementTree.ParseError'> 13
 88%|████████▊ | 53/60 [08:23<01:01,  8.78s/it]
no element found: line 2384030, column 0 ./53.CsSnI3-rm-Sn1
<class 'xml.etree.ElementTree.ParseError'> 13
 90%|█████████ | 54/60 [08:25<00:41,  6.92s/it]
no element found: line 2442044, column 0 ./54.CsSnI3-rm-I1
<class 'xml.etree.ElementTree.ParseError'> 13
100%|██████████| 60/60 [09:35<00:00,  9.59s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 6
```

* 6개의 ParsingError 발생 : 모두 계산수렴이 안되서 발생하는 에러 -> 아마 1stMD에 비해 NSW를 늘려서 그런 것 같다.
* 재계산 : 초기 INCAR 구성에서 NSW: 7000 -> 4000으로 바꿔서 다시 계산 완료 -> **이제 데이터 추출(tar.gz) 및 파싱(pickle)만 하면 된다.**

* 최종 파싱 결과는 다음과 같다.

``` Python
100%|██████████| 60/60 [09:15<00:00,  9.27s/it]
======================== Total XML Parsing Completed!! =========================
Number of Parsing-Error-Count : 0
```

* 재계산한 6개의 계산폴더는 모두 정상적으로 수렴된 것 같다. : 402000개 데이터포인트


---
