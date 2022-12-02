# import libraries
import pandas as pd
import numpy as np
import sqlalchemy as db
from dotenv import load_dotenv
import datetime
import os


def loader():

    df = pd.read_csv('transformed1.csv') 

    load_dotenv()
    database_username= os.getenv('DATABASE_USERNAME')
    database_password= os.getenv('DATABASE_PASSWORD')
    database_ip= os.getenv('DATABASE_IP')
    database_name=os.getenv('DATABASE_NAME')


    def fetch_id():
        # This query fetches the 20 latest id from database
        database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
        connection = database_conection.raw_connection()
        metadata=db.MetaData()
        cursor = connection.cursor()
        sql_query = """
        SELECT id FROM public.earthquake
        ORDER BY time DESC
        LIMIT 20;
        """
        res = database_conection.execute(sql_query).fetchall()
        #print('fetching ids from database')
        connection.close()

        return res

    def list_id(res):
        list = []
        n = 0
        for i in range(20):
            list.append(res[n][0])
            n = n + 1    
        return list

    def df_checked(df):
        '''
        This funtion takes a df as argument. 
        First will make a list with the last 20 ids from database (using function list_id)
        and then will compare thoses id with the df and created a new (filter) dataframe only with ids that are not in the database
        '''
        print('fetching ids from database')
        ids = list_id(fetch_id())
        df_actual = df[~df.id.isin(ids)]
        print('generation new filtered dataframe')
        return df_actual

    def load(df, table_name):
        '''
        This function make the incremental load into a postgress database. 
        The args would be a dataframe and a table name that should be pass as string
        '''
        #database_conection = db.create_engine(f"mysql+pymysql://{database_username}:{database_password}@{database_ip}/{database_name}")
        database_conection=db.create_engine(f"postgresql://{database_username}:{database_password}@{database_ip}/{database_name}")
        connection = database_conection.raw_connection()
        #cursor = connection.cursor()
        metadata=db.MetaData()

        try:
            df.to_sql(table_name, database_conection, index=False, if_exists='append')
            print("conection open")
            print(f'data succesfully add to {table_name} table')
        except Exception as e:
            print("Has been a error with database conection")
            print(e)

        connection.close()
        print("The conection has been closed")

    #executa la función de carga
    load(df_checked(df), 'earthquake')

loader()
