import pandas as pd


df = pd.read_csv("./outputs/full_02_basic-cleaning.csv")

# member change
member_translate = {
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

df["member"] = df["member"].map(member_translate)

# new ['person'] as value defined by member value
# which poinst to [member1] - [member6]


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

df.to_csv("./outputs/full_03_member_definition.csv")
