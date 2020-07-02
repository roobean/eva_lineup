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

    # here goes individual df manipulations
    # 1. filling whole [lecture_time] based on last value
    try:
        df["lecture_time"] = list(df["lecture_time"])[-1]
    except:
        print("no lecture_time for ", path)

    # 2. filling whole [time_end] based on last value
    try:
        df["time_end_of_experiment"] = list(df["time_end_of_experiment"])[-1]
    except:
        print("no time_end_of_experiment for ", path)

    full_df = pd.concat([df, full_df], axis=0, sort=True)


full_df["row_order"] = full_df.index
full_df = full_df.reset_index(drop=True)
full_df.to_csv("./outputs_v2/full_01_merged.csv")
