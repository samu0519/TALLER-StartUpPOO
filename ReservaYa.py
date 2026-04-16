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


#Funcion para guardar los archivos de reserva con json

def guardar_reserva():
    datos = [] #se crea una lista para guardar los datos que se usaran en json

    for g in reservas.values():
        if g.get_estado == "Activa":
            datos.append({
                "cod_reserva": g.get_cod_reserva(),
                "id_pasajero": g.get_pasajero().get_id(),
                "nombre":      g.get_pasajero().get_nombre(),
                "edad":        g.get_pasajero().get_edad(),
                "telefono":    g.get_pasajero().get_numtlf(),
                "id_vuelo":    g.get_vuelo().get_id_vuelo(),
                "num_asiento": g.get_asiento().get_num_asi()

            })

    """Se crea el archivo "reservas.json" en modo escritura (w), se hace uso del utf-8 para que permita tildes
       despues lo guarda el archivo en la variable f
"""
    with open(ARCHIVO_RESERVAS, "w", encoding="utf-8") as f: #with open cierra automáticamente al salir del bloque
        json.dump(datos, f, indent=2, ensure_ascii=False) #dump guarda el archivo json y ensure_ascii hace que las tildes se lean

def cargar_reservas():
    global contador_cod_re #Global se utiliza para usar una variable global en este caso seria el contador de reserva, se le pidio ayuda a la ia en esto porqu daba errore al usar return
    
    if not os.path.exists(ARCHIVO_RESERVAS): #Lee si hay o no un archivo path
        print("No se encontró archivo de reservas guardadas.")
        return

    with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as f :
        """Se hace uso del for para recorrer la lista de datos que se ha creado antes,
           y se verifica si esta el id_vuelo, si no esta sigue con la proxima iteracion,
           en caso que esxista guarda en la variable vuelo"""
        datos = json.load(f)#Carga el archivo JSON, y lo convierte en una lista para una facil lectura
    
    cargadas = 0 # Con este contador sabemos cuantas reservas fueron cargadas
    for d in datos:
        id_vuelo = d["id_vuelo"]
        if id_vuelo not in vuelos:
            continue #omite el resto del código en la iteracion actual y salta a la siguiente iteracion
        vuelo = vuelos[id_vuelo]

# Buscar el asiento por número
    """Recorre todos los asientos del vuelo buscando el que tiene el número guardado
       cuanod lo encuentra, lo guarda en asiento, y si no encontro el asiento o ya está ocupado,
       salta la reserva
    """
    asiento = None
    for a in vuelo.get_lista_asiento():
        if a.get_lista_asiento == d["num_asiento"]:
            asiento = a
            break
        if asiento is None or not asiento.get_dispo():
            continue

        """En este bloque buscamos reorganizar los datos de el archivo json en el objeto reserva,
        posteriormente llamamos a confrimar reserva para validar que el asiento efectivamente este bloqueado"""

        pasajero = Pasajero(d["id_pasajero"], d["nombre"], d["edad"], d["telefono"])
        r_cod = d["cod_reserva"]
        g = Reserva(r_cod, pasajero, vuelo, asiento)
        g.confirmar_reserva()
        reservas[r_cod] = g 
        if r_cod >= contador_cod:
            contador_cod = r_cod + 1
        cargadas += 1
    print(f" {cargadas} reserva(s) cargada(s) desde '{ARCHIVO_RESERVAS}'.")
