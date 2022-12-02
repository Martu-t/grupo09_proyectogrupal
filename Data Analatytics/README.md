# Data Analytics 
¿Por qué Chile?
Nuestro trabajo se encontraba con el objetivo de realizar una base de datos estandarizada entre Estados Unidos, Japón y un país a elección de Latinoamérica.
Nuestra elección de país fue Chile. En primer lugar, por nuestra cercanía al país y nos interesaba realizar un proyecto en el cual podamos “ayudar” con un sentido de pertenencia, como lo es un país vecino.
En segundo lugar, Chile es considerado el país sísmicamente más activo del mundo y el cuarto más expuesto a sufrir daños mayores por catástrofes naturales.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/mapa.png' height = 300 >


El más fuerte se dio el 22 de mayo de 1960, cuando el país registró lo que aún sigue siendo el mayor sismo en la historia de la humanidad. El llamado "Gran Terremoto de Chile", cuyo epicentro se localizó en la ciudad de Valdivia, en el sur del país, midió 9,5 grados en la Escala de Richter.
El movimiento telúrico generó un tsunami que arrasó con varias poblaciones costeras e incluso provocó víctimas del otro lado del Pacífico, en Japón, Hawaii y Filipinas. Más de 2.000 personas perdieron la vida como consecuencia del temblor, y el sur del país quedó devastado.
En el siguiente gráfico se observa que de los 15 terremotos más fuertes del mundo, 3 son en Chile.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_1.png' height = 300 >


A su vez desde el 200 en Latinoamérica, los terremotos por países, de mayor a menor fueron: Chile en 2010, de 8,8 en la escala de Richter; Perú en 2001, de 8,4; Chile en 2015, de 8,3; Chile en 2014, de 8,3; Perú en 2007, de 8,0. Es decir, 3 de los 5 más fuerte fueron en este país.

Chile, es uno de los países más proclives del mundo a sufrir temblores, debido a que está en el llamado Cinturón, o “anillo”, de fuego del Pacífico y gran parte de su territorio está expuesto al constante choque de la placa tectónicas de Nazca y la placa Sudamericana.


<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/anillo.png' height = 200 >
En el anillo de fuego se encuentra el 90 % de la actividad sísmica del planeta y concentra un 75% de los volcanes activos del mundo. (por eso la palabra fuego)


# Análisis Clasificación Twitter.
En cuanto al análisis de la clasificación para tabla de twitter, en un comienzo se creyó que lo ideal era basar la búsqueda en base a magnitud y profundidad, ya que a menor profundidad de los movimientos sísmicos en la tierra, más daño produce, tanto a humanos como materiales. Pero a través del siguiente gráfico, se observa la correlación entre la magnitud y profundidad de un terremoto y se demuestra que a medida que la magnitud se va incrementando la profundidad rara vez tiende a ser grande. 

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/seas.png' height = 300 >

La clasificación elegida a través del análisis de los datos se dividirá en 4 grupos de la siguiente manera: 

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_2.png' height = 300 >

•	0 = No se informará en twitter.
•	1 = Se enviará un mensaje de “aviso” (verde).
•	2 = El bot de twitter enviará un mensaje de “Advertencia” (naranja).
•	3 = Se tweeteará un mensaje de “Alerta” (como máximo nivel) (rojo).

Por lo que el análisis de como se categorizará el “dato” que ingrese como nuevo terremoto, se decidió realizar a través Magnitud y por cercania / tipo de ciudad. Esto, dado que la cercania (distancia en kilómetros) a una zona específica puede ser parámetro subjetivo de informe, como también si la ciudad es grande o chica. Ya que sin dudas, las consecuencias de un terremoto en una ciudad como Santiago de Chile, pueden ser muy distintas a si ocurre en una zona rural.
Para ello, se diseñó la siguiente tabla, en la que, dependiendo los sucesos que vayan aconteciendo y según las características antes mencionadas, puedan encontrarse clasificadas en alguna, y sólo una, de las categorías antes mencionadas: “0”,”1”,”2” o “3”.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_3.png' height = 300 >

Y luego los siguientes gráficos son parte del análisis de la clasificación de la tabla twitter. Estos particularmente a la última categoría de Magnitud.

•	Si la magnitud es menor a 3 no se informa ya que es imperceptible.
•	Si la magnitud es entre 3 y 5 lo percibirán la mayor cantidad de personas en la zona afectada y provocar destrozos en edificios en mal estado o algunas víctimas.
•	Si la magnitud es entre 5 y 7 pueden implicar miles de víctimas mortales en función a la zona afectada y suelen ser significativos en la zona situada hasta 250 km del epicentro.
•	Si la magnitud es de más de 7 provocan una destrucción casi total en zonas muy amplias y en todo tipo de edificios. Además se producen cambios permanentes en la topografía de la zona afectada. Ya se debe evacuar.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_4.png' height = 200 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_5.png' height = 200 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_6.png' height = 200 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analatytics/src/grafico_7.png' height = 200 >

