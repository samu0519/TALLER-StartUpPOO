from Asientos import Asiento
from Pasajeros import Pasajero
from Vuelos import Vuelo

class Reserva:
    def __init__(self, cod_reserva, pasajero, vuelo, asiento):
        
        if not isinstance(cod_reserva, int) or cod_reserva <= 0:  # Se utiliza isinstance() para verificar que los datos recibidos sean del tipo correcto.
            raise ValueError("Código de reserva inválido")

        if not isinstance(pasajero, Pasajero):  # Por ejemplo isinstance(pasajero, Pasajero)
            raise TypeError("Pasajero inválido")  # verifica que la variable pasajero sea un objeto de la clase Pasajero. Esto evita errores cuando se intentan usar métodos que no existen en otros tipos de datos.

        if not isinstance(vuelo, Vuelo):
            raise TypeError("Vuelo inválido")  # El raise permite generar errores de forma controlada cuando los datos no cumplen con las condiciones necesarias.
                                             # Esto detiene la ejecución del programa
                                             # y evita que el sistema continúe con información incorrecta.

        if not isinstance(asiento, Asiento):
            raise TypeError("Asiento inválido")
            # Estas validaciones garantizan que los objetos se creen correctamente,
            # evitando fallos en tiempo de ejecución y asegurando la integridad del sistema.
            # Esto hace el programa más robusto y confiable.

        self.__cod_reserva = cod_reserva
        self.__estado = "ACTIVA"

        # Datos simples (para mostrar fácilmente)
        self.__nombre = pasajero.get_nombre()
        self.__destino = vuelo.get_destino()
        self.__horario = vuelo.get_horario_vuelo()
        self.__fecha = vuelo.get_fecha()
        self.__hora_despe = vuelo.get_hora_despe()
        self.__hora_at = vuelo.get_hora_at()

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
        print(f"Hora de despegue: {self.__hora_despe}")
        print(f"Hora aterrizaje: {self.__hora_at}")
        print(f"Asiento: {self.__asiento.get_num_asi()}")
        print(f"Ubicación: {self.__asiento.get_ubi()}")
        print(f"Tipo: {self.__asiento.describir()}")
        print("-------------------")