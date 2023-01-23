"""
    Ejercicio 3:
        Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos
        métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un
        test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de
        dicho rectángulo.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked

from Tema_06_POO.Tanda1POO.ejercicio2.point import Point


class Rectangulo:
    @typechecked
    def __init__(self, punto1: Point, punto2: Point):
        self.punto1 = punto1
        self.punto2 = punto2

    @property
    def punto1(self):
        return self.__punto1

    @punto1.setter
    @typechecked
    def punto1(self, value: Point):
        self.__punto1 = value

    @property
    def punto2(self):
        return self.__punto2

    @punto2.setter
    @typechecked
    def punto2(self, value: Point):
        self.__punto2 = value

    @property
    def perimetro(self):
        return (2 * abs(self.__punto1.coo_x - self.__punto2.coo_y)) + \
               (2 * abs(self.__punto1.coo_y - self.__punto2.coo_y))

    @property
    def area(self):
        return (abs(self.__punto1.coo_x - self.__punto2.coo_x)) * (abs(self.__punto1.coo_y - self.__punto2.coo_y))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__punto1}, {self.__punto2})"
