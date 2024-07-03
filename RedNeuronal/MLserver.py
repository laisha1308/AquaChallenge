import mysql.connector
import NeuralNetwork
from datetime import datetime
import requests


# Establecer la conexión con la base de datos
conection = mysql.connector.connect(
    host="localhost",
    port=33,
    user="root",
    password="",
    database="AquaChallenge"
)

def consulta():
    # Crear un cursor para ejecutar consultas
    cursor = conection.cursor()

    # Obtener la fecha actual
    date_py = datetime.now().strftime('%Y-%m-%d')
    # Ejecutar una consulta para obtener los últimos datos de la base de datos
    query = f"SELECT humidityAir, temperature, pressure, date FROM information WHERE date = '{date_py}' ORDER BY datahour DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchall()

    # Cerrar la conexión y el cursor
    # cursor.close()
    # conection.close()

    # Hacer algo con los datos obtenidos
    if result:
        print(result)
        humidityAir, temperature, pressure, date = result[0]
        date = int(date[5:7])

        # Crear la lista data
        data = [date, temperature, humidityAir, pressure]
        print(data)

        # Hacer prediccion con el modelo entrenado
        prediction = NeuralNetwork.predict(data, rounded=True)
        print(prediction)

        # Definir la URL a la que quieres enviar los datos
        url = "http://localhost/ServicioRedNeuronal/iotMLPredictions.php"

        # Definir los parámetros GET
        params = {"prediction": prediction}

        # Enviar la solicitud GET
        response = requests.post(url, params=params)

        # Imprimir la respuesta del servidor
        print(response.text)

        # Imprimir la prediccion sin redondear
        prediction = NeuralNetwork.predict(data, rounded=False)
        print(prediction)

    else:
        print("No se devolvieron datos de la consulta.")
