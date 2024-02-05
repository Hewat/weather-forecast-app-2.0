import datetime
import sqlite3
import json

def connect_to_database():
    """Conecta ao banco de dados."""

    return sqlite3.connect("linx-weather-database.sqlite3")


def insert_search(connection, fetched_data):
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
                fetched_data TEXT
            )
        """)  


    
        # Insere os dados na tabela

    serialized_data = json.dumps(fetched_data, indent=4)
    timestamp = datetime.datetime.now().isoformat()  # Adjust as needed for your desired timestamp format
    cursor.execute("""
        INSERT INTO weather (insertion_time, fetched_data) VALUES (?, ?)
    """, (timestamp, serialized_data))

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