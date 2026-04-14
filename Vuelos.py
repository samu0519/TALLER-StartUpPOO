from Asientos import AsientoEco, AsientoNorm, AsientoPrem

class Vuelo:
    def __init__(self, id_vuelo, horario_vuelo, destino, precio_base_vu):
        self.__id_vuelo = id_vuelo
        self.__horario_vuelo = horario_vuelo
        self.__destino = destino
        self.__precio_base_vu = precio_base_vu
        self.__lista_asiento = []
        
        for i in range(1, 21):
            self.__lista_asiento.append(AsientoEco(i, 1, 50000))
        for i in range(21, 36):
            self.__lista_asiento.append(AsientoNorm(i, 1, 80000))
        for i in range(36, 46):
            self.__lista_asiento.append(AsientoPrem(i, 1, 120000))

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

