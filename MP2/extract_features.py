import pandas as pd
import FATS

df = pd.read_csv("filtered_alerts.csv")
df.drop('Unnamed: 0', inplace=True, axis=1)
df = df.rename(columns=({'magpsf_corr': 'magnitude', 'sigmapsf_corr': 'error'}))#, 'mjd': 'time'}))
print(df)
df.to_csv("renamed_alerts.csv", header=True, index=False)
