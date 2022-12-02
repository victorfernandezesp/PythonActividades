""" Ejercicio 17.
        Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y
        muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

        Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
        Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número
        incorrecto.”.
        Ejemplo:

        Introduzca número del dado: 5
        En la cara opuesta está el "dos".
    Author: Victor Fernandez España
    Curso:  2022-2003
"""
import sys

NUMERO_CARA_ERROR = 1
print("Este programa te dice la cara opuesta del dado ")

dado = int(input("Introduce el numero de la cara, por favor! "))
if 0 > dado or dado > 6:
    print(f"ERROR. Tiene que ser un numero entre 1 y 6 ", file=sys.stderr)
    sys.exit(NUMERO_CARA_ERROR)

match dado:
    case 1:
        print("La cara opuesta es el 6")
    case 2:
        print("La cara opuesta es el 5")
    case 3:
        print("La cara opuesta es el 4")
    case 4:
        print("La cara opuesta es el 3")
    case 5:
        print("La cara opuesta es el 2")
    case 6:
        print("La cara opuesta es el 1")

