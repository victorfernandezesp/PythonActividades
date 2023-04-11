"""
        Ejercicio 1:
            Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


def main():
    archivo = open("primos.txt", "w")

    for i in range(1, 501):
        if es_primo(i):
            archivo.write(str(i) + "\n")
    archivo.close()


def es_primo(num):
    if num < 2:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


if __name__ == '__main__':
    main()
