""" Ejercicio 14.
        Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por
        teclado.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
print("Este programa te dice si hay una subcadena dentro de una cadena")
cadena = input("Introduce la cadena: ")
sub_cadena = input("Introduce la sub-cadena a buscar: ")
es_cadena = False
for i in range(len(cadena) - len(sub_cadena)):
    if sub_cadena == cadena[i:i + len(sub_cadena)]:
        es_cadena = True
        break

if es_cadena:
    print(f"La subcadena {sub_cadena} SI se encuentra en la cadena")
else:
    print(f"La subcadena {sub_cadena} NO se encuentra en la cadena")