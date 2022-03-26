# ===============================================================================
# Program : prepare_KPOINTS.py
# Author  : Hyeongseon Park
# must be run in the main_dataset directory!!
# generation code to make 6 kinds of KPOINTS files with respect to unitcell size
# must be run in the main_dataset directory -> generate 6 KPOINTS files
# ===============================================================================

# --------------- Library import -------------------------
import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle
import os
import glob
from math import sqrt

# 미리 수동으로 만들어둔 unitcell_size_dict <- 나중에 Mapping 예정
unitcell_size_dict = {
    '1x1x1'   : [1, 1, 1],
    '2x1x1'   : [2, 1, 1],
    'r2xr2x1' : [sqrt(2), sqrt(2), 1],
    '2x2x1'   : [2, 2, 1],
    'r2xr2x2' : [sqrt(2), sqrt(2), 2],
    '2x2x2'   : [2, 2, 2]}

# ------------------------------------------------------------------
path = './*'                   # 현재 디렉터리의 모든 파일 경로
file_list = glob.glob(path)    # path 의 모든 경로 리스트 
original_vasp_list = [element for element in file_list if element.endswith('.vasp')] # original vasp file list
original_vasp_list_sorted = sorted(original_vasp_list)  # 정렬
# ------------------------------------------------------------------

for each_original_vasp in original_vasp_list_sorted:

    _index = each_original_vasp.replace('.vasp', '').rfind('_')
    current_unitcell_size = each_original_vasp.replace('.vasp', '')[_index + 1:] # vasp 파일의 unitcell size 구한다.

    # unitcell size 알면 딕셔너리 맵핑으로 수치화 가능 -> 나중에 이 값은 KPOINTS 파일의 k-grid 값에 역수로 곱해주어야 함.
    R = unitcell_size_dict[current_unitcell_size]

    # 동일한 unitcell size의 vasp file 및 noise_vasp_file -> 모두 동일한 KPOINTS 파일을 가진다.
    # 그러므로 KPOINTS_BASE 파일로부터 미리 6종류의 KPOINTS 파일들을 만들어두면 된다.
    with open('./KPOINTS_BASE', 'r') as f:
        content = f.readlines()    # content 변수에 KPOINTS_BASE 파일의 내용을 리스트로 모두 저장
        f.close()                  # KPOINTS_BASE 파일은 필요 없으므로 종료.

    k_grid_list = content[3].replace('\n', '').strip().split('  ')   # content의 4번째 줄에 접근. 기존의 k-grid 값을 리스트로 추출
    k_grid_list = [float(k) for k in k_grid_list]                    # k-grid 문자열을 실수로 변환

    new_k_grid = []
    for k, r in zip(k_grid_list, R):         # 현재의 k_x, k_y, k_z 값과 unitcell size r_x, r_y, r_z를 함께 추출
        new_k = k / r                        # k값을 unitcell size로 나눈 값을 새로운 k값으로 선언 
        new_k_grid.append(str(int(new_k)))   # integer -> string 변환하여 리스트에 저장

    result = ' '           # content[3]에 갱신할 k-grid 값을 저장하는 변수
    for i in new_k_grid:
        result += i + '  '
    result += '\n'
    content[3] = result    # content에 갱신
    
    with open('KPOINTS_{}'.format(current_unitcell_size), 'w') as p:  # unitcell size에 특화된 KPOINTS 파일 생성
        for element in content:
            p.write(element)    # 갱신된 content 문자열 내용 입력
        p.close()               # 파일 종료

# ============================================ END ===============================================