""" Ejercicio 8.
        Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import time

print("Este programa hace la funcion de un cronometro")
hora = 0
minutos = 0
segundos = 0
concatenado = 0
while concatenado != 235959:
    segundos += 1
    time.sleep(1)
    if segundos == 60:
        minutos += 1
        segundos -= 60
        if minutos == 60:
            hora += 1
            minutos -= 60
        if hora == 24:
            hora -= 24
            break
    concatenado = (hora + minutos + segundos)

    print(f"{hora}:{minutos}:{segundos}")
