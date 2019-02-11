import pandas as pd
import pickle

df = pickle.load(open('../../data/pickles/df_full.pickle', 'rb'))

df_count = df.sum()
df_count.to_csv('recid_count.csv')
