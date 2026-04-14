from Asiento import Asiento

class Reserva:
    def __init__(self, cod_reserva, pasajero, vuelo, asiento):
        """
        cod_reserva: identificador único
        pasajero: objeto Pasajero
        vuelo: objeto Vuelo
        asiento: objeto Asiento
        """

        self.__cod_reserva = cod_reserva

        # Datos simples (para mostrar fácil)
        self.__nombre = pasajero.get_nombre()
        self.__destino = vuelo.get_destino()
        self.__horario = vuelo.get_horario_vuelo()

        # Objetos reales (para lógica del sistema)
        self.__pasajero = pasajero
        self.__vuelo = vuelo
        self.__asiento = asiento

   
def get_cod_reserva(self):
        return self.__cod_reserva

def get_nombre(self):
        return self.__nombre

def get_destino(self):
        return self.__destino

def get_horario(self):
        return self.__horario

def get_asiento(self):
        return self.__asiento

  
def confirmar_reserva(self):
        """
        Intenta reservar el asiento.
        Evita sobreventa.
        """
        if self.__asiento.reservar():
            print("Reserva confirmada")
            return True
        else:
            print("Asiento no disponible")
            return False

def cancelar_reserva(self):
        """
        Libera el asiento
        """
        self.__asiento.liberar()
        print("Reserva cancelada")

def mostrar_reserva(self):
        print("----- RESERVA -----")
        print(f"Código: {self.__cod_reserva}")
        print(f"Nombre: {self.__nombre}")
        print(f"Destino: {self.__destino}")
        print(f"Horario: {self.__horario}")
        print(f"Asiento: {self.__asiento.get_num_asi()}")
        print(f"Ubicación: {self.__asiento.get_ubi()}")
        print(f"Tipo: {self.__asiento.describir()}")
        print("-------------------")
