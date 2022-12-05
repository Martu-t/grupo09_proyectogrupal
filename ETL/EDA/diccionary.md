![USGSLogo](https://png.pngitem.com/pimgs/s/244-2444558_usgs-png-usgs-logo-black-fox-sports-texarkana.png)

## The folowing file is to give information regarding all features get from API: https://earthquake.usgs.gov/fdsnws/event/1/

We provide an English (ENG) and spanish (SPA) version so can be useful for more people.

            ENG
1. id: Unique identifier for a specific version of data row

2. mag: magnitud of the event. For more info please refer to: https://www.usgs.gov/programs/earthquake-hazards/
earthquake-magnitude-energy-release-and-shaking-intensity

3. place: Reference populated places that are in close proximity to a seismic event.

4. time: time where the event started in unix format

5. updated: last time of update in linux format

6. tz: Timezone offset from UTC in minutes at the event epicenter.

7. url: url where the data is locatted

8. detail: query used to get data from tthe API

9. felt: The total number of felt reported (submitted to the https://earthquake.usgs.gov/data/dyfi )

10. cdi: The maximum reported intensity for the event. Computed by DYFI. While typically reported as a roman numeral, for the purposes of this API, intensity is expected as the decimal equivalent of the roman numeral. For more information, please refer to: https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity

11. mmi: average record of modified Mercalli intensity. For more info please refer to: https://www.usgs.gov/programs/earthquake-hazards/modified-mercalli-intensity-scale

12. alert: Suggested levels of response: no response needed (green), local/regional (yellow), national (orange), or international (red).

13. status: status of the data. If is 'DELETE', means the data has been removed from the original link.. ANY other value indicated that is available. 

14. tsunami: "1" for large events in oceanic regions and "0" otherwise. The existence or value of this flag does not indicate if a tsunami actually did or will exist.

15. sig: An identifying code assigned by - and unique from - the corresponding source for the event.

16. net: The ID of a data contributor. Identifies the network considered to be the preferred source of information for this event.

17. code: An identifying code assigned by - and unique from - the corresponding source for the event.

18. ids: A comma-separated list of event ids that are associated to an event.

19. sources: list of contributors

20. types: all types/categories of events

21. nst: The total number of seismic stations used to determine earthquake location.

22. dmin: Horizontal distance from the epicenter to the nearest station (in degrees). 1 degree is approximately 111.2 kilometers. In general, the smaller this number, the more reliable is the calculated depth of the earthquake.

23. rms: The root-mean-square (RMS) travel time residual, in sec, using all weights. This parameter provides a measure of the fit of the observed arrival times to the predicted arrival times for this location. Smaller numbers reflect a better fit of the data. The value is dependent on the accuracy of the velocity model used to compute the earthquake location, the quality weights assigned to the arrival time data, and the procedure used to locate the earthquake.

24. gap: The largest azimuthal gap between azimuthally adjacent stations (in degrees).

25. magType: The method usde to calculate the preferred magnitude for the event.

26. type: Type of seismic event.

27. title: title of feed. Usually: “USGS Magnitude 1+ Earthquakes, Past Day”, “USGS Magnitude 4.5+ Earthquakes, Past Month”

28. geometry* add with geopandas

            SPA
+ id: Identificador único para cada fila

+ mag: magnitud del evento. Para más información entrar a: https://www.usgs.gov/programs/earthquake-hazards/
earthquake-magnitude-energy-release-and-shaking-intensity

+ place: se utiliza GeoNames datast para hacer referencia a lugares poblados cercanos al envento sísmico

+ time: hora en formato unix

+ updated: última hora de actualización

+ tz: Zona horaria (tomando sistema UTC) convertido a minutos del epicentro del sismo 

+ url: url de donde se obtienen los datos

+ detail: consulta utilizada en la API para obtener los datos

+ felt: número total reportado de sensación del sismo (registros hechos la página: https://earthquake.usgs.gov/data/dyfi )

+ cdi: Máximo de intensidad reportado para el sismo. Generalmente se reporta en números romanos, pero para practicidad, la API envïa el número decimal equivalente al nümero romano. Para mäs informaciön entrar a: https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity

+ mmi: promedio registrado medido en la escala sismológica de Mercalli. Para más información entrar en: https://www.usgs.gov/programs/earthquake-hazards/modified-mercalli-intensity-scale

+ alert: Grado de respuesta sugerido, siendo posibles 'green' (verde) = no se necesita respuesta; 'yellow' (amarillo) = local/regional, 'orange' (naranja) = nacional, 'red' (rojo) = internacional

+ status: estado de los datos al momento de descargar la información. En caso de figurar 'DELETE' esa url no se encontrarä más disponible.


+ tsunami: utiliza "1" para eventos grandes en zonas oceánicas y "0" para otras zonas. La existencia del valor no implica que haya habido o que habrá un tsunami.

+ sig: identificador único asignado por la fuente que informa el evento

+ net: ID del contribuidor. Se identifica quien es la fuente más recomendable para informar sobre el evento.

+ code: cödigo identificatorio (único) correspondiente a la fuente para el evento

+ ids: lista de valores con ids asociadas al evento

+ sources: lista de contribuidores

+ types: todas los tipos o categoría de eventos

+ nst: número total de estaciones sísmicas usadas para determinar la localización del terremoto

+ dmin: Distancia horizontal desde el epicentro a la estación más cercana (en grados). 1 grado es apróximadamente 111.2 kilómetros. En general cuanto menor es este número, mäs confiable es el cálculo de profundidad del terremoto

+ rms: raíz cuadrática medio en segundos. Este parámetro proporciona una medida de ajuste de los tiempos de llegada observados a los tiempos de llegada predichos en dicha localización. Números pequeños reflejan un mejor ajuste de datos. El valor depende de la precisión del modelo de velocidad utilizado para calcular la ubicación del terremoto, los pesos asignados a la calidad de los datos de la hora de llegada, y el procedimiento utilizado para localizar el terremoto.

+ gap: La mayor distancia azmutual de la estación (en grados)

+ magType: Método utilizado para calcular la magnitud preferente del evento

+ type: Tipo de evento sísmico

+ title: título de la página/noticia

+ geometry* agregado geopandas
