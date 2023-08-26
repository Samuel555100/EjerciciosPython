numeros = []

tamaño = 5

for i in range(tamaño):
    print("Ingrese los numeros: ", i + 1)
    numero = int(input("Numeros: "))
    
    numeros.append(numero)
    
contador = 0
for i in range(tamaño):
    print("Mostrar los numeros pares e impares: ", i + 1)
    if i % 2 == 0:
        print("Numeros pares", numeros[i])
        contador += 1
    elif i % 2 != 0:
        print("Numeros impares", numeros[i])
        contador += 1

    