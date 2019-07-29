import pandas as pd

df = pd.read_csv("./outputs/full_04_condition_added.csv")

targetDict = {"[target1]": "target1", "[target2]": "target2"}
df["target"] = df["target"].map(targetDict)


def targetter(row):
    column_address = row["target"]
    try:
        row["target_value"] = row[column_address]
    except:
        pass
    return row


df["target_value"] = ""
df = df.apply(targetter, axis=1)

df.to_csv("./outputs/full_05_target_value_added.csv")
