import funcionProyecto as fb

print('Bienvenido al Sistema de Inventario\n')

while True:
    print('Digite la opcion a utilizar:\n 1- Agregar producto al inventario\n 2-Mostrar inventario\n 3-Actualizar inventario\n 4- Borrar un inventario\n 0- Salir del sistema')

    opcion = int(input('Ingrese el número de la opción:'))

    if opcion == 0:
        print('\n Gracias por usar el sistema!!!')
        break
    elif opcion == 1:
        nombre = input('Ingrese el nombre del proyecto: ')
        descripcion = input('Ingrese la descripcion del proyecto: ')
        fecha = input('Ingrese la fecha de vencimiento AAAA-MM-DD: ')
        fb.agregar_proyecto(nombre, descripcion, fecha)

    elif opcion == 2:
        print('El libro a mostrar es: \n\n')
        fb.mostrar_proyecto()

    elif opcion == 3:
        actualizar = input('Actualiza el precio del inventario: \n')
        fb.actualizar_proyecto(actualizar)

    elif opcion == 4:
        proyectoT = input('digite en nombre del Titulo a eliminar: \n')
        fb.eliminar_proyecto(proyectoT)
        print('libro eliminado con exito\n')
        fb.mostrar_proyecto()
    else:
        print('Opcion Inválida')
