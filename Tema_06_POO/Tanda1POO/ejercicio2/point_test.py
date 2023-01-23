"""
    Ejercicio 2:
        Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y
        setters (propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además, la clase
        debe tener un __str__() para poder imprimir los puntos en formato “(x, y)”. Implementa un test donde crees un
        punto, lo imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su
        coordenada x, y vuelvas a imprimir el punto.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from point import Point

punto = Point(2, 4)

print(f"Punto: ({punto.coo_x}, {punto.coo_y})")
punto.invert_coordinates()
print(f"Punto invertido: {punto}")