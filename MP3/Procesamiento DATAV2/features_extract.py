#import FATS
import pandas as pd
import numpy as np
import os.path
import csv
#import matplotlib.pyplot as plt

if not os.path.isfile("present_curves.csv"):
    filtered_alerts = pd.read_csv("joined_chunks.csv")
    print("Creando present_curves.csv")
    f = open("present_curves.csv", 'w')
    present_curves = []
    for index, row in filtered_alerts.iterrows():
        if row['oid'] not in present_curves:
            present_curves.append(row['oid'])
            f.write(row['oid'] + '\n')

if not os.path.isfile("alerts_G.csv") and not os.path.isfile("alerts_R.csv"):
    filtered_alerts = pd.read_csv("joined_chunks.csv")
    present_curves = pd.read_csv("present_curves.csv")
    print("Creando alerts_G.csv y alerts_R.csv")
    fG = open("alerts_G.csv", 'w', newline='')
    fR = open("alerts_R.csv", 'w', newline='')
    writerG = csv.writer(fG, delimiter=',')
    writerR = csv.writer(fR, delimiter=',')
    header = ['oid', 'magpsf_corr', 'mjd', 'sigmapsf_corr', 'sigmapsf_corr_ext']
    writerG.writerow(header)
    writerR.writerow(header)
    for index, row in filtered_alerts.iterrows():
        current_fid = row['fid']
        trow = [row['oid'], row['magpsf_corr'], row['mjd'], row['sigmapsf_corr'],
                row['sigmapsf_corr_ext']]
        if current_fid == 1:
            writerG.writerow(trow)
        elif current_fid == 2:
            writerR.writerow(trow)
        else:
            writerG.writerow(trow)
            writerR.writerow(trow)
