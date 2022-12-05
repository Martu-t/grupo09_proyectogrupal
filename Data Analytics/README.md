# Data Analytics 

# Análisis Clasificación Twitter.
En cuanto al análisis de la clasificación para la tabla de twitter, en un comienzo se creyó que lo ideal era basar la búsqueda en base a magnitud y profundidad, ya que a menor profundidad de los movimientos sísmicos en la tierra, más daño produce, tanto a humanos como materiales. Pero a través del siguiente gráfico, se observa la correlación entre la magnitud y profundidad de un terremoto y se demuestra que a medida que la magnitud se va incrementando la profundidad rara vez tiende a ser grande. Por este motivo, y para no tediar mucho el análisis, decidimos tomar de esta comparación, sólo la magnitud.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/seas.png' height = 300 >

La clasificación elegida a través del análisis de los datos se dividirá en 4 grupos de la siguiente manera: 

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_2.png' height = 100 >

•	0 = No se informará en twitter.

•	1 = Se enviará un mensaje de “aviso” (verde).

•	2 = El bot de twitter enviará un mensaje de “Advertencia” (naranja).

•	3 = Se tweeteará un mensaje de “Alerta” (como máximo nivel) (rojo).


Por lo que el análisis de como se categorizará el “dato” que ingrese como nuevo terremoto, se decidió realizar a través de Magnitud y por cercania / tipo de ciudad. Ésto, dado que la cercania (distancia en kilómetros) a una zona específica puede ser parámetro subjetivo de informe, como también si la ciudad es grande o chica. Ya que sin dudas, las consecuencias de un terremoto en una ciudad como Santiago de Chile, pueden ser muy distintas a si ocurre en una zona rural.
Para ello, se diseñó la siguiente tabla, en la que, dependiendo los sucesos que vayan aconteciendo y según las características antes mencionadas, puedan encontrarse clasificadas en alguna, y sólo una, de las categorías antes mencionadas: “0”,”1”,”2” o “3”.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_3.png' height = 100 >

Los siguientes gráficos son parte del análisis de la clasificación de la tabla twitter. Estos particularmente a la última categoría de Magnitud.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_4.png' height = 250 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_5.png' height = 250 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_6.png' height = 250 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_7.png' height = 250 >

Para distancia y ciudades nos basamos en registros de prevención y que hacer en cada caso según la magnitud, que se mueve y sensaciones (y seguridad a tener en cuenta) a medida que crece en escala.

El gráfico de tendencia de magnitudes en base al tiempo no nos indica mucho. Solo significa que puede llegar a ocurrir algún terremoto más grave. Pero no se puede predecir con certeza cuando ni mucho menos. Cabe destacar, que las construcciones chilenas están muy bien estructurada antisísmicamente (sobre todo después de 2010) y la población está bien concientizada y hasta suele realizar una auto evacuación.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_8.png' height = 200 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_9.png' height = 200 >

En cuanto a la distancia en kilómetros realizamos un estimativo, siempre utilizando el mismo criterio sobre preferencia de prevención (en las 3 clasificaciones), en base a terremotos ocurridos y sobre todo a información recolectada de institutos y centros sismológicos de 250 km para considerar como chica o grande. Mismo criterio sobre población, basándonos en intercuartiles (1/4) de la cantidad de población por ciudad.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_10.png' height = 250 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_11.png' height = 250 >

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_12.png' height = 100 >

Aquí, se puede observar que los cuartiles de población son “10.833”,”21.477” y “74.188” habitantes, respectivamente. Tomamos como criterio utilizar la mediana, ya que debemos darle importancia a la mayoría y por ello decidimos utilizar un valor muy cercano a la mediana 20.000 habitantes. 
Al no haber criterio establecido de cual zona se considera amplia y no poder establecerlo con precisión, utilizando la prevención ya que estamos hablando de fenómenos naturales y que está relacionado a vidas de personas o probables pérdidas materiales, es que se utiliza el parámetro de 250km como divisor entre distancia chica y distancia grande.
A su vez, el impacto, o nivel de daños, que un sismo puede llegar a provocar en un lugar determinado, no depende exclusivamente de lo potente que sea el movimiento, sino también de la competencia sísmica con que las edificaciones hayan sido diseñadas y construidas.
De este modo, reducir la vulnerabilidad de las construcciones en las zonas sísmicamente más activas, puede mitigar sustancialmente las consecuencias esperables de un terremoto severo.
Todo esto dado que también depende las condiciones del suelo, por ejemplo, capas gruesas de suelo blando (como relleno) pueden amplificar las zonas sísmicas, es decir depende la falla en la que se encuentre donde se produce.
Entonces, como parte final de nuestro análisis y luego de explicar como logramos con los datos obtenidos, poder llegar a una clasificación, nos adentramos en la muestra final de grupos de clasificación.

Para ello, se diseñó la siguiente tabla, en la que, dependiendo los sucesos que vayan aconteciendo y según las características antes mencionadas, puedan encontrarse clasificadas en alguna, y sólo una, de las categorías antes mencionadas: “0”,”1”,”2” o “3”.

<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_13.png' height = 200 >

•	Si la magnitud es menor a 3 no se informa ya que es imperceptible.

•	Si la magnitud es entre 3 y 5 lo percibirán la mayor cantidad de personas en la zona afectada y provocar destrozos en edificios en mal estado o algunas víctimas.

•	Si la magnitud es entre 5 y 7 pueden implicar miles de víctimas mortales en función a la zona afectada y suelen ser significativos en la zona situada hasta 250 km del epicentro.

•	Si la magnitud es de más de 7 provocan una destrucción casi total en zonas muy amplias y en todo tipo de edificios. Además se producen cambios permanentes en la topografía de la zona afectada. Ya se debe evacuar.
