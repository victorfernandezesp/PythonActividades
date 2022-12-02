"""
    Ejercicio 3:

        Realiza un conversor del sistema decimal al sistema de “palotes”.
        Ejemplo:
        Por favor, introduzca un número entero positivo: 47021
        El 47021 en decimal es el | | | | - | | | | | | | - - | | - | en el sistema de palotes.
        Si no se introduce un número entero positivo el programa debe terminar de manera anormal con un
        mensaje de error.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

ERROR_NUMERO_NO_ENTERO_POSITIVO = 1

contador_guiones = 1
guion = "-"
concatenacion_total = ""

num_entero = input("Por favor, introduzca un número entero positivo: ")
if not num_entero.isdigit():
    print("ERROR. El número introducido solo acepta valores positivos, introduce solo enteros positivos",
          file=sys.stderr)
    sys.exit(ERROR_NUMERO_NO_ENTERO_POSITIVO)
longitud_num = len(num_entero)

for digito in num_entero:
    digito = int(digito)
    palos = "|" * digito
    concatenacion_parcial = palos
    if contador_guiones < longitud_num:
        concatenacion_parcial += guion
        contador_guiones += 1

    concatenacion_total += concatenacion_parcial
print(f"{concatenacion_total}")