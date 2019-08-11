import pandas as pd
from datetime import time

df = pd.read_csv("./outputs_v2/full_01_merged.csv")

# dropping columns
columns_to_filter = pd.read_csv("./input_other/filter_columns_v2.csv")[
    "filter_column"
].to_list()


df_invert = df.drop(columns_to_filter, axis=1)
df = df.loc[:, columns_to_filter]
dropped_columns = pd.Series(list(df_invert.columns))
dropped_columns.to_csv(
    "./outputs_v2/INFO_dropped_columns.csv",
    header=["dropped_columns"],
    index=False,
)

# 1.one-dimensional columns
column_names, column_values = [], []
for column in df.columns:
    if len(df[column].unique()) == 1:
        column_names.append(column)
        column_values.append(df[column].unique()[0])
    else:
        pass

df_singletons = pd.DataFrame(
    dict(column_name=column_names, column_value=column_values)
)

df_singletons.to_csv("./outputs_v2/other/singletons.csv", index=False)

df = df.drop(column_names, axis=1)

# 2. rows where [member] == null
df = df[df["member"].notna()]


# [datetime] repair
df["date"] = df.apply(lambda x: str(x["datetime"]).split()[0], axis=1)
df["time"] = df.apply(lambda x: str(x["datetime"]).split()[1], axis=1)


def time_fix(cell):
    if len(cell) != 8:
        cell += ":00"
    return cell


df["time"] = df["time"].apply(time_fix)

DATE_FIX = {
    "02/07/18": "2018/02/07",
    "02/07/2018": "2018/02/07",
    "11/04/17": "2017/11/04",
    "11/04/2017": "2017/11/04",
    "12/02/17": "2017/12/02",
    "02/14/18": "2018/02/14",
    "02/21/18": "2018/02/21",
    "03/21/18": "2018/03/21",
    "10/06/18": "2018/10/06",
    "11/10/18": "2018/11/10",
    "12/01/18": "2018/12/01",
}

df["date"] = df["date"].map(DATE_FIX)
df["datetime_updated"] = df["date"] + " " + df["time"]


df["date_rank"] = df["date"].rank(method="dense")
df["datetime_rank"] = df["datetime_updated"].rank(method="dense")
# lecture_time

df["lecture_time"].fillna("other", inplace=True)

LECTURE_TIME_DICT = {
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
    "no": time(12),
}
df["lecture_time"] = df["lecture_time"].map(LECTURE_TIME_DICT)


df.to_csv("./outputs_v2/full_02_cleaning_1.csv", index=False)
