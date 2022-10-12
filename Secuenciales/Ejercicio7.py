""" 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos
        corresponde.
       Este programa mediante una entrada por teclado de minutos que almacena en una variable, realizara una
       serie de cálculos y mediante un mensaje lo muestra por pantalla el resultado en horas y minutos.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce los minutos y te dire a cuantas horas y minutos corresponde ")
numero_minutos = int(input("¡Introduce el valor de los minutos, por favor! "))

horas = (numero_minutos // 60)
minutos = numero_minutos % 60

print("El resultado son ", horas, " horas y ", minutos, " minutos ")


