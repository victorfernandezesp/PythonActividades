""" 18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

       Este programa mediante una entrada por teclado de nombre, apellido1 y apellido2 en varias variables, realizara
       una serie de cálculos para adivinar las iniciales y mediante un mensaje lo muestra por pantalla el resultado.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce los datos que se le pedirán a continuación para mostrar sus iniciales!")
nombre = str(input("¡Introduce tu Nombre, por favor! "))
apellido1 = str(input("¡Introduce tu Apellido Nº1, por favor! "))
apellido2 = str(input("¡Introduce tu Apellido Nº2, por favor! "))

iniciales = (nombre[0] + apellido1[0] + apellido2[0]).upper()

print(" Tus iniciales son ", iniciales)