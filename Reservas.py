from Asiento import Asiento

class Reservas:
    def __init__(self, id_reserva, pasajero, vuelo, asiento):
        self.__id_reserva = id_reserva
        self.__pasajero = pasajero
        self.__vuelo = vuelo
        self.__asiento = asiento

def get_id_reserva(self):
        return self.__id_reserva

def get_pasajero(self):
        return self.__pasajero  
 
def get_vuelo(self):
        return self.__vuelo

def get_asiento(self):      
        return self.__asiento 

def confirmar_reserva(self):
    if self.__asiento.reservar(): 
        print("Reserva confirmada para el pasajero")
        return True
    else:
        print("El asiento está no disponible")
        return False
    
def cancelar_reserva(self):
        """
        Libera el asiento asociado a la reserva.
        Se usa cuando el usuario cancela.
        """
        self.__asiento.liberar()
        print("Reserva cancelada correctamente")

def mostrar_reserva(self):
        print("----- RESERVA -----")
        print(f"ID Reserva: {self.__id_reserva}")
        print(f"Pasajero: {self.__pasajero.get_nombre()}")
        print(f"Documento: {self.__pasajero.get_id()}")
        print(f"Destino: {self.__vuelo.get_destino()}")
        print(f"Asiento: {self.__asiento.get_num_asi()}")
        print(f"Ubicación: {self.__asiento.get_ubi()}")
        print(f"Tipo: {self.__asiento.describir()}")
        print("-------------------")
