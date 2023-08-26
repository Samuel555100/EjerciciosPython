num_productos = int(input("Ingrese el número de estudiantes: "))

datos_productos = {}

for it in range(1, num_productos + 1):
    producto = input(f"Ingrese el nombre del producto {it}: ")
    precio = float(input(f"Ingrese el precio del producto {it}: "))
    datos_productos[producto] = precio


print("\nDatos de los estudiantes:")
for producto, precio in datos_productos.items():
    print(
        f"Nombre del producto: {producto}, Precio: {precio} ")