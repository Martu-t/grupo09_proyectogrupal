# Proyecto Grupal -  Sistema de alerta de sismos
## Sección Data Engineering
<img src="https://inesdi-cdn.s3.eu-west-3.amazonaws.com/inesdi-prod/2021-08/iStock-1329530347.jpg" width=50% height=30%>

##  Propuesta de la sección
Bienvenido/a la sección de ETL. Aquí te explicaremos el flujo de los datos y el código utilizado para llevar a cabo nuestro proceso de extracción, transformación y carga a una base de datos en la nube. Todo de manera automatizada con python.

## Herramientas utilizadas:

 - Python y sus librerías, cómo Pandas, Numpy y SQLalchemy
 - Maquina virtual a tráves de AWS (EC2)
 - Gestor de base de datos: PostgreSQL
 - Servicio de Bases de Datos Relacionales en AWS (RDS)

 ## Flujo de trabajo

En la siguiente imagen se pueden ver el flujo completo de los datos a tráves del pipeline y las herramientas útilizadas en cada instancia.

[![flujo-pipeline.jpg](https://i.postimg.cc/FKDyShXP/flujo-pipeline.jpg)](https://postimg.cc/cKttyyHY)

## Estructura del Pipeline

Para poder entender mejor el flujo del datos, se identifican distintos momentos que conforman la totalidad del ETL:

1. Carga inicial/preeliminar: Se realiza una extración, transformación y carga de las tablas, del contenido obtenido de distintas APIs. 
2. Carga incremental: Utilizando cómo base las tablas creadas, se hace una nueva extracción e incorporación de datos. Para que los datos sean precisos, tanto en la nueva extracción, cómo en la carga, se compara la última fecha de nuestra base de datos. El código de transformación se re-utiliza.
3. Carga addicional: A partir de un módelo de Machine Learning, explicado en la carpeta "ML", se genera una clasificación inicial. Se descartarán todos los del cluster 0. 
Estos datos son cruzados con la tabla final de clasificación hecha de forma análitica, y se produce la tabla final de clasificaciones específica para Twitter.

Además cabe resaltar que antes de las transformaciones, se hace un análisis exploratorio de datos (EDA). En el caso del dataset principal, dicho análisis se encuentra en un notebook llamado EDA.ipynb, mientras que para los datasets adiccionales se realiza en el mismo notebook de transformación.

Con estos conceptos más claros, pasamos a explicar cada paso

### **Extración** (E)

En la etapa de extración se realizan consultas a diversas APIs, como así también se incluye un archivo de excel llamado "poblacion_chile_xlxs".

**Dataset principal:**

La API de donde se extraen los datos para la tabla principal es [USGS](https://earthquake.usgs.gov/fdsnws/event/1/)
Se realiza una extración inicial con datos desde el 2010 al presente.
Luego se hacen consultas cada 15 minutos para agregar dicha información a la nuestra base de datos.

**Dataset adicionales**

Además se utilizan:
- 3 dataset adicionales para comparar fénomenos naturales cómo vólcanes, tsunamies y terremotos significantes, para encontrar si hay alguna relación entre ellos. 

Fuente: [National Centers for Environmental Information](https://https://www.ngdc.noaa.gov/ngdc.html)

- Datos del clima para entender sí esto tiene alguna implicancia en los movimientos sísmicos. Esta información se cruza con el dataset de "terremotos relevantes"

Fuente: [Free Weather API](https://open-meteo.com/en)

- Datos de la población chilena, que incluye las 345 comunas, con sus respectivas superficies y cantidad de habitates.

Fuente: [Tabla poblacional](https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile)

### **Tránsfomación (T)**

**Dataset principal:**

Los datos extraídos de la API de USGS, tanto de manera inicial, cómo incremental, pasan por el mismo proceso de transformación que se puede ver en el script de transform2.py.

***Transformaciones destacables:***

* Cambiar la fecha de formato unix a formato datetime.
* Tratamiento específico de datos faltantes y outliers (para esto fue necesario una investigación sobre máximos y mínimos de magnitud, profundidad y medición de estaciones sísmicas)
* Separar los datos de latitud, longitud y profundidad en distintas columnas
* Agrupar "tipos de eventos" para limitar las categorías.

**Dataset adicionales**

Para la tablas adicionales de volcanes y tsunamis ya que los datos, al provienen de la misma fuente, comparten similitudes en sus transformaciones. Los notebooks de transformación se encuentran el la carpeta de 'additional dataset' junto con los datos descargados. Se destaca la eliminación de columnas redundantes, imputación de fechas y valores faltantes. También se garantiza que el tipo de dato sea acorde al valor (por ejemplo fecha de tipo date)

Por otro lado también descargamos los datos de terremotos más significativos. Utilizando la fecha cómo columna en cómun, se cruzan dichos datos con los obtenidos con la API del clima y se crea un nuevo dataset llamado "earquakes_weather".

Una vez unificados los datos, se pasa a la transformación, en donde se eliminan columnas, se imputan algunos datos faltantes y también se chequea que los tipos de datos estén bien.

### **Carga (Load - L)**

Se realiza una carga inicial de todas las tablas ya limpias y con sus datos validados.

Para poder hacerlo, se crea un montor (engine) desde python para establecer la conexión a la base de datos a tráves de la librería SQLAlchemy.

Es importante aclarar que, cómo fue mencionando anteriormente, también hay una carga con la clasificación de los terremotos y la fecha en la información fue tweeteada. 

### **Automatización**

Desde el inicio del ciclo (consulta a la API), hasta las cargas secuenciales a la base de datos en la nube, se ha logrado automatizar el proceso. 

Para hacerlo, decidimos utilizar una máquina virtual a tráves de AWS (EC2), para asegurarnos que se encuentre siempre funcionando y haya muy pocas posibilidades de caída de servicio. Igualmente es importante aclarar que, los scripts utilizan una consulta a la base de datos para obtener los ültimos registros y a partir de eso pedir la información a las APIs. Por este motivo en caso de falla, la actualización sólo se irá acumulando, pero no producirá errores o cargas duplicadas.

Dentro de la máquina virtual, contamos con un orquestador que corre en secuencia todos los scripts de cargas incrementales/adicionales cada 15 mínutos.

El proceso completo se compone de 6 script de python que se mantienen en ejecución:

1. ***extract2.py***
 Hace una consulta a la base de datos para obtener la fecha (con horas y minutos) del útilmo registro. Ese dato se utiliza como "Start Date" en el pedido a la API, para que traiga sölo los registros desde esa fecha, al momento presente. 
 Los datos obtenidos se almacenan en un dataframe para pasar al siguiente script

2.  ***transform2.py***
Toma los datos del script anterior y aplica distintas funciones para transformar el dato (eliminar columna, imputar faltantes, cambiar outliers y convertir el tipo de dato, en caso de ser necesario).
Como resultado, se crea un dataframe "limpio" y un archivo .CSV para que quede el registro.

3. ***deploy_model.py***
Toma el archivo .CSV del paso anterior y lo pasa por nuestro módelo de Machine Learning, para su clasificación en el cluster correspondiente. Estos datos se guardan para los siguientes pasos

4. ***twitter_selector.py***
Con los datos pre-clasificados del módelo anterior, se hace un cruce entre los mismos y nuestra matríz de clasificación (explicada en la carpeta de "Data Analytics"). Esto produce una tabla con la clasificación final para ser envíada a Twitter.

5. ***load2.py***
Este script realiza la carga incremental de las 3 tablas, de forma autómatica a tráves de SQLalchemy. Cabe aclarar que las validaciones para evitar repeticiones se realizan en cada script de los pasos anteriores.

6.  ***orqustrator.py***
Usamos estre script cómo orquestador, donde se cargan los demás y se ejecutan cada 15 minutos. En caso de haber una falla se volverá a ejecutar.

A continuación mostramos un ejemplo del script completo corriendo:

<img src="https://iili.io/HCvqNun.png" width=75% height=75%>


## Objetivos alcanzados
- Procesar datos extraídos de diferentes APIs
- Diseño ER que mejor se ajusta al proyecto
- Pipeline para alimentar el Data Warehouse en la nube. Todo corriendo de forma automatizada
- Automatización
- Validar datos antes de la carga a la base de datos

