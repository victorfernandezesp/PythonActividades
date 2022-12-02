""" 20.Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
      tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

    Author: Victor Fernandez España
    Curso:  2022-2003
"""
print("Este programa te cuenta las monedas y te da el dinero total en euros y céntimos")
moneda2e = int(input("¿Cuántas monedas de 2 euros tienes? "))
moneda1e = int(input("¿Cuántas monedas de 1 euro tienes? "))
moneda50cent = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
moneda20cent = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
moneda10cent = int(input("¿Cuántas monedas de 10 céntimos tienes? "))

euros_to_cent = (moneda1e + (moneda2e * 2)) * 100
euros_tot = int((euros_to_cent + moneda10cent + moneda20cent + moneda50cent)/100)
cent_tot = int((euros_to_cent + moneda10cent + moneda20cent + moneda50cent) % 100)

print(f"Los euros totales son: {euros_tot} y los céntimos restantes son {cent_tot}")