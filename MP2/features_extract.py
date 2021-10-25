import FATS
import pandas as pd
import numpy as np
import os.path
import csv
import matplotlib.pyplot as plt

#Primero creamos el archivo con las curvas presentes en las alertas filtradas
if not os.path.isfile("present_curves.csv"):
    filtered_alerts = pd.read_csv("filtered_alerts.csv")
    print("Creando present_curves.csv")
    f = open("present_curves.csv", 'w')
    present_curves = []
    for index, row in filtered_alerts.iterrows():
        if row['oid'] not in present_curves:
            present_curves.append(row['oid'])
            f.write(row['oid'] + '\n')

# para cada entrada en filtered_alerts, la agregamos a alerts_G o alerts_R según su fid.
# Esto es principalmente para cumpir con el formato necesario para FATS.
if not os.path.isfile("alerts_G.csv") and not os.path.isfile("alerts_R.csv"):
    filtered_alerts = pd.read_csv("filtered_alerts.csv")
    print("Creando alerts_G.csv y alerts_R.csv")
    present_curves = pd.read_csv("present_curves.csv")
    fG = open("alerts_G.csv", 'w')
    fR = open("alerts_R.csv", 'w')
    fG.write("oid,magnitude,time,error\n")
    fR.write("oid,magnitude,time,error\n")
    writerG = csv.writer(fG, delimiter=',')
    writerR = csv.writer(fR, delimiter=',')
    for index, row in filtered_alerts.iterrows():
        current_fid = row['fid']
        trow = [row['oid'], row['magpsf_corr'], row['mjd'], row['sigmapsf_corr']]
        if current_fid == 1:
            writerG.writerow(trow)
        elif current_fid == 2:
            writerR.writerow(trow)
        else:
            writerG.writerow(trow)
            writerR.writerow(trow)

# De aqui en adelante intentabamos calcular features con FATS, pero no lo logramos.
# Los csv generados anteriormente fueron útiles para pasarselos al notebook con TURBO-FATS.
exit(0)

# ------------ UNREACHABLE CODE ------------
if not os.path.isfile("featured_alerts.csv"):
    print("Creando featured_alerts.csv")
    fG = pd.read_csv("alerts_G.csv", index_col = 'oid')
    fR = pd.read_csv("alerts_R.csv", index_col = 'oid')
    fG = fG.sort_values(["oid", "time"])
    fR = fR.sort_values(["oid", "time"])
    present_curves = pd.read_csv("present_curves.csv", names=['oid'])
    for index, row in present_curves.iterrows():
        [mag, time, error] = [[], [], []]
        [mag2, time2, error2] = [[], [], []]
        current_curve = row['oid']
        try:
            lc_G = fG.loc[row['oid']]
        except:
            lc_G = None
        try:
            lc_R = fR.loc[row['oid']]
        except:
            lc_R = None
        if lc_G is not None and lc_R is not None:
            print("Case 1 for {}".format(current_curve))
            #calcular con ambas bandas
            mag, time, error = lc_G.loc[:, "magnitude"].values, \
                                  lc_G.loc[:, "time"].values, \
                                  lc_G.loc[:, "error"].values
            mag2, time2, error2 = lc_R.loc[:, "magnitude"].values, \
                                  lc_R.loc[:, "time"].values, \
                                  lc_R.loc[:, "error"].values

            #Color = [1, 0.498039, 0.313725];
            #p = plt.plot(time, mag, '*-', color=Color, alpha=0.6)
            #plt.xlabel("Time")
            #plt.ylabel("Magnitude")
            #plt.gca().invert_yaxis()
            #plt.waitforbuttonpress()

            # Preprocesar la data (quitar outliers)
            preproccesed_data = FATS.Preprocess_LC(mag, time, error)
            [mag, time, error] = preproccesed_data.Preprocess()

            preproccesed_data = FATS.Preprocess_LC(mag2, time2, error2)
            [mag2, time2, error2] = preproccesed_data.Preprocess()

            lc = np.array(
                [mag, time, error])
            a = FATS.FeatureSpace(Data=['magnitude', 'time', 'error'],
                                  featureList=['Mean','Beyond1Std','CAR_sigma','Color','SlottedA_length'])

            # Sincronizar ambas bandas
            if len(mag) != len(mag2):
                 [aligned_mag, aligned_mag2, aligned_time, aligned_error, aligned_error2] = \
                   FATS.Align_LC(time, time2, mag, mag2, error, error2)
                 lc = np.array([mag, time, error, mag2, aligned_mag, aligned_mag2, aligned_time, aligned_error, aligned_error2])
                 a = FATS.FeatureSpace(Data='all',
                                       excludeList=['SlottedA_length', 'StetsonK_AC', 'PeriodLS'])

        elif lc_G is not None and lc_R is None:
            print("Case 2 for {}".format(current_curve))
            #calcular para una sola banda
            mag, time, error = lc_G.loc[:, "magnitude"].values, \
                                  lc_G.loc[:, "time"].values, \
                                  lc_G.loc[:, "error"].values
            lc = np.array([mag, time, error])
            a = FATS.FeatureSpace(Data=['magnitude', 'time', 'error'],
                                  featureList=['Mean','Beyond1Std','CAR_sigma','Color','SlottedA_length'])

        elif lc_G is None and lc_R is not None:
            print("Case 3 for {}".format(current_curve))
            #calcular para una sola banda
            mag2, time2, error2 = lc_R.loc[:, "magnitude"].values, \
                                  lc_R.loc[:, "time"].values, \
                                  lc_R.loc[:, "error"].values
            lc = np.array([mag2, time2, error2])
            a = FATS.FeatureSpace(Data=['magnitude', 'time', 'error'],
                                  featureList=['Mean','Beyond1Std','CAR_sigma','Color','SlottedA_length'])

        a = a.calculateFeature(lc)
        print(a.result(method='dict'))
