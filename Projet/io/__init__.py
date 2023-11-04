import os

url_db = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=rain,cloudcover&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,windspeed_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin&format=csv"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "weather_db.csv"
)