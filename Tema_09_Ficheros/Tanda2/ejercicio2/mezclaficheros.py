"""
        Ejercicio 2:
            Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el
            fichero resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea
            será del primer fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer
            fichero, etc.

            Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la
            línea de comandos.

            Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños
            diferentes.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

nombre_archivo1 = sys.argv[1]
nombre_archivo2 = sys.argv[2]
nombre_archivo_final = sys.argv[3]
lista_mas_grande = 0

with open(nombre_archivo1 + ".txt", 'w') as archivo_para_escritura1:
    while True:
        palabra = input(f"Que palabra quieres guardar en el archivo: {nombre_archivo1}(Introduce enter si no quieres "
                        f"introducir mas):  ")
        if palabra == "":
            print("______________________________________")
            break
        archivo_para_escritura1.write(palabra + "\n")

lista1 = []
with open(nombre_archivo1 + ".txt", 'r') as archivo_para_lectura1:
    recorre = archivo_para_lectura1.readlines()
    for i in recorre:
        lista1.append(i)


with open(nombre_archivo2 + ".txt", 'w') as archivo_para_escritura2:
    while True:
        palabra2 = input(f"Que palabra quieres guardar en el archivo: {nombre_archivo2}(Introduce enter si no quieres "
                        f"introducir mas):  ")
        if palabra2 == "":
            print("______________________________________")
            break
        archivo_para_escritura2.write(palabra2 + "\n")

lista2 = []
with open(nombre_archivo2 + ".txt", 'r') as archivo_para_lectura2:
    recorre = archivo_para_lectura2.readlines()
    for i in recorre:
        lista2.append(i)

if len(lista1) > len(lista2) or len(lista1) == len(lista2):
    lista_mas_grande = len(lista1)
else:
    lista_mas_grande = len(lista2)

with open(nombre_archivo_final + ".txt", 'w') as archivo3:
    for j in range(lista_mas_grande):
        if j < len(lista1):
            archivo3.write(str(lista1[j]))
        if j < len(lista2):
            archivo3.write(str(lista2[j]))
