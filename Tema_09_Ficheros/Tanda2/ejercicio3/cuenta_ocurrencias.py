"""
        Ejercicio 3:
            Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero. Tanto el nombre del
            fichero como la palabra se deben pasar como argumentos en la línea de comandos.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

nombre_de_fichero = sys.argv[1]
palabra_a_buscar = sys.argv[2]

palabras_del_fichero = ["hola", "marcao", "uno", "dos", "tres", "marcao", "cuatro", "cinco", "seis", "marcao", "siete"]

with open(nombre_de_fichero + ".txt", 'w') as archivo_para_escritura1:
    for i in palabras_del_fichero:
        archivo_para_escritura1.write(i + "\n")

lista1 = []
with open(nombre_de_fichero + ".txt", 'r') as archivo_para_lectura1:
    recorre = archivo_para_lectura1.readlines()
    for i in recorre:
        lista1.append(i)

cantidad = lista1.count(palabra_a_buscar + "\n")
print(f"La palabra: {palabra_a_buscar} aparece en el fichero: {cantidad} veces. ")
