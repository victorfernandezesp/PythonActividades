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

# Comprobaciones normales
f1 = Fraction(5, 3)
valor = f1.resultado()
print(f"Resultado de la fraccion: {valor}")
f1.multiplica_por_numero(3)
print(f"Resultado de multiplicar por 3: {f1}")

f1 = Fraction(5, 3)
f2 = Fraction(8, 7)
f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")

f1 = Fraction(5, 3)
f2 = Fraction(8, 7)
f4 = f1 - f2
print(f"{f1} - {f2} = {f4}")

f1 = Fraction(5, 3)
f2 = Fraction(8, 7)
f5 = f1 * f2
print(f"{f1} * {f2} = {f5}")

f1 = Fraction(5, 3)
f2 = Fraction(8, 7)
f6 = f2 * f1
print(f"{f2} * {f1} = {f6}")

f1 = Fraction(5, 3)
f2 = Fraction(8, 7)
f7 = f1 // f2
print(f"{f1} // {f2} = {f7}")

# Comprobación denominador negativo
f1 = Fraction(5, -3)
f2 = Fraction(8, 7)
f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")

# Comprobación numerador y denominador negativo
f1 = Fraction(-5, -3)
f2 = Fraction(8, 7)
f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")

# Comprobación numerador negativo
f1 = Fraction(-5, 3)
f2 = Fraction(8, 7)
f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")

# Comprobación denominador negativo
"""f1 = Fraction(-5, 0)"""
