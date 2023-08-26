numero = int(input("Registre un numero de la tabla de multiplicar: "))

for it in range(1,11):
    resultado = numero * it
    print(f'{numero}X{it} = {resultado}')