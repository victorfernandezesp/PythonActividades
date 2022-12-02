""" Ejercicio 1.
        Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
        A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
        introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina
        cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de
        intentos te muestra el número que había generado.

        Para usar números aleatorios en Python:
        http://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
import sys
from random import randrange

NUMERO_INTENTOS = 10

NUM_MAXIMO = 100

NUM_MINIMO = 1

print("Este programa genera un numero al azar y tienes 10 intentos para adivinarlo ")
numero_azar = randrange(NUM_MINIMO, NUM_MAXIMO)
intentos = 0
while True:
    numero_usuario = int(input("Introduce un numero entero y te dire si has acertado "))
    if 1 > numero_usuario or numero_usuario > NUM_MAXIMO:
        print(f"ERROR. Tiene que ser un numero entre 1 y 100 ", file=sys.stderr)
        sys.exit(1)
    if numero_usuario > numero_azar:
        print(f"{numero_usuario} es MAYOR que el numero random, prueba a poner un numero mas pequeño ")
    else:
        print(f"{numero_usuario} es MENOR que el numero random, prueba a poner un numero mas grande ")

    intentos += 1

    print(f"Llevas {intentos} intentos, te quedan {NUMERO_INTENTOS - intentos}")
    if numero_usuario == numero_azar or intentos == NUMERO_INTENTOS:
        if numero_usuario == numero_azar:
            print("Enhorabuena, has acertado")
        else:
            print(f"Has agotado tus intentos y el numero era {numero_azar}")

        break