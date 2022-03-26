# ===============================================================================
# Program : generate_noised_vasp_files.py
# Author  : Hyeongseon Park
# must be run in the main_dataset directory!!
# This code generates multiple number of vasp files with Gaussian noises 
# for the internal coordinates (fractional coordinates) and lattice parameters of
# the Crystal structure
# ===============================================================================

# --------------- Library import -------------------------
import numpy as np
import pandas as pd
from tqdm import tqdm
from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp import Poscar
from pymatgen.core.structure import Structure, Lattice
import pickle
import os
import glob
from math import sqrt

# ------------ Calculation parameter ---------------------
num_noised_files = 100
gaussian_noise_level = 0.01

# ---------------------------------------------------------
path = './*'                   # 현재 디렉터리의 모든 파일 경로
file_list = glob.glob(path)    # path 의 모든 경로 리스트 
vasp_list = [element for element in file_list if element.endswith('.vasp')]    # vasp 확장자 파일 리스트
vasp_list_sorted = sorted(vasp_list)    # 정렬
# ---------------------------------------------------------

for each_original_vasp in tqdm(vasp_list_sorted):                   # 각각의 original vasp file에 대해 순서대로 접근(정렬) 

    crystal = Structure.from_file(filename = each_original_vasp)    # vasp file read -> structure 정보 접근

    for i in range(num_noised_files):                               # original vasp file로부터 noised vasp 파일을 횟수만큼 생성

        # -------------------------- lattice 구조에 noise 부여하기 -----------------------------------------
        lattice_shell = np.zeros(shape = crystal.lattice.matrix.shape)                     # 새로운 lattice matrix shell 생성
        
        noised_lattice = gaussian_noise_level * np.random.normal(0, 1, 9).reshape((3, 3))  # 기존 lattice matrix에 넣을 noise 생성

        new_lattice_matrix = crystal.lattice.matrix + noised_lattice                       # 기존 lattice matrix에 noise 추가

        noised_lattice = Lattice(new_lattice_matrix)                                       # noise 추가된 새로운 lattice 
        noised_crystal = Structure(noised_lattice, crystal.species, crystal.frac_coords)   # unitcell에 noise 추가된 결정구조
        # -----------------------------------------------------------------------------------------------

        # --------------------------- 결정구조 안의 각 원자에 대해 좌표 noise 부여 -------------------------
        for j in range(len(noised_crystal)):  # For each atom in the crystal structure
            noised_coord = list(gaussian_noise_level * np.random.normal(0, 1, 3).reshape(-1)) # internal coordinate noise 
            noised_crystal[j] = noised_crystal[j].specie.name, noised_crystal[j].frac_coords + noised_coord # 각 원자 좌표에 noise 추가
        # -----------------------------------------------------------------------------------------------

        # vasp file saved
        noised_crystal.to(fmt = 'poscar',
                          filename = '{}_with_noise_{}.vasp'.format(each_original_vasp[:-5], i+1)) # 변화된 structure를 .vasp로 저장

# -------------------------------------------------------------------------------------------------------
# 36개의 original vasp file을 기반으로 x (num_noised_files) 만큼의 noised_vasp file을 만들었다면
# 원본에 해당하는 noise가 섞이지 않은 36개의 초기 vaso 파일들은 제거 -> [36 x num_noised_files]개의 noised vasp file 생성
for each_original_vasp in tqdm(vasp_list_sorted):  
    os.remove(each_original_vasp) # original vasp removed

# -------------- 만들어진 noised_vasp_files의 개수를 확인 -------------------
path = './*'                  
file_list = glob.glob(path)    
vasp_list = [element for element in file_list if element.endswith('.vasp')]  # vasp file list
vasp_list_sorted = sorted(vasp_list)    # 정렬
print()
print('The number of generated noised vasp files : {}'.format(len(vasp_list_sorted))) # 36 x num_noised_files

# ============================================= END =============================================