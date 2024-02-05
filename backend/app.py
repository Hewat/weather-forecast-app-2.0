from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from api_calls import get_weather

from database import connect_to_database, insert_search, get_searches

app = Flask(__name__)

CORS(app)

@app.route("/search", methods=["GET"])
def search():
    city = request.args.get("city")

    # Obtém a previsão do tempo
    weather = get_weather(city)

    # Insere a pesquisa no banco de dados
    insert_search(connect_to_database(), weather)

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