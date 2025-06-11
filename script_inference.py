import glob
import os
import json

base_path = "./data/different_types"
#dir_names = glob.glob(f"experiments/*")
dir_names=['experiments/double_stretch_sloth']
for dir_name in dir_names:
    case_name = dir_name.split("/")[-1]

    os.system(
        f"python inference_warp.py --base_path {base_path} --case_name {case_name}"
    )
