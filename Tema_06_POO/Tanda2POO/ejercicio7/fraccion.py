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

from bibliotecafunciones.funciones_matematicas.mcd_y_mcm import maximo_comun_divisor


@typechecked
class Fraction:
    def __init__(self, numerador: int, denominador: int):
        if self.__denominador == 0:
            raise ValueError("No se puede dividir por 0")
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
        return self.__denominador

    def resultado(self):
        return self.__numerador / self.__denominador

    def __add__(self, other: 'Fraction'):
        return Fraction(self.__numerador * other.__denominador + other.__numerador * self.__denominador,
                        self.__denominador * other.__denominador)

    def __sub__(self, other: 'Fraction'):
        return self + other * -1

    def __mul__(self, other: (int, 'Fraction')):
        if isinstance(other, Fraction):
            return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)
        return Fraction(self.__numerador * other, self.__denominador)

    def __rmul__(self, other: int):
        return self * other

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.__numerador * other.__denominador, self.__denominador * other.__numerador)

    # Esto también funcionaria con fracciones equivalentes, pero no va a ocurrir, ya que simplificamos en el
    # constructor.
    def __eq__(self, other: 'Fraction'):
        return (self.__numerador, self.__denominador) == (other.__numerador, other.__denominador)

    def __ne__(self, other: 'Fraction'):
        return not self == other

    def __lt__(self, other: 'Fraction'):
        return self.__numerador * other.__denominador < other.__numerador * self.__denominador

    def __gt__(self, other: 'Fraction'):
        return (not self == other) and (not self < other)

    def __le__(self, other: 'Fraction'):
        return not self > other

    def __ge__(self, other: 'Fraction'):
        return not self < other

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}/{self.__denominador} )"
