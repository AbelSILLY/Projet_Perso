# %%
#import Projet
import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt 
import os
import pooch
import pandas as pd
import json
from PIL import Image
import urllib

# IMPORT DES DONNEES:
#### météo ####
path_target=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "weather_data.csv"
)
path, fname_compressed = os.path.split(path_target)
url_db ='https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe%2FBerlin&format=csv'
pooch.retrieve(url=url_db, known_hash='9b26b817be45aca3f5bbf634307fad7f107b2e34803125c09da522be0c55a691',path=path,fname=fname_compressed)
df=pd.read_csv(
     path +"/"+fname_compressed,skiprows=[0,1,2],
     converters={"time": str, 'weather_code (wmo code)':str,'temperature_2m_max (°C)':str,'temperature_2m_min (°C)':str,'precipitation_sum (mm)':str,'wind_speed_10m_max (km/h)':str}
     )
print(df)
##### json des icones #####
path_target_im=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "im.json"
)
path_im, fname_compressed_im = os.path.split(path_target_im)
url_im = "https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json"
pooch.retrieve(url=url_im, known_hash=None,path=path_im,fname=fname_compressed_im) #import du fichier image
with open(path_im +"/"+fname_compressed_im) as f:
     data = json.load(f)
# %%
def icon_dl(data,path,fname):
     '''
     Télécharge l'icone soleil de la météo
     Args:
        data ("json"): une bibliothèque python contenant le fichier json relatif au weathercode
        path (str): le chemin où l'on va stocker l'image
        fname (str): nom du fichier
     '''
     url=data['0']['day']['image']
     pooch.retrieve(url=url,known_hash=None,path=path,fname=fname)
# %%
def dl_ic(df,data,i,path, fname):
    '''
    Cette fonction télécharge l'icone (format png) de la météo du jour.
    Args:
        df (data_frame): data frame contenant les infos météo
        data (bibliothèque python): biblio python relative au fichier json contenant l'url des images
        i (int): l'indice où ce situe le code météo dans df
        path (str or path-like object): chemin où stocker l'image
        fname (str): nom du fichier image
    '''
    code=df[i].iloc[0]
    url=data[code]['day']['image']
    pooch.retrieve(url,path=path,fname=fname,known_hash=None)

#%%
path_target_ic=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "icone.png"
)
path_ic, fname_compressed_ic = os.path.split(path_target_ic)
icon_dl(data=data,path=path_ic,fname=fname_compressed_ic)
# %%
df
df.columns=['Date','Code Météo','Température Max','Température Min','Précipitations','Vitesse Max du vent']
ajd=datetime.today().strftime("%d %B %Y")#date d'aujourd'hui au bon format
jp1=datetime.today()+timedelta(1)#date de demain
jp1=jp1.strftime("%d %B %Y")#date de demain au bon format
jp2=datetime.today()+timedelta(2)
jp2=jp2.strftime("%d %B %Y")
jp3=datetime.today()+timedelta(3)
jp3=jp3.strftime("%d %B %Y")
df['Date'][0]=ajd #je remplace dans mon data frame les dates avec le bon format
df['Date'][1]=jp1
df['Date'][2]=jp2
df['Date'][3]=jp3
df
### Modif Température ###
df['Température Max']+='°C'
df['Température Min']+='°C'
### Modif Précipitations
df['Précipitations']+=' mm'
### Modif Vent ###
df['Vitesse Max du vent']+=' km/h'
df
# %%
df2=df.drop(columns='Date')
df2=df2.transpose()
df=df.transpose()
df2
# %%
############ Import des images de la météo ############
path_target_im=os.path.join(
    os.path.dirname(os.path.realpath(__file__)),"Projet", "data", "im_j0.png"
    )
path_im, fname_im = os.path.split(path_target_im)
dl_ic(df=df2,data=data,i=0,path=path_im,fname=fname_im)
# %%
def temp_max(df,i,fname):
    '''
    Télécharge une image (format svg) affichant la température max du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        path (str or path-like object): chemin où stocker l'image
        fname (str or path-like object): nom de l'image
    '''
    fig = plt.figure(figsize=(0.5,0.5), dpi=100)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[1],
    ha='center',
    va='center',
    #weight='bold'
    )
    ax.set_axis_off()
    plt.show
    plt.savefig(fname,format='svg',dpi=100)
# %%
def temp_min(df,i,fname):
    '''
    Télécharge une image (format svg) affichant la température min du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        path (str or path-like object): chemin où stocker l'image
        fname (str or path-like object): nom de l'image
    '''
    fig = plt.figure(figsize=(0.5,0.5), dpi=100)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[2],
    ha='center',
    va='center',
    #weight='bold'
    )
    ax.set_axis_off()
    plt.show
    plt.savefig(fname,format='svg',dpi=100)
#%%
def pluie(df,i,fname):
    '''
    Télécharge une image (format svg) affichant la pluie du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        path (str or path-like object): chemin où stocker l'image
        fname (str or path-like object): nom de l'image
    '''
    fig = plt.figure(figsize=(0.5,0.5), dpi=100)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[3],
    ha='center',
    va='center',
    #weight='bold'
    )
    ax.set_axis_off()
    plt.show
    plt.savefig(fname,format='svg',dpi=100)
#%%
def vent(df,i,fname):
    '''
    Télécharge une image (format svg) affichant le vent du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        path (str or path-like object): chemin où stocker l'image
        fname (str or path-like object): nom de l'image
    '''
    fig = plt.figure(figsize=(0.5,0.5), dpi=100)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[5],
    ha='center',
    va='center',
    #weight='bold'
    )
    ax.set_axis_off()
    plt.show
    plt.savefig(fname,format='svg',dpi=100)