"""
    Autotest V4:
        1. Crear fichero de test.

        Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
        La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.
        Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
        Finalmente se creará el fichero correspondiente.


    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import os
import xml.etree.ElementTree as ET


def comprueba_si_existe_el_fichero(fichero):
    try:
        f = open(fichero, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False


def crear_fichero_test():
    while True:
        extension, nombre_fichero = pregunta_archivo()
        if ".json" in extension:
            if not comprueba_si_existe_el_fichero(nombre_fichero):
                f = open(nombre_fichero, 'wt')
                f.close()
                print(f"Fichero {nombre_fichero} creado correctamente")
                break
            else:
                sobreescribe = input(f"El archivo {nombre_fichero} existe, si no desea continuar introduzca N:   ")
                if sobreescribe.upper() == "N":
                    continue
                else:
                    os.remove(nombre_fichero)
                    f = open(nombre_fichero, 'wt')
                    f.close()
                    print(f"Fichero {nombre_fichero} creado correctamente")
                    break


        elif ".xml" in extension:
            extension = extension[1:]
            if not comprueba_si_existe_el_fichero(nombre_fichero):
                root = ET.Element('test')
                tree = ET.ElementTree(root)
                with open(nombre_fichero, 'wb') as f:
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                print(f"Fichero {nombre_fichero} creado correctamente")
                break
            else:
                sobreescribe = input(f"El archivo {nombre_fichero} existe, si no desea continuar introduzca N:   ")
                if sobreescribe.upper() == "N":
                    continue
                else:
                    os.remove(nombre_fichero)

                    root = ET.Element('test')
                    tree = ET.ElementTree(root)
                    with open(nombre_fichero, 'wb') as f:
                        tree.write(f, encoding='utf-8', xml_declaration=True)
                    print(f"Fichero {nombre_fichero} creado correctamente")
                    break
        else:
            print("Tiene que tener extension .json o .xml")
            continue


def pregunta_archivo():
    nombre_fichero = input("Cual sera el nombre del fichero?:   ")
    longitud_nombre_fichero = len(nombre_fichero)
    extension = nombre_fichero[(longitud_nombre_fichero - 5):]
    return extension, nombre_fichero


if __name__ == '__main__':
    crear_fichero_test()