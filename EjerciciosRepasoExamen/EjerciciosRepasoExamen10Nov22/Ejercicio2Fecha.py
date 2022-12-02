"""
    Ejercicio 2:

        Pide una fecha en formato dd/mm/aaaa del siglo XXI, comprueba si es correcta, en caso de no serlo, señala el
        error correspondiente (en el dispositivo de errores) y acaba el programa de forma anormal, en caso de serlo,
        muestra el día siguiente a la misma en el mismo formato.

    Autor: Víctor Fernández España
    Curso: 2022-2023

"""
import sys

ERROR_DIAS_INCORRECTOS = 3

ERROR_MESES_INCORRECTOS = 2

ERROR_NO_SIGLO_XXI = 1

fecha = input("Escribe la fecha en formato 'dd/mm/aaaa', recuerda que tiene que ser del siglo XXI (01/01/2001): ")
dia = int(fecha[0:2])
mes = int(fecha[3:5])
ano = int(fecha[6:10])
if 2001 > ano > 2101:
    print(f"ERROR. Tu fecha no es del siglo XXI (01 / 01 / 2001 –  31 / 12 / 2100)", file=sys.stderr)
    sys.exit(ERROR_NO_SIGLO_XXI)

if 1 > mes > 12:
    print(f"ERROR. Tu mes no esta comprendido entre 1 y 12", file=sys.stderr)
    sys.exit(ERROR_MESES_INCORRECTOS)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10:
            if 1 <= dia <= 31:
                if 30 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

        case 4 | 6 | 9 | 11:
            if 1 <= dia <= 30:
                if 29 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

        case 2:
            if 1 <= dia <= 29:
                if 29 > dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

        case 12:
            if 1 <= dia <= 31:
                if 30 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes = 1
                    ano += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

else:
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10:
            if 1 <= dia <= 31:
                if 30 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

        case 4 | 6 | 9 | 11:
            if 1 <= dia <= 30:
                if 29 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)
        case 2:
            if 1 <= dia <= 29:
                if 28 > dia:
                    dia += 1
                else:
                    dia = 1
                    mes += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)

        case 12:
            if 1 <= dia <= 31:
                if 30 >= dia:
                    dia += 1
                else:
                    dia = 1
                    mes = 1
                    ano += 1
            else:
                print(f"ERROR. Tu dia no es proporcional al numero de dias del mes", file=sys.stderr)
                sys.exit(ERROR_DIAS_INCORRECTOS)
print(f"Mañana sera {dia:02d}/{mes:02d}/{ano:04d}")