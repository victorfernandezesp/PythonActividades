# 16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está
# detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km)
# y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más
# rápido al otro.

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar

v1 = float(input("Introduce la velocidad a la que va el coche 1 en km/h "))
v2 = float(input("Introduce la velocidad a la que va el coche 2 en km/h "))
distance = float(input("Introduce la distancia entre los coches en km "))

# Realizamos las distintas operaciones
time_v = abs((distance/(v2-v1))*60)


# Mostramos por pantalla los resultados

print(f"Tardara {time_v} minutos")