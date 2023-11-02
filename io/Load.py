import pooch
import pandas as pd
#%%
weather_path=pooch.retrieve(url="https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin&format=csv"
                            ,known_hash=None,fname="weather.csv",path="~/OneDrive/Bureau/HAX712X/Projet_Perso/data")
#%%
