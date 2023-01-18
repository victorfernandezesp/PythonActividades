"""
    Ejercicio 3:
        Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos
        métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un
        test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de
        dicho rectángulo.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


class Rectangulo:
    def __init__(self):
        self.perimetro = 0
        self.area = 0
        self.distancia = 0
        self.base = 0
        self.altura = 0

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    @property
    def perimetro(self):
        return self.__perimetro

    @property
    def area(self):
        return self.__area

    @property
    def distancia(self):
        return self.__distancia

    def distancia_entre_puntos(self, c1, c2):
        self.distancia = abs(c2) - abs(c1)
        return self.__distancia

    @distancia.setter
    def distancia(self, value):
        self.__distancia = value

    @base.setter
    def base(self, value):
        self.__base = value

    @altura.setter
    def altura(self, value):
        self.__altura = value

    def calculo_perimetro(self, base, altura):
        self.perimetro = (base * 2) + (altura * 2)
        return self.__perimetro

    def calculo_area(self, base, altura):
        self.area = base * altura
        return self.__area

    @perimetro.setter
    def perimetro(self, value):
        self.__perimetro = value

    @area.setter
    def area(self, value):
        self.__area = value
