![USGSLogo](https://png.pngitem.com/pimgs/s/244-2444558_usgs-png-usgs-logo-black-fox-sports-texarkana.png)

## The folowing file is to give information regarding all features get from API: https://earthquake.usgs.gov/fdsnws/event/1/

We provide an English (ENG) and spanish (SPA) version so can be useful for more people.

    - ENG
1. id: Unique identifier for a specific version of data row

2. mag: magnitud of the event. For more info please refer to: https://www.usgs.gov/programs/earthquake-hazards/
earthquake-magnitude-energy-release-and-shaking-intensity

3. place: aprox location 

4. time: time where the event started in linux format

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
