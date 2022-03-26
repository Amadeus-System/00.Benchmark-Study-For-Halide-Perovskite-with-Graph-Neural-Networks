# ===============================================================================
# Program : prepare_sub_directory.py
# Author  : Hyeongseon Park
# must be run in the main_dataset directory!!
# This code generates multiple sub-directories for vasp calculation for each vasp 
# files in the main_dataset directory
# ===============================================================================

# ------------------ Library import -------------------------
import os
import shutil
import glob
from math import sqrt
from tqdm import tqdm

unitcell_size_dict = {
    '1x1x1'   : [1, 1, 1],
    '2x1x1'   : [2, 1, 1],
    'r2xr2x1' : [sqrt(2), sqrt(2), 1],
    '2x2x1'   : [2, 2, 1],
    'r2xr2x2' : [sqrt(2), sqrt(2), 2],
    '2x2x2'   : [2, 2, 2]}

# ----------------------- vasp file list ----------------------------------
path = './*'
file_list = glob.glob(path)
vasp_list = [element for element in file_list if element.endswith('.vasp')]  # vasp file list
vasp_list_sorted = sorted(vasp_list)    # 정렬

# ------------------------- vasp_run.sh -----------------------------------
qsub_contents = """#!/bin/sh
#PBS -V 
#PBS -A vasp 
#PBS -N vasp_run 
#PBS -q normal 
#PBS -l select=1:ncpus=8:mpiprocs=4:ompthreads=2 
#PBS -l walltime=2:00:00 

cd $PBS_O_WORKDIR

module load craype-mic-knl 
module load intel/18.0.3 impi/18.0.3 
export PATH=/home01/x2219a05/bin:$PATH 

time mpirun --map-by NUMA:PE=2 vasp_5.4.4.std > mpi.out """

# ----------------------------------------------------------
for each_vasp_file in tqdm(vasp_list_sorted):

    # Directory name
    dir_name = each_vasp_file[:-5]  # 뒷 문자열 '.vasp'를 제외한 것을 서브디렉터리 이름으로 지정

    # INCAR 파일에 넣을 title 추출
    _index = each_vasp_file[2:-5].find('_')
    incar_title = each_vasp_file[2:-5][:_index]

    # -------------------- 계산 디렉터리 생성 --------------------
    if not os.path.exists(path = dir_name):      # 계산 디렉터리가 존재하지 않으면
        os.mkdir(dir_name)                       # 계산 디렉터리 생성
    else:                                        # 디렉터리가 이미 있다면?
        print('Sub-Directory Already Exist!')    # 경고문 출력
    # -----------------------------------------------------------

    # --------- POSCAR / INCAR / KPOINTS 파일을 서브디렉터리 안으로 복사로 넣어줌 ----------
    shutil.copy(src = each_vasp_file, dst = dir_name)   # vasp 파일 넣어줌
    shutil.copy(src = './INCAR_BASE', dst = dir_name)   # INCAR_BASE 파일을 넣어줌

    # ----------- KPOINTS 파일은 unitcell_size를 알아내고 나서 복사로 넣어준다. -------------
    for key in unitcell_size_dict.keys():
        if key in dir_name:        # 만약 unitcell_size가 dir_name 안에 있다면
            unitcell_size = key    # 디렉터리에 맞는 unitcell_size 구한 것
            break                  # 반복문 중지
    shutil.copy(src = './KPOINTS_{}'.format(unitcell_size), dst = dir_name)  # 해당 unitcell_size의 KPOINTS 파일을 서브디렉터리에 넣어줌

    # ------------- 만든 계산 디렉터리로 이동 (주의! 나중에 다시 나와야 함!) ---------------
    os.chdir(path = dir_name)

    # -------------------------------- Rename --------------------------------------------
    os.rename(src = each_vasp_file, dst = 'POSCAR')
    os.rename(src = './KPOINTS_{}'.format(unitcell_size), dst = 'KPOINTS')

    # ---------- INCAR_BASE 파일 열어서 첫 줄만 내용변경하여 INCAR로 다시 저장 (편집과 raname 동시에 함) ----------
    with open('./INCAR_BASE', 'r+') as f:
        content = f.readlines()
        content[0] = 'SYSTEM = {}'.format(incar_title)
        f.close()
    with open('./INCAR', 'w') as p:
        for element in content:
            p.write(element)
        p.close()
    os.remove('./INCAR_BASE')    # 필요 없으므로 삭제

    # ------------------------------ POTCAR 생성코드 ----------------------------------------
    os.system(command = 'GenPOTCAR.py PBE') # return 0하면 제대로 실행되었다는 것

    # vasp_run.sh Script 생성 -> 각 서브 디렉터리에 이것이 준비되어 있어야 qsub 명령으로 연산넣어주기 가능!
    with open('vasp_run.sh', 'w') as f:
        f.write(qsub_contents) 
        f.close()    

    # 계산종료 감지할 필요없이 qsub 명령으로 넣어주고 바로 이전 디렉터리로 돌아감.
    os.chdir(path = '../')    
    

# ------------------- main dataset 디렉터리로 돌아와서 남은 .vasp 파일들 모두 제거 --------------------
path = './*'
file_list = glob.glob(path)
vasp_list = [element for element in file_list if element.endswith('.vasp')]    # vasp file list
vasp_list_sorted = sorted(vasp_list)    # 정렬

for each_vasp_file in vasp_list_sorted:   # 각각의 vasp 파일들에 대해
    os.remove(each_vasp_file)             # 모두 제거


# --------------------- 생성된 모든 계산 디렉터리에 대해 구별하기 쉽게 앞에 인덱스 붙여줌! -------------------
path = './*'
file_list = glob.glob(path)
dir_list = [element for element in file_list if os.path.isdir(element)]  # sub-directory list
dir_list_sorted = sorted(dir_list) # 정렬

for index, each_dir in enumerate(dir_list_sorted):
    new_dir_name = '{0:04d}_'.format(index + 1) + each_dir[2:] # new directory name with pre_index
    os.rename(src = each_dir, dst = new_dir_name) # rename

# ========================================== END ===========================================