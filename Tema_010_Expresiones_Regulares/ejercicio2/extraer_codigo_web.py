"""
        Ejercicio 2:
            Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la
            pantalla el contenido de cada etiqueta.

            Ejemplo:

            si ejecuto python mi programa https://www.iesgrancapitan.org/ title

            La salida sería:

            Centro Educativo IES Gran Capitán

            Número de etiquetas encontradas: 1

            ó si ejecuto python mi programa https://example.com/ p

            La salida sería:

            This domain is for use in illustrative examples in documents. You may use this domain in literature without
            prior coordination or asking for permission.


            <a href="https://www.iana.org/domains/example">More information...</a>

            Número de etiquetas encontradas: 2

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys
import requests


def main():
    comprueba_argumentos()
    codigo_fuente = sacar_codigo_fuente()

    etiqueta = sys.argv[2]
    patron = f"<{etiqueta}>(.*?)</{etiqueta}>"
    resultados = extraer_datos(patron, codigo_fuente)
    if resultados is None:
        print("Esa etiqueta no esta en el codigo")
    else:
        print(resultados[0])
        print(f" Número de etiquetas encontradas: {len(resultados)}")


def extraer_datos(patron, cadena):
    import re
    return re.findall(patron, cadena)

def sacar_codigo_fuente():
    try:
        url = sys.argv[1]
        response = requests.get(url)
        codigo_fuente = response.text
        return codigo_fuente

    except requests.exceptions.RequestException:
        print("Dicha pagina no existe", file=sys.stderr)
        sys.exit(1)

def comprueba_argumentos():
    import sys
    if len(sys.argv) != 3:
        print("El número de argumentos es erróneo", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()