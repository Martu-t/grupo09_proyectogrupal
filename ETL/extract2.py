# import libraries
import geopandas as gpd 
import sqlalchemy as db
import psycopg2
from dotenv import load_dotenv
import datetime
import os

def extr():
    #Declare globar variable - credentials in .env to make it secure
    load_dotenv()
    database_username= os.getenv('DATABASE_USERNAME')
    database_password= os.getenv('DATABASE_PASSWORD')
    database_ip= os.getenv('DATABASE_IP')
    database_name=os.getenv('DATABASE_NAME')

    # Create connection and cursor
    database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
    connection = database_conection.raw_connection()
    cursor = connection.cursor()
    metadata=db.MetaData()

    # This query fetches the date and time for the most recent event registered in the main DB
    sql_query = """
    SELECT time FROM public.earthquake
    ORDER BY time DESC
    LIMIT 1;
    """
    res = database_conection.execute(sql_query).fetchall()
    connection.close()

    # Defining the query to bring data from USGS API; starttime => fetched result from before
    now = res[0][0]
    t = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'T'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

    # get data from the API and save as .csv
    query = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime='+t
    gdf = gpd.read_file(query)
    gdf.drop(gdf.tail(1).index, inplace=True) #eliminates last row because it will be duplicated in our DB
    gdf.to_csv('extracted1.csv', index=False)

extr()

