import pandas as pd
from datetime import datetime, time, date

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
    except:
        date_from_datetime = datetime.strptime(
            row["datetime"], "%d/%m/%Y %H:%M"
        ).date()

    combo = datetime.combine(date_from_datetime, row["lecture_time"])
    return combo.isoformat()


df["new_datetime"] = df.apply(datetimer, axis=1)

list_datetime = list(df["new_datetime"].unique())
print(list_datetime.sort())
rank_dict = {}
for i, value in enumerate(list_datetime):
    rank_dict.update({value: i})


df["rank"] = df["new_datetime"].map(rank_dict)


df.to_csv("./outputs/full_07_datetime.csv")
