"""from Pasajeros import Pasajero

p1 = Pasajero(123456789123, "Samúel sapoperró  ", 21, "573137328358")

try:
print(p1.get_id())
print(p1.get_nombre())
except ValueError as e:
    print(f"Error: {e}")"""


"""from Asientos import AsientoEco, AsientoNorm, AsientoPrem

a1 = AsientoEco(1, 1, 50000)
a2 = AsientoNorm(2, 1, 80000)
a3 = AsientoPrem(3, 1, 120000)

print(a1.describir())
print(a2.describir())
print(a3.describir())

print(a1.get_precio())
print(a1.get_dispo())

a1.set_dispo(1)
print(a1.get_dispo())

try:
    a1.set_dispo(5)
except ValueError as e:
    print(f"Error: {e}")"""

from Vuelos import Vuelo

v1 = Vuelo("VU001", "10:00", "Bogota - Buenos Aires", 500000)

print(v1.get_id_vuelo())
print(v1.get_destino())
print(v1.get_precio_base_vu())

for asiento in v1.get_lista_asiento():
    print(asiento.get_num_asi(), asiento.describir(), asiento.get_dispo())