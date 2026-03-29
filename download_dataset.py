"""
This code was provided by Kaggle:
Network Intrusion Detection. (2018, October 9). https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection/code

"""

import kagglehub
import shutil
import os
import sys

# Download latest version
path = kagglehub.dataset_download("sampadab17/network-intrusion-detection")

print("Path to dataset files:", path)
# (Network Intrusion Detection, 2018)

source_path = path.removesuffix("\\versions\\1")
repo_path = os.path.dirname(os.path.abspath(sys.argv[0]))
dest = shutil.move(source_path, repo_path, copy_function=shutil.copytree)
