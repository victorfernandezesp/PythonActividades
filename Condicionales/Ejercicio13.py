""" Ejercicio 13.
        Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
        Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

        Por ejemplo, si deseamos conocer el desglose de 434€, el programa mostrará por pantalla el siguiente resultado:

        2 billetes de 200 euros.
        1 billete de 20 euros.
        1 billete de 10 euros.
        2 monedas de 2 euros.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

print("Este programa te desglosa una cantidad de dinero en billetes y monedas ")
cantidad = int(input("Introduce la cantidad de dinero, por favor! "))
if cantidad <= 0:
    print(f"ERROR.{cantidad} no puede ser desglosado en una cantidad mencionada", file=sys.stderr)
    sys.exit(1)


billetes500 = cantidad // 500
rest500 = cantidad % 500

billetes200 = rest500 // 200
rest200 = rest500 % 200

billetes100 = rest200 // 100
rest100 = rest200 % 100

billetes50 = rest100 // 50
rest50 = rest100 % 50

billetes20 = rest50 // 20
rest20 = rest50 % 20

billetes10 = rest20 // 10
rest10 = rest20 % 10

billetes5 = rest10 // 5
rest5 = rest10 % 5

monedas2 = rest5 // 2
monedas1 = rest5 % 2

if billetes500 >= 1:
    print(f"Seria {billetes500} billetes de 500€")

if billetes200 >= 1:
    print(f"Seria {billetes200} billetes de 200€")

if billetes100 >= 1:
    print(f"Seria {billetes100} billetes de 100€")

if billetes50 >= 1:
    print(f"Seria {billetes50} billetes de 50€")

if billetes20 >= 1:
    print(f"Seria {billetes20} billetes de 20€")

if billetes10 >= 1:
    print(f"Seria {billetes10} billetes de 10€")

if billetes5 >= 1:
    print(f"Seria {billetes5} billetes de 5€")

if monedas2 >= 1:
    print(f"Seria {monedas2} monedas de 2€")

if monedas1 >= 1:
    print(f"Seria {monedas1} monedas de 1€")
