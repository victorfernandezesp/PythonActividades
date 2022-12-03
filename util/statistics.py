def maximum(array):
    maximo = 0
    for i in array:
        if i > maximo:
            maximo = i
    return maximo


def minimum(array):
    minimo = array[0]
    for i in array:
        if i < minimo:
            minimo = i
    return minimo


def mean(array):
    longitud = len(array)
    acumulador = 0
    for i in array:
        acumulador += i
    media = acumulador / longitud
    return round(media, 2)


def variance(array):
    media = mean(array)
    varianza = 0
    for i in array:
        varianza += (i - media) ** 2
    varianza = varianza / len(array)
    varianza = varianza ** 0.5
    return round(varianza, 2)


def median(array):
    longitud = len(array)
    if longitud % 2 != 0:
        mediana = array[longitud // 2]
        return mediana
    else:
        parte_mediana_1 = array[longitud // 2]
        parte_mediana_2 = array[longitud // 2 - 1]
        mediana = (parte_mediana_1 + parte_mediana_2) / 2
        return mediana


def mode(array):
    numero_sale = []
    veces_que_sale = 0
    for i in array:
        cuenta = array.count(i)
        if cuenta > veces_que_sale:
            veces_que_sale = cuenta
            numero_sale.clear()
            if i not in numero_sale:
                numero_sale.append(i)
        elif cuenta == veces_que_sale:
            if i not in numero_sale:
                numero_sale.append(i)
    return numero_sale