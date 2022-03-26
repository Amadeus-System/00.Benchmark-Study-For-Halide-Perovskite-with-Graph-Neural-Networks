# ===============================================================================
# Program : iterative_vasp_run.py
# Author  : Hyeongseon Park
# must be run in the main_dataset directory!!
# This code iteratively runs "vasp_run.sh" using "qsub" command in super-computing
# server in NURION (by KISTI)
# ===============================================================================

# ------------------ Library import -------------------------
import os
import shutil
import glob
from tqdm import tqdm

# ------------------ sub-directory list -------------------------
path = './*'
file_list = glob.glob(path)
dir_list = [element for element in file_list if os.path.isdir(element)]  # 계산 디렉터리 리스트 추출
dir_list_sorted = sorted(dir_list) # 정렬

# ------------------ Calculation Number -------------------------
# Sub-Directory Number-Parameter : from START -> to END
# 주의! 한번에 qsub 명령으로 제출할 수 있는 job의 수는 최대 40개!
# 주의! 한번에 qsub 명령으로 연산할 수 있는 job의 수는 최대 20개!
END = 40
START = END - 40

# ----------------------------------------------------------------
for each_dir in tqdm( dir_list_sorted[START:END] ):

    os.chdir(path = each_dir)       # 계산 서브디렉터리 들어가고

    os.system('qsub vasp_run.sh')   # qsub 명령 실행

    os.chdir(path = '../')          # 이전 디렉터리로 다시 나옴.

# 경고! : qsub 명령으로 연산실행되면, 그 디렉터리 위치를 함부로 바꿀 경우 경로를 찾지 못해 Error 발생!
# 이전 단계인 3단계 코드 : prepare_sub_directory.py에서 미리 앞에 인덱스 붙이는 정도가 적당할 듯 하다...
# ============================================ END ================================================ 