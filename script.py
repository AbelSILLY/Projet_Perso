import Projet
df = Projet.Load_db().save_as_df()#data frame données météo
df.columns=['Date','Température Max','Température Min','Levé du soleil','Couché du soleil','Neige','Heure de pluie','Vitesse Max du vent','Direction dominante du vent']
print(df)