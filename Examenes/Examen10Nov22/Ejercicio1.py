"""
    Ejercicio 1:

         Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El
        programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo
        siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto
        satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.
        Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera
        anormal con un mensaje de error.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

INTENTOS_CAJA_FUERTE_PREESTABLECIDOS = 4

ERROR_NO_SON_CIFRAS_NUMERICAS = 2

ERROR_LONGITUD_DISTINTO_A_4 = 1

contrasena = "1234"
intentos = 0
while True:
    combinacion = input("Introduce la contraseña de 4 cifras para abrir la caja fuerte: ")
    if len(combinacion) != 4:
        print("ERROR. Tu contraseña tiene que tener una longitud de 4 cifras", file=sys.stderr)
        sys.exit(ERROR_LONGITUD_DISTINTO_A_4)

    if not combinacion.isdigit():
        print("ERROR. Tu combinacion no debe contener otros caracteres ajenos a los digitos", file=sys.stderr)
        sys.exit(ERROR_NO_SON_CIFRAS_NUMERICAS)

    if combinacion == contrasena:
        print("La caja fuerte se ha abierto satisfactoriamente.")
        intentos += 1
        break
    else:
        print("Lo siento, esa no es la combinación.")
        intentos += 1
        print(f"Te quedan {INTENTOS_CAJA_FUERTE_PREESTABLECIDOS-intentos} intentos")

    if intentos == INTENTOS_CAJA_FUERTE_PREESTABLECIDOS:
        print("Has agotado todos los intentos")
        break