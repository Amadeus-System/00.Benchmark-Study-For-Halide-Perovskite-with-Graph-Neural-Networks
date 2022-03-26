# Python APIs to generate Halide Perovskite Datasets

* DFT calculation using **Vasp 5.4.4.std**
* main materials : **halide perovskites** (6 kinds)
* Machine Learning application such as GNN

![DFT](https://user-images.githubusercontent.com/76824867/139533526-fe6d443a-9e0a-4e24-a4b5-64b691a1e1b8.png)

## Expected main directory configuration
> **main_dataset** <br>
├── perovskite1.vasp <br>
├── perovskite2.vasp <br>
├── perovskite3.vasp <br>
├── ... <br>
├── INCAR_BASE <br>
├── KPOINTS_BASE <br>
├── 1.prepare_KPOINTS.py <br>
├── 2.generate_noised_vasp_files.py <br>
├── 3.prepare_sub_directory.py <br>
├── 4.iterative_vasp_run.py <br>
├── 5.check_qsub_results.py <br>

## Running order of python codes.
**All of these python codes must be run in the main_dataset directory!!**

1. **prepare_KPOINTS.py**
> This code must be run in the main_dataset directory --> generate 6 "KPOINTS" files.
2. **generate_noised_vasp_files.py** 
> This code generates multiple number of vasp files with Gaussian noises for the internal coordinates (fractional coordinates) and lattice parameters of the Crystal structure.
3. **prepare_sub_directory.py** 
> This code generates multiple sub-directories for vasp calculation for each vasp files in the main_dataset directory.
4. **iterative_vasp_run.py** 
> This code iteratively runs "vasp_run.sh" using "qsub" command in the super-computing server in NURION (by KISTI)
5. **check_qsub_results.py** 
> This code checks how many sub-directories are calculated using "qsub" command and it returns the number of already-calculated sub-directories.
