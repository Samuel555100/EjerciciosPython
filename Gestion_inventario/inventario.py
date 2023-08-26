import funciones as fb

print('Bienvenido al Sistema de Inventario\n')

while True:
    print('Digite la opcion a utilizar:\n 1- Agregar producto al inventario\n 2-Mostrar inventario\n 3-Actualizar inventario\n 4- Borrar un inventario\n 0- Salir del sistema')

    opcion = int(input('Ingrese el número de la opción:'))

    if opcion == 0:
        print('\n Gracias por usar el sistema!!!')
        break
    elif opcion == 1:
        producto = input('Ingrese nombre del producto: ')
        precio = float(input('Ingrese el precio del producto: '))
        fb.agregar_inventario(producto, precio)

    elif opcion == 2:
        print('El producto a mostrar es: \n\n')
        fb.mostrar_inventario()

    elif opcion == 3:
        actualizar = input('Actualiza el precio del inventario: \n')
        fb.actualizar_inventario(actualizar)

    elif opcion == 4:
        inventarioT = input('digite en nombre del Titulo a eliminar: \n')
        fb.eliminar_inventario(inventarioT)
        print('libro eliminado con exito\n')
        fb.mostrar_inventario()
    else:
        print('Opcion Inválida')
