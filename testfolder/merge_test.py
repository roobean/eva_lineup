import pandas as pd

full_df = pd.DataFrame()

paths = (
    "./testfolder/merge_input/subject-1.csv",
    "./testfolder/merge_input/subject-122.csv",
)

for path in paths:
    df = pd.read_csv(path)
    df["path_file"] = path
    full_df = pd.concat([df, full_df], axis=0)


# full_df.to_csv("./outputs/concat_test01.csv")
full_df["row_order"] = full_df.index
full_df = full_df.reset_index(drop=True)
print(full_df.head())
print(full_df["row_order"])
