"""
    Examen 22-Mayo-2023
    Clase AddressBook

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import xml.etree.ElementTree as ET

from Victor_Fernandez_Espana.contact import Contact


class LongitudNombreArchivoXMLError(ValueError):
    def __init__(self, archivo):
        super().__init__(f"La longitud del nombre del archivo no puede ser menor de 5(ej: x.xml). Recibido ({archivo}).")
        self.archivo = archivo


class NombreRegistradoError(ValueError):
    def __init__(self, nombre):
        super().__init__(f"Ese nombre de contacto ya esta registrado. Recibido ({nombre}).")
        self.archivo = nombre


class NumeroMaximoContactosRegistradosError(ValueError):
    def __init__(self):
        super().__init__(f"No puedes registrar mas contactos, la agenda esta llena.")


class AddressBook:
    def __init__(self, fichero_xml=""):
        self.__lista_agenda = []
        self.__MAXIMO_CONTACTOS = 100
        self.__lista_de_nombres = []
        self.__numero_de_contactos = 0

        if len(fichero_xml)!= 0:
            if 1 < len(fichero_xml) < 5:
                raise LongitudNombreArchivoXMLError(fichero_xml)
            else:
                self.__pasa_xml_a_agenda(fichero_xml)

    @property
    def lista_agenda(self):
        return self.__lista_agenda.copy()

    def __pasa_xml_a_agenda(self, nombre_de_fichero):
        archivo = ET.parse(nombre_de_fichero)
        root = archivo.getroot()
        for i in range(len(root)):
            nombre_contacto = root[i].get("nombre")
            telefono_contacto = root[i][0].text
            correo_contacto = root[i][1].text
            direccion_contacto = root[i][2].text
            self.alta_contacto(nombre_contacto, telefono_contacto, correo_contacto, direccion_contacto)

    def alta_contacto(self, nombre, telefono, correo, direccion = ""):
        if nombre in self.__lista_de_nombres:
            raise NombreRegistradoError(nombre)
        if self.__numero_de_contactos == self.__MAXIMO_CONTACTOS:
            raise NumeroMaximoContactosRegistradosError()

        self.__lista_agenda.append(Contact(nombre, telefono, correo, direccion))
        self.__lista_de_nombres.append(nombre)
        self.__numero_de_contactos += 1

    def baja_contacto(self, nombre):
        for i in self.__lista_agenda:
            if i.nombre == nombre:
                self.__lista_agenda.remove(i)
                self.__lista_de_nombres.remove(i.nombre)

    def busca_contacto(self, nombre):
        for i in self.__lista_agenda:
            if i.nombre == nombre:
                return i
        return None

    def listar_contactos(self):
        lista_interna = []
        for i in self.__lista_agenda:
            lista_interna.append(i)
        return lista_interna

    def exportar_a_xml(self, fichero_donde_se_anaden_contactos):
        tree = ET.parse(fichero_donde_se_anaden_contactos)
        root = tree.getroot()
        for i in self.__lista_agenda:
            nombre_contacto = i.nombre
            telefono_contacto = i.telefono
            correo_contacto = i.correo
            direccion_contacto = i.direccion

            contacto = ET.Element('contacto', {'nombre': nombre_contacto})
            telefono = ET.SubElement(contacto, 'telefono')
            telefono.text = telefono_contacto

            correo = ET.SubElement(contacto, 'correo')
            correo.text = correo_contacto

            direccion = ET.SubElement(contacto, 'direccion')
            direccion.text = direccion_contacto

            root.append(contacto)
            ET.indent(root, space='    ')
            tree.write(fichero_donde_se_anaden_contactos, encoding='unicode')


