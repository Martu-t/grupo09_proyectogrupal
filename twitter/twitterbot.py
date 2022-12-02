import tweepy
from dotenv import load_dotenv
import os
import sqlalchemy as db
import psycopg2
import datetime
import pandas as pd
import numpy as np
import time

load_dotenv()

#database credentials
database_username= os.getenv('DATABASE_USERNAME')
database_password= os.getenv('DATABASE_PASSWORD')
database_ip= os.getenv('DATABASE_IP')
database_name=os.getenv('DATABASE_NAME')

#Twitter API credentials
API_KEY =os.getenv('API_KEY')
API_SECRET =os.getenv('API_SECRET')
ACCESS_TOKEN= os.getenv('ACCESS_TOKEN')
ACCESS_SECRET=os.getenv('ACCESS_SECRET')

#Auth for twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

'''
def getdata():
    database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
    connection = database_conection.raw_connection()
    metadata=db.MetaData()
    cursor = connection.cursor()
    df = pd.read_sql_query('SELECT p.nombre, t.id, t.id_terremotos, t.fecha, t.clasificacion, t.id_ciudad, t.distancia FROM public.poblacion_chile as p JOIN public.twitter as t ON t.id_ciudad = p.id WHERE fecha is null',con=database_conection)
    connection.close()
    return df
'''

# twitter functions
def ObtenerUsuario(user_name):
    return api.get_user(screen_name=user_name)
def PublicarTweet(message):
    api.update_status(status=message)

def ObtenerTweetsDeUsuario(user_name, number_of_tweets):
    tweets = api.user_timeline(screen_name=user_name, count=number_of_tweets)
    return tweets

def ObtenerSeguidoresDeUsuario(user_name, number_of_followers):
    return tweepy.Cursor(method=api.get_followers, screen_name=user_name).items(number_of_followers)

def getdata():
    database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
    connection = database_conection.raw_connection()
    metadata=db.MetaData()
    cursor = connection.cursor()
    df = pd.read_sql_query('SELECT p.nombre, t.id, t.id_terremotos, t.fecha, t.clasificacion, t.id_ciudad, t.distancia FROM public.poblacion_chile as p JOIN public.twitter as t ON t.id_ciudad = p.id WHERE fecha is null',con=database_conection)
    connection.close()
    df1 = df[df['clasificacion'] == 1]
    df2 = df[df['clasificacion'] == 2]
    df3 = df[df['clasificacion'] == 3]
    return df1, df2, df3

def tweet_alerta1():
    mundo = '\U0001F30F'
    ginio = '\U0001F61C'
    green = '\U0000274E'

    df1 =  getdata()[0]
    #df1 = getdata()[0]
    for i in range(len(df1)):
        id_terremoto = (df1.iloc[i]['id_terremotos'])
        ciudad = (df1.iloc[i]['nombre'])
        dist = (df1.iloc[i]['distancia'])
        alerta_verde = f'TEST. {green} ¿Lo sentiste? No estás loco/a! Sismo leve a {dist} km de {ciudad}. No te preocupes. La tierra {mundo} solo se está acomodando {ginio}'
        PublicarTweet(alerta_verde)
        print(f'Se ha emitido el Tweet del terremoto con id: {id_terremoto}')
        

def tweet_alerta2():
    alert = '\U00002757'
    auto = '\U0001F697'
    no = '\U0001F6AB'
    caminar = '\U0001F6B6'
    df2 =  getdata()[1]
    for i in range(len(df2)):
        id_terremoto = (df2.iloc[i]['id_terremotos'])
        ciudad = (df2.iloc[i]['nombre'])
        dist = (df2.iloc[i]['distancia'])
        alerta_naranja = f'''{alert} Quedate donde estás. Sismo medio a {dist} km de {ciudad}.
        El manejo de vehículos {auto} no es seguro {no} y podés tener dificultad de mantenerte en pie{caminar}. 
        Si estás en un vehiculo, detente. Agáchate, Cubrite y agarrate. Alejarse de muebles y ventanas. 
        Tranquilo, ya pasará.'''
        PublicarTweet(alerta_naranja)
        print(f'Se ha emitido el Tweet del terremoto con id: {id_terremoto}')

def tweet_alerta3():
    casa = '\U0001F3E1'
    alerta = '\U0001F6A8'
    ojos = '\U0001F440'
    megafono = '\U0001F4E2'
    soon = '\U0001F51C'
    df3 =  getdata()[2]
    for i in range(len(df3)):
        id_terremoto = (df3.iloc[i]['id_terremotos'])
        ciudad = (df3.iloc[i]['nombre'])
        dist = (df3.iloc[i]['distancia'])
        alerta_roja = f'{alerta} PRUEBA Alerta máxima. Atención{ojos}. Sismo importante a {dist} de {ciudad}. Importante agacharse, cubrirse la cabeza y agarrarte a algo. Atento a las estructuras {casa}. Tu perspectiva quedará distorsionada. Es normal. Algunos servicios sin funcionamiento. Atento/a a futuras réplicas{soon}'
        PublicarTweet(alerta_roja)  
        print(f'Se ha emitido el Tweet del terremoto con id: {id_terremoto}')

def updatetime():
    # This query fetches the 20 latest id from database
    database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
    connection = database_conection.raw_connection()
    metadata=db.MetaData()
    cursor = connection.cursor()
    sql_query = """
    UPDATE public.twitter
    SET fecha = current_timestamp
    WHERE fecha is null;
    """
    database_conection.execute(sql_query)
    connection.close()

while True:
    tweet_alerta1()
    time.sleep(3)
    tweet_alerta2()
    time.sleep(3)
    tweet_alerta3()
    updatetime()
    time.sleep(3600)