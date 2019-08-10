import pandas as pd
import os


def main():
    """
    00
    # exploration of folders
    01
    # loading single dataframes and merging them together
    02
    # droping columns with no or single value + exporting
    # droping rows where [member].isna
    03
    # mapping values of ['member'] to list
    # NEW ['person'] returns value of column defined as 'member' + ['member'] 
      or empty
    04
    # NEW ['condition'] based on substring match in ['experiment_file']
      using dict
    05
    # NEW ['target'] mapped from dict in this way: '[target1]' > 'target1'
    # NEW ['target_value'] returns value of column defined as ['target']
    06
    # droping columns that are not in external sheet
    # saving dropped column names into external sheet
    07
    # where ['lecture_time'].isna, assing 'other'
    # map ['lecture_time'] to time objects using dict, 'other' = time(0)
    # NEW ['new_datetime'] as date object from ['datetime'] +
      + time object from ['lecture_time']
    # repairing ['new_datetime] by mapping its substring to dict
    # NEW ['rank'] - rank based on ['new_datetime'], using dense method (squeeze low)
    # NEW ['solo_date'] getting date object from ['new_datetime'] string
    # NEW ['date_rank'] - rank based on ['solo_date'], dense method
    # NEW ['gender_updated'] fills empty cells of ['gender']
      based on substring of ['experiment_file']
    08
    # PROCESS groupby
      through groupby ["subject_nr", "condition", "solo_date"]
      and drilling to row with ['datetime'].min() & ['row_order'].min() setting
      ['gender_first'] = value of first ['gender_updated']
      ['repetition] = ['member'].value_counts.min() - 1

      merging all groupby to NEW *new_df*

    09
    # droping duplicates of where these match:
      ["member", "condition", "subject_nr", "gender_updated"]

    """



if __name__ == "__main__":
    main()
