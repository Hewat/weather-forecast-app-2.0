import datetime
import sqlite3

def connect_to_database():
    """Conecta ao banco de dados."""

    return sqlite3.connect("linx-weather-database.sqlite3")


def insert_search(connection, city, country, current_weather, forecast):
    """Insere uma pesquisa no banco de dados."""

    cursor = connection.cursor()

    # Checa se a tabela existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather'")
    table_exists = cursor.fetchone() is not None

    if not table_exists:

        # Cria a tabela
        cursor.execute("""
            CREATE TABLE weather(
                insertion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                city TEXT,
                country TEXT,               
                date DATE,
                current_weather_temp REAL,
                current_weather_feels_like_temp REAL,
                current_weather_overall_title TEXT,
                current_weather_overall_description TEXT,
                current_weather_humidity REAL,
                current_weather_wind_speed REAL,
                forecast_temp REAL,
                forecast_feels_like_temp REAL,
                forecast_weather_overall_title TEXT,
                forecast_weather_overall_description TEXT,
                forecast_humidity REAL,
                forecast_wind_speed REAL
            )
        """)  

    # Trata os dados de forecast, que é uma lista de dictionaries, em um array por propriedade 
    
    current_weather_temp =  current_weather["main"]["temp"]
    current_weather_feels_like_temp = current_weather["main"]["feels_like"]
    current_weather_overall_title = current_weather["weather"][0]["main"]
    current_weather_overall_description = current_weather["weather"][0]["description"]
    current_weather_humidity = current_weather["main"]["humidity"]
    current_weather_wind_speed = current_weather["wind"]["speed"]


    date = []
    forecast_temp = []
    forecast_feels_like_temp = []
    forecast_weather_overall_title = []
    forecast_weather_overall_description = []
    forecast_humidity = []
    forecast_wind_speed = []

    for weather_data in forecast:
        date.append(weather_data["dt_txt"])
        forecast_temp.append(weather_data["main"]["temp"])
        forecast_feels_like_temp.append(weather_data["main"]["feels_like"])
        forecast_weather_overall_title.append(weather_data["weather"][0]["main"])
        forecast_weather_overall_description.append(weather_data["weather"][0]["description"])
        forecast_humidity.append(weather_data["main"]["humidity"])
        forecast_wind_speed.append(weather_data["wind"]["speed"])

    # Insere os dados

    tuplas = [
        (
            datetime.datetime.now(),
            city,
            country,
            date,
            forecast_temp,
            forecast_feels_like_temp,
            forecast_weather_overall_title,
            forecast_weather_overall_description,
            forecast_humidity,
            forecast_wind_speed,
            current_weather_temp,
            current_weather_feels_like_temp,
            current_weather_overall_title,
            current_weather_overall_description,
            current_weather_humidity,
            current_weather_wind_speed
        )
        for date, forecast_temp, forecast_feels_like_temp, forecast_weather_overall_title, forecast_weather_overall_description, forecast_humidity, forecast_wind_speed in zip(
            date, forecast_temp, forecast_feels_like_temp, forecast_weather_overall_title, forecast_weather_overall_description, forecast_humidity, forecast_wind_speed
        )
    ]
        # Insere as tuplas no banco de dados
    for tupla in tuplas:
        cursor.execute(
            """INSERT INTO weather (
                insertion_time,
                city,
                country,
                date,
                forecast_temp,
                forecast_feels_like_temp,
                forecast_weather_overall_title,
                forecast_weather_overall_description,
                forecast_humidity,
                forecast_wind_speed,
                current_weather_temp,
                current_weather_feels_like_temp,
                current_weather_overall_title,
                current_weather_overall_description,
                current_weather_humidity,
                current_weather_wind_speed
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            tupla,
        )

    connection.commit()
    cursor.close()

def get_searches(connection):
    """Recupera o histórico das pesquisas do banco de dados."""

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM weather;
        """
    )

    results = cursor.fetchall()
    cursor.close()

    return results