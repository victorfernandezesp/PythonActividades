"""
    Ejercicio 6:
        Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de
        tiempo y se crean de la forma:

        t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

        t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

        t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

        Crea los getters y setters mediante propiedades y métodos para:

        -   Sumar y restar objetos de la clase (el resultado es otro objeto).
        -   Sumar y restar segundos, minutos y/u horas (se cambia el objeto actual).
        -   Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea
            10 h 35 m 5 s.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from Tema_06_POO.Tanda2POO.ejercicio6.tiempo import Duration


t1 = Duration(1, 20, 30)

t2 = Duration(2, 75, -10)

t3 = Duration(t2)

print(f"{t1 + t2}")
print(f"{t1 - t2}")

t1.sumar_al_objeto(1, 20, 30)
print(f"{t1}")

t1 = Duration(1, 20, 30)
t1.restar_al_objeto(1, 20, 29)
print(f"{t1}")
