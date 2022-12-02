# %%
# THIS SCRIPT SETS THE TWITTER TABLE, GETTING IT READY TO LOAD INTO THE DB

# importing libraries
import pandas as pd
import numpy as np
import sqlalchemy as db
from geopy.distance import geodesic
import os
from dotenv import load_dotenv

# %%
# LOADING NEEDED DATAFRAMES
def twitter_csv():
    #1
    transf = pd.read_csv('transformed1.csv')
    #2
    clus =  pd.read_csv('clusterized.csv')

    load_dotenv()
    database_username= os.getenv('DATABASE_USERNAME')
    database_password= os.getenv('DATABASE_PASSWORD')
    database_ip= os.getenv('DATABASE_IP')
    database_name=os.getenv('DATABASE_NAME')
    database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
    connection = database_conection.raw_connection()
    #3
    city = pd.read_sql_query('SELECT id, poblacion, latitud, longitud FROM public.poblacion_chile',con=database_conection)
    connection.close()

    # selecting relevant features, into a new DataFrame
    data = pd.DataFrame()
    data[['id', 'mag', 'lat', 'lon']] = transf[['id', 'mag', 'lat', 'lon']]
    data['cluster'] = clus['cluster'] 

    # %%
    # SETTING GLOBAL VARIABLES

    # DECISION MATRIX, establishes classification boundaries
    # ---------------
    # ROWS:_________
    # row 0: [0-3) mag
    # row 1: [3-5) mag
    # row 2: [5-7) mag
    # row 3: [7+ mag 
    # ---------------
    # COLUMNS: ______
    # col 0: big city & short dist
    # col 1: big city & large dist
    # col 2: small city & large dist
    # col 3: small city & short dist

    r0 = 3 # mag limit for row 0
    r1 = 5 # mag limit for row 1
    r2 = 7 # mag limit for row 2

    big_city = 50 # Population limit [thousand habitants]
    large_dist = 250 # distance limit [km]


    decision_matrix = np.array([
        [0,  0,  0,  0],
        [2,  1,  0,  1],
        [2,  1,  1,  2],
        [3,  3,  2,  3]
    ])

    # DEFINITION RESULTS:_____
    # 0: Not informed
    # 1: Just an announcement
    # 2: Warning
    # 3: Alert

    # CHILEAN BOUNDARIES
    plus = 0.1
    max_lat = 90#-17.483 + plus
    min_lat = -90#-56.5366 - plus
    max_lon = 180#-66.4233 + plus
    min_lon = -180#-109.45833 - plus


    # M.L. MODEL clusters to keep
    k = [0, 2, 3]


    # %%
    # Filter DataFrame to keep rows within chilean boundaries
    data = data[(data['lat']>min_lat) & (data['lat']<max_lat) & (data['lon']>min_lon) & (data['lon']<max_lon)]

    # %%
    # Filter dataframe to discard non desired clusters
    data = data[data['cluster'].isin(k)]

    # %%
    # Defining functions to classify the remaining rows in the reporting scale established in the decision matrix.

    def city_class(x):
        '''
        Classifies the cities according to established population limit.
        returns 'chi' for smal cities; and 'gde' for big cities.
        '''
        if x < big_city:
            return 'chi'
        else:
            return 'gde'
            
    def row_result(x):
        '''
        Inputs the magnitude and returns the corresponding row in the decision matrix for that value.
        '''
        if x < r0:
            a = 0
        elif x < r1:
            a = 1
        elif x < r2:
            a = 2
        else:
            a = 3
        return a 


    def closest_city(lat,lon,city):
        '''
        Inputs a latitude and longitude defining a place; then returns a comma separated string with:
        a. id of the closest city.
        b. distance to the closest city.
        c. city size according to established criteria.
        '''
        a = city.loc[0,'id']
        b = 21000 # half the Earth's perimeter (max possible distance).
        c = city.loc[0,'size']

        for i in range (0,len(city)):
            try:
                aux = geodesic((lat,lon),(city.loc[i,'latitud'],city.loc[i,'longitud'])).kilometers
                if aux < b:
                    a = city.loc[i,'id']
                    b = aux
                    c = city.loc[i,'size']
            except:
                pass    

        return str(a)+','+str(round(b,2))+','+str(c)
        
    def col_result(dist, size):
        '''
        Inputs distance to the closest city and its size, 
        and returns the corresponding columns in the decision matrix for that combination of value.
        '''
        
        if size == 'gde':
            if dist < large_dist:
                col = 0
            else:
                col = 1
        else:
            if dist > large_dist:
                col = 2
            else:
                col = 3    
        return  col

    def final_class(row,col):
        '''
        Returns the final classification based on row-col of the decision matrix.
        '''
        return decision_matrix[row,col]

    # %%
    if len(data) > 0:
        city['size'] = city['poblacion'].apply(lambda x: city_class(x))
        data['row_result'] = data['mag'].apply(lambda x: row_result(x))
        data['id_ciudad'] = data.apply(lambda x: closest_city(x['lat'],x['lon'],city), axis =1)
        data[['id_ciudad', 'dist', 'size']] = data['id_ciudad'].str.split(',', expand=True)
        data['dist']=data['dist'].astype(float)
        data['col_result'] = data.apply(lambda x: col_result(x['dist'],x['size']), axis =1)
        data['final_class'] = data.apply(lambda x: final_class(x['row_result'],x['col_result']), axis =1)

    # %%
    data.reset_index(inplace=True)

    # %%
    twitter = pd.DataFrame()
    nan_series = pd.Series(np.nan, index = np.arange(len(data)))

    #twitter['id'] = nan_series
    twitter['id_terremotos'] =  data['id']
    twitter['fecha'] = nan_series
    twitter['clasificacion'] = data['final_class']
    twitter['id_ciudad'] = data['id_ciudad']
    twitter['distancia']= data['dist']

    # %%
    # Final filter, only upload to report events with final classification not equal to 0
    twitter_final = twitter[twitter['clasificacion']!=0]

    # %%
    # Export as csv
    twitter_final.to_csv('twitter.csv', index=False)

twitter_csv()

