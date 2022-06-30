# 19. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
# tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

# Author: Victor Fernandez España


# Introducimos por teclado el número con el que vamos a trabajar
moneda2e = int(input("¿Cuantas monedas de 2 euros tienes? "))
moneda1e = int(input("¿Cuantas monedas de 1 euro tienes? "))

moneda50cent = int(input("¿Cuantas monedas de 50 centimos tienes? "))
moneda20cent = int(input("¿Cuantas monedas de 20 centimos tienes? "))
moneda10cent = int(input("¿Cuantas monedas de 10 centimos tienes? "))


# Realizamos las distintas operaciones
euros_to_cent = (moneda1e + (moneda2e * 2)) * 100
euros_tot = int((euros_to_cent + moneda10cent + moneda20cent + moneda50cent)/100)
cent_tot = int((euros_to_cent + moneda10cent + moneda20cent + moneda50cent) % 100)

# Mostramos por pantalla los resultados
print(f"Los euros totales son: {euros_tot} y los centimos restantes son {cent_tot}")
