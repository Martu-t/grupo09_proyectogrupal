![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# ** GROUP PROJECT **

- - -

# <h1 align="center">**`SEISMIC ALERT SYSTEM`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/198112414-ebe5a60f-6bbf-4f94-9924-20da4d702bb5.png"  height=700> 
</p>


## About the context:

A natural disaster can bring several deaths, loss of land and damaged beyond repair.
For this reason, early prediction, safety measures and proper attention became an urgent matter.

In particular, the seismic are the natural phenomenon with less posibility to predict, concerning most of population who live in siesmic areas. Therefore, this project try to make their lifes easiest, giving them access to valuable information in a simple and put it in relatable words.

##  Goals: 

### General: 
Help the cominity and preserve they safety.

### Project´s specifics:

- Create a database that holds standardized information about seismic from the USA, Japan and Chile.

- Grow interested and comprehension from the community regarding the earthquakes.

- Develop an automated Twitter bot, that can inform society, once the seismic occurs. We aim to include if the health or security might be in danger. 


## Scope: 

Our scope would be to give a service to society, focusing on a valuable analysis for them. To achieve this, we will be on the role of ordinary citizens and bring the concept to earth, so the public can understand and make the most of the collected information. 

We would try to make alerts with accurate information to act accordingly, understanding what they should expect in case of an earthquake. Also, we would provide some additional information in our streamlit web app.

To do this, we have a normalized database that helps us to understand past information (from different countries) and used them for analysis.

We will update our database hourly.

Also, we implemented an unsupervised machine learning model, that help us cluster different type of earthquakes and make a pre-clasiffication on what we will inform through Twitter.

All our records will be displayed through our chatbot https://twitter.com/alertas_sismos, with automatic tweets including recommendations in case of medium or severe earthquakes. 

Our project runs with a cloud environment, using RDS (AWS relational database) and a virtual machine to run all the scripts. 

Is out of the scope, for complexity and time reason, to make a scientific conclusion regarding the obtained information such as whether, tsunamis, volcanic explosion or any technical report. 


###  KPIs for this project:

In order to measure, we will used the following metrics as base, from our Twitter account:

**Audience growth rate** = 
New followers / total followers 𝑥 100

**Post reach** = 
Tweet view / Total followers 𝑥 100

**Engagment rate.** = 
total interactions / Total followers 𝑥 100

**Profile´s vitit rate** =
 profile visualizations / total followers  𝑥 100

**Enlargement rate** =
Quantity of detail´s visit / total followers 𝑥 100

From that metrics, we defined the followings KPIs

- Get over 10.0000 followers on our first year.
- Increase the ´post reach´ by 10 times for the first year, after the first month.
- Rise the engagment by 5% per during the first year
- Get a number of profile visualization of at least 50K average the first year, per event.

Also, we keep open the posibility of future pools, such as:

- Scale of satisfaction: From 1 to 10, How satisfy are you with the service?

- Loyalty: Pool to group answer - How likely is that you recommend our service?

This will be define after some advance in the project is made.

All the KPIs depends on the time and would be consider only in a specific period, and would be break down prior to execute. 

### Tech Stack

- Python = ETL, EDA, load (initial and incremental), Twitter bot. Also we used libaries to make faster process, conections, ML models and graphics.

- Github = Version control

- PostgreSQL= Database host by AWS (RDS).

- Power BI = Dashboard and analysis

- Streamlit = Deploy for an interactive map

- Metodología de trabajo: 

We consider an important key implementation of agile methodologies in order to achieve the goals. We use SCRUM method, based on weekly sprints. Every srpint will be finished by a demo/presentation with the Product Owner. The total duration is 4 weeks, being the last one only to finaliced details. 

We have daily meeting wih our Scrum Master to organized the work and timetables, and divided the workload acordingly. 

### Desing for each sprint  

#### Week 1: 
Work proposal, basis and initial documentation.
 **Completed.**

#### Week 2: 
Database creation with initial and incremental loads. Using the most adecuate technologies. Documentation all the way.
 **Completed.** 

#### Week 3:
Dashboard and Machine Learning Model. Twitter bot working independently. **Completed.**

#### Week 4:
Final presentation with Product Owner. Final deploys. 

## Meet the team: 

Martha Alejandra Tarantino. 

Federico Gonzalez Pietranera. 

Deiner Fabian Silva Rueda. 

Axel Moriena. 

All roles and responsibilities of each person would be assigned according to their expertise and would change if the project required so.

Is encourage the funcionality and convinience of the team. That's why all taks are deivded for the common benefit and achivment of goals. 
The comunication daily is vital for a succesful project. 

We use the app "Asana" to easily distributed the workload and see what each one is doing. In this way we can report to the PO or scrum master how long does it take to acomplish each taks. 


<p align="center">
<img src= https://iili.io/H9gfLv9.png
</p>


## ETL
All process, including EDA and dictionaries, can be found here [ETL](https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/ETL) de este mismo repositorio.

## Analysis
You can find all the relevant analysis and how we end up the clasification 
https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/Data%20Analytics

## Machine Learning
Model and analysis of clusters
https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/ML

## Twitter bot
Bot that automaticly tweet when there is an earthquake in Chile region
Code: https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/twitter
Deploy: https://twitter.com/alertas_sismos

## Streamlit deploy
Interactive map and information about earthquakes
Code: https://github.com/Martu-t/grupo09_proyectogrupal/tree/main/streamlit
Deploy: https://terremotos-chile.streamlit.app/

## General dictionary 

For a general knowledge, we present a glosary of main words.

<p align="center">
<img src= https://github.com/soyHenry/PF_DS/blob/main/Proyectos/Image/sismos.png?raw=true
 height="500">
</p>


#### Earthquake: 
An earthquake (also known as a quake, tremor or temblor) is the shaking of the surface of the Earth resulting from a sudden release of energy in the Earth's lithosphere that creates seismic waves. Earthquakes can range in intensity, from those that are so weak that they cannot be felt, to those violent enough to propel objects and people into the air, damage critical infrastructure, and wreak destruction across entire cities. The seismic activity of an area is the frequency, type, and size of earthquakes experienced over a particular time period. The seismicity at a particular location in the Earth is the average rate of seismic energy release per unit volume

#### Epicenter
The epicenter is the location on Earth’s surface directly above where an earthquake occurs and spreads. It is used as a reference point by seismologists to study the spread and effects of earthquakes.

#### Hypocenter
The hypocenter is the actual point at which an earthquake occurs and the point from which body waves of an earthquake ultimately originate.

Read more: Difference Between Epicenter and Hypocenter | Difference Between http://www.differencebetween.net/miscellaneous/geography-miscellaneous/difference-between-epicenter-and-hypocenter/#ixzz7mey6Rcyp


 #### Magnitude
An earthquake radiates energy in the form of different kinds of seismic waves, whose characteristics reflect the nature of both the rupture and the earth's crust the waves travel through.[6] Determination of an earthquake's magnitude generally involves identifying specific kinds of these waves on a seismogram, and then measuring one or more characteristics of a wave, such as its timing, orientation, amplitude, frequency, or duration.[7] Additional adjustments are made for distance, kind of crust, and the characteristics of the seismograph that recorded the seismogram.

The various magnitude scales represent different ways of deriving magnitude from such information as is available. All magnitude scales retain the logarithmic scale as devised by Charles Richter, and are adjusted so the mid-range approximately correlates with the original "Richter" scale.[8]

Most magnitude scales are based on measurements of only part of an earthquake's seismic wave-train, and therefore are incomplete. This results in systematic underestimation of magnitude in certain cases, a condition called saturation


#### Ring of fire

The Ring of Fire is a direct result of plate tectonics: specifically the movement, collision and destruction of lithospheric plates (e.g. the Pacific Plate) under and around the Pacific Ocean. The collisions have created a nearly continuous series of subduction zones, where volcanoes are created and earthquakes occur.

![image](https://user-images.githubusercontent.com/103937102/202608869-04d5764c-c594-411c-bb31-44aff7b52b1f.png)


## Why Chile?

As we mentioned before, our work was focused on creating a standard database with 3 countries, USA, Japan and another Latin American country of our selection. 
We choose Chile. Firstly, because of the closeness with this country, and with this project, we can "help out" our neighbour. Secondly,  Chile is considered the most active country in terms of earthquakes and the 4th most likely to suffer higher damaged due to natural catastrophes. 


<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/mapa.png' height = 450 >

As mentioned above, on May 22, 1960, Chile recorded what is still the largest earthquake in human history. The so-called "Great Earthquake of Chile", whose epicenter was located in the city of Valdivia, in the south of the country, measured 9.5 degrees on the Richter Scale at that time.
The telluric movement generated a tsunami that devastated several coastal towns and even caused victims on the other side of the Pacific, in Japan, Hawaii and the Philippines. More than 2,000 people lost their lives as a result of the tremor, and the south of the country was devastated.
Also, the following graph shows that of the 15 strongest earthquakes in the world, 3 were in Chile.


<img src = 'https://github.com/Martu-t/grupo09_proyectogrupal/blob/main/Data%20Analytics/src/grafico_1.png' height = 350 >


Moreover, since 2000 in Latin America, the earthquakes by country, from largest to smallest, were: Chile in 2010, measuring 8.8 on the Richter scale; Peru in 2001, 8.4; Chile in 2015, 8.3; Chile in 2014, 8.3; Peru in 2007, 8.0. That is, 3 of the 5 strongest were in this country.

Chile is one of the countries most prone to earthquakes in the world, because it is in the so-called Belt, or "ring", of fire in the Pacific and a large part of its territory is exposed to the constant clash of the Nazca tectonic plate. and the South American plate. What causes subduction movements, previously explained.

Finally, having to carry out the project with the United States, Japan and the Latin American country of free choice, added to all the aforementioned characteristics, Chile was chosen, since it is located in a completely different territory from the previous ones (in another hemisphere , compared to the United States) and another continent and hemisphere relative to Japan.

This generates different geographical areas, different climates and different points on the world map, which is why, for example, Mexico was not chosen, since it is a neighboring country to the United States.

In this country and more precisely in a large part of its capital, Santiago de Chile, there is another important fault to consider, the San Ramón fault. This is closely studied by seismologists, who say that it represents a very strong threat to the metropolitan area, as it is close to large urban centers and that it could be a danger to the lives of millions of people, in addition to the large number of buildings that are find about it.

To conclude, it should be noted that even so (and no less important), the three countries belong to the Pacific ring of fire
 