# 5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Author: Victor Fernandez España
# En este programa se introducirá 1 valor por teclado el cual se transformara a Celsius cuyo
# resultado se mostrara por pantalla

# Introducimos por teclado los grados con los cuales vamos a trabajar
Fahrenheit = float(input("Introduce los grados Fahrenheit "))

# Realizamos la operación
Celsius = (Fahrenheit - 32) * 5 / 9

# Mostramos por pantalla los resultados
print("Los grados Fahrenheit al cambio, son ", Celsius, "º Celsius ")