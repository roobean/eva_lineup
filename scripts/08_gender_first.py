import pandas as pd

df = pd.read_csv("./outputs/full_07_datetime.csv")


"""
GOAL
- 
-new ['gender_first']
-for every subset ['subject_no', 'condition', 'solo_date']  
    -filter row of minimum [datetime] and gets its 'gender' value
    -save to ['gender_first']
"""
df["gender_first"] = ""
grouped = df.groupby(["subject_nr", "condition", "solo_date"])

new_df = pd.DataFrame()
for name, group in grouped:
    # getting row of minimum datetime
    minimum_datetime = group["datetime"].min()
    minimum_rank = group["row_order"].min()
    min_df = group[
        (group["datetime"] == minimum_datetime)
        & (group["row_order"] == minimum_rank)
    ]
    group["gender_first"] = min_df["gender_updated"].to_list()[0]
    group["repetition"] = (group["member"].value_counts().min()) - 1
    new_df = pd.concat([new_df, group])

new_df.to_csv("./outputs/full_08_gender_first.csv", index=False)
