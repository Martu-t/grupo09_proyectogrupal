import pandas as pd
import joblib

def clusterize():
    data = pd.read_csv('transformed1.csv')
    dataml = data[['mag', 'tsunami', 'type', 'depth', 'dist']]
    pre = joblib.load('model/pre.pkl')
    clf = joblib.load('model/km_4.pkl')
    dataml = pre.transform(dataml)
    clus = clf.predict(dataml)
    clusters = pd.DataFrame()
    clusters['id_terremotos'], clusters['cluster'] = data['id'], clus
    clusters.to_csv('clusterized.csv', index=False)

clusterize()
