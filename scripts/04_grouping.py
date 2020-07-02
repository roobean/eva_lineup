import pandas as pd

df = pd.read_csv("./outputs/03_cleaning_2.csv")

# gender first
grouped = df.groupby(["subject_nr", "condition", "date"])

df_merge = pd.DataFrame()
for name, group in grouped:

    selected_df = group[
        (group["datetime_updated"] == group["datetime_updated"].min())
        & (group["row_order"] == group["row_order"].min())
    ]

    gender_selected = (selected_df["gender_updated"].to_list())[0]
    group["gender_first"] = gender_selected

    df_merge = pd.concat([df_merge, group])


df_merge.to_csv("./outputs/04_grouping.csv", index=False)
