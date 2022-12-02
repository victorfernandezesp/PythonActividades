""" 5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
       Este programa mediante una entrada por teclado almacena en 1 variables, los grados Fahrenheit luego realiza una
       serie de cálculos y mediante un mensaje lo muestra por pantalla el resultado en Celsius.
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("¡Introduce los grados Fahrenheit y los pasare a Celsius ")
Fahrenheit = float(input("¡Introduce el valor de los grados Fahrenheit, por favor! "))

Celsius = (Fahrenheit - 32) * 5 / 9

print("El resultado de pasar los ", Fahrenheit, " grados Fahrenheit a grados Celsius es ", Celsius)


