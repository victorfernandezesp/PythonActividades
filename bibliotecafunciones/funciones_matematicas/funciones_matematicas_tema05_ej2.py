import sys
from math import sqrt

ERROR_FUERA_DE_RANGO = 1


def voltea(numero):
    signo_num = signo(numero)
    numero = abs(numero)
    contador = digitos(numero)
    numero_volteado = 0

    if numero < 10:
        numero_volteado = numero
    else:
        for i in range(contador - 1, -1, -1):
            if numero >= 10:
                parte_invertido = numero % 10
                numero_volteado += parte_invertido * 10 ** i
                numero = numero // 10
            else:
                numero_volteado += numero

    return signo_num * numero_volteado


def es_capicua(numero):
    volteado = voltea(numero)
    if numero == volteado:
        return True
    else:
        return False


def digitos(numero):
    numero = abs(numero)
    contador = 1
    while numero > 10:
        numero = numero // 10
        contador += 1
    return contador


def es_primo(posible_primo):
    primo = False
    if posible_primo < 0:
        return False
    divisor = 2
    while divisor <= sqrt(posible_primo) and not primo:
        if posible_primo % divisor == 0:
            return False
        divisor += 1
    return True


def siguiente_primo(numero):
    if numero < 0:
        return 2
    numero += 1
    while not es_primo(numero):
        numero += 1

    return numero


def digito_n(numero, posicion):
    if posicion >= digitos(numero) or posicion < 0:
        print("ERROR. La posicion es superior o inferior al numero de digitos que tiene el numero", file=sys.stderr)
        sys.exit(ERROR_FUERA_DE_RANGO)
    else:
        auxiliar = numero // 10 ** (digitos(numero) - (posicion + 1))
        auxiliar = auxiliar % 10
    return auxiliar


def posicion_de_digito(numero, digito):
    for i in range(digitos(numero)):
        if digito == digito_n(numero, i):
            return i
    return -1


def quita_por_delante(numero, quita):
    auxiliar_1 = quita_por_detras(voltea(numero), quita)

    return voltea(auxiliar_1)


def quita_por_detras(numero, quita):
    numero = numero // 10 ** quita
    return numero


def pega_por_detras(numero, pego):
    numero = numero * 10 + pego
    return numero


def pega_por_delante(numero, pego):
    auxiliar_1 = pega_por_detras(voltea(numero), pego)

    return voltea(auxiliar_1)


def trozo_de_numero(numero):
    aux_delante = quita_por_detras(numero, digitos(numero) - 1)
    aux_detras = quita_por_delante(numero, digitos(numero) - 1)
    return aux_delante * 10 + aux_detras


def junta_numeros(junta1, junta2):
    numero_juntado = junta1 * 10 ** digitos(junta2) + junta2
    return numero_juntado


def signo(num):
    if num < 0:
        return -1
    return 1
