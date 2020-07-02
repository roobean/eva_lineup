import pandas as pd


df = pd.read_csv("./outputs/full_02_cleaning_1.csv")

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
for index, row in df.iterrows():
    if pd.isnull(row["member1"]):
        # getting address details
        gender = row["gender_updated"]
        subject_nr = row["subject_nr"]
        date_rank = row["date_rank"]

        # getting row value from external file
        row_select = live_data[
            (live_data["Day"] == date_rank)
            & (live_data["Trial#"] == subject_nr)
        ]

        if gender == "male":
            new_values = (row_select.iloc[:, 2:8].values.tolist())[0]
            df.loc[index, "member1":"member6"] = new_values
        else:
            new_values = (row_select.iloc[:, 8:].values.tolist())[0]
            df.loc[index, "member1":"member6"] = new_values

    else:
        pass


# member_translate
MEMBER_TRANSLATE = {
    "[member6]": "6",
    "[member5]": "5",
    "[member4]": "4",
    "[member3]": "3",
    "[member2]": "2",
    "[member1]": "1",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
}

df["member"] = df["member"].map(MEMBER_TRANSLATE)

df["person"] = ""


def member_locator(row):
    try:
        member_location = row["member"]
        member_address = "member" + member_location
        row["person"] = row[member_address]
    except:
        pass

    return row


df = df.apply(member_locator, axis=1)

df.to_csv("./outputs/03_cleaning_2.csv", index=False)
