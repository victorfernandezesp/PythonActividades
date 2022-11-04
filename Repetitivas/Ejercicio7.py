""" Ejercicio 7.
        Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €,
        el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el
        total de lo que pagará después de los 20 meses.

    Author: Victor Fernandez España
    Curso:  2022-2023
"""
NUMERO_CUOTAS = 20

print("Este programa te calcula cuanto pagara la persona cada mes durante 20 meses ")
pago_mes = 10
num_mes = 1
acumulador_pagado = 0
print(f"El pago del mes {num_mes} es {pago_mes}")
while num_mes <= NUMERO_CUOTAS:
    pago_mes = pago_mes * 2
    acumulador_pagado = acumulador_pagado + pago_mes
    num_mes += 1
    print(f"El pago del mes {num_mes} es {pago_mes}")

print(f" El pago total asciende a {acumulador_pagado}")