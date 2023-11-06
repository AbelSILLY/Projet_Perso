import os

url_db = "https://api.open-meteo.com/v1/meteofrance?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,wind_direction_10m_dominant&timezone=Europe%2FBerlin&format=csv"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "weather_db.csv"
)
#print(os.path.dirname(os.path.realpath(__file__)))
#print(__file__)
#print(path_target)