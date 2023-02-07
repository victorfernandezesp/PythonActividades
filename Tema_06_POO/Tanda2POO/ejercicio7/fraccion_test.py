"""
    Ejercicio 7:
        Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que
        podamos hacer las siguientes operaciones:

        - Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
            simplificada, no se puede dividir por cero.
        - Obtener resultado de la fracción (número real).
        - Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
        - Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_06_POO.Tanda2POO.ejercicio7.fraccion import Fraction

f1 = Fraction(7, 11)
print(f1)

f2 = f1 * 17.32
print(f2)

f3 = Fraction(3, 2)
f4 = Fraction(8, 6)
f5 = f3 + f4
print(f5)
f6 = f3 - f4
print(f6)

f7 = f3 * f4
print(f7)
f8 = f3 // f4
print(f8)

