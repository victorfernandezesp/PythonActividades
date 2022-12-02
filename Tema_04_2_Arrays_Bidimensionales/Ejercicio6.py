"""
    Ejercicio 6:

    Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países.
    El array que contiene los nombres de los países es el siguiente:

    paises = [“España”, “Rusia”, “Japón”, “Australia”]

    Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
    generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se
    deben mostrar utilizando el array de países (no se pueden escribir directamente).

    Ejemplo:

                                                         MED MIN MAX

    España:    178 165 148 185 155 141 165 149 155 201 | 164 141 201

    Rusia:     189 208 167 186 174 152 192 173 179 179 | 179 152 208

    Japón:     173 182 168 170 181 197 146 168 166 177 | 172 146 197

    Australia: 172 170 187 186 197 143 190 199 187 191 | 182 143 199

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from random import randrange

array_paises = ["España   ", "Rusia    ", "Japón    ", "Australia"]
contador_paises = 0
COLUMNAS = 10
FILAS = 4
mayor = 0
menor = 211
media_fila = 0
print("                                                                       ", "| MED | MIN | MAX")
matriz = [[0] * COLUMNAS for _ in range(FILAS)]
for x in range(FILAS):
    print(f"{array_paises[contador_paises] }  ", end="")
    for y in range(COLUMNAS):
        matriz[x][y] = randrange(140, 211)
        if mayor < matriz[x][y]:
            mayor = matriz[x][y]
        if menor > matriz[x][y]:
            menor = matriz[x][y]
        media_fila += matriz[x][y]
        print(f"{matriz[x][y]:3d}   ", end="")
    media_fila = media_fila//COLUMNAS
    print(f" | {media_fila},  {menor},  {mayor}")
    mayor = 0
    menor = 211
    media_fila = 0
    contador_paises += 1
