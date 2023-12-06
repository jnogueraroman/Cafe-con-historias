
import mysql.connector

class Lista:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
            nombre VARCHAR(40) NOT NULL,
            telefono INT,
            cantidad INT NOT NULL,
            email VARCHAR(60) NOT NULL)''')
        self.conn.commit()

    def agregar_reserva(self, nombre, telefono, cantidad, email):

        self.cursor.execute(f"SELECT * FROM reservas WHERE telefono ={telefono}")
        reserva_existe = self.cursor.fetchone()
        if reserva_existe:
            return False
        
        sql = f"INSERT INTO reservas (nombre, telefono, cantidad, email) VALUES ('{nombre}', {telefono}, {cantidad}, '{email}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

#-----------------------------------------------------------------------------------------------------------------------    

    def consultar_reserva(self, telefono):
        self.cursor.execute(f"SELECT * FROM reservas WHERE telefono = {telefono}")
        return self.cursor.fetchone()
    
#------------------------------------------------------------------------------------------------------------------------

    def modificar_reserva(self, nuevo_nombre, telefono, nueva_cantidad, nuevo_email):
        sql = f"UPDATE reservas SET nombre = '{nuevo_nombre}', cantidad = {nueva_cantidad}, email = '{nuevo_email}' WHERE telefono = {telefono}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
#-------------------------------------------------------------------------------------------------------------------------

    def mostrar_reserva(self, telefono):
        reserva = self.consultar_reserva(telefono)
        if reserva:
            print("-"*40)
            print(f'Nombre......: {reserva['nombre']}')
            print(f'Telefono....: {reserva['telefono']}')
            print(f'Cantidad....: {reserva['cantidad']}')
            print(f'Email.......: {reserva['email']}')
            print("-"*40)
        else:
            print("Reserva no encontrada.")

#-------------------------------------------------------------------------------------------------------------------------

    def listar_reservas(self):
        self.cursor.execute("SELECT * FROM reservas")
        reservas = self.cursor.fetchall()
        print("-"*40)
        for reserva in reservas:
            print(f'Nombre......: {reserva['nombre']}')
            print(f'Telefono....: {reserva['telefono']}')
            print(f'Cantidad....: {reserva['cantidad']}')
            print(f'Email.......: {reserva['email']}')
            print("-"*40)

#-----------------------------------------------------------------------------------------------------------------------

    def eliminar_reserva(self, telefono):
        self.cursor.execute(f"DELETE FROM reservas WHERE telefono = {telefono}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#--------------------------------------------------------------------------------------------

lista = Lista(host='localhost', user='root', password='', database='mis_reservas')

# Agrego algunas reservas:

lista.agregar_reserva('Jesus Noguera', 1167510712, 2, 'jnogueraroman27@gamil.com')
lista.agregar_reserva('Elizeidys Marchan', 1128636134, 4, 'elymarchan@gmail.com')
lista.agregar_reserva('Federico Gomez', 1123245578, 3, 'fede.gomez@hotmail.com')
lista.agregar_reserva('Sandra Roman', 1155678786, 6, 'sandraroman@gmail.com')
lista.agregar_reserva('Gustavo Noguera', 1198975643, 2, 'gustavo.noguera@gamil.com')
lista.agregar_reserva('Victor Roman', 1145478785, 3, 'vnroman@hotmail.com')
lista.agregar_reserva('Francisco Espinoza', 1123456787, 3, 'frankesp@gmail.com')
lista.agregar_reserva('Mateo Espinoza', 1123567345, 5, 'mateoign33@gmail.com')
lista.agregar_reserva('Eglis Marchan', 1123459876, 2, 'eglis.mar@gmail.com')
lista.agregar_reserva('Jorge Fernandes', 1165437898, 3, 'jorgefer@hotmail.com')

#--------------------------------------------------------------------------------------------------------

# Consulta de reservas:

#telf_reserva = int(input("Ingrese el numero de telefono de la reserva: "))
#reserva = lista.consultar_reserva(telf_reserva)
#if reserva:
#    print(f"Reserva encontrada: {reserva['telefono']} - {reserva['nombre']}")
#else:
#    print(f'Reserva {'telefono'} no existe')

#--------------------------------------------------------------------------------------------------------

# Mostramos y modificamos reservas:

#lista.mostrar_reserva(1167510712)
#lista.modificar_reserva('Jesus Noguera', 1167510712, 3, 'jnoguera@gmail.com')
#lista.mostrar_reserva(1167510712)

#--------------------------------------------------------------------------------------------------------

# Listamos y Eliminamos reservas:

#lista.listar_reservas()
#lista.eliminar_reserva(1123456787)
#lista.listar_reservas()
