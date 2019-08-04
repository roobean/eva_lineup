import pandas as pd

from datetime import datetime, time

df = pd.read_csv("./outputs/full_06_pruning_columns.csv")

"""
2) convert lecture times to real times
3) get new datetime_updated from date of datetime and lecture_time
4) get ranks and save as [event]
"""
# lecture time convert

df["lecture_time"].fillna("other", inplace=True)

lecture_time_dict = {
    "other": time(0),
    "1pm": time(13),
    "10am": time(10),
    "11am": time(11),
    "12.15pm": time(12, 15),
    "11.30am": time(11, 30),
    "10.45am": time(10, 45),
    "12am": time(12),
    "2pm": time(14),
    "12noon": time(12),
    "12 noon": time(12),
}
df["lecture_time"] = df["lecture_time"].map(lecture_time_dict)


def datetimer(row):
    # from try / except to if/else
    try:
        date_from_datetime = datetime.strptime(
            row["datetime"], "%m/%d/%y %H:%M:%S"
        ).date()
    except Exception:
        date_from_datetime = datetime.strptime(
            row["datetime"], "%d/%m/%Y %H:%M"
        ).date()

    combo = datetime.combine(date_from_datetime, row["lecture_time"])
    return combo.isoformat()


df["new_datetime"] = df.apply(datetimer, axis=1)


def date_fixer(row):
    date_fixer_dict = {"2017-04-11": "2017-11-04", "2018-07-02": "2018-02-07"}
    date_value = row["new_datetime"]
    date_value_part = date_value[:10]
    if date_value_part in date_fixer_dict:
        date_value = date_value.replace(
            date_value_part, date_fixer_dict[date_value_part]
        )
        return date_value
    else:
        return date_value


df["new_datetime"] = df.apply(date_fixer, axis=1)

df["rank"] = df["new_datetime"].rank(method="dense")


def date_only_parser(row):
    date_from_datetime = datetime.strptime(
        row["new_datetime"], "%Y-%m-%dT%H:%M:%S"
    ).date()
    return date_from_datetime


df["solo_date"] = df.apply(date_only_parser, axis=1)
df["date_rank"] = df["solo_date"].rank(method="dense")


# gender fill
def gender_first_selector(row):
    if row["gender"] in ["female", "male"]:
        return row["gender"]
    else:
        if "WOMEN" in row["experiment_file"]:
            return "female"
        else:
            return "male"


df["gender_updated"] = df.apply(gender_first_selector, axis=1)


df.to_csv("./outputs/full_07_datetime.csv", index=False)

# df.iloc[:,np.r_[4,11:18,21:25,37:]]
