
# Librerías
import pandas as pd
import numpy as np
from datetime import datetime

# importo a DataFrame
#defino data como variable global?
data = pd.read_csv('../USGS_events_2010-01-01_2022-11-01.csv') #puse relative path lo tenía en otra carpeta

# read dataset  
# def read_csv(path):
#    data = pd.read_csv(path)
#    return data
# esto no va, ya está hecho arriba


def NormMag(df):
    df.loc[df['mag'] < (-1.5), 'mag'] = (-1.5)
    df['mag'] = df['mag'].fillna(1.32)  #(dfc['mag'].median())
    return df

def NormDate(x):
    x = pd.to_datetime(x, unit='ms')
    return x
# hay q aplicarla a 2 columnas

def NormStatus(x):
    x = x.str.lower()
    #df['status'] = df['status'].apply(str.lower)
    return x

# def NormNst(x):
#    x = x.fillna(1)
#    return x
# la hago abajo con dataframe idem las otras, pq faltaba imputarle los outliers a esta

def NormNst(df):
    df.loc[df['nst'] > (100), 'nst'] = (100)
    df['nst'] = df['nst'].fillna(1)
    return df


# def NormDmi(x):
#     x = x.fillna(7.1)
#     return x
# esta abajo de nuevo la misma columna

def NormDmin(df):
    df.loc[df[df['dmin'] > (0.154)].index, 'dmin'] = (0.154)
    df['dmin'] = df['dmin'].fillna(0.0587)
    return df

# we use the max typical value for outliers: https://earthquake.usgs.gov/data/comcat/
def NormRms(df):
    df.loc[df['rms'] > (1.39), 'rms'] = (1.39)
    df['rms'] = df['rms'].fillna(0.18)
    return df

def NormGap(df):
    df.loc[df['gap'] > (180), 'gap'] = (180)
    df['gap'] = df['gap'].fillna(110)
    return df

def col_type(x):
    '''
    This function inputs the 'type' column and returns a normalized 'type' column.
    '''
    x = x.str.lower()
    x = x.str.strip()
    x = x.str.replace('chemical explosion', 'explosion')
    x = x.str.replace('accidental explosion', 'explosion')
    x = x.str.replace('nuclear explosion', 'explosion')
    x = x.str.replace('mining explosion', 'explosion')
    x = x.str.replace('experimental explosion', 'explosion')
    x = x.str.replace('quarry blast', 'quarry')
    x = x.str.replace('rock burst', 'quarry')
    x = x.str.replace('sonicboom', 'other event')
    x = x.str.replace('acoustic noise', 'other event')
    x = x.str.replace('sonic boom', 'other event')
    x = x.str.replace('rockslide', 'other event')
    x = x.str.replace('landslide', 'other event')
    x = x.str.replace('mine collapse', 'other event')
    x = x.str.replace('collapse', 'other event')
    x = x.str.replace('building collapse', 'other event')
    x = x.str.replace('meteorite', 'other event')
    x = x.str.replace('not reported', 'other event')
    x = x.str.replace('induced or triggered event', 'other event')
    return x    

def col_geometry(pdseries):
    '''
    This function inputs a pandas series, which refers to a geometry column in POINT Z format; and
    returns 3 pandas series, one for each coordinate.
    '''
    new = pdseries.str.split(' ', expand=True)
    new[2]=new[2].apply(lambda x: str(x).replace('(',''))
    new[4]=new[4].apply(lambda x: str(x).replace(')',''))
    x = new[2].astype(float)
    y = new[3].astype(float)
    z = new[4].astype(float)

    return x, y, z


def delete_col(df):
    '''
    Takes as arg a df and deliminate specific columns with pandas
    '''
    df = df.drop(['url', 'detail', 'tz', 'alert','title','geometry'], axis=1) 
    #agregué geometry, pq no se si va a haber problemas para cargarlo dps a la base
    #agregué title
    return df


# inicio el bloque de aplicación de las funciones
data = NormMag(data)
print('mag OK')
data['time'] = NormDate(data['time'])
print('time OK')
data['updated'] = NormDate(data['updated'])
print('updated OK')
data['status'] = NormStatus(data['status'])
print('status OK')
data = NormNst(data)
print('nst OK')
data = NormDmin(data)
print('dmin OK')
data = NormRms(data)
print('rms OK')
data = NormGap(data)
print('gap OK')
data['type'] = col_type(data['type'])
print('type OK')
data['lon'], data['lat'], data['depth'] = col_geometry(data['geometry'])
print('lat lon depth OK')
data = delete_col(data)
print('drop column OK')

print('Exporting')
# Export
data.to_parquet('USGS_transformed.parquet',index=False)
print('Export OK')






