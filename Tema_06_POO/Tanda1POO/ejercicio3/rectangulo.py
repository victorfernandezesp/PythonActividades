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


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.x1 = punto1.coo_x
        self.y1 = punto1.coo_y
        self.x2 = punto2.coo_x
        self.y2 = punto2.coo_y

    @property
    def x1(self):
        return self.__x1

    @x1.setter
    @typechecked
    def x1(self, value: int):
        self.__x1 = value

    @property
    def y1(self):
        return self.__y1

    @y1.setter
    @typechecked
    def y1(self, value: int):
        self.__y1 = value

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    @typechecked
    def x2(self, value: int):
        self.__x2 = value

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    @typechecked
    def y2(self, value: int):
        self.__y2 = value

    def calcular_perimetro(self):
        perimetro = (2 * abs(self.__x2 - self.__x1)) + (2 * abs(self.__y2 - self.__y1))
        return perimetro

    def calcular_area(self):
        area = (abs(self.__x2 - self.__x1)) * (abs(self.__y2 - self.__y1))
        return area

    def __repr__(self):
        return f"{self.__class__.__name__}()"
