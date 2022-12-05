# Proyecto Grupal -  Sistema de alerta de sismos
## Sección Data Engineering
![image](https://inesdi-cdn.s3.eu-west-3.amazonaws.com/inesdi-prod/2021-08/iStock-1329530347.jpg)


##  Propuesta de la sección
Bienvenido/a a la sección de ETL. Aquí podrás encontrar todo el código utilizado para llevar a cabo un proceso de extracción, transformación y carga a una base de datos en la nube. Todo de manera automatizada con python.

## Herramientas utilizadas:

 - Python y sus librerías, como Pandas, Numpy y SQLalchemy
 - Maquina virtual a través de AWS 
 - Gestor SQL: Postgress 
 - Host base de datos: en AWS (S3)

## Pasos de forma detallada del ETL

### Extración (E)

En la etapa de extración se realizan consultas a diversas APIs. Así podremos tener información suficiente para un posterior análisis de terremotos, teniendo en cuenta distintos factores. 

La API de donde se extrae la mayor cantidad de datos es [USGS](https://earthquake.usgs.gov/fdsnws/event/1/).
Se realiza una extración inicial con datos desde el 2010 al presente.
Luego se hacen consultas cada una hora para agregar dicha información a nuestra base de datos.

Además se utilizan 3 datasets adicionales para comparar fenómenos naturales como volcanes, tsunamis y terremotos significativos, para encontrar si hay alguna relación entre ellos. 

Fuente: [National Centers for Environmental Information](https://https://www.ngdc.noaa.gov/ngdc.html)

Por último, se extraen datos del clima para entender si ésto tiene alguna implicancia en los movimientos sísmicos.
Todas estas tablas se guardan como TSV para fácil lectura.

Fuente: [Free Weather API](https://open-meteo.com/en)

### Tránsfomación (T)

Para las tablas adicionales de volcanes y tsunamis se utiliza una limpieza similar, ya que los datos al provenir de la misma fuente, tienen un formato casi igual. Los notebooks de transformación se encuentran en la carpeta de 'additional dataset' junto con los datos descargados. Se destaca la eliminación de columnas redundantes, imputación de fechas y valores faltantes. También se garantiza que el tipo de dato sea acorde al valor (por ejemplo fecha de tipo date).

Por otro lado también descargamos los datos de terremotos más significativos. A partir de la fecha, se cruzan dichos datos con los obtenidos con la API del clima y se crea un nuevo dataset llamado eartquakes_weather.

Una vez unificados los datos, se pasa a la transformación, en donde se eliminan columnas, se imputan algunos datos faltantes y también se chequea que los tipos de datos estén bien.

Por último contamos con un dataset principal, donde se encuentran todos los terremotos ocurridos desde el 2010 y algunas de sus features importantes incluyen la magnitud y las coordenadas. 

Este dataset pasa por un proceso de limpieza "standard" que se reutiliza para todos los nuevos datos que vayan ingresando. 

### Carga (Load - L)

Se realiza una carga inicial de todas las tablas ya limpias y con sus datos validados.
Para poder hacerlo, se crea un motor desde python para poder realizar la conexión a la base de datos a tráves de la librería SQLAlchemy.

Luego, en un archivo separado, se procede a la carga incremental. 


### Automatización

Desde el inicio del ciclo (consulta a la API), hasta la carga a la base de datos en la nube, se ha logrado automatizar el proceso. 

Para hacerlo, decidimos utilizar una máquina virtual a tráves de AWS, para asegurarnos que se encuentre siempre funcionando y haya muy pocas posibilidades de caída de servicio. 

El proceso completo se compone de 4 script de python que se mantienen en ejecución:

1. *** Extract.py ***
 Hace una consulta a la base de datos para obtener la fecha (con horas y minutos) del útilmo registro. Ese dato se utiliza como "Start Date" en el pedido a la API, para que traiga solo los registros desde esa fecha, al momento presente. 
 Los datos obtenidos se almacenan en un dataframe para pasar al siguiente script.

2.  *** Transform.py ***
Toma los datos del script anterior y aplica distintas funciones para transformar el dato (eliminar columna, imputar faltantes, cambiar outliers y convertir el tipo de dato, en caso de ser necesario).
Como resultado, se crea un dataframe "limpio" y un archivo .CSV para que quede el registro.

3.  *** Load.py ***
Primero trae de la base de datos los últimos registros para asegurarse que no haya repeticiones, luego realiza la carga de forma autómatica a tráves de SQLalchemy.

4.  *** script.py ***
Usamos este script como orquestador, donde se cargan los demás y se ejecutan cada hora. En caso de haber una falla se volverá a ejecutar en una hora. 

## Flujo de trabajo

En la siguiente imagen, se puede ver el flujo completo de los datos a tráves del pipeline y las herramientas utilizadas en cada instancia.

[![flujo-pipeline.jpg](https://i.postimg.cc/FKDyShXP/flujo-pipeline.jpg)](https://postimg.cc/cKttyyHY)


## Objetivos alcanzados
- Procesar datos extraídos de diferentes aPIs.
- Diseño ER (Entidad-Relación), que mejor se ajusta al proyecto.
- Pipeline para alimentar el Data Warehouse en la nube. Todo corriendo de forma automatizada.
- Automatización.
- Validar datos antes de la carga a la base de datos.
- Documentación que se encuentra en esta carpeta:
    - Notebooks y scripts de extracción, transformacion y carga.
    - Diseño del diagrama Entidad-Relación.
    - Diccionario de datos para cada tabla utilizada.
    - Workflow detallando el ciclo del dato (adjunto en este Readme).



