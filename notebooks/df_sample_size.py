import  pandas as pd
import pickle

df = pickle.load(open('../data/pickles/df_full.pickle', 'rb'))

def df_trimmer(df):

    df_large_features = [feature  for feature in list(df)
                         if df[feature].sum() > 50]
    return df_large_features
