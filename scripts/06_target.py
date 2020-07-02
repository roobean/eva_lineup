import pandas as pd


df = pd.read_csv("./outputs_v2/05_grouping_2.csv")

RANK_SELECTION = [2, 4, 6, 8, 17, 19, 22]
TARGET_PAIR = {
    1: "a",
    2: "b",
    3: "a",
    4: "b",
    5: "c",
    6: "d",
    7: "c",
    8: "d",
    9: "c",
    10: "c",
    11: "d",
    12: "d",
    13: "e",
    14: "e",
    15: "e",
    16: "f",
    17: "g",
    18: "f",
    19: "g",
    20: "f",
    21: "h",
    22: "h",
}

df["lecture_datetime_rank"] = df["lecture_datetime"].rank(method="dense")


# df['Fruit Total']= df.iloc[:, -4:-1].sum(axis=1)
def target_from_sum(row):
    my_sum = row.loc["member1":"member6"].sum()
    if my_sum == 21:
        return "present"
    elif my_sum == 22:
        return "absent"
    else:
        return "error"


df["target_value"] = df.apply(target_from_sum, axis=1)


def target_translator(row):
    if row["lecture_datetime_rank"] in RANK_SELECTION:
        if row["target_value"] == "present":
            return "absent"
        else:
            return "present"

    else:
        if row["target_value"] == "present":
            return "present"
        else:
            return "absent"


df["target_correct"] = df.apply(target_translator, axis=1)


df["target_pair"] = df["lecture_datetime_rank"].map(TARGET_PAIR)


df.to_csv("./outputs_v2/06_target.csv", index=False)
