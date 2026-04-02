from flask import Flask, request, jsonify, render_template
import sqlite3
import os

# Obtener la ruta absoluta de la carpeta donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "la_despista.db")

#iniciar app
app = Flask(__name__)

#Preparar la DB
def iniciar_db():
    #conecta con el archivo usando la ruta absoluta
    conexion=sqlite3.connect(DB_PATH)
    cursor= conexion.cursor()
    #Escribimos el comando SQL para crear la tabla
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            como_nos_conocio TEXT,
            quejas TEXT,
            sugerencias TEXT,
            acepta_datos BOOLEAN
         )
    """)
    conexion.commit() #Guardamos
    conexion.close()

iniciar_db() #Llamar a la funcion al arrancar


#Crear ruta
@app.route("/",methods=["GET"])
def saludo_inicial():
    return render_template("index.html")

@app.route("/privacidad",methods=["GET"])
def politica_privacidad():
    return render_template("privacidad.html")


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
    
    #Conectar a la DB con ruta absoluta
    conexion=sqlite3.connect(DB_PATH)
    cursor= conexion.cursor()

    #Inserta fila con lso valores
    cursor.execute("""
        INSERT INTO clientes (nombre, email, como_nos_conocio, quejas, sugerencias, acepta_datos, acepta_promos)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datos_cliente.get('fullname', ''), #un string vacio para evitar errores si el cliente no manda el paquete entero.
        datos_cliente.get('email', ''), 
        datos_cliente.get('discovery', ''),
        datos_cliente.get('complaints', ''),
        datos_cliente.get('suggestions', ''), 
        datos_cliente.get('dataConsent', False), 
        datos_cliente.get('promoConsent', False)
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