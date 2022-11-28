from math import sqrt


def voltea(numero):
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

    return numero_volteado


def es_capicua(numero, volteado):
    if numero == volteado and numero > 9:
        return True
    else:
        return False


def digitos(numero):
    contador = 1
    while numero > 10:
        numero = numero // 10
        contador += 1
    return contador


def es_primo(posible_primo):
    primo = False
    divisor = 2
    while divisor <= sqrt(posible_primo) and not primo:
        if posible_primo % divisor == 0:
            return False
        divisor += 1
    return True


def siguiente_primo(numero):
    numero += 1
    while not es_primo(numero):
        numero += 1

    return numero
