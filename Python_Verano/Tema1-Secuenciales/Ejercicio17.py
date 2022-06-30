# 17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra
# ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
hour_exit = int(input("Introduce la hora a la que salio el ciclista "))
min_exit = int(input("Introduce el minuto al que salio el ciclista "))
sec_exit = int(input("Introduce el segundo al que salio el ciclista "))
print(f"-----------------------------------------------------------------")
travel_time = int(input("Introduce el numero de segundos que tardo en llegar el ciclista "))
print(f"-----------------------------------------------------------------")


# Realizamos las distintas operaciones
chg_hour_to_seconds = hour_exit * 3600
chg_min_to_seconds = min_exit * 60
seconds_free = sec_exit + travel_time
tot_seconds = chg_hour_to_seconds + chg_min_to_seconds + seconds_free

final_hour = int(tot_seconds/3600)
final_min = int((tot_seconds % 3600)/60)
final_sec = int((tot_seconds % 3600) % 60)


# Mostramos por pantalla los resultados

print(f"Llego a las: {final_hour}:{final_min}:{final_sec}")
