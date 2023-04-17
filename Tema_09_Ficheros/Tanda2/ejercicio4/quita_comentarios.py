"""
        Ejercicio 4:
            Escribe un programa capaz de quitar los comentarios de un programa de Java.

            Se utilizaría de la siguiente manera:

            python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

            Por ejemplo:

            python quita-comentarios.py Holav1.java Holav2.java

            crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.

            P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de
            error correspondiente.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


def main():
    with open("Holav1.java", 'r') as archivo_para_lectura1:
        archivo = archivo_para_lectura1.read()

    cadena = str(archivo)
    cadena = elimina_comentarios_en_linea(cadena, "//", "\n")
    cadena = elimina_comentarios_en_bloque(cadena, "/*", "*/")

    print("------------------")
    print(cadena)
    print("------------------")


def elimina_comentarios_en_linea(cadena, caracter_inicial, caracter_final):
    while True:
        comentario_linea = cadena.find(caracter_inicial)
        final_comentario_linea = cadena.find(caracter_final, comentario_linea)
        cadena = cadena[0:comentario_linea] + cadena[final_comentario_linea:]
        if comentario_linea == -1:
            break
    return cadena


def elimina_comentarios_en_bloque(cadena, caracter_inicial, caracter_final):
    while True:
        comentario_bloque = cadena.find(caracter_inicial)
        if comentario_bloque == -1:
            break
        final_comentario_bloque = cadena.find(caracter_final, comentario_bloque)
        cadena = cadena[0:comentario_bloque] + cadena[(final_comentario_bloque + 2):]

    return cadena


if __name__ == '__main__':
    main()
