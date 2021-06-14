import pandas as pd
import numpy as np
import glob
import os

# Add extra information into Exit Ticket Response
def add_info_to_df(df, cohort=None, phase=None, lecture=None):
    df['cohort'] = cohort
    df['phase'] = phase
    df['lecture'] = lecture
    return df

def clean_column_names(df):
    # Remove prefix from Exit Ticket column names
    df = df.rename(lambda x: str(x).split(': ')[-1], axis=1)
    # Have to rename duplicate Exit Ticket column names
    df.columns = [
        f'{col_name}_other' if flag
        else col_name 
            for col_name,flag in zip(df.columns,df.columns.duplicated())
    ]
    # Remove the "Attempt" columns (start with '1')
    df = df[[c for c in df.columns if c[0] != '1']]

    return df

# Find CSVs by nested directories
def load_csvs():
    path = 'data'
    # Form of 'data/COHORT/Phase#/*csv'
    all_files = cohorts = glob.glob(os.path.join(path, '*', 'Phase*/', '*.csv'))
    
    df_from_each_file = (
        add_info_to_df(
            clean_column_names(pd.read_csv(f)),
            # Use path to get extra info
            cohort=f.split('/')[1],
            phase=f.split('/')[2],
            lecture=f.split('/')[3].split('Exit Ticket')[0] # Keep only lecture info
        ) 
        for f in all_files
    )

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