import pandas as pd


df = pd.read_csv("./outputs/06_target.csv")
"""


NEW [identification_decision]
- if [identification] = YES
    if [person] < 6:
        return 'filler'
    else:
        if [target_correct] == 'present':
            return 'target'
        else:
            return 'innocent'
- else:
            return 'rejection'
"""


def ident_decision(row):
    if row["identification"] == "Yes":
        if row["person"] < 6:
            return "filler"
        else:
            if row["target_correct"] == "present":
                return "target"
            else:
                return "innocent"
    else:
        return "rejection"


df["identification_decision"] = df.apply(ident_decision, axis=1)


def not_sure_decision(row):
    if row["identification"] == "Not sure":
        if row["person"] < 6:
            return "filler"
        else:
            if row["target_correct"] == "present":
                return "target"
            else:
                return "innocent"
    else:
        return "other"


df["not_sure_decision"] = df.apply(not_sure_decision, axis=1)


"""
final selections
- pro subject_nr, condition, gender_updated SELECT highest rep
- to NEW [final_lineup] = 'yes' or 'no'
"""
df["final_lineup"] = ""
df["repetition_numeric"] = pd.to_numeric(df["repetition"], errors="coerce")
grouped = df.groupby(
    ["subject_nr", "condition", "gender_updated", "date_rank"]
)
df_merge = pd.DataFrame()
for name, group in grouped:
    group_copy = group.copy()
    rep_max = group_copy["repetition_numeric"].max()

    group_copy["final_lineup"] = group_copy["repetition_numeric"] == rep_max

    df_merge = pd.concat([df_merge, group_copy])


df_merge.to_csv("./outputs/07_final_selections.csv", index=False)
