# %%
#import Projet
import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt 
import os
import pooch
import pandas as pd
path_target=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "weather_data.csv"
)
path, fname_compressed = os.path.split(path_target)
url_db ='https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe%2FBerlin&format=csv'
pooch.retrieve(url=url_db, known_hash=None,path=path,fname=fname_compressed)
df=pd.read_csv(path +"/"+fname_compressed,skiprows=[0,1,2],converters={"time": str})
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
df=df.transpose()
fig = plt.figure(figsize=(10,10), dpi=300)
ax = plt.subplot()
ncols=df.shape[1]
nrows=df.shape[0]

ax.set_xlim(0, ncols + 1)
ax.set_ylim(0, nrows)

#df=df.transpose()

positions = [1, 2, 3, 4]
columns = df.columns

#ajout des données du tableau
for i in range(nrows):
    print(i)
    for j, column in enumerate(columns):
        print(i)
        ax.annotate(
            xy=(positions[j],(nrows-1)-i),
            text=df[column].iloc[i],
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

ax.set_axis_off()
plt.show
# %%
