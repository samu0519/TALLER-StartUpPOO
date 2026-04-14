class Asiento:#Super clase
    def __init__(self, num_asi, dispo):
        self.__num_asi = num_asi
        self.set_dispo(dispo)

    def describir(self):
        return "Asiento común"
   
#Getters
    def get_num_asi(self):
        return self.__num_asi
    
    def get_dispo(self):
        return self.__dispo

#Setters
    def set_dispo(self, new_dispo):
        """Validación de si y no en este caso 1 y 0 
            para la disponibilidad de asientos"""
        if new_dispo == 1:
            self.__dispo = True
        elif new_dispo == 0:
            self.__dispo = False
        else:
            raise ValueError("ERROR disponibilidad")

    """En este caso en especial de los setters no hace falta asignarlo nuevamente
        dado que ya lo estamos haciedno con el if para el booleano"""


#SubClase AsientoEco
class AsientoEco(Asiento):
    def __init__(self, num_asi, dispo, precio):
        super().__init__(num_asi, dispo)
        self.__precio = 50000 #se tienen que agregar un precio fijo

#Sobreescritura de la subclase
    def describir(self): #Con esta funcion redefinimos lo que contiene cada contenido de los asientos
        return "Asiento Economico, - comodidad, - precio"
   
#Getters de la subclase
    def get_precio(self):
        return self.__precio


#SubClase AsientoNorm
class AsientoNorm(Asiento):
    def __init__(self, num_asi, dispo, precio):
        super().__init__(num_asi, dispo)
        self.__precio = 80000

#Getters de la subclase
    def get_precio(self):
        return self.__precio

#Sobreescritura de la subclase
    def describir(self):
        return "Asiento Normal, + comodidad, = precio"


#SubClase AsientoPrem   
class AsientoPrem(Asiento):
    def __init__(self, num_asi, dispo, precio):
        super().__init__(num_asi, dispo)
        self.__precio = 120000
        
#Getters de la subclase
    def get_precio(self):
        return self.__precio

#Sobreescritura de la subclase
    def describir(self):
        return "Asiento Premium, ++ comodidad, ++ precio"
   
"""No se usan los setters en las subclases de los asientos dado que estan asignados como un valor fijo"""








