import math
import calculos as cal 

while True:
    
    print("Bienvenido a la calculadora de Fibonacci")
    print('1: Usar el fibonacci, 2: Salida de la calculadora')
    fibo = int(input("Escriba el numero del signo: "))
    
    if fibo == 1:
        n = int(input("Ingrese el numero: "))
        ans=cal.fibonacci(n)
        
        for n in range(0, n):
            print(ans[n], end = ' ')
            print("")
    elif fibo == 2:
        print('Gracias por usar la calculadora')
        print("")
        break
    
    