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


def main():
    comprueba_numero_de_argumentos()
    nombre_archivo1 = sys.argv[1]
    nombre_archivo2 = sys.argv[2]
    nombre_archivo_final = sys.argv[3]

    lista1 = almacena_en_lista_contenido_del_archivo(nombre_archivo1)
    lista2 = almacena_en_lista_contenido_del_archivo(nombre_archivo2)

    archivo_mas_grande = almacena_longitud_del_archivo_mas_grande(lista1, lista2)

    mezcla_ficheros(archivo_mas_grande, lista1, lista2, nombre_archivo_final)
    print(f"Éxito con la operación, {nombre_archivo_final} creado correctamente.")


def mezcla_ficheros(archivo_mas_grande, lista1, lista2, nombre_archivo_final):
    with open(nombre_archivo_final, 'w') as archivo3:
        for j in range(archivo_mas_grande):
            if j < len(lista1):
                archivo3.write(str(lista1[j]))
            if j < len(lista2):
                archivo3.write(str(lista2[j]))


def almacena_longitud_del_archivo_mas_grande(lista1, lista2):
    if len(lista1) > len(lista2) or len(lista1) == len(lista2):
        archivo_mas_grande = len(lista1)
    else:
        archivo_mas_grande = len(lista2)
    return archivo_mas_grande


def almacena_en_lista_contenido_del_archivo(archivo):
    lista = []
    try:
        with open(archivo, 'r') as archivo_para_lectura:
            recorre = archivo_para_lectura.readlines()
            for i in recorre:
                lista.append(i)
    except FileNotFoundError:
        print("ERROR. El archivo no existe")
    return lista


def comprueba_numero_de_argumentos():
    if len(sys.argv) != 4:
        print("El número de argumentos es erróneo", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
