![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# **PROYECTO GRUPAL **

- - -

# <h1 align="center">**`SISTEMA DE ALERTAS SISMICAS`**</h1>

***If you would like to see the info in English, please [Click Here](https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/README_EN.md)***

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/198112414-ebe5a60f-6bbf-4f94-9924-20da4d702bb5.png"  height=700> 
</p>


## Entendimiento de la situación:

Los desastres naturales pueden resultar en un gran número de muertes, pérdida de propiedades, y daños irreparables. Es por esto que la predicción temprana, las medidas de protección y de atención apropiadas resultan urgentes. 

Particularmente, los sismos, son el fenómeno natural del cual tenemos menor capacidad predictiva, lo que deriva en una problemática que afecta a la población. Por consiguiente, éste proyecto busca facilitar la vida a la sociedad, dándole acceso a información de manera simplificada y en lenguaje cotidiano. 

##  Objetivos: 

### General: 
Contribuir a la comunidad y a su seguridad. 

### Específicos del trabajo:   

Crear una base de datos que contemple información de sismos en Estados Unidos, Japón y Chile de forma estandarizada. 

Incrementar el interés y comprensión de la comunidad en torno a la temática sismográfica.  

Desarrollar un bot automatizado de Twitter, que una vez sucedido un sismo informe a la sociedad. Se intentará incluir si la salud o seguridad se encuentran en peligro.


### Específicos del grupo:

Fortalecer habilidades blandas y de comunicación. 

Afianzar y perfeccionar conocimientos aprendidos en la carrera de Data Science. 


## Alcance: 

El alcance del trabajo será ofrecer un servicio para la sociedad, enfocándose en un análisis valioso para la misma. Para esto se pondrá en el papel del ciudadano común y se intentará “bajar a tierra” conocimientos científicos para que el público pueda comprender y beneficiarse de la información recolectada. 

Se intentará brindar alertas con mayor detalle para el accionar de las personas, sabiendo a que se enfrentan en caso de suceder un sismo. 

Para ello se utilizarán datos de tres (3) países ubicados en distintas zonas geográficas para realizar un análisis heterogéneo de sismos, relacionándoselos con el clima, los tsunamis y los volcanes activos en sus respectivas zonas. 

Se creará una base de datos que albergue información de éstos tres países de manera normalizada.  

Luego, se realizará en ella, cargas incrementales de los datos a medida que vayan sucediendo, actualizándose cada una hora aproximadamente. 

Además, se implementará un modelo de Machine Learning (ML), específicamente de aprendizaje no supervisado. Podremos así, tener una clasificación de distintos tipos de eventos de manera sencilla. En el caso de no obtener una clasificación específica a través del ML, se utilizará un Data Analytics para complementar la información.

En la cuenta de twitter https://twitter.com/alertas_sismos, y en base a la clasificación mencionada, nuestro bot indicará a la sociedad, a través de publicaciones automáticas, si se deberá tomar medidas previsionales añadiendo mínimos detalles técnicos del fenómeno ocurrido.  

Se plantea la posibilidad de realizar el trabajo en un ambiente cloud, para ello se están analizando los distintos entornos para elegir el que más se adecúa al mismo. 

Estará fuera del alcance del proyecto, por razones de complejidad y tiempo, la elaboración de conclusiones específicas cuantitativas respecto a la información secundaria obtenida, como clima, tsunamis y erupciones volcánicas, asi como técnicas / científicas en general. 

Se plantea la posibilidad de continuación del proyecto una vez concluido el plazo del mismo.



###  KPIs asociados al proyecto:

Para poder medirlos se tomarán las siguientes métricas que sacaremos de nuestra cuenta de Twitter. 

**Tasa de crecimiento de la audiencia.** = 
𝑁𝑢𝑒𝑣𝑜𝑠 𝑠𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠 / 𝑇𝑜𝑡𝑎𝑙 𝑠𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠 𝑥 100

 
  

**Alcance de la publicación.** = 
𝑃𝑒𝑟𝑠𝑜𝑛𝑎𝑠 𝑞𝑢𝑒 𝑣𝑖𝑒𝑟𝑜𝑛 𝑒𝑙 𝑡𝑤𝑖𝑡 / 𝑇𝑜𝑡𝑎𝑙 𝑠𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠 𝑥 100

 
 

**Tasa de interacción (o aplauso).** = 
𝑇𝑜𝑡𝑎𝑙 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑐𝑖𝑜𝑛𝑒𝑠 / 𝑇𝑜𝑡𝑎𝑙 𝑠𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠 𝑥 100

 
 

**Tasa de visitas de perfil.** =
 𝑁ú𝑚𝑒𝑟𝑜 𝑣𝑖𝑠𝑢𝑎𝑙𝑖𝑧𝑎𝑐𝑖𝑜𝑛𝑒𝑠 𝑑𝑒 𝑝𝑒𝑟𝑓𝑖𝑙 / 𝑇𝑜𝑡𝑎𝑙 𝑆𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠𝑥 100

 
 

**Tasa de ampliación (detalles).** =
 𝐶𝑎𝑛𝑡𝑖𝑑𝑎𝑑 𝑑𝑒 𝑣𝑖𝑠𝑡𝑎𝑠 𝑑𝑒 𝑑𝑒𝑡𝑎𝑙𝑙𝑒𝑠 / 𝑇𝑜𝑡𝑎𝑙 𝑆𝑒𝑔𝑢𝑖𝑑𝑜𝑟𝑒𝑠𝑥 100

 
A partir de dichas métricas, definimos los siguientes KPIs:

- Superar los 10.000 seguidores en el primer año.

- Incrementar el alcance de las publicaciones diez veces el primer año, a partir del primer mes.

- Aumentar las interacciones un 5 % por mes durante el primer año.

- Obtener un número de visualizaciones de perfil de al menos 50k en promedio en el primer año, por evento.


Además se contempla la posibilidad de hacer encuestas en el futuro: 

* Escala de satisfacción del cliente. Con un nivel de 1 a 10, ¿Qué nivel de satisfacción encuentras con nuestro servicio?

* Lealtad del cliente. Encuesta y “agrupar respuestas” ¿Qué probabilidades hay que recomiendes nuestro servicio? 

Esto se definirá una vez avanzado el proyecto.

Estos KPIs serán contemplados en un determinado período de tiempo y se desglosarán a la hora de ejecutarlos. 

Repositorio del proyecto: 

Nuestro repositorio es https://github.com/Martu-t/grupo09_proyectogrupal y en él se irán cargando los distintos códigos fuente (con su respectiva documentación) utilizados para alcanzar con éxito los objetivos. 

### Stack tecnológico: 

Python = Extracción, EDA, Transformación, carga a base de datos (inicial e incremental) y bot de Twitter. Se utilizarán librerías para agilizar los procesos de conexión a base de datos, preparación de modelos de ML y gráficos de geolocalización. 

- Github = Repositorio de GITHUB y control de versiones. 

- Python y sus librerías = Para ETL automatizado (incluída conexión a BD). Uso de Tweepy para conectar a la API de Twitter.

- PostgreSQL= Creación y manejo de Base de datos. Se utiliza el motor a traves de AWS (con base de datos RDS).

- Power BI = Presentación de dashboard.

- Streamlit = Deploy del módelo de machine learning y mapa interactivo. 

- Ambiente cloud = Desarrollo de trabajo. 

- Metodología de trabajo: 

La metodología de gestión de proyecto utilizada se cree muy importante para llegar a los objetivos propuestos. Se utilizará metodología considerada ágil al ser colaborativa, rápida y efectiva, iterativa, respaldada por datos y fundamentalmente que se valore a las personas por encima de los procesos ya que se deduce que es la mejor y más eficiente manera de trabajo. 

En particular se realizará la metodología Scrum, que se basa en “sprints” para crear un ciclo de proyecto, en este caso, sprints de una semana. Cada sprint culminará con la demostración del progreso del trabajo realizado hasta el momento, frente al Product Owner. La duración total del proyecto será de 4 semanas. Siendo la última exclusivamente para presentación final y demostrar puesta en producción. 

Se realizan reuniones diarias (guiadas por un Scrum Master) con el objetivo de conectar a todos los participantes del proyecto, dividiendo, organizando trabajo y tiempos por cada integrante y así garantizar que las tareas se finalicen a tiempo.  

### Diseño: 

Los entregables de cada sprints serán: 

#### Semana 1: 
Propuesta de trabajo, efectivamente fundamentada y documentada. **Completo.**

#### Semana 2: 
Creación de Data Warehouse y carga inicial e incremental. Utilizando el Stack tecnológico más adecuado y documentando el proceso. **Completo.** 

#### Semana 3:
Dashboard y modelo de Machine Learning. **Completo.**

#### Semana 4:
Demostración final y storytelling ante el Product Owner. 

## Equipo de trabajo: 

El equipo de trabajo está conformado por: 

Martha Alejandra Tarantino. 

Federico Gonzalez Pietranera. 

Deiner Fabian Silva Rueda. 

Axel Moriena. 

Los roles y responsabilidades de cada integrante estarán suscitados al perfil de cada uno y en dependencia de las tareas a realizar en cada sprint. 

Se promueve en primer lugar la funcionalidad y comodidad del grupo y para ello se dividen las tareas con el propósito del bien común y la obtención de los objetivos planteados. Para ello es fundamental en cada día la comunicación y el diálogo constante en el grupo humano, sin perder de vista la consecución de los objetivos. 

Los roles en cada tarea realizada se delimitarán, dando siempre lugar al pedido y ofrecimiento de colaboración de todos y para todos. Sin quitar responsabilidad a cada integrante y al grupo en general por sus tareas. 

Decidimos utilizar la aplicación "Asana" para la distribución de tareas y simple visualización de la carga de trabajo.

Se obtendrá más información en detalle en el siguiente diagrama de Gantt.

<p align="center">
<img src= https://iili.io/H9gfLv9.png>
</p>

## ETL
Todo el proceso se encuentra en la carpeta [ETL](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/ETL) de este mismo repositorio.

## Analysis
En la sección de [Data Analysis](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/Data%20Analytics) encontrarás tanto el análisis de los datos generales, como asï tambiën una explicaciön de los parámetros que hemos tenido en cuenta al momento de planificar la clasificación de sismos.

## Machine Learning
En la carpeta de [ML](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/ML) podrás ver la elección del nuestro módelos, fundamentos y puesta en marcha del mismo

## Twitter bot
Dentro de la carpeta de [twiiter](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/ML)https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/twitter puedes ver todo el cödigo que mantiene a nuestro bot funcionando. Adicionalmente te invitamos pasar por nuestro [Perfil de Twitter](https://twitter.com/alertas_sismos) para verlo en marcha.

## Streamlit
En la carpeta de este repositorio llamada [streamlit](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/streamlit) puedes ver el código fuente y requerimientos para poner la app en la web.
Te invitamos a visitar la página de [Streamlit](Deploy: https://terremotos-chile.streamlit.app/) donde encontrarás un poco mäs sobre nosotros, recomendaciones generales sobre sismos y un mapa interactivo de los ültimos eventos emitidos en nuestro Twitter.


## Diccionario de datos general: 

Para continuar, se cree importante dar el significado de algunos conceptos básicos a utilizar. 

<p align="center">
<img src= https://github.com/soyHenry/PF_DS/blob/main/Proyectos/Image/sismos.png?raw=true
 height="500">
</p>


#### Sismo: 
Un sismo es el movimiento brusco de la Tierra (con mayúsculas, ya que se refiere al planeta), causado por la liberación de energía acumulada durante un largo tiempo.  Estos movimientos son habitualmente lentos e imperceptibles. Pero en algunos casos el desplazamiento libera una gran cantidad de energía, cuando una de las placas se mueve bruscamente contra la otra, rompiéndola y originando un terremoto. 

La diferencia entre sismo y terremoto está dada por la intensidad del movimiento sísmico, el más peligroso, con efectos destructivos que puedan llegar a ser fatales, es el terremoto. 

Las placas tectónicas son planchas de piedra, sólida, rígida que se encuentran en la litosfera (Capa externa y rígida de la Tierra, de profundidad entre los 10 y 50 km, es decir la más superficial). Se apoyan sobre otra plancha de roca fundida, el manto, que se comporta como si fuera un plástico deforme, maleable que se estira sin romperse. 

Aunque las placas son rígidas, también se mueven, lo hacen de “rebote”, por el enorme calor que desprende el interior de nuestro planeta (núcleo), que arde a 6.700°C, casi como el sol. Este calor ardiente mueve el manto y en consecuencia se expande a la litosfera y la corteza terrestre. 

El calor en expansión hace que las placas frías de la superficie choquen, friccionen y provoquen terremotos, grietas, incluso tsunamis. Este dinamismo, a la larga, cambia la fisonomía de la Tierra.  

#### El hipocentro y el epicentro:
 El hipocentro fuente o foco, es el lugar en el interior de la corteza terrestre donde tiene origen un sismo (a cierta profundidad con respecto a la superficie). En cambio, **el epicentro**, es el punto en la superficie terrestre sobre el que se proyecta el hipocentro (donde el terremoto es más intenso). 

**La profundidad** de un sismo, es el punto en la profundidad (de hipocentro) de la Tierra desde donde se libera la energía de un terremoto. En base a ésta se clasifican en superficial, intermedio o profundo.  

Los sismos ocurridos a una mayor profundidad causan menos daño porque la mayoría de su energía se disipa antes de llegar a la superficie, de lo contrario los superficiales son los más destructivos, ya que tienen un impacto más directo sobre la superficie de la tierra. 

 #### Magnitud
Magnitud es una medida única del tamaño de un terremoto. Ésta indica cuanta energía fue liberada durante el terremoto y es independiente de la localización y profundidad. Se mide utilizando sismógrafos, que monitorean las ondas sísmicas que viajan a través de la Tierra después de un terremoto. Ya no se usa la Escala Richter, se usa un medidor de ondas sísmicas, que si bien es similar, ya no se dice por ejemplo: “El terremoto fue de 5,6 escala Richter, sino solo 5,6”. 

Cabe destacar algunos datos importantes, que en un primer momento se analizarán para el proyecto y luego se sacará conclusiones al respecto.

El **Anillo de Fuego,** o **Cinturón de Fuego**, se encuentra en las costas del océano Pacífico y concentra varias de las zonas con mayor actividad sísmica del planeta. Abarca una región de alrededor de 40.000 kilómetros y contiene territorios de 31 países. El 90% de los terremotos y el 75% de los volcanes de todo el mundo se encuentran allí. Aquí se generó el terremoto más fuerte desde que se realizan registros, el terremoto de Valdivia, Chile, el 22 de mayo de 1960 con magnitud de 9,5, con posterior Tsunami en Japón, Filipinas y Hawai.

![image](https://user-images.githubusercontent.com/103937102/202608869-04d5764c-c594-411c-bb31-44aff7b52b1f.png)


Ésta particularidad se debe al tipo de límite que se puede observar entre las placas tectónicas. Existen 3 clases; divergentes, convergentes y de fricción.
En las clases divergentes las placas se separan en sentido opuesto (por ejemplo Gran Valle de Rift, que puede ocasionar que África se divida en el futuro). En el caso de las convergentes, las placas tienden a enfrentarse hacia la misma dirección, generando las llamadas zonas de subducción. Éste tipo se encuentra en buena parte del Anillo de Fuego. En éstas, una de las placas se hunde lentamente por debajo de la otra, generando tanto terremotos como erupciones de volcanes.

Las clases de fricción, son conocidas como “fallas”. Se desplazan de forma lateral en sentido opuesto (ocurre en la famosa Falla de San Andrés, en el oeste de América del Norte). Éste en particular se trata de uno de los lugares que genera mayor preocupación por los sismólogos por las consecuencias que puede presentar en un futuro cercano. Aquí sucedió uno de las mayores catástrofes de la historia de Estados Unidos, el terremoto de San Francisco en 1906. 

De esta manera, para poder cumplir con los objetivos del proyecto, debimos realizar un análisis de datos, para elegir un país latinoamericano que se adapta a la consigna y a nuestras necesidades, entonces...

## ¿Por qué Chile?

Como se comentaba anteriormente, nuestro trabajo se encontraba con el objetivo de realizar una base de datos estandarizada entre Estados Unidos, Japón y un país a elección de Latinoamérica.
Nuestra elección de país fue Chile. En primer lugar, por nuestra cercanía al país, ya que nos interesaba realizar un proyecto en el cual podamos “ayudar” con un sentido de pertenencia, como lo es un país vecino.
En segundo lugar, Chile es considerado el país sísmicamente más activo del mundo y el cuarto más expuesto a sufrir daños mayores por catástrofes naturales.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/mapa.png' height = 450 >


Como se mencionó ut supra, el 22 de mayo de 1960, Chile registró lo que aún sigue siendo el mayor sismo en la historia de la humanidad. El llamado "Gran Terremoto de Chile", cuyo epicentro se localizó en la ciudad de Valdivia, en el sur del país, midió 9,5 grados en la Escala de Richter, en ese momento.
El movimiento telúrico generó un tsunami que arrasó con varias poblaciones costeras e incluso provocó víctimas del otro lado del Pacífico, en Japón, Hawaii y Filipinas. Más de 2.000 personas perdieron la vida como consecuencia del temblor, y el sur del país quedó devastado.
También, en el siguiente gráfico se observa que de los 15 terremotos más fuertes del mundo, 3 fueron en Chile.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_1.png' height = 350 >


A su vez desde el 2000 en Latinoamérica, los terremotos por países, de mayor a menor fueron: Chile en 2010, de 8,8 en la escala de Richter; Perú en 2001, de 8,4; Chile en 2015, de 8,3; Chile en 2014, de 8,3; Perú en 2007, de 8,0. Es decir, 3 de los 5 más fuerte fueron en este país.

Chile, es uno de los países más proclives del mundo a sufrir temblores, debido a que está en el llamado Cinturón, o “anillo”, de fuego del Pacífico y gran parte de su territorio está expuesto al constante choque de la placa tectónica de Nazca y la placa Sudamericana. Lo que provoca movimientos de subducción, anteriormente explicados.

Para terminar, al tener que realizar el proyecto con Estados Unidos, Japón y el país latinoamericano a libre elección, sumado a todas las características anteriormente mencionadas, se eligió Chile, ya que se encuentra en otro territorio completamente diferente a los anteriores (en otro hemisferio, comparado con Estados Unidos) y otro continente y hemisferio en relación a Japón. 

Esto genera que sean distintas zonas geográficas, distintos clima y diferentes puntos en el mapa del mundo, por eso no se optó por ejemplo, por México, ya que es un país vecino a Estados Unidos. 

En este país y más precisamente en gran parte de su capital, Santiago de Chile, se encuentra otra falla importante a considerar, la falla de San Ramón. Ésta es muy estudiada por sismólogos, quienes dicen que representa una amenaza muy fuerte para la zona metropolitana, al estar cercana a grandes centros urbanos y que podría ser un peligro para la vida de millones de personas, además por la gran cantidad de edificaciones que se encuentran sobre la misma.

Para concluir, cabe destacar que así y todo (y no menos importante), los tres países pertenecen al anillo de fuego del pacífico.
 

## Disclaimer  
De parte del equipo de Henry se quiere aclarar y remarcar que los fines de los proyectos propuestos son exclusivamente pedagógicos, con el objetivo de realizar proyectos que simulen un entorno laboral, en el cual se trabajen diversas temáticas ajustadas a la realidad.
 No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones en base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos, nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).

