import pandas as pd


df = pd.read_csv("./outputs_v2/04_grouping.csv")


# repetition

df_merge = pd.DataFrame()

grouped = df.groupby(["subject_nr", "condition", "date", "gender_updated"])
for name, group in grouped:

    # just for some inspection
    inspect = False
    if inspect is True:
        print(name)
        print(
            group[
                [
                    "path_file",
                    "subject_nr",
                    "gender_updated",
                    "datetime",
                    "datetime_updated",
                    "lecture_datetime",
                    "member",
                    "row_order",
                ]
            ]
        )
        print(20 * "-")
        input()
    else:
        pass

    # to assign repetions
    member_list = group["member"].to_list()

    repetition_list = []
    counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    if member_list[0] == 1:
        for index, member in enumerate(member_list):
            # checks for repeated 6
            if (member == 6) & (member_list[index - 1] == 6):
                repetition_list.append("repeated_six")
            else:
                repetition_list.append(counter[member])
                counter[member] += 1

    elif member_list[0] == 6:
        for index, member in enumerate(member_list):
            if index == 0:
                repetition_list.append("first_six")
            else:
                # checks for repeated 6
                if (member == 6) & (member_list[index - 1] == 6):
                    repetition_list.append("repeated_six")
                else:
                    repetition_list.append(counter[member])
                    counter[member] += 1
    else:
        print("something else?")
        input()

    group["repetition"] = repetition_list
    df_merge = pd.concat([df_merge, group])


df_merge.to_csv("./outputs_v2/05_grouping_2.csv", index=False)

