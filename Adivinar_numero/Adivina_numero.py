number = 14

estado = False

while not estado:
    numero = int(input("Digita el numero para adivinar: "))

    if numero == number:
        print("Felicidades, Adivinaste")
        estado = True
    elif numero <= number:
        print("El numero es menor de lo pensado") 
        print("Intente de nuevo ")
    elif numero >= number:
        print("El numero es mayor de lo pensado")
        print("Intente de nuevo ")