"""
        Ejercicio 1:
            Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero de texto.
            El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.
            El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
            palabras_sort.txt.
            Suponemos que cada palabra ocupa una línea.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

import sys
lista = []
if len(sys.argv) != 2:
    print("El número de argumentos es erróneo", file=sys.stderr)
    sys.exit(1)
try:
    nombre_archivo = sys.argv[1]
    ultimo_punto = nombre_archivo.rfind(".")
    ultimo_archivo = nombre_archivo[:ultimo_punto] + "_short" + nombre_archivo[ultimo_punto:]
    with open(nombre_archivo, 'r') as archivo2:
        recorre = archivo2.readlines()
        for i in recorre:
            lista.append(i)

    lista.sort()
    with open(ultimo_archivo, 'w') as archivo3:
        for j in lista:
            archivo3.write(j)

except FileNotFoundError:
    print("ERROR. El archivo no existe")

except IndexError:
    print("ERROR. No has pasado por linea de argumentos")

print(f"Éxito con la operación, {ultimo_archivo} creado correctamente.")
