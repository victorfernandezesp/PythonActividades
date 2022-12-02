"""
    Ejercicio 2:

        Nos podemos aproximar al número PI usando la serie de Leibniz que dice que PI se puede
        obtener a partir de la siguiente sucesión: 4/1 – 4/3 + 4/5 – 4/7 + 4/9…
        Si te fijas, el 4 (numerador) es fijo, y el denominador se aumenta de 2 en 2. Además, en cada paso
        se intercambia el signo.
        Haz un programa que pidiendo el número de iteraciones nos de el valor de PI.



    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

numerador = 4
denominador = 1
contador = 0
acumulador = 0
iteraciones = int(input("¿Cuántas iteraciones quieres que muestre? "))
while contador <= iteraciones:
    valor_pi = numerador / denominador
    acumulador += valor_pi
    numerador *= -1
    denominador += 2
    contador += 1

print(f" El valor es {acumulador}")
