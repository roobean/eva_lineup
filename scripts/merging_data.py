import pandas as pd
import os

rootdir = "./input_data"

list_of_paths = []
for root, dirs, files in os.walk(rootdir, topdown=False):
    for name in files:
        if ".csv" in name:
            list_of_paths.append(os.path.join(root, name))

full_df = pd.DataFrame()
for path in list_of_paths:
    df = pd.read_csv(path)
    df["path_file"] = path
    full_df = pd.concat([df, full_df], axis=0)

full_df["row_order"] = full_df.index
full_df = full_df.reset_index(drop=True)
full_df.to_csv("./outputs/alldata.csv")
