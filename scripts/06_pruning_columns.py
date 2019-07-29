import pandas as pd


df = pd.read_csv("./outputs/full_05_target_value_added.csv")
columns_to_filter = pd.read_csv("./input_other/filter_columns.csv")[
    "filter_column"
].to_list()

df_filtered = df.loc[:, columns_to_filter]
# filtered columns in outputs as well!
df_invert = df.drop(columns_to_filter, axis=1)
dropped_columns = pd.Series(list(df_invert.columns))
dropped_columns.to_csv(
    "./outputs/full_06_INFO_dropped_columns.csv",
    header=["dropped_columns"],
    index=False,
)
df_filtered.to_csv("./outputs/full_06_pruning_columns.csv")
