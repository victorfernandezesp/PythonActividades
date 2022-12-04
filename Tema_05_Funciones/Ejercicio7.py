"""
    Ejercicio 7:

            Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de
             mezclar los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc.
             Los arrays a y b pueden tener longitudes diferentes; por tanto, si se terminan los números de un array
             se terminan de coger todos los que quedan del otro.

            Ejemplos:

            Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

            Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

            Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

            Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from bibliotecafunciones.funciones_matematicas.crea_array_de_n_parametros_comprendidos import crea_array


def mezcla_1(array_dos, array_mas_corto, array_mezcla, array_uno):
    for i in range(array_mas_corto):
        array_mezcla.append(array_uno[i])
        array_mezcla.append(array_dos[i])


def mezcla_de_forma(array_uno, array_dos):
    longitud_arr_a = len(array_uno)
    longitud_arr_b = len(array_dos)
    array_mezcla = []

    if longitud_arr_a > longitud_arr_b:
        array_mas_corto = longitud_arr_b
        mezcla_1(array_dos, array_mas_corto, array_mezcla, array_uno)
        array_mezcla.extend(array_uno[array_mas_corto:])

    elif longitud_arr_a < longitud_arr_b:
        array_mas_corto = longitud_arr_a
        mezcla_1(array_dos, array_mas_corto, array_mezcla, array_uno)
        array_mezcla.extend(array_dos[array_mas_corto:])

    else:
        array_mas_corto = longitud_arr_a
        mezcla_1(array_dos, array_mas_corto, array_mezcla, array_uno)

    return array_mezcla


array_a = crea_array()
print(f"El array A: {array_a}")
array_b = crea_array()
print(f"El array B: {array_b}")

print(f"El array mezclado es: {mezcla_de_forma(array_a, array_b)}")
