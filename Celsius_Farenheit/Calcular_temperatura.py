while True:
    
    Celsius = float(input(f"Ingrese la tempetatura en Celsius : "))
    Farenheit = (Celsius * 9/5) + 32
    
    print("\nDatos de las temperaturas:")
    print(f"Tempetatura de Celsius {Celsius}°C a Farenheit {Farenheit}°F")
    
    continuar = input("¿Desea convertir otra temperatura? (s/n): ")
    if continuar != "s":
        break