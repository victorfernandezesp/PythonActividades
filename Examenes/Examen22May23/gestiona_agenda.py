"""
    Examen 22-Mayo-2023
    Programa de Prueba

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
import os
import xml.etree.ElementTree as ET

from Victor_Fernandez_Espana.addressbook import AddressBook
from Victor_Fernandez_Espana.menu import Menu


class NoExisteFicheroError(FileNotFoundError):
    def __init__(self, archivo):
        super().__init__(f"Lo siento pero ese nombre de archivo no existe, introduce uno que sí exista. Recibido ({archivo}).")
        self.archivo = archivo

class AccesoAlArchivoError(PermissionError):
    def __init__(self, archivo):
        super().__init__(f"Lo siento pero el acceso a ese archivo esta denegado.")
        self.archivo = archivo

class ExtensionArchivoError(ValueError):
    def __init__(self, extension):
        super().__init__(f"Lo siento pero el archivo tiene que tener la extension '.xml'.")
        self.extension = extension

def alta_contacto(agenda):
    nombre_nuevo_contacto = input("Escribe el nombre del nuevo contacto:    ")
    telefono_nuevo_contacto = input("Escribe el telefono del nuevo contacto:    ")
    correo_nuevo_contacto = input("Escribe el correo del nuevo contacto:    ")
    direccion_nuevo_contacto = input("Escribe la direccion del nuevo contacto (Pulsa Enter para no introducirla, no es obligatoria):    ")

    agenda.alta_contacto(nombre_nuevo_contacto, telefono_nuevo_contacto, correo_nuevo_contacto, direccion_nuevo_contacto)

def importar_archivo_desde_xml():
    nombre_fichero_xml = input("¿Cuál es el nombre del archivo XML, desde el que quieres importar la agenda?:   ")
    comprueba_fichero(nombre_fichero_xml)
    return AddressBook(nombre_fichero_xml)

def comprueba_fichero(fichero):
    try:
        fichero_comprueba = open(fichero, 'rt')
        fichero_comprueba.close()
    except FileNotFoundError:
        raise NoExisteFicheroError(fichero)
    except PermissionError:
        raise AccesoAlArchivoError(fichero)


def baja_contacto(agenda):
    nombre_baja_contacto = input("Escribe el nombre del contacto a eliminar:    ")
    agenda.baja_contacto(nombre_baja_contacto)



def listado_contactos(agenda):
    contactos = agenda.listar_contactos()
    for i in contactos:
        print(i)


def busqueda_contacto(agenda):
    nombre_busca_contacto = input("Escribe el nombre del contacto a buscar:    ")
    contacto = agenda.busca_contacto(nombre_busca_contacto)
    print(contacto)


def comprueba_si_existe_el_fichero(fichero):
    try:
        f = open(fichero, 'rt')
        f.close()
        return True
    except FileNotFoundError:
        return False

def exportar_a_xml(agenda):
    fichero = pregunta_nombre_archivo_xml_a_exportar()
    agenda.exportar_a_xml(fichero)

def pregunta_nombre_archivo_xml_a_exportar():
    while True:
        nombre_fichero = input("¿Cuál será el nombre del fichero XML?:   ")
        longitud_nombre_fichero = len(nombre_fichero) - 4
        extension = nombre_fichero[longitud_nombre_fichero:]
        if extension != ".xml":
            raise ExtensionArchivoError(extension)

        if not comprueba_si_existe_el_fichero(nombre_fichero):
            root = ET.Element('agenda')
            tree = ET.ElementTree(root)
            with open(nombre_fichero, 'wb') as f:
                tree.write(f, encoding='utf-8', xml_declaration=True)
            print(f"Fichero {nombre_fichero} creado correctamente")
            return nombre_fichero
        else:
            sobreescribe = input(f"El archivo {nombre_fichero} existe, si no desea continuar introduzca N:   ")
            if sobreescribe.upper() == "N":
                continue
            else:
                os.remove(nombre_fichero)

                root = ET.Element('agenda')
                tree = ET.ElementTree(root)
                with open(nombre_fichero, 'wb') as f:
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                print(f"Fichero {nombre_fichero} creado correctamente")
                return nombre_fichero


def main():
    SALIDA_DEL_PROGRAMA_CON_EXITO = 0
    agenda = AddressBook()
    menu_anade_pregunta = Menu("AGENDA",
                 "Crear agenda desde XML.",
                 "Alta de contacto.",
                 "Baja de contacto.",
                 "Búsqueda de contacto.",
                 "Listado de contactos.",
                 "Exportar a XML."
                    )

    while True:
        option = menu_anade_pregunta.escoger()
        match option:

            case 1:
                agenda = importar_archivo_desde_xml()
            case 2:
                alta_contacto(agenda)
            case 3:
                baja_contacto(agenda)
            case 4:
                busqueda_contacto(agenda)
            case 5:
                listado_contactos(agenda)
            case 6:
                exportar_a_xml(agenda)
            case 7:
                print("¡Hasta la próxima ^_^!")
                sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
            case _:
                print("Ha introducido una opcion incorrecta, vuelva a intentarlo.")



if __name__ == '__main__':
    main()