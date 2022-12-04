"""
    Ejercicio 6:
        Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

        Por ejemplo, el 213 es el . . _ _ _ . _ _ _ _ . . . _ _ en Morse. Utiliza esta función en un programa para
        comprobar que funciona bien.

        Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

        Los números en Morse los puedes encontrar aquí.
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys


def convertir_numeros_a_morse(numero):
    concatena = ""
    for i in numero:
        num = int(i)
        match num:
            case 1:
                concatena += ".----"

            case 2:
                concatena += "..---"

            case 3:
                concatena += "...--"

            case 4:
                concatena += "....-"

            case 5:
                concatena += "....."

            case 6:
                concatena += "-...."

            case 7:
                concatena += "--..."

            case 8:
                concatena += "---.."

            case 9:
                concatena += "----."

            case 0:
                concatena += "-----"

    return concatena


ERROR_NUMERO_NO_ENTERO_POSITIVO = 1

num_entero = input("Por favor, introduzca un número: ")
if not num_entero.isdigit():
    print("ERROR. El número introducido solo acepta valores positivos, introduce solo enteros positivos",
          file=sys.stderr)
    sys.exit(ERROR_NUMERO_NO_ENTERO_POSITIVO)

print(f"{convertir_numeros_a_morse(num_entero)}")
