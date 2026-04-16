import json 
import os #Lo usamos para guardar el json
from Pasajeros import Pasajero
from Vuelos import Vuelo
from Reservas import Reserva

#Datos globales que se usaran

vuelos = {
    "V01": Vuelo("V01", "10:00", "Bogota - España", "Marzo 20/2025", "10:40", "21:00"),
    "V02": Vuelo("V02", "14:30", "Bogota - Alemania", "Abril 9/2025", "14:30", "6:00"),
    "V03": Vuelo("V03", "06:15", "Bogota - Cali", "Diciembre 31/2025", "06:15", "7:15"),
    "V04": Vuelo("V04", "21:30", "Bogota - Holanda", "Agosto 20/2025", "21:30", "16:30"),
    "V05": Vuelo("V05", "23:50", "Bogota - Medellin", "Octubre 1/2025", "23:50", "00:40")

}

reservas = {}
contador_cod_re = 1


print("ola")
