import os
import requests
import json
from utils import build_weather_icon_url, unix_utc_to_local_dict , kelvin_to_celsius , meters_per_second_to_kilometers_per_hour

def get_weather(city):

    api_key = os.getenv("API_KEY")
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?&unit=metric&q={}&appid={}".format(city, api_key)
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?&unit=metric&q={}&appid={}".format(city, api_key)

    # Building the current weather part of the return

    current_weather_response = requests.get(current_weather_url)

    if current_weather_response.status_code == 200:
        current_weather_data = json.loads(current_weather_response.content.decode())

        current_weather_treated_data = {
            "datetime": unix_utc_to_local_dict(current_weather_data["dt"], current_weather_data["timezone"]),
            "description": current_weather_data["weather"][0]["description"].title(),
            "main_description": current_weather_data["weather"][0]["main"],
            "wind_speed": meters_per_second_to_kilometers_per_hour(current_weather_data["wind"]["speed"]),
            "sunset_time": unix_utc_to_local_dict(current_weather_data["sys"]["sunset"],current_weather_data["timezone"]),
            "sunrise_time": unix_utc_to_local_dict(current_weather_data["sys"]["sunrise"], current_weather_data["timezone"]),
            "max_day_temp": kelvin_to_celsius(current_weather_data["main"]["temp_max"]),
            "min_day_temp": kelvin_to_celsius(current_weather_data["main"]["temp_min"]),
            "current_temp":kelvin_to_celsius(current_weather_data["main"]["temp"]),
            "feels_like_temp":kelvin_to_celsius(current_weather_data["main"]["feels_like"]),
            "humidity":current_weather_data["main"]["humidity"],
            "icon_url": build_weather_icon_url(current_weather_data["weather"][0]["icon"]),
        }
    else:
        return {"error": "Failed to retrieve current weather data"}
    # Building the weather forecast part of the return

    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        forecast_data = json.loads(forecast_response.content.decode())
        forecast_periods_list = forecast_data["list"]

        grouped_by_day_forecast_data = {
            "max_day_temp" : -100,
            "min_day_temp" : 100,
            "day_forecast_list" : {},
        }

        for forecast in forecast_periods_list:
            current_date = unix_utc_to_local_dict(forecast["dt"], forecast_data["city"]["timezone"])["short_date"]

            if current_date not in grouped_by_day_forecast_data["day_forecast_list"]:
                grouped_by_day_forecast_data["day_forecast_list"][current_date] = []

            formatted_forecast = {
                "datetime": unix_utc_to_local_dict(forecast["dt"], forecast_data["city"]["timezone"]),
                "description": forecast["weather"][0]["description"].title(),
                "main_description": forecast["weather"][0]["main"],
                "wind_speed": meters_per_second_to_kilometers_per_hour(forecast["wind"]["speed"]),
                "forecast_temp": kelvin_to_celsius(forecast["main"]["temp"]),
                "feels_like_temp": kelvin_to_celsius(forecast["main"]["feels_like"]),
                "humidity": forecast["main"]["humidity"],
                "icon_url": build_weather_icon_url(forecast["weather"][0]["icon"]),
            }

            # Check the highest and lowest temperatures within a day

            if formatted_forecast["forecast_temp"] > grouped_by_day_forecast_data["max_day_temp"]:
                grouped_by_day_forecast_data["max_day_temp"]  = formatted_forecast["forecast_temp"]

            if formatted_forecast["forecast_temp"] < grouped_by_day_forecast_data["min_day_temp"]:
                grouped_by_day_forecast_data["min_day_temp"]  = formatted_forecast["forecast_temp"]
                
            # Append the element with the formatex forecast to its relative "day_forecast_list" key.
            grouped_by_day_forecast_data["day_forecast_list"][current_date].append(formatted_forecast)

# Now formatted_forecast_data is a dictionary where keys are dates and values are arrays of forecasts for those dates

    else:
        return {"error": "Failed to retrieve forecast data"}    

    weather = {
        "city": forecast_data["city"]["name"],
        "country": forecast_data["city"]["country"],
        "current_weather": current_weather_treated_data, 
        "forecast": grouped_by_day_forecast_data,
    }
        
    return weather
