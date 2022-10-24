""" Ejercicio 15.
        El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a
        cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si
        son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de
        30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
        número de alumnos. Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe
        pagar cada alumno por el viaje.


        En este ejercicio mediante input pedimos el numero de asistentes que acudirán y mediante las condiciones vamos a
        calcular  el importe por niño o el total.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

ALUMNOS_MAS_O_IGUAL_100 = 65
ALUMNOS_MAS_O_IGUAL_50 = 70
ALUMNOS_MAS_O_IGUAL_30 = 95
ERROR_NUMERO_ALUMNOS_MENOR_O_IGUAL_0 = 1
print("Este programa te calcula el precio del viaje según el numero de niños que asistan ")

alumnos = int(input("Introduce el numero de niños que asistirán, por favor! "))
if alumnos <= 0:
    print(f"ERROR. Tiene que haber un numero de alumnos superior a 0", file=sys.stderr)
    sys.exit(ERROR_NUMERO_ALUMNOS_MENOR_O_IGUAL_0)

if alumnos >= 100:
    print(f"El precio por niño es de {ALUMNOS_MAS_O_IGUAL_100} el total es {alumnos * ALUMNOS_MAS_O_IGUAL_100} €")

elif alumnos >= 50:
    print(f"El precio por niño es de {ALUMNOS_MAS_O_IGUAL_50} el total es {alumnos * ALUMNOS_MAS_O_IGUAL_50} €")

elif alumnos >= 30:
    print(f"El precio por niño es de {ALUMNOS_MAS_O_IGUAL_30} el total es {alumnos * ALUMNOS_MAS_O_IGUAL_30} €")

else:
    print(f"El precio por niño es de {4000/alumnos} €")