# EL4106-8a
Clustering y visualización de curvas de luz de estrellas periódicas


Link al drive con los datos:
https://drive.google.com/drive/folders/1CKlSU8ZU5yAGG5LgeorxjPdAt0HztVvS?usp=sharing

El drive se encuentra estructurado en carpetas. Cada carpeta contiene un estado de los datos:
- DATA_ORIGINAL: el resultado de procesar los datos como nos fueron entregados la primera vez, con las siguientes columnas:
-- **oid**: object id
-- **candid**: candidate id
-- **dec:** declination
-- **ra:** right ascension
-- **sigmapsf_corr**:  estandar deviation from PSF-fit photometry
-- **magpsf_corr**: magnitude from PSF-fit photometry
-- **fid**: fid=1 (g filter) or fid=2 (R filter)
-- **mjd**: Modified Julian date

- DATA_V2: lo mismo, pero para los datos entregados en segunda instancia: corrección de los primeros agregando la columna **sigmapsf_corr_ext**. En este caso se incluye también el archivo `lc_features.csv`, que corresponde al resultado de calcular características sobre cada objeto en el dataset (con estos datos si se logró). También se incluye un resumen de los datos generado mediante _pandas profiler_ en el archivo `profile_lc_features.html`. 
- DATA_AUGMENTATION: observaciones sintéticas generadas para los objetos de tipo CEP, DSCT y PeriodicOther, en base a DATA_V2. Se incluye un archivo `lc_features_augmented.csv` que reune las curvas de luz de DATA_V2 con aquellas sintéticas, incorporando además una columna "target": el valor de `classALeRCE` asociado a cada objeto en el archivo `labels.csv`. 
