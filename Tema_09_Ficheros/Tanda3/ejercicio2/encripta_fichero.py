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


def main():
    nombre_archivo1 = error_num_argumentos()
    nombre_archivo_final = sobreescribe_archivo(nombre_archivo1)
    error_archivo_no_existe(nombre_archivo1)
    error_no_puede_abrir_archivo_escritura(nombre_archivo_final)
    clave = int(input("Introduce la clave numerica(1-27):   "))
    if 1 > clave > 27:
        raise ValueError
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
    machaca = False
    with open(nombre_archivo1 + ".txt", 'r') as archivo_para_lectura1:
        recorre = archivo_para_lectura1.read()
        recorre = recorre.upper()
        encriptado = ""
        for i in recorre:
            if i in abecedario:
                posicion_letra = abecedario.index(i)
                posicion_letra += clave
                if posicion_letra > 26:
                    posicion_letra = posicion_letra - 27
                encriptado += str(abecedario[posicion_letra])
            else:
                encriptado += str(i)
    if not machaca:
        with open(nombre_archivo_final + ".txt", 'w') as archivo_para_escritura1:
            archivo_para_escritura1.write(encriptado)
    else:
        with open(nombre_archivo1 + ".txt", 'w') as archivo_para_escritura1:
            archivo_para_escritura1.write(encriptado)


def error_num_argumentos():
    try:
        nombre_archivo1 = sys.argv[1]
    except IndexError:
        print("Parametros insuficientes o fuera de rango, debes introducir minimo 1 argumento: "
              "Nombre de archivo", file=sys.stderr)
        sys.exit(1)
    return nombre_archivo1


def sobreescribe_archivo(nombre_archivo1):
    try:
        nombre_archivo_final = sys.argv[2]
    except IndexError:
        machaca_archivo = input("Machacará el archivo de origen, esta seguro? (S/N) ")
        machaca_archivo = machaca_archivo.upper()
        if machaca_archivo == "N":
            sys.exit(0)
        else:
            machaca = True
            nombre_archivo_final = nombre_archivo1
    return nombre_archivo_final


def error_archivo_no_existe(nombre_archivo1):
    try:
        f = open(nombre_archivo1 + ".txt", 'r')
        f.close()

    except FileNotFoundError:
        print("El archivo no existe", file=sys.stderr)
        sys.exit(2)


def error_no_puede_abrir_archivo_escritura(nombre_archivo_final):
    try:
        f = open(nombre_archivo_final + ".txt", 'w')
        f.close()
    except PermissionError:
        print("El archivo no se puede abrir", file=sys.stderr)
        sys.exit(3)


if __name__ == '__main__':
    main()