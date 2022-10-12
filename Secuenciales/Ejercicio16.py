""" 16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
        El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los
        dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
        alcanzará el vehículo más rápido al otro.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te calcula cuanto tarda el vehiculo 2 en alcanzar al vehiculo 1")
v1 = float(input("¡Introduce la velocidad a la que va el coche 1 en km/h, por favor! "))
v2 = float(input("¡Introduce la velocidad a la que va el coche 2 en km/h, por favor! "))
distance = float(input("Introduce la distancia entre los coches en km, por favor !"))

time_v = abs((distance/(v2-v1))*60)

print(f"Tardara {time_v} minutos")