import os
import requests
import json
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

from database import connect_to_database, insert_search, get_searches

def get_weather(city):
    """Obtém a previsão do tempo para uma cidade."""

    api_key = os.getenv("API_KEY")
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast/?&unit=metric&q={}&appid={}".format(city, api_key)
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather/?&unit=metric&q={}&appid={}".format(city, api_key)

    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        forecast_data = json.loads(forecast_response.content.decode())

    current_weather_response = requests.get(current_weather_url)

    if current_weather_response.status_code == 200:
        current_weather_data = json.loads(current_weather_response.content.decode())   

        weather = {
            "city": forecast_data["city"]["name"],
            "country": forecast_data["city"]["country"],
            "current_weather": current_weather_data, 
            "forecast": forecast_data["list"],
        }
        

        return weather
    else:
        return None


app = Flask(__name__)

CORS(app)

@app.route("/search", methods=["GET"])
def search():
    city = request.args.get("city")

    # Obtém a previsão do tempo
    weather = get_weather(city)

    # Insere a pesquisa no banco de dados
    insert_search(connect_to_database(), weather["city"],weather["country"], weather["current_weather"], weather["forecast"])

    # Retorna a previsão do tempo no formato JSON
    return jsonify(weather)


@app.route("/history", methods=["GET"])
def history():
    # Recupera o histórico das pesquisas
    searches = get_searches(connect_to_database())

    # Retorna o histórico das pesquisas no formato JSON
    return jsonify(searches)


if __name__ == "__main__":
    app.run(debug=True)