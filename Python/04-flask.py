#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

class Lista:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()


        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:

            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
            nombre VARCHAR(40) NOT NULL,
            telefono INT,
            cantidad INT NOT NULL,
            email VARCHAR(60) NOT NULL)''')
        self.conn.commit()

        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

#-------------------------------------------------------------------------------------------------

    def listar_reservas(self):
        self.cursor.execute("SELECT * FROM reservas")
        reservas = self.cursor.fetchall()
        return reservas
    
#--------------------------------------------------------------------------------------------------

    def consultar_reserva(self, telefono):
        self.cursor.execute(f"SELECT * FROM reservas WHERE telefono = {telefono}")
        return self.cursor.fetchone()

#---------------------------------------------------------------------------------------------------

    def mostrar_reserva(self, telefono):
        reserva = self.consultar_reserva(telefono)
        if reserva:
            print("-"*40)
            print(f'Nombre......: {reserva["nombre"]}')
            print(f'Telefono....: {reserva["telefono"]}')
            print(f'Cantidad....: {reserva["cantidad"]}')
            print(f'Email.......: {reserva["email"]}')
            print("-"*40)
        else:
            print("Reserva no encontrada.")

#-----------------------------------------------------------------------------------------------

    def agregar_reserva(self, nombre, telefono, cantidad, email):
        self.cursor.execute(f"SELECT * FROM reservas WHERE telefono = {telefono}")
        reserva_existe = self.cursor.fetchone()
        if reserva_existe:
            return False
        
        sql = f"INSERT INTO reservas (nombre, telefono, cantidad, email) VALUES (%s, %s, %s, %s)"
        valores = (nombre, telefono, cantidad, email)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True
    
#-----------------------------------------------------------------------------------------------------------
    def eliminar_reserva(self, telefono):
        self.cursor.execute(f"DELETE FROM reservas WHERE telefono = {telefono}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#------------------------------------------------------------------------------------------------------------

    def modificar_reserva(self, nuevo_nombre, telefono, nueva_cantidad, nuevo_email):
        sql = "UPDATE reservas SET nombre = %s, cantidad = %s, email = %s WHERE telefono = %s"
        valores = (nuevo_nombre, nueva_cantidad, nuevo_email, telefono)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

#---------------------------------------------------------------------------------------------------
# Instancio la clase:

#lista = Lista(host='localhost', user='root', password='', database='mis_reservas')
lista = Lista(host='jnogueraroman.mysql.pythonanywhere-services.com', user='jnogueraroman', password='python1234', database='jnogueraroman$mis_reservas')



#--------------------------------------------------------------------------------------------------

@app.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = lista.listar_reservas()
    return jsonify(reservas)

#----------------------------------------------------------------------------------------------------

@app.route("/reservas/<int:telefono>", methods=["GET"])
def mostrar_reserva(telefono):
    reserva = lista.consultar_reserva(telefono)
    if reserva:
        return jsonify(reserva)
    else:
         return "Reserva no encontrada", 404

#----------------------------------------------------------------------------------------------------

@app.route("/reservas", methods=["POST"])
def agregar_reserva():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    cantidad = request.form['cantidad']
    email = request.form['email']

    if lista.agregar_reserva(nombre, telefono, cantidad, email):
        return jsonify({"mensaje": "Reserva agregada"}), 201
    else:
        return jsonify({"mensaje": "Reserva ya existe"}), 400
    
#-------------------------------------------------------------------------------------------------------

@app.route("/reservas/<int:telefono>", methods=["DELETE"])
def eliminar_reserva(telefono):
    reserva = lista.consultar_reserva(telefono)
    if lista.eliminar_reserva(telefono):
        return jsonify({"mensaje": "Producto eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    
#-----------------------------------------------------------------------------------------------------

@app.route("/reservas/<int:telefono>", methods=["PUT"])
def modificar_reserva(telefono):
     nuevo_nombre = request.form.get("nombre")
     nueva_cantidad = request.form.get("cantidad")
     nuevo_email = request.form.get("email")

     if lista.modificar_reserva(nuevo_nombre, telefono, nueva_cantidad, nuevo_email):
         return jsonify({"mensaje": "Reserva modificada"}), 200
     else:
         return jsonify({"mensaje": "Reserva no encontrada"}), 404

    
#-------------------------------------------------------------------------------------------------------
# Funcion para hacer correr la api

if __name__ == "__main__":
    app.run(debug=True)

#---------------------------------------------------------------------------------------------------