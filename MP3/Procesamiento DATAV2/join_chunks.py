import glob
import pandas as pd

all_files = glob.glob("filtered_chunks/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=[0])
    li.append(df)

frame = pd.concat(li)

print(frame)

frame.to_csv('joined_chunks.csv')
