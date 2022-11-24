# Proyecto Grupal -  Sistema de alerta de sismos
## Sección Data Engineering
![image](https://user-images.githubusercontent.com/108296379/182138583-9011699a-f009-4454-885e-80dca182b6c8.png)


##  Propuesta de la sección
Bienvenidx a la sección de ETL

## Herramientas utilizadas:

 - Python y sus librerías, cómo Pandas, Numpy y SQLalchemy
 - Maquina virtual a tráves de AWS 
 - Gestor SQL: Postgress 
 - Host base de datos: e AWS (S3)


## Flujo de trabajo

En la siguiente imagen se pueden ver el flujo completo de los datos a tráves del pipeline y las herramientas útilizadas en cada uno.

![image](https://i.ibb.co/4F2F0tC/Diagrama-Pipeline.png)

### Pasos de forma detallada

#### Extración (E)

La extración se realizan con consultas a diversas APIs para poder hacer un análisis de terremotos, teniendo en cuenta distintos factores. 

La API de donde se extrae la mayor cantidad de información es [USGS](https://earthquake.usgs.gov/fdsnws/event/1/)
Se realiza una extración inicial con datos desde el 2010 al presente.
Luego se hacen consultas cada una hora para agregar dicha información a la nuestra base de datos.

Además se utilizan 3 dataset adicionales para comparar fénomenos naturales cómo vólcanes, tsunamies y terremotos significantes, para encontrar si hay alguna relación entre ellos. 

Fuente: [National Centers for Environmental Information](https://https://www.ngdc.noaa.gov/ngdc.html)

Por último se extraen datos del clima para entender sí esto tiene alguna implicancia en los movimientos sísmicos.
Todas estas tablas se guardan como TSV para fácil lectura

Fuente: [Free Weather API](https://open-meteo.com/en)

#### Tránsfomación (T)

Para la tablas adicionales de volcanes y tsunami utuliza una limpieza similar, ya que los datos, al proveenir de la misma fuente, tienen un formato casi igual. Los notebooks de transformación se encuentran el la carpeta de 'additional dataset'




#### Carga (Load - L)

Una vez tenemos los datos limpios, podemos disponibilizarlos para su consumo. Utlizaremos MySQL para almacenar los datos y haremos la conexión a tráves de SQLalquemy, una librería de Python.
Primero, se crearan las tablas con sus tipos de datos acordes. 
Se cargan los datos transformados y guardados en el dataframe directo a la base de datos, utilizando una conexión con SQLalquemy. 
Una vez cargados todos los datos en sus tablas, se pueden hacer algunas queries para asegurarse que todo se encuentra funcionando bien. 

    
## Objetivos alcanzados
- Procesar datos extraídos de diferentes aPIs
- Diseño ER que mejor se ajusta al proyecto
- Pipeline para alimentar el Data Warehouse en la nube. Todo corriendo de forma automatizada
- Automatización
- Validar datos antes de la carga a la base de datos
- Documentación que se adjunta:
    - Diagrama ER detallado (tablas PK, FK y tipos de datos)
    - Diccionario de datos
    - Workflow detallando el ciclo del dato



