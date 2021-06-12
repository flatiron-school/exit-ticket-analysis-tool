import pandas as pd
import numpy as np
import glob
import os


def load_csvs():
    path = 'data'
    all_files = glob.glob(os.path.join(path, "*.csv"))

    df_from_each_file = (pd.read_csv(f) for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
    return concatenated_df


def get_student_names(data, column_name='name'):
    # Get IDs, and references to IDs
    names = data[column_name].unique()
    return np.sort(names)
    

def get_cohorts():
    # TODO: Load for DB
    return ['Washington D.C.', 'San Francisco']

def get_phases():
    # Could pull from DB
    return ['Phase {}'.format(i) for i in range(1,6)]