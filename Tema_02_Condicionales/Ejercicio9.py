""" Ejercicio 9.
    Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si
    el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o
    acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un
    carácter» si el usuario ha introducido más de un carácter.

Pista: quizás te pueda venir bien usar el método find de la clase str.

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te muestra si el carácter introducido por teclado es un signo de puntuación, es una letra o un "
      "digito")
char = str(input("Introduce tu carácter, por favor! "))
if len(char) == 1:

    if char in ".:;()[]¡!¿?'\",-/—:":
        print(f"El carácter {char} es un signo de puntuación")

    elif char.isalpha():
        print(f"El carácter {char} es una letra ")

    elif char.isdigit():
        print(f"El carácter {char} es un número ")
    else:
        print(f"Es otro carácter")
else:
    print("Carácter no aceptado, debes introducir un solo carácter ")
