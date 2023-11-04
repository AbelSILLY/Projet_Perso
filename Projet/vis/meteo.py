# %%
import sys
print(sys.path)
sys.path.append('C:\\Users\\abels\\OneDrive\\Bureau\\HAX712X\\Projet_Perso')
import pooch
import pandas as pd
import os
import matplotlib.pyplot as plt
import calendar
from Projet.io import Load
# %%
df_weather=Load.df_weather_raw #plus facile à manipuler
print(df_weather)
plt.plot(df_weather["Date"],df_weather["Température Max"]) #test
plt.xlabel("Date")
plt.ylabel("Température en °C")
plt.show()
# %%

df_weather["Date"][0]
# %%
df_weather2=df_weather.transpose() #meilleur affichage
df_weather2