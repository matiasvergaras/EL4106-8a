from csv import reader
import pandas as pd

# First we test that the number of entries in the sum of chunks is equal to the one of joined_chunks
df = pd.read_csv("filtered_chunks/chunk_10000000.csv")
n_rows = len(df)
for i in range(20000000, 130000000, 10000000):
    df_i = pd.read_csv("filtered_chunks/chunk_" + str(i) + ".csv")
    n_rows += len(df_i)

df = pd.read_csv("joined_chunks.csv")
print(len(df))
print(n_rows)

# values should meet len(df) =  n_rows
assert (len(df) == n_rows)

# now we test that every entry in joined_chunks corresponds to an object classified as periodic by ALeRCE
oid_periodics = []
periodic_classes = ["LPV", "Periodic-Other", "RRL", "CEP", "E", "DSCT"]

with open('labels_set.csv', 'r') as labels:
    csv_reader = reader(labels)
    for row in csv_reader:
        if row[1] in periodic_classes:
            oid_periodics.append(row[0])

filtered_joined = open('joined_chunks.csv', 'r')

with open('joined_chunks.csv', 'r') as filtered_joined:
    csv_reader = reader(filtered_joined)
    for row in csv_reader:
        try:
            assert (row[1] in oid_periodics)
        except:
            print(row)
