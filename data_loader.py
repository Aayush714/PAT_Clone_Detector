from datasets import load_dataset
import pandas as pd
import multiprocessing as mp


pool = mp.Pool(mp.cpu_count())
# Reading the .csv file
print("Loading Data from file and removing missing data")
bcb = pd.read_csv(
    "/Users/aayushgupta/Library/Mobile Documents/com~apple~CloudDocs/Program testing and analysis/PAT-Clone-Detection_old/train.csv")

pool.close()
# print("Dataset Loaded !!!")


# def load_big_clone_bench(split=None):
#     bcb = load_dataset("code_x_glue_cc_clone_detection_big_clone_bench")
#     if split == None:
#         return bcb
#     else:
#         return bcb[split]
