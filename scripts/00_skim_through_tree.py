import pandas as pd
import os

rootdir = "./input_data"

list_of_paths = []
for root, dirs, files in os.walk(rootdir, topdown=False):
    for name in files:
        if ".csv" in name:
            list_of_paths.append(os.path.join(root, name))

with open("./outputs/list_of_csv-files.txt", "w") as f:
    for path in list_of_paths:
        f.write(f"\n{path}")

if os.path.isfile("./outputs/dimensions_of_csv-files.txt") is True:
    os.remove("./outputs/dimensions_of_csv-files.txt")
for path in list_of_paths:
    df = pd.read_csv(path)
    with open("./outputs/dimensions_of_csv-files.txt", "a") as f:
        f.write(f"\n{path}\t{df.shape}")
