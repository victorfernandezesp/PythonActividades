"""
        Ejercicio 3:
            Haz el ejercicio 1 usando una función generada.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
def funcion_generadora_de_primos(tope, posible_primo):
    for j in range(tope):
        if comprueba_primo(posible_primo):
            yield posible_primo
        posible_primo += 1

def comprueba_primo(numero):
    import math
    if numero <= 1:
        return False
    for divisor in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisor == 0:
            return False
    return True

if __name__ == '__main__':
    num_tope = int(input("Dame un numero y te dire todos los primos desde 1 hasta el numero que me digas (1, x]:   "))
    primo = 0
    for i in funcion_generadora_de_primos(num_tope, primo):
        print(i, end=" ")
    print()