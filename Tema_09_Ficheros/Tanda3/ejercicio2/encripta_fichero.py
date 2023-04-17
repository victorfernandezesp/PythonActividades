"""
        Ejercicio 2:

            Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que
            también pasamos como parámetro, de manera que:

            *   Si el programa no recibe el número de parámetros adecuado termina con un error 1.

            *   Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que
                lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación
                no se haga.

            *   Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de
                error y código 2.

            *   Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina
                con un mensaje de error y código 3.

            *   Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

try:
    nombre_archivo1 = sys.argv[1]
except IndexError:
    print("Parametros insuficientes o fuera de rango, debes introducir minimo 1 argumento: Nombre de archivo")
    sys.exit(1)

try:
    nombre_archivo_final = sys.argv[2]
except IndexError:
    machaca_archivo = input("Machacará el archivo de origen, esta seguro? (S/N) ")
    machaca_archivo = machaca_archivo.upper()
    if machaca_archivo == "N":
        pass


