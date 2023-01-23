"""
    Ejercicio 3:
        Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos
        métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un
        test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de
        dicho rectángulo.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from rectangulo import Rectangulo
from Tema_06_POO.Tanda1POO.ejercicio2.point import Point

p1 = Point(2, 2)

p2 = Point(4, 8)

rectangulo = Rectangulo(p1, p2)
print(f"Perimetro: {rectangulo.perimetro} Area: {rectangulo.area}")
