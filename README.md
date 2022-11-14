![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# **PROYECTO GRUPAL **

- - -

# <h1 align="center">**`SISTEMA DE ALERTAS SISMICAS`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/198112414-ebe5a60f-6bbf-4f94-9924-20da4d702bb5.png"  height=700> 
</p>


## **Contexto**

Los desastres naturales pueden resultar en un gran número de muertes, pérdida de propiedades, y daños irreparables. Es por esto que la predicción temprana y medidas de protección y atención apropiadas resultan urgentes.

Particularmente, los sismos, son el fenómeno natural del cual tenemos menor capacidad predictiva 


## **Propuesta de trabajo**

Para este proyecto, nuestro equipo de atención de desastres del [país latinoamericano a definir]. En este momento se encuentran trabajando en un proyecto tri-nacional en conjunto con el Estados unidos (USGS) y Japón (JMA) llamado “Working towards global standardization of seismological networks and effective communication to the civilian community.” 

Los objetivos de esta alianza son:

<h4>1. Crear una  base de datos depurada que contemple los datos de las tres naciones de forma estandarizada:</h4>

A las autoridades les interesa tener la información estándar de todos los países para poder crear un mecanismo de clasificación. La definición de un evento sísmico y los criterios de alerta adecuados deben tener en cuenta la calidad de los datos.

<sub>Observación: Los "outliers" presentes, no son errores 👀. </sub>


<h4>2. Implementar mecanismos de comunicación y alerta a la comunidad civil en un lenguaje intuitivamente interpretable a través de Internet o cellBroadCast:</h4>

Al público le interesa saber si se produjeron daños en los edificios o si la salud y la seguridad están en peligro. Nos proponemos en brindar ese servicio que al día de hoy no se encuentra desarrollado.
***********

Por lo tanto nos enfocaremos en análisis valiosos para la comunidad! Este grupo de trabajo se pone en el papel del ciudadano común e intentará brindar alertas con mayor detalle, para que las personas sepan a que se enfrentan. 

Se investigarán
¿Qué significa Magnitud? ¿Profundidad? ¿La diferencia entre hipocentro o epicentro? Por que podria importar? 

Vamos a traducir esto al lenguaje cotidiano para facilitar la vida de la gente. 
<p align="center">
<img src= "https://t2.ev.ltmcdn.com/es/posts/4/4/6/terremoto_que_es_como_se_produce_y_tipos_3644_600.webp"  height="200">
</p>

### Enfoque 1 [Data Analysis focus]

Analizando profundamente la relacion de los sismos con otra u otras particularidades de su pais latinoamericano escogido.

Ejemplos de lineas de investigacion (Solo para que se inspiren. Pueden divagar y escoger lo que se les ocurra, su mente es el limite!):

- Sismicidad secundaria (después de un gran sismo) ¿cómo afecta? ¿Qué ha pasado? Se pueden anticipar medidas si es que hay algo sistemáticamente mal?
- Es aconsejable que haya una reubicación de habitantes en zonas como CDMX que es sabido esta construida en una zona geológicamente inestable y con alta actividad sísmica?
- Derribando (o acentuando) mitos: Tiene que ver el clima con la propensión a sismos de mayor “magnitud” y los cambios estacionales?
- Efectos secundarios no deseables: Sismos y Tsunamis, Problemas en redes eléctricas, incendios…


Entregables tangibles minimos:
Mapa de geolocalizacion de los sismos escogidos que contemple la actualizacion cada hora. 
La informacion que debe tener DEBE ser la escogida en su analisis. NO debe ir informacion cientifica como: Magnitud, Profundidad si esta no esta explicada o se indica por que es relevante.


### Enfoque 2 [Machine Learning Focus]

Aplicar un modelo de clasificacion no supervisada. 
Se generarán clasificcadores según patrones. Por el momento se plantea 'Peligrosidad Media/Alta/Baja'

Para ellos se cuenta con
Presentacion de las etiquetas de clasificacion y performancia del modelo.  
Deploy del modelo de ML - puesta en produccion (plataforma a elección)

- - -
<p align="center">
<img src= https://github.com/soyHenry/PF_DS/blob/main/Proyectos/Image/sismos.png?raw=true
 height="500">
</p>

## **Datasets y fuentes complementarias**

Fuentes de datos obligatorias:
+ Estados Unidos https://earthquake.usgs.gov/fdsnws/event/1/
+ Japon https://www.fdsn.org/networks/detail/JP/

+ Observatorio Latinoamericano: 

Fuentes de datos alternativas
+ Ejemplo de inspiracion de ciencia para la sociedad: https://twitter.com/cfariasvega/status/1586112199524614144?t=ZI428WweSDDuG_m_uWhlDg&s=19


## Disclaimer  
De parte del equipo de Henry se quiere aclarar y remarcar que los fines de los proyectos propuestos son exclusivamente pedagógicos, con el objetivo de realizar proyectos que simulen un entorno laboral, en el cual se trabajen diversas temáticas ajustadas a la realidad.
 No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones en base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos, nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).

