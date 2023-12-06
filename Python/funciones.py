
def agregar_reserva(nombre, telefono, cantidad, email):

    if consultar_reserva(telefono):
        return False
    
    nueva_reserva = {
        'nombre': nombre,
        'telefono': telefono,
        'cantidad': cantidad,
        'email': email
    }
    reservas.append(nueva_reserva)
    return True
    
def consultar_reserva(telefono):
    for reserva in reservas:
        if reserva['telefono'] == telefono:
            return reserva
    return False   

def listar_reservas():
    print()
    print("-"*50)
    for reserva in reservas:
        print(f'Nombre......: {reserva['nombre']}')
        print(f'Telefono....: {reserva['telefono']}')
        print(f'Cantidad....: {reserva['cantidad']}')
        print(f'Email.......: {reserva['email']}')
        print("-"*50)


#--------------------------------------------------------------------

# Programa principal
# Defino la lista que contedra los diccionarios....
reservas = []

#------------------------------------------------------------------------
# Agrego las reservas a la lista...

agregar_reserva('Jesus Noguera', 1167510712, 2, 'jnogueraroman27@gamil.com')
agregar_reserva('Elizeidys Marchan', 1128636134, 4, 'elymarchan@gmail.com')
agregar_reserva('Federico Gomez', 1123245578, 3, 'fede.gomez@hotmail.com')
agregar_reserva('Sandra Roman', 1155678786, 6, 'sandraroman@gmail.com')
agregar_reserva('Gustavo Noguera', 1198975643, 2, 'gustavo.noguera@gamil.com')
agregar_reserva('Victor Roman', 1145478785, 3, 'vnroman@hotmail.com')
agregar_reserva('Francisco Espinoza', 1123456787, 3, 'frankesp@gmail.com')
agregar_reserva('Mateo Espinoza', 1123567345, 5, 'mateoign33@gmail.com')
agregar_reserva('Eglis Marchan', 1123459876, 2, 'eglis.mar@gmail.com')
agregar_reserva('Jorge Fernandes', 1165437898, 3, 'jorgefer@hotmail.com')

#-------------------------------------------------------------------------------
# Para modificar los productos

def modificar_reserva(nuevo_nombre, telefono, nueva_cantidad, nuevo_email):
    for reserva in reservas:
        if reserva['telefono'] == telefono:
            reserva['nombre'] = nuevo_nombre
            reserva['cantidad'] = nueva_cantidad
            reserva['email'] = nuevo_email
            return True
    return False

#--------------------------------------------------------------------------------
# Eliminamos alguna reserva

def eliminar_reserva(telefono):
    for reserva in reservas:
        if reserva['telefono'] == telefono:
            reservas.remove(reserva)
            return True
    return False

#----------------------------------------------------------------------------
# Ponemos en una lista presentable las reservas

print()
print("**********LISTA DE RESERVAS PARA HOY**********")
listar_reservas()

#-----------------------------------------------------------------------------
# Probamos la modificacion de las reservas

#modificar_reserva('Jorge Fernandez', 1165437898, 7, 'jorgefer@hotmail.es')
#modificar_reserva('Jesus Roman', 1167510712, 5, 'jnogueraroman27@gamil.es')

#print()
#print("**********LISTA DE RESERVAS PARA HOY**********")
#listar_reservas()

#--------------------------------------------------------------------------------

# Eliminar una reserva

#eliminar_reserva(1123456787)

#print()
#print("**********LISTA DE RESERVAS PARA HOY**********")
#listar_reservas()

#-------------------------------------------------------------------------------------