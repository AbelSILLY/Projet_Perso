# %%
import pooch
import pandas as pd
import os
import matplotlib.pyplot as plt
#%%
#weather_path=pooch.retrieve(url="https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin&format=csv"
#                            ,known_hash=None,fname="weather.csv",path="~/OneDrive/Bureau/HAX712X/Projet_Perso/data")


# %%
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=rain,cloudcover&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,windspeed_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin&format=csv"
path_target = "./data/weather.csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)
#%%
df_weather_raw=pd.read_csv("weather.csv",skiprows=[0,1,2,3,4])#data frame daily weather
df_weather_raw.columns=["Date","Température Max","Température Min","Précipitation","Neige","Vitesse Max du vent","Direction de vent dominante"]
df_weather_raw.head()
# %%
df_cwweather_raw=pd.read_csv("weather.csv",skiprows=[0,1,2,5,6,7,8,9,10,11]) #data frame current weather
df_cwweather_raw
# %%
