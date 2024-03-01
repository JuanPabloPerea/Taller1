from flask import Flask, jsonify, request 
import random 
import pandas as pd

app = Flask(__name__)

nombres = ["Sebastian", "Tanya", "Juan", "Ana", "Carlos", "Laura", "camilo", "Samanta", "Tomas", "Angie"]
apellidos = ["Tellez", "Pachon", "Hernández", "Celis", "Navia", "Valero", "Gracia", "Beltral", "Buitrago", "Prieto"]
dominios = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com","@gmail.es", "@hotmail.es", "@yahoo.es", "@outlook.es"] 


@app.route('/nombres_ramdom', methods=['GET'])
def datos_ramdom():
    cantidad_total = 500000
    datos = []
    k = random.choice(7,8,9,10,11)
    batch_size = 1000
    for i in range(cantidad_total // batch_size):
        batch_data = []
        for x in range(batch_size):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            nombre_completo = f"{nombre} {apellido}"
            correo = f"{nombre.lower()}{apellido.lower()}{random.choice(dominios)}"
            contrasena = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k))
            datos.append({"nombre": nombre_completo, "correo": correo, "contrasena": contrasena})
    return jsonify({"datos_aleatorios": datos})


@app.route("/save_data_file", methods=['POST'])
def save_data_file():
    data = request.json
    if data:
        dataFrame = pd.DataFrame(data)
        dataFrame.to_csv('data.csv', index=False)
        return "Datos guardados en data.csv"
    else:
        return "No se recibieron datos en el formato JSON"

@app.route('/consume_json', methods=['GET'])
def consume_json():
    data={'nombre':'juan','apellido':'Tellez','email':'juantellez@gmail.com', 'password':'Ejemplo'}
    response = jsonify(data)
    return response

if __name__ == '__main__':
    app.run(debug=True)
