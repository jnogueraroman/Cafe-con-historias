class Lista:
    reservas = []
    
    def agregar_reserva(self, nombre, telefono, cantidad, email):

        if self.consultar_reserva(telefono):
         return False
    
        nueva_reserva = {
        'nombre': nombre,
        'telefono': telefono,
        'cantidad': cantidad,
        'email': email
    }
        self.reservas.append(nueva_reserva)
        return True
    
    def consultar_reserva(self, telefono):
        for reserva in self.reservas:
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
    
        #-------------------------------------------------------------------------------
        # Para modificar los productos

    def modificar_reserva(self, nuevo_nombre, telefono, nueva_cantidad, nuevo_email):
        for reserva in self.reservas:
            if reserva['telefono'] == telefono:
                reserva['nombre'] = nuevo_nombre
                reserva['cantidad'] = nueva_cantidad
                reserva['email'] = nuevo_email
                return True
        return False

    #--------------------------------------------------------------------------------
    # Eliminamos alguna reserva

    def eliminar_reserva(self, telefono):
        for reserva in self.reservas:
            if reserva['telefono'] == telefono:
                self.reservas.remove(reserva)
                return True
        return False