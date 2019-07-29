import pandas as pd

df = pd.read_csv("./outputs/full_03_member_definition.csv")


def conditioner(row):
    condition_dict = {"live": "live", "FB": "FB", "VIPER": "HS"}
    string_to_search = row["experiment_file"]
    for key, value in condition_dict.items():
        if key in string_to_search:
            row["condition"] = value
            return row
    print(row["experiment_file"])

    return row


df["condition"] = ""
df = df.apply(conditioner, axis=1)
df.to_csv("./outputs/full_04_condition_added.csv")
