from csv import reader
import pandas as pd

oid_periodics = []
periodic_classes = ["LPV", "Periodic-Other", "RRL", "CEP", "E", "DSCT"]

with open('labels_set.csv', 'r') as labels:
    csv_reader = reader(labels)
    for row in csv_reader:
        if row[1] in periodic_classes:
            oid_periodics.append(row[0])

filtered = open('alert_periodics.csv', 'w')
detections = open('alert_detections.csv', 'r')
row_counter = 0
chunksize = 10000000
for chunk in pd.read_csv('alert_detections.csv', chunksize=chunksize): #index_col=[0]): para remover columna n_index
    indexNames = chunk[~chunk['oid'].isin(oid_periodics)].index
    chunk.drop(indexNames, inplace=True)
    chunk.to_csv("filtered_chunks_B/chunk_"+str(row_counter+chunksize)+".csv", header=True, index=False)
    row_counter+=chunksize
    print(row_counter)
