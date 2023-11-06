import Projet
import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt 
df = Projet.Load_db().save_as_df()#data frame données météo
df.columns=['Date','Code Météo','Température Max','Température Min','Précipitations','Vitesse Max du vent','Direction dominante du vent']
ajd=datetime.today().strftime("%d %B %Y")
jp1=datetime.today()+timedelta(1)
jp1=jp1.strftime("%d %B %Y")
jp2=datetime.today()+timedelta(2)
jp2=jp2.strftime("%d %B %Y")
jp3=datetime.today()+timedelta(3)
jp3=jp3.strftime("%d %B %Y")
df['Date'][0]=ajd
df['Date'][1]=jp1
df['Date'][2]=jp2
df['Date'][3]=jp3
df=df.transpose()#meilleur affichage 
print(df)
fig, ax = plt.subplots(1,1)
ax.axis("tight")
ax.axis("off")
ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.transpose().columns, loc="center")
plt.show()# tableau d'affichage très sommaire