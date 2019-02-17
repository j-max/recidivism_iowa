import pandas as pd
import pickle

df = pd.read_csv("csv_fromAWSupload.csv")

####Drop features without data and features populated after recidivism####
df.drop(columns = ['Unnamed: 0',
                   'sex',
                   'recidivism_type',
                   'days_to_recidivism',
                   'new_conviction_class',
                   'new_conviction_type',
                   'new_conviction_subtype',
                   'sort_number', #zero non-null entries in original csv
                   'initial_supervision_status',  #zero non-null entries in original csv
                   'recidivism_supervision_status'], inplace=True)


df['supervising_district'].fillna('None-Discharged', inplace=True)    


####TRANSFORM ROWS TO BINARIES####
def recid_to_binary(row):
    if row['recidivism'] == 'Yes':
        return 1
    else:
        return 0
    
df['recid_flag'] = df.apply(lambda row: recid_to_binary(row), axis=1)
df.drop('recidivism', axis=1, inplace=True)


def target_pop_to_binary(row):
    if row['target_poulation'] == 'Yes':
        return 1
    else:
        return 0
    
df['target_pop_flag'] = df.apply(lambda row: target_pop_to_binary(row), axis=1)
df.drop('target_poulation', axis=1, inplace=True)

#####DROP RECORDS WITH RARE ETHNICITY LABELS: COUNT < 100####

mask = ((df['race'] == 'White - Non-Hispanic') | (df['race'] == 'Black - Non-Hispanic')|
         (df['race'] == 'American Indian or Alaska Native - Non-Hispanic') | (df['race'] == 'White - Hispanic')|
          (df['race'] == 'Asian or Pacific Islander - Non-Hispanic' ))
df = df[mask]

#There are under 1800 na's in release type, which are dropped to have values in every cell.
df = df.dropna()

###Make dummies out of all columns####
X = df.drop(columns = ['recid_flag', 'target_pop_flag'])

for feature in list(X):
    df = pd.concat((df, pd.get_dummies(df[feature],prefix=feature)), axis=1)
    df.drop(feature, axis =1, inplace=True)

with open('pickles/df_full.pickle', 'wb') as write_file:
    pickle.dump(df, write_file)
