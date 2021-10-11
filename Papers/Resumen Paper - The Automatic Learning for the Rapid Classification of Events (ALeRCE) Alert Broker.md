# The Automatic Learning for the Rapid Classification of Events (ALeRCE) Alert Broker

## Abstract

Se introduce el broker ALeRCE, un broker de alertas astronómicas diseñado para proveer una clasificación rápida y consistente de un largo grupo de streams de alerta de telescopios, tales como el que entrega Zwicky Transient Facility (ZTF) y, en el futuro, el observatorio Vera C. Rubin Legacy Survey of Sace and Time (LSST). ALeRCE es un broker chileno, llevado a cabo por un equipo interdisciplinario de astrónomos e ingenieros, trabajando para volverse intermediarios entre las surveys astronómicas y las facilidades de seguimiento. ALeRCE usa una pipeline que incluye la inyección de data en tiempo real, agregación, cross-matching, clasificación ML, y visualización del sistema de alertas ZTF. Se utilizan dos clasificadores: uno basado en stamp, diseñado para la clasificación rápida, y un clasificador basado en curvas de luz, que usa la evolución del flujo multi-banda para lograr una clasificación más refinada. Hasta la fecha del paper, se han procesado más de 9.7 x 10^7 alertas en tiempo real, clasificado más de 1.9 x 10^7 objetos según stamp, y más de 8.5 x 10^5 según clasificación de curva de luz. Esto ha dado paso al reporte de 3088 candidatos a supernova, y diferentes experimentos usando sistemas de alerta similares a lo que será el LSST. Finalmente, se discute el desafío futuro de pasar de un single-stream de alertas como lo es ZTF, a un ecosistema multi-alerta dominado por LSST.

# Introducción

El crecimiento exponencial del área de recolección de luz en telescopios y del número de pixeles de los detectores digitales ha resultado en una nueva generación de telescopios de survey que están revolucionando la forma en la que se estudia el dominio del tiempo en astronomía. Nuevas surveys que escanean sistemáticamente el cielo óptico/casi infrarrojo con observaciones profundas, amplias y de cadencia rápida están descubriendo una gran población de fenómenos astrofísicos variables en el tiempo, incluyendo nuevas poblaciones de *dim, rare, and/or short-lived events.*

Mientras tanto, la construcción del observatorio Vera C. Rubin y su survey Legacy Survey of Space and Time (LSST) está avanzando, y se espera que ocurra una convergencia con surveys en otras regiones del espectro electromagnético y de las ondas gravitacionales. 

La cantidad fundamental que define a un telescopio de survey es el producto de un área espejo y un campo de vista (FOV), conocida como *etendue*, que es un proxy simple para el volumen en el espacio que puede ser monitoreado por diferentes telescopios en un mismo tiempo de exposición y para una luminosidad intrínsica de un objeto dada. En la Figura 1 se muestra el FOV, el área de recolección y el número de pixeles de una selección de telescopios de survey con un gran valor *etendue*.  

![image-20211002214152463](C:\Users\m_jvs\AppData\Roaming\Typora\typora-user-images\image-20211002214152463.png)

Estos telescopios varian desde aquellos con un valor de FOV muy alto o colecciones *all-sky* de pequeños telescopios de apertura, a detectores de mosaicos con grandes aperturas y un alto valor de FOV. Los telescopios con apertura pequeña pueden explorar a cadencias muy rápidas, pero están restringidos en la práctica a objetos brillantes del universo cercanos. Los telescopios de gran apertura pueden explorar objetos más tenues y el universo más distante, pero tienen cadencias más limitadas para las observaciones *all-sky*.

Los detectores en estos grandes *etendue* telescopes producen data a tasas cada vez más rápidas. Millones de eventos, es decir, de objetos para los cuales se observa un cambio en su brillo o posición en el cielo, son detectados y reportados en la forma de alertas astronómicas continuas mediante streams. Esos streams crean la oportunidad para una nueva generación de telescopios de seguimiento de caracterizar grandes números de eventos astronómicos de manera coordinada, guiando finalmente a un mejor entendimiento de la naturaleza del fenómeno variable y consecuentemente a la evolución de nuestro universo local y más distante. 

Un nuevo ecosistema de dominio del tiempo se está construyendo de acuerdo a ello, donde los telescopios se especializan ya sea como survey o como follow-up (seguimiento), pero también donde los nuevos componentes de información digital se desarrollan para ser conectados con estos telescopios sin problemas. La agregación, anotación y clasificación de alertas en una manera rápida y consistente se realiza por **astronomical alert brokers**, como lo son ALeRCE, y otros que no voy a copiar. Frecuentemente, diferentes brokers se especializan en distintos casos de ciencia. Su principal rol es proveer una clasificación rápida y consistente de la alerta usando toda la información disponible, pero también siendo capaz de filtrar un stream para las distintas comunidades. La clasificación rápida de eventos es crítica para el estudio ya sea de fenómenos de corta vida o las fases tempranas de evolución de procesos de larga vida, pues permite que las observaciones de seguimiento ocurran lo suficientemente rápido para que ciertas propiedades físicas puedan ser inferidas. Así mismo, estas clasificaciones contribuyen también a la detección de nuevos fenómenos astrofísicos en la forma de outliers o anomalías, y ayudarán a revelar nuevas sub poblaciones entre familias conocidas de eventos. 

Se necesita un ecosistema interoperable y ágil, con todas las partes relevantes siendo capaces de interactuar automáticamente para llevar a cabo observaciones coordinadas, pero también siendo capaces de adaptarse rápidamente a nuevos casos de estudio, instrumentos, o tecnologías digitales. En este nuevo escenario, los telescopios de seguimiento (follow-up) escucharán y reaccionarán a los Target and Observation Managers (TOMs). Los TOMs, por su parte, escucharán a los streams de alert broker ya clasificados, y los brokers van a escuchar a telescopios de survey de alertas. Cuando una observación de seguimiento se lleve acabo y sus resultados estén disponibles, los TOMs podrán modificar la estrategia de seguimiento, los brokers podrán mejorar su clasificación, y los telescopios de survey podrán cambiar sus estrategias de survey, dando paso a un mecanismo de feedback para el ecosistema completo, que de esta forma será capaz de mejorar continuamente. 

Secciones importantes que no agregaré en esta ocasión:

- 2.1. Transients
- 2.2. Variable Starts
- 2.3. Active Galactic Nuclei

La sección 3.1 aa 3.3 ya están en el resumen del otro paper. Lo que viene después creo que no es tan importante, salvo por las métricas y matrices de confusión.