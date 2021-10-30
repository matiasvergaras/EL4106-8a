# EL4106-8a
# Clustering y visualización de curvas de luz de estrellas periódicas
Link al drive con los datos:
https://drive.google.com/drive/folders/1CKlSU8ZU5yAGG5LgeorxjPdAt0HztVvS?usp=sharing

## Estructura del repositorio 
Cada carpeta tiene el avance relativo a un Meeting Project del curso. La carpeta Papers, por su parte, incluye los papers de referencia del proyecto. En la raíz se incluye el informe preliminar, el dataset de labels (transversal a todos los MP) y el html con el análisis exploratorio de los datos, incluyendo la data sintética (profile_data_augmented). 

El preprocesamiento de datos se realiza principalmente mediante scripts destinados a correr localmente, pues requieren de tiempos de computación excesivos (sobre 40 horas). Por otro lado, la aplicación de modelos se lleva a cabo mediante Notebooks de Python, los cuales se encuentran disponibles a partir de la carpeta MP3 (UMAP.ipynb, Autoencoders.ipynb). 

Cada notebook incluye instrucciones para descargar los datos necesarios desde una carpeta Drive donde están accesibles mediante `gdown`, por lo cual deberían ser reproducibles por cualquier usuario. En caso de presentar dificultades, contactar a matiasvergara@ug.uchile.cl.

## Estructura del Drive
El drive se encuentra estructurado en carpetas. Cada carpeta contiene un estado de los datos:

**DATA_ORIGINAL:** el resultado de procesar los datos como nos fueron entregados la primera vez, con las siguientes columnas:

- **oid**: object id
- **candid**: candidate id
- **dec:** declination
- **ra:** right ascension
- **sigmapsf_corr**:  estandar deviation from PSF-fit photometry
- **magpsf_corr**: magnitude from PSF-fit photometry
- **fid**: fid=1 (g filter) or fid=2 (R filter)
- **mjd**: Modified Julian date

**DATA_V2:** lo mismo, pero para los datos entregados en segunda instancia: corrección de los primeros agregando la columna **sigmapsf_corr_ext**. En este caso se incluye también el archivo `lc_features.csv`, que corresponde al resultado de calcular características sobre cada objeto en el dataset (con estos datos si se logró). También se incluye un resumen de los datos generado mediante _pandas profiler_ en el archivo `profile_lc_features.html`. 

**DATA_AUGMENTATION:** observaciones sintéticas generadas para los objetos de tipo CEP, DSCT y PeriodicOther, en base a DATA_V2. Se incluye un archivo `lc_features_augmented.csv` que reune las curvas de luz de DATA_V2 con aquellas sintéticas, incorporando además una columna "target": el valor de `classALeRCE` asociado a cada objeto en el archivo `labels.csv`. 

## ¿Cómo explorar el trabajo realizado?
La respuesta es algo compleja. Dado que inicialmente hubieron muchas dificultades para obtener features desde los datos (inicialmente se indicó usar una librería deprecada y se cambiaron los datos 3 veces), entender el camino que se ha seguido es un tanto complejo. Se recomienda tomar el siguiente enfoque:
- En la carpeta MP1, se encuentra la Carta Gantt inicial del proyecto. Debido a las dificultades, esta no pudo ser respetada.
- En la carpeta MP2, se encuentran los primeros intentos de extracción de features, con la librería FATS deprecada. Tampoco hubo éxito.
- A partir de la carpeta MP3, se trabaja con los datos nuevos (V2) y comienza el verdadero avance del proyecto. El orden en el que se fue trabajando los scripts ahí presentes fue el siguiente:
    - `filter_periodics.py`, script que filtra las observaciones a solo aquellas que están asociadas a un objeto periodico en `labels_set.csv`, mediante chunks.
    - `join_chunks.py`, que se encarga de reunir los chunks de data filtrada del script anterior en un solo gran archivo.
    - `features_extract.py`, que separa el resultado del script anterior en dos archivos: uno para cada banda. Este formato se adaptó porque era el que la librería original requería para funcionar, mas resultó ser un paso innecesario para la librería final. 
    - `features_turbofats_data2_succeed_local.ipynb`, notebook de Python que ejemplifica como se realizó la extracción final de features, la cual resultó exitosa. Cabe mencionar que, si bien el notebook es una representación fiel de lo que se realizó, el éxito se obtuvo trabajando en local, pues el procesamiento tomó más de 40 horas (lo cual excede el tiempo permitido por Colab, entorno en el cual se estaba trabajando).
    - `data_augmentation.ipynb`, notebook en el cual se realizo una aumentación de datos de alrededor del 3% para doblar el número de objetos de las clases menos representadas: CEP, DSCT y Periodic-Other. 
    -  `UMAP.ipynb`, notebook en donde se realiza la reducción de dimensionalidad mediante UMAP y se generan las primeras visualizaciones de clusters de curvas de luz. 
