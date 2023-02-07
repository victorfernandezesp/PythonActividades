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
from typeguard import typechecked


@typechecked
class Fraction:
    def __init__(self, *valores):
        if len(valores) == 1 and isinstance(valores[0], Fraction):
            self.valores = list(valores[0].valores[:])
        else:
            self.valores = list(valores)

        a = self.valores[0]
        b = self.valores[1]

        if b == 0:
            raise ValueError("El denominador no puede ser 0")

        while b != 0:
            aux = b
            b = a % b
            a = aux

        self.__numerador = self.valores[0] // a
        self.__denominador = self.valores[1] // a

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def resultado_de_la_fraccion(self):
        return self.__numerador / self.__denominador

    def multiplica_por_numero(self, numero):
        self.__numerador *= numero
        self.__denominador *= 1

    def __add__(self, other):
        return Fraction(self.__numerador + other.__numerador, self.__denominador + other.__denominador)

    def __sub__(self, other):
        return Fraction(self.__numerador - other.__numerador, self.__denominador - other.__denominador)

    def __mul__(self, other):
        return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)

    def __rmul__(self, other):
        return Fraction.__mul__(self, other)

    def __floordiv__(self, other):
        return Fraction(self.__numerador / other.__numerador, self.__denominador / other.__denominador)

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}/{self.__denominador} )"
