import pandas as pd


df = pd.read_csv("./outputs_v2/full_02_cleaning_1.csv")

# condition assignment


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


# target value

TARGET_DICT = {"[target1]": "target1", "[target2]": "target2"}
df["target"] = df["target"].map(TARGET_DICT)


def targetter(row):
    column_address = row["target"]
    try:
        row["target_value"] = row[column_address]
    except:
        pass
    return row


df["target_value"] = ""
df = df.apply(targetter, axis=1)

# filling gender


def gender_first_selector(row):
    if row["gender"] in ["female", "male"]:
        return row["gender"]
    else:
        if "WOMEN" in row["experiment_file"]:
            return "female"
        else:
            return "male"


df["gender_updated"] = df.apply(gender_first_selector, axis=1)
df["lecture_datetime"] = df["date"] + " " + df["lecture_time"]


# filling missing member data for live condition
live_data = pd.read_csv("./input_other/live_update.csv")
print(live_data)
for index, row in df.iterrows():
    if pd.isnull(row["member1"]):
        print(row["gender_updated"])
        print(row["subject_nr"])
        print(row["date_rank"])
        input()
    else:
        pass


df.to_csv("./outputs_v2/03_cleaning_2.csv", index=False)
