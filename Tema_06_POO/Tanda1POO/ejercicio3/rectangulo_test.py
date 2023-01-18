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

punto1 = Point()
punto1.coo_x = 2
punto1.coo_y = 2

punto2 = Point()
punto2.coo_x = 4
punto2.coo_y = 8

rectangulo = Rectangulo()
rectangulo.base = rectangulo.distancia_entre_puntos(punto1.coo_x, punto2.coo_x)
rectangulo.altura = rectangulo.distancia_entre_puntos(punto1.coo_y, punto2.coo_y)

print(f"Perimetro: {rectangulo.calculo_perimetro(rectangulo.base, rectangulo.altura)}")
print(f"Area: {rectangulo.calculo_area(rectangulo.base, rectangulo.altura)}")
