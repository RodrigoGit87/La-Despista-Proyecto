from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
#iniciar app
app = Flask(__name__)
CORS(app)

#Preparar la DB
def iniciar_db():
    #conecta con el archivo o lo crea si no existe
    conexion=sqlite3.connect("la_despista.db")
    cursor= conexion.cursor()
    #Escribimos el comando SQL para crear la tabla
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            como_nos_conocio TEXT,
            sugerencias TEXT,
            acepta_datos BOOLEAN,
            acepta_promos BOOLEAN
        )
    """)
    conexion.commit() #Guardamos
    conexion.close()

iniciar_db() #Llamar a la funcion al arrancar


#Crear ruta
@app.route("/",methods=["GET"])
def saludo_inicial():
    return{"mensaje":"El servidor de La despistá está funcionando"}


"""Para recibir el formulario de los clientes desde la web, los datos tienen q viajar desde index.html hasta app.py
Para hacer eso, necesitamos dos cosas:

Que Python abra una "puerta" preparada para recibir un paquete de datos.
Que JavaScript coja los datos, forme el paquete y se lo envíe a esa puerta.
"""    
#Nueva ruta para recibir el formulario
@app.route("/recibir_datos", methods=["POST"])
def recibir_formulario():
    # Extraemos los datos que llegarán desde JavaScript (que vendrán en formato JSON)
    datos_cliente = request.json
    
    #Conectar a la DB
    conexion=sqlite3.connect("la_despista.db")
    cursor= conexion.cursor()

    #Inserta fila con lso valores
    cursor.execute("""
        INSERT INTO clientes (nombre, email, como_nos_conocio, sugerencias, acepta_datos, acepta_promos)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datos_cliente['fullname'], 
        datos_cliente['email'], 
        datos_cliente['discovery'], 
        datos_cliente['suggestions'], 
        datos_cliente['dataConsent'], 
        datos_cliente['promoConsent']
    ))
    conexion.commit()
    conexion.close()

    # Imprimimos los datos en la terminal para comprobarlos
    print("\n--- ¡NUEVO CLIENTE HA ENVIADO FEEDBACK! ---")
    print("Datos:", datos_cliente)
    print("------------------------------------------\n")
    
    # Le respondemos al móvil del cliente que todo ha ido genial
    return jsonify({"estado": "exito", "mensaje": "Datos guardados correctamente"})


# Esto hace que el servidor arranque cuando ejecutamos el archivo
if __name__ == "__main__":
    app.run(debug=True, port=5000) #port=5000 servidor de prueba