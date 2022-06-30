# 9. Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo
# si el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula
# o acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un
# carácter» si el usuario ha introducido más de un carácter.
#
# Pista: quizás te pueda venir bien usar el método find de la clase str.
# Author: Victor Fernandez España

# Introducimos por teclado el número con el que vamos a trabajar
character = str(input("Introduce una cadena por teclado: "))

print(f"-----------------------------------------------------------------")
# Realizamos las distintas operaciones
if len(character) == 1 and character in ".:;()[]¡!¿?'\",-/—:":
    print(f"Es un character")

elif len(character) and 'a' <= character <= 'z' or 'A' <= character <= 'Z':
    print(f"Es una letra")

elif len(character) and character.isdigit():
    print(f"Es un numero ")

else:
    print("No es un character valido")
