# import libraries
import pandas as pd
import numpy as np
import sqlalchemy as db
from dotenv import load_dotenv
import datetime
import os


def loader():

    df = pd.read_csv('transformed1.csv')
    df2 = pd.read_csv('clusterized.csv')


    def load(df, table_name):
        '''
        This function make the incremental load into a postgress database. 
        The args would be a dataframe and a table name that should be pass as string
        '''
        load_dotenv()
        database_username= os.getenv('DATABASE_USERNAME')
        database_password= os.getenv('DATABASE_PASSWORD')
        database_ip= os.getenv('DATABASE_IP')
        database_name=os.getenv('DATABASE_NAME')
    
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

    #ejecuta las cargas
    load(df, 'earthquake')
    load(df2, 'cluster')

loader()
