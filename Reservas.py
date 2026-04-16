from Asientos import Asiento
from Pasajeros import Pasajero
from Vuelos import Vuelo

class Reserva:
    def __init__(self, cod_reserva, pasajero, vuelo, asiento):
        
        if not isinstance(cod_reserva, int) or cod_reserva <= 0:
            raise ValueError("Código de reserva inválido")

        if not isinstance(pasajero, Pasajero):
            raise TypeError("Pasajero inválido")

        if not isinstance(vuelo, Vuelo):
            raise TypeError("Vuelo inválido")

        if not isinstance(asiento, Asiento):
            raise TypeError("Asiento inválido")

        self.__cod_reserva = cod_reserva
        self.__estado = "ACTIVA"

        # Datos simples
        self.__nombre = pasajero.get_nombre()
        self.__destino = vuelo.get_destino()
        self.__horario = vuelo.get_horario_vuelo()
        self.__fecha = vuelo.get_fecha()

        # Objetos reales
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

    def get_pasajero(self):
        return self.__pasajero

    def get_vuelo(self):
        return self.__vuelo

    def get_asiento(self):
        return self.__asiento

    def confirmar_reserva(self):
        """
        Intenta reservar el asiento.
        Evita sobreventa
        """
        if not self.__asiento.get_dispo():
            print("Asiento ocupado")
            return False

        if self.__asiento.reservar():
            print("Reserva confirmada correctamente")
            return True

        print("Error al reservar el asiento")
        return False

    def cancelar_reserva(self):
        """
        Cancela la reserva si está activa
        """
        if self.__estado == "CANCELADA":
            print("La reserva ya está cancelada")
            return

        self.__asiento.liberar()
        self.__estado = "CANCELADA"
        print("Reserva cancelada correctamente")

    def mostrar_reserva(self):
        print("----- RESERVA -----")
        print(f"Código: {self.__cod_reserva}")
        print(f"Nombre: {self.__nombre}")
        print(f"Destino: {self.__destino}")
        print(f"Horario: {self.__horario}")
        print(f"Fecha: {self.__fecha}")
        print(f"Asiento: {self.__asiento.get_num_asi()}")
        print(f"Ubicación: {self.__asiento.get_ubi()}")
        print(f"Tipo: {self.__asiento.describir()}")
        print("-------------------")
