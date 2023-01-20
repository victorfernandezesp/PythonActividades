"""
    Ejercicio 1:
    Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma
    probabilidad de salir y un programa de prueba.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_06_POO.Tanda1POO.ejercicio1.dice import Dado

dado = Dado()
dado.cara = dado.tirar_dado()
print(dado)
