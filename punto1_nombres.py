#from dotenv import load_dotend
from flask import Flask, Response, request #Request permite obtener los datos que se envian en el body de la peticion
import random #Permite trabajar con datos en formato de dataframes

app = Flask(__name__)

nombres = ["Sebastian", "Tanya", "Juan", "Ana", "Carlos", "Laura", "camilo", "Samanta", "Tomas", "Angie"]
apellidos = ["Tellez", "Pachon", "Hernández", "Celis", "Navia", "Valero", "Gracia", "Beltral", "Buitrago", "Prieto"]
dominios = ["@gmail.com", "hotmail.com", "yahoo.com", "outlook.com","@gmail.es", "hotmail.es", "yahoo.es", "outlook.es"] 

@app.route('/nombres_ramdom', methods=['GET'])
def datos_aleatorios(numero):    
    datos = []
    for i in range(numero):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido}"
        orreo = f"{nombre.lower()}{apellido.lower()}@{random.choice(dominios)}"
        contrasena = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8 or k=9))
        datos.append({"nombre": nombre_completo, "correo": correo, "contrasena": contrasena})
    return jsonify({"datos_aleatorios": datos})

if __name__ == '__main__':
    app.run(debug=True)
