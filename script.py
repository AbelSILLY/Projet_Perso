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
path_target=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "weather_data.csv"
)
path, fname_compressed = os.path.split(path_target)
url_db ='https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe%2FBerlin&format=csv'
pooch.retrieve(url=url_db, known_hash='169686be5d07b0aedab11e33a575d3387e5e39f7b942b7c4d3df88f179d70c3a',path=path,fname=fname_compressed)
df=pd.read_csv(path +"/"+fname_compressed,skiprows=[0,1,2],converters={"time": str, 'weather_code (wmo code)':str})
print(df)
path_target_im=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "im.json"
)
path_im, fname_compressed_im = os.path.split(path_target_im)
url_im = "https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json"
pooch.retrieve(url=url_im, known_hash=None,path=path_im,fname=fname_compressed_im) #import du fichier image
with open(path_im +"/"+fname_compressed_im) as f:
     data = json.load(f)

# %% 
def ax_icon(data,ax):
    '''
    Plots the weather icon at a specific axes.
    Args:
        data ("json"): une bibliothèque python contenant le fichier json relatif au weathercode
        ax (object): the matplotlib axes where we'll draw the image.
    '''
    weather_icon = Image.open(urllib.request.urlopen(data['0']['day']['image']))
    ax.imshow(weather_icon)
    ax.axis('off')
    return ax

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
    code=str(df[i].iloc[1])
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
# %%
df2=df.drop(columns='Date')
df2=df2.transpose()
df=df.transpose()
fig = plt.figure(figsize=(10,7), dpi=300)
ax = plt.subplot()
ncols=df2.shape[1]
nrows=df2.shape[0]

ax.set_xlim(0, ncols + 1)
ax.set_ylim(0, nrows)

#df=df.transpose()

positions = [0.5, 2, 3.5, 5]
columns = df2.columns

#ajout des données du tableau
for i in range(nrows):
#    print(i)
    for j, column in enumerate(columns):
#        print(i)
        ax.annotate(
            xy=(positions[j],(nrows)-(i + .5)),
            text=df2[column].iloc[i],
            ha='center',
            va='center'
        )


#ajout des noms des colonnes
df1=df.transpose()
col_names=df1['Date']
for index, c in enumerate(col_names):
        ax.annotate(
            xy=(positions[index], nrows),
            text=col_names[index],
            ha='center',
            va='bottom',
            weight='bold'
        )

# Ajout de lignes dans le tableau
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [nrows, nrows], lw=1.5, color='black', marker='', zorder=4)
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [0, 0], lw=1.5, color='black', marker='', zorder=4)
for x in range(1, nrows):
    ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [x, x], lw=1.5, color='gray', ls=':', zorder=3 , marker='')

ax.set_axis_off()

# -- Transformation functions
DC_to_FC = ax.transData.transform
FC_to_NFC = fig.transFigure.inverted().transform
# -- Take data coordinates and transform them to normalized figure coordinates
DC_to_NFC = lambda x: FC_to_NFC(DC_to_FC(x))
ax_point_1 = DC_to_NFC([0.25, 0.25])
ax_point_2 = DC_to_NFC([2.75, 0.75])
ax_width = abs(ax_point_1[0] - ax_point_2[0])
ax_height = abs(ax_point_1[1] - ax_point_2[1])
ax_coords=DC_to_NFC([1,1])

#ax_coords=DC_to_NFC([-0.75,4.25])
#flag_ax=fig.add_axes(
#    [ax_coords[0],ax_coords[1],ax_width,ax_height]
#)
#ax_icon(data,flag_ax)


for x in range(0,nrows-1):
     ax_coords=DC_to_NFC([2*x-0.75,4.25])
     flag_ax=fig.add_axes(
          [ax_coords[0],ax_coords[1],ax_width,ax_height]
     )
     ax_icon(data,flag_ax)
plt.show
#faire un ajout un à un ?
# %%
