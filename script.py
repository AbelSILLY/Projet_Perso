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
import shutil
import requests
#%%
# IMPORT DES DONNEES:
#### météo ####
path_target=os.path.join(
    os.path.dirname(os.path.realpath(__file__)),'Projet', "data", "weather_data.csv"
)
path, fname_compressed = os.path.split(path_target)
url_db ='https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&format=csv'
data = requests.get(url_db)
with open("./Projet/data/weather.csv",'w') as output_file:
    output_file.write(data.text)

df=pd.read_csv(
     "./Projet/data/weather.csv",skiprows=[0,1,2],
     converters={"time": str, 'weather_code (wmo code)':str,'temperature_2m_max (Â°C)':str,'temperature_2m_min (Â°C)':str,'precipitation_sum (mm)':str,'wind_speed_10m_max (km/h)':str},
     encoding="unicode_escape"
     )
#%%
##### json des icones #####
path_target_im=os.path.join(
    os.path.dirname(os.path.realpath(__file__)),'Projet', "data", "im.json"
)
path_im, fname_compressed_im = os.path.split(path_target_im)
url_im = "https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json"
pooch.retrieve(url=url_im, known_hash=None,path=path_im,fname=fname_compressed_im) #import du fichier image
with open(path_im +"/"+fname_compressed_im) as f:
     data = json.load(f)

# %%
def dl_ic(df,data,i, fname):
    '''
    Cette fonction télécharge l'icone (format png) de la météo du jour i.
    Args:
        df (data_frame): data frame contenant les infos météo
        data (bibliothèque python): biblio python relative au fichier json contenant l'url des images
        i (int): l'indice où ce situe le code météo dans df
        fname (str): nom du fichier image
    '''
    code=df[i].iloc[0]
    url=data[code]['day']['image']
    im=requests.get(url,stream=True)
    with open("./Projet/data/"+fname,"wb") as output_image:
         im.raw.decode_content=True
         shutil.copyfileobj(im.raw,output_image)

# %%
def date(df,i,fname):
    '''
    Télécharge une image (format svg) affichant la température max du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        path (str or path-like object): chemin où stocker l'image
        fname (str or path-like object): nom de l'image
    '''
    plt.ioff()
    fig = plt.figure(figsize=(1,0.5),dpi=100,frameon=False)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[0],
    ha='center',
    va='center',
    )
    ax.set_axis_off()
    plt.savefig("./Projet/data/" + fname,format='svg',dpi=100)
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
    plt.ioff()
    fig = plt.figure(figsize=(1,0.5),dpi=100,frameon=False)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[1],
    ha='center',
    va='center',
    )
    ax.set_axis_off()
    plt.savefig("./Projet/data/" + fname,format='svg',dpi=100)
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
    plt.ioff()
    fig = plt.figure(figsize=(1,0.5),dpi=100,frameon=False)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[2],
    ha='center',
    va='center',
    )
    ax.set_axis_off()
    plt.savefig("./Projet/data/" + fname,format='svg',dpi=100)
#%%
def pluie(df,i,fname):
    '''
    Télécharge une image (format svg) affichant la pluie du jour i.
    Args:
        df (dataframe): datframe des données météo
        i (int): indice du jour
        fname (str or path-like object): nom de l'image
    '''
    plt.ioff()
    fig = plt.figure(figsize=(1,0.5), dpi=100,frameon=False)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[3],
    ha='center',
    va='center',
    )
    ax.set_axis_off()
    plt.savefig("./Projet/data/" + fname,format='svg',dpi=100)
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
    plt.ioff()
    fig = plt.figure(figsize=(1,0.5), dpi=100,frameon=False)
    ax = plt.subplot()
    ax.annotate(
    xy=(0.5,0.5),
    text=df[i].iloc[4],
    ha='center',
    va='center',
    )
    ax.set_axis_off()
    plt.savefig("./Projet/data/" + fname,format='svg',dpi=100)
# %%
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
### Modif Température ###
df['Température Max']+='°C'
df['Température Min']+='°C'
### Modif Précipitations
df['Précipitations']+=' mm'
### Modif Vent ###
df['Vitesse Max du vent']+=' km/h'
# %%
df2=df.drop(columns='Date')
df2=df2.transpose()
df=df.transpose()
# %%
######## "EXTRACTION" DES DONNEES DU TABLEAU ########
##### Code météo #####
for i in range(4):
    dl_ic(df2,data,i,'im_j'+str(i)+'.png')

##### Date #####
for i in range(4):
    date(df,i,'date_j'+str(i)+'.svg')

##### Température Max #####
for i in range(4):
    temp_max(df2,i,'tempmax_j'+str(i)+'.svg')

##### Température Min #####
for i in range(4):
    temp_min(df2,i,'tempmin_j'+str(i)+'.svg')

##### Pluie #####
for i in range(4):
    pluie(df2,i,'pluie_j'+str(i)+'.svg')

##### Vent #####
for i in range(4):
    vent(df2,i,'vent_j'+str(i)+'.svg')