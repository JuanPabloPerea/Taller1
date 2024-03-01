#from dotenv import load_dotend
from flask import Flask, Response, request #Request permite obtener los datos que se envian en el body de la peticion
import random #Permite trabajar con datos en formato de dataframes

app = Flask(__name__)

nombres = ["Sebastian", "Tanya", "Juan", "Ana", "Carlos", "Laura", "camilo", "Samanta", "Tomas", "Angie"]
apellidos = ["Tellez", "Pachon", "Hernández", "Celis", "Navia", "Valero", "Gracia", "Beltral", "Buitrago", "Prieto"]

@app.route('/nombres_ramdom', methods=['GET'])
def nombres_ramdom():
    numero_nombres = 10
    nombres_aleatorios = []
    for i in range(numero_nombres):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido}"
        nombres_aleatorios.append(nombre_completo)
    return jsonify
 
