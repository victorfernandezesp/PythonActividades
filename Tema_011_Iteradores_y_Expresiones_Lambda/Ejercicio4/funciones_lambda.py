"""
        Ejercicio 4:
        Vamos a probar los streams de Java, que están muy relacionados con las expresiones lambda, para ello, usando
        este artículo como referencia, vamos a crear una lista de 1000 números enteros aleatorios entre -5000 y 5000
        y usando streams vamos a averiguar:

            El máximo de los números pares.
            El mínimo de los números múltiplos de 3.
            El total de números negativos.
            El total de números primos.
            El máximo número primo.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import random
def main():
    lista_numeros = []
    for i in range(1000):
        lista_numeros.append(random.randint(-5000, 5000))

    max_numero = lambda list_: max(filter(lambda x: x % 2 == 0, list_))
    print(f"El par mas grande es:   {max_numero(lista_numeros)}")

    min_multiplo_3 = lambda list_: min(filter(lambda x: x % 3 == 0, list_))
    print(f"El minimo multiplo de 3 es:   {min_multiplo_3(lista_numeros)}")

    total_num_negativos = lambda list_: len(list(filter(lambda x: x < 0, list_)))
    print(f"El total de numeros negativos es:   {total_num_negativos(lista_numeros)}")

    # TODO Numero primo

if __name__ == '__main__':
    main()