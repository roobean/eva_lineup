import pandas as pd

df = pd.read_csv("./outputs/alldata.csv")

# one-dimensional columns
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

df_singletons.to_csv("./outputs/singletons.csv", index=False)

df = df.drop(column_names, axis=1)
df.to_csv("./outputs/all_droped_singletons.csv")
