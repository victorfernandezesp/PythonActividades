"""
Escribe un programa que pida 20 números enteros. Estos números se deben
introducir en un array de 4 filas por 5 columnas. El programa mostrará
las sumas parciales de filas y columnas igual que si de una hoja de cálculo
se tratara. La suma total debe aparecer en la esquina inferior derecha.
"""

# CONSTANTES.
CANT_NUM = 20
FILAS = 4
COLUMNAS = 5
NUM_MAXIMO = 1000
suma_total = 0

arraynumeros = [[0] * COLUMNAS for i in range(FILAS)]

# Datos del array.
for rows in range(FILAS):
    for columns in range(COLUMNAS):
        arraynumeros[rows][columns] = int(input(f'Introduce el número del array de la posición [{rows}][{columns}]: '))
        while NUM_MAXIMO < arraynumeros[rows][columns]:
            arraynumeros[rows][columns] = int(input(f'ERROR: Número mayor que 999, introduce el número del array de la '
                                                    f'posición [{rows}],[{columns}]'))

# Mostrar array y suma de sus columnas.
for rows in range(FILAS):
    for columns in range(COLUMNAS):
        print(f'{arraynumeros[rows][columns]:3d}', end=' ')
    print(f'| {sum(arraynumeros[rows])}')

# Mostrar suma de las filas del array.
for columns in range(COLUMNAS):
    print('__', end='')
print('__')

for columns in range(COLUMNAS):
    suma_columnas = 0
    for rows in range(FILAS):
        suma_columnas += arraynumeros[rows][columns]
    suma_total += suma_columnas
    print(f'{suma_columnas:3}', end=' ')
print(f'| {suma_total}')
