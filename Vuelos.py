from Asientos import AsientoEco, AsientoNorm, AsientoPrem

class Vuelo:
    def __init__(self, id_vuelo, horario_vuelo, destino, fecha, hora_despe, hora_at):
        self.__id_vuelo = id_vuelo
        self.__horario_vuelo = horario_vuelo
        self.__destino = destino
        self.__fecha = fecha
        self.__hora_despe = hora_despe
        self.__hora_at = hora_at
        self.__lista_asiento = []
        """Se hace uso de la lista para aglomerar la cantidad de asientos que poseemos y sus diferentes caracteristicas
        """

        """Con este for ordenamos la lista de asientos para normal, economico y premium, haciendo el uso de %
        y se le asigna a cada uno la distinta posicion, se uso ia para conseguir el patron deseado (Ventana-Mitad-pasillo)
    """  
        for i in range(1, 21):
            if i % 6 == 1: #Modulo toma el residuo de la division
                ubi = "Ventana"
            elif i % 6 == 2:
                ubi = "Mitad"
            elif i % 6 == 3:
                ubi = "Pasillo"
            elif i % 6 == 4:
                ubi = "Pasillo"
            elif i % 6 == 5:
                ubi = "Mitad"
            else:
                ubi = "Ventana"
            self.__lista_asiento.append(AsientoEco(i, 1, ubi))
        for i in range(21, 36):
            if i % 6 == 0:
                ubi = "Ventana"
            elif i % 6 == 2:
                ubi = "Mitad"
            elif i % 6 == 3:
                ubi = "Pasillo"
            elif i % 6 == 4:
                ubi = "Pasillo"
            elif i % 6 == 5:
                ubi = "Mitad"
            else:
                ubi = "Ventana"
            self.__lista_asiento.append(AsientoNorm(i, 1, ubi))
        for i in range(36, 46):
            if i % 6 == 1:
                ubi = "Ventana"
            elif i % 6 == 2:
                ubi = "Mitad"
            elif i % 6 == 3:
                ubi = "Pasillo"
            elif i % 6 == 4:
                ubi = "Pasillo"
            elif i % 6 == 5:
                ubi = "Mitad"
            else:
                ubi = "Ventana"
            self.__lista_asiento.append(AsientoPrem(i, 1, ubi))

    # Getters
    def get_id_vuelo(self):
        return self.__id_vuelo

    def get_horario_vuelo(self):
        return self.__horario_vuelo
    
    def get_destino(self):
        return self.__destino

    def get_precio_base_vu(self):
        return self.__precio_base_vu
    
    def get_lista_asiento(self):
        return self.__lista_asiento
    
    def get_fecha(self):
        return self.__fecha
    
    def get_hora_despe(self):
        return self.__hora_despe

    def get_hora_at(self):
        return self.__hora_at


    def mostrar_asientos(self):
        for asiento in self.__lista_asiento:
            dispo = "Disponible" if asiento.get_dispo() else "No disponible"
            print(f"{asiento.get_num_asi()} - {asiento.get_ubi()} - {asiento.describir()} - {dispo}")

