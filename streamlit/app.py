import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
#from folium.plugins import HeatMap
from datetime import datetime

#columns

# import libraries
import sqlalchemy as db
from dotenv import load_dotenv
import datetime
import os

load_dotenv()
database_username= os.getenv('DATABASE_USERNAME')
database_password= os.getenv('DATABASE_PASSWORD')
database_ip= os.getenv('DATABASE_IP')
database_name=os.getenv('DATABASE_NAME')


#def getdata():
database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
connection = database_conection.raw_connection()
metadata=db.MetaData()
cursor = connection.cursor()
df = pd.read_sql_query('SELECT mag, place, time, type, depth, lon, lat FROM public.earthquake ORDER BY time DESC LIMIT 5000;',con=database_conection)
connection.close()
df = df.dropna()
chile = df[df['place'].str.contains('Chile')]
chile[['date', 'time_only']] = chile['time'].apply(lambda x: pd.Series(str(x).split(' ')))
    #return chile

#fields = ['mag', 'place', 'time', 'depth', 'lon', 'lat']
#earthquake = pd.read_parquet('USGS_transformed2.parquet', engine='pyarrow') #usecols = fields)
#earthquake.dropna(inplace=True)
#earthquake = pd.read_csv('/Users/marthatarantino/Desktop/henry/streamlit/transformed1.csv', usecols = fields)

def generate_color(magnitude):
        if magnitude <= 4:
            c_outline, c_fill = '#4a7a1c', '#4a7a1c'
            m_opacity, f_opacity = 0.9, 0.7
        elif magnitude <= 5:
            c_outline, c_fill = '#e89638', '#e89638'
            m_opacity, f_opacity = 0.9, 0.7
        else:
            c_outline, c_fill = '#c0392b', '#e74c3c'
            m_opacity, f_opacity = 1, 1
        return c_outline, c_fill, m_opacity, f_opacity

def generate_popup(magnitude, depth, time_only):
    return f'''<strong>Magnitude:</strong> {magnitude}<br><strong>Depth:</strong> {depth} km <br><strong>Time:</strong> {time_only}'''    

def main_page():
    #getdata()
    st.markdown("Bienvenidos")
    st.subheader('Sistema de alertas sísmico')
    st.write('****')

    st.title('Datos de los últimos terremotos en Chile')
    if st.checkbox('Ver tabla completa'):
        st.dataframe(chile)

    if st.checkbox('Ver ultimos 5 sismos'):
        if st.button('show head'):
            st.write(chile.head())
        #if st.button('show tail'):
            #st.write(chile.tail())

    st.subheader('Conocé nuestros datos')
    df_dim = st.radio('Seleccionar dimensión:', ('Filas', 'Columnas', 'Ambas'), horizontal=True)

    if df_dim == 'Filas':
        st.write('Total de Filas:', chile.shape[0])

    if df_dim == 'Columnas':
        st.write('Total de columnas:', chile.shape[1])

    if df_dim == 'Ambas':
        st.write('Total Filas', chile.shape[0], 'Total de Columas:', chile.shape[1])
    
    st.write('****')

    st.subheader('Mapa de últimos sismos en Chile')
    st.write('En el mapa se pueden visualizar los últimos sismos en la región de Chile')
    st.write('Se puede elegir un filtro por magnitud y/o fecha para una búsquda acotada.')
    st.write('Por defecto se muestra todo')
    mag_max = st.slider('Max Magnitud', 0, 10, 9)
    start_date = st.date_input("Start Date", value=pd.to_datetime(chile['date'].iloc[-1], format="%Y-%m-%d"))
    end_date = st.date_input("End Date", value=pd.to_datetime(chile['date'].iloc[1], format="%Y-%m-%d"))

    # convert the dates to string
    start_d = start_date.strftime("%Y-%m-%d")
    end_d = end_date.strftime("%Y-%m-%d")

    #st.sidebar.slider('Dates', value=datetime(chile['time'].iloc[1]))#, chile['date'].iloc[-1])
    if st.checkbox('Show Map', value=True):

        #zoom_starts = st.sidebar.slider('Zoom del mapa', 3,15,5)
        quake_map = folium.Map(
        location=[-35.675147, -71.542969],
        zoom_start=5,
        tiles='Stamen Terrain',
        width=1024,
        height=600
    )
    chile2 = chile.loc[((chile['date'] >= start_d) & (chile['date'] <= end_d )) & (chile['mag']<=mag_max)]

    for _, row in chile2.iterrows():
        c_outline, c_fill, m_opacity, f_opacity = generate_color(row['mag'])
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            popup=generate_popup(row['mag'], row['depth'], row['time_only']),
            color=c_outline,
            fill=True,
            fillColor=c_fill,
            opacity=m_opacity,
            fillOpacity=f_opacity,
            radius=(row['mag'] ** 3) / 5
        ).add_to(quake_map)
    quake_map

    st.subheader('Sobre la visualización')
    st.markdown('''
    En el mapa se pueden ver los últimos sismos del país de Chile y alrededores.
    Los círculos están representados con colores, según la magnitud del mismo, siendo:
    - Verde: Sismos con magnitudes menores a 4
    - Naranja: Sismos con magnitudes menores entre 4 y 5
    - Rojo: Sismos con magnitudes menores a 5
    ''')

def about():
    st.markdown("Bienvenidos")
    st.subheader('Sistema de alertas sísmico')
    st.write('****')
    st.sidebar.markdown('''

    Contenido:

    * :information_source: En la sección "I. Sobre nosotros" vas a conocer un poco sobre nuestro trabajo
    
    * :flag-cl: En la sección de "II. Mapa" vas a ver los últimos registros sobre sismos significativos de Chile. 
''')

    st.markdown('''
    Somos un equipo enfocado en convertir datos en información útil para la sociedad.
    A tráves de este proyecto buscamos informar a la población sobre sismos ocurridos recientemente. 
    Para lograrlo contamos con un módelo de Machile Learning que nos ayuda a clasificar ágilmente aqullos eventos más significativos.
    También disponemos de un Twiiter donde informamos de dichos eventos y nuestras recomendaciones particulares. ''')
    st.markdown('''Recomendamos seguirnos para poder acceder a la información en tiempo real [Twitter](https://twitter.com/alertas_sismos) ''')
    st.markdown('''Además nuestro código está disponible en nuestro repositorio de [GitHub del proyecto](hhttps://github.com/Martu-t/grupo09_proyectogrupal)
    ''')

    st.write('****')
    st.subheader('Nuestras recomendaciones generales')
    st.markdown('''
    En caso de sismos es importante:
    - Mantener calma y ubicarse en lugares de “protección sísmica”: es decir, debajo de un elemento firme y, si ello no fuera posible, junto al mismo.
    - Cortar la energía eléctrica y cerrar las llaves de paso de agua y gas.
    - Alejarse de los objetos que puedan caerse, deslizarse o quebrarse, como vidrios, espejos o muebles.
    ''')
    

page_names_to_funcs = {
    'I. Sobre nosotros': about,
    'II. Mapa Chile': main_page
}

selected_page = st.sidebar.selectbox("Elija la página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()











footer="""<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: blue;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Seguinos en <a style='display: inline-block; text-align: center;' href="https://twitter.com/alertas_sismos/" target="_blank">Twitter</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


#st.write('## Seguinos en las redes')
#st.markdown(''' * [Twitter](https://twitter.com/alertas_sismos) ''')
#st.markdown(''' * [GitHub del proyecto](hhttps://github.com/Martu-t/grupo09_proyectogrupal) ''')
