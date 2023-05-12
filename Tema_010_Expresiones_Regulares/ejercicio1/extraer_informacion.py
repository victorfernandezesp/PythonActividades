"""
        Ejercicio 1:
            Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va
            extraer del mismo, después muestra por la pantalla los datos extraídos.

            Los posibles valores del segundo parámetro y la información que extrae es:

            DNI: extrae los DNIs.
            IP: extrae las direcciones IP.
            MAT: extrae matrículas de coche con formato 0000XXX.
            HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número
                    empieza con #.
            FEC: extrae fechas con formato dd/mm/aaaa.
            TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayúsculas y minusculas, numeros,
                guiones y guiones bajos.
            El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
def main():
    nombre_archivo, tipo = leer_argumentos()
    cadena = leer_archivo(nombre_archivo)

    if tipo == "DNI":
        patron = "\d{8}[A-HJ-NP-TV-Z]"
        print("LISTA DE DNIs")
        extraer_y_mostrar_datos(patron, cadena)

    elif tipo == "IP":
        patron = '\d{2,3}.\d{1,3}.\d{1,3}.\d{1,3}'
        print("LISTA DE IPs")
        extraer_y_mostrar_datos(patron, cadena)

    elif tipo == "MAT":
        patron = "\d{4}[A-Z]{3}"
        print("LISTA DE MATRICULAS")
        extraer_y_mostrar_datos(patron, cadena)

    elif tipo == "HEX":
        patron = "#[0-9A-Fa-f]{0,6}"
        print("LISTA DE HEXADECIMALES")
        extraer_y_mostrar_datos(patron, cadena)

    elif tipo == "FEC":
        patron = "\d[1-31]/\\d[1-12]/\\d{4}"
        print("LISTA DE FECHAS")
        extraer_y_mostrar_datos(patron, cadena)

    elif tipo == "TWT":
        patron = "@[A-Za-z0-9_-]+"
        print("LISTA DE CUENTAS DE TWITTER")
        extraer_y_mostrar_datos(patron, cadena)

    else:
        raise ValueError("El tipo tiene que ser: DNI, IP, MAT, HEX, FEC o TWT")


def leer_argumentos():
    import sys
    if len(sys.argv) != 3:
        print("El número de argumentos es erróneo", file=sys.stderr)
        sys.exit(1)
    nombre_archivo = sys.argv[1]
    tipo = sys.argv[2]
    return nombre_archivo, tipo


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo_para_lectura:
            cadena = archivo_para_lectura.read()

    except FileNotFoundError:
        print("ERROR. El archivo no existe")
    return cadena


def extraer_y_mostrar_datos(patron, cadena):
    import re
    resultados = re.findall(patron, cadena)
    for i in range(len(resultados)):
        print(f"{i+1}. {resultados[i]}")


if __name__ == '__main__':
    main()