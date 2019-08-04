import pandas as pd

df = pd.read_csv("./outputs/full_08_gender_first.csv")

df = df.drop_duplicates(
    subset=["member", "condition", "subject_nr", "gender_updated"]
)

df.to_csv("./outputs/full_09_repetion.csv", index=False)

