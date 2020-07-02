import pandas as pd

"""
GOAL:
NEW [unique_decision]
for final_selection == True
    row, kde identification yes -> new['unique_decision'] = 'identification'
    (row, kde identification not sure) & (person > 5)
        -> [unique_decision] = 'not sure'
    else
        tak 1st row -> new['unique_decision'] = 'rejection'
"""


df = pd.read_csv("./outputs_v2/07_final_selections.csv")

df["unique_decision"] = ""

grouped = df[df["final_lineup"] == True].groupby(
    ["subject_nr", "condition", "gender_updated", "date_rank"]
)


for name, group in grouped:
    if (group["identification"] == "Yes").any():
        index = group[group["identification"] == "Yes"].index
        df.loc[index, "unique_decision"] = "identification"

    elif (group["identification"] == "Not sure").any():
        select_df = group[group["identification"] == "Not sure"]
        if (select_df["person"] > 5).any():
            select_df_person = select_df[(select_df["person"] > 5)]
            index = (select_df_person.iloc[[0]]).index
            df.loc[index, "unique_decision"] = "not sure"
        else:
            index = (group.iloc[[0]]).index
            df.loc[index, "unique_decision"] = "rejection"

    else:
        index = (group.iloc[[0]]).index
        df.loc[index, "unique_decision"] = "rejection"

df.to_csv("./outputs_v2/final_data_2019-08-11.csv", index=False)
