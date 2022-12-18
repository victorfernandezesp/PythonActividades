def menu(*u):
    contador = 1
    print("Menu de opciones:")
    print("Selecciona una de las siguientes opciones:   ")
    for i in u:
        print(f"{contador}. {i}")
        contador += 1
    print('-------------------------------------------------------------------------------------------------------')
    x = int(input("¿Que vas a selecionar?    "))
    return x


