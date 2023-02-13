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


def maximo_comun_divisor(numero_1, numero_2):
    a1 = numero_1
    b1 = numero_2
    while b1 != 0:
        aux = b1
        b1 = a1 % b1
        a1 = aux
    return a1


def minimo_comun_multiplo(numero_1, numero_2):
    mcd = maximo_comun_divisor(numero_1, numero_2)
    mcm = (numero_1 * numero_2) // mcd
    return mcm


@typechecked
class Fraction:
    def __init__(self, numerador, denominador):
        if denominador < 0:
            numerador *= -1
            denominador *= -1

        self.__numerador = numerador
        self.__denominador = denominador
        self.__simplificar()

    def __simplificar(self):
        mcd = maximo_comun_divisor(self.numerador, self.denominador)
        self.__numerador = self.numerador // mcd
        self.__denominador = self.denominador // mcd

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        if self.__denominador == 0:
            raise ValueError("No se puede dividir por 0")
        return self.__denominador

    def resultado_de_la_fraccion(self):
        return self.__numerador / self.__denominador

    def multiplica_por_numero(self, numero):
        self.__numerador *= numero
        self.__denominador *= 1
        self.__simplificar()

    def igualar_denominador(self, other):
        mcm = minimo_comun_multiplo(self.__denominador, other.__denominador)
        self.__numerador *= mcm // self.__denominador
        other.__numerador *= mcm // other.__denominador
        self.__denominador = mcm
        other.__denominador = mcm

    def __add__(self, other):
        self.igualar_denominador(other)
        return Fraction(self.__numerador + other.__numerador, self.__denominador)

    def __sub__(self, other):
        self.igualar_denominador(other)
        return Fraction(self.__numerador - other.__numerador, self.__denominador)

    def __mul__(self, other):
        return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)

    def __rmul__(self, other):
        return Fraction.__mul__(self, other)

    def __floordiv__(self, other):
        return Fraction(self.__numerador * other.__denominador, self.__denominador * other.__numerador)

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}/{self.__denominador} )"
