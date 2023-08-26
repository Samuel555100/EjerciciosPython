import datetime

proyectos = []


def agregar_proyecto(nombre, descripcion, fecha):
    proyectos.append({'Nombre': nombre, 'Descripcion': descripcion, 'FechaVencimiento': fecha})


def mostrar_proyecto():
    for it in proyectos:
        print(
            f"Nombre: {it['Nombre'] }, Descripcion: {it['Descripcion']}, FechaVencimiento: {it['FechaVencimiento']}")

def actualizar_proyecto(proyecto):
    for it, value in inventario:
        if it == proyecto:
            inventario[it] = print(f"Nombre: {it['Nombre'] }, Descripcion: {it['Descripcion']}, FechaVencimiento: {it['FechaVencimiento']}")
    
def eliminar_proyecto(proyecto):
    eliminar = False
    for it in proyectos:
        if proyecto.lower() in it['Nombre'].lower():
            print(
                f"Nombre: {it['Nombre'] }, Descripcion: {it['Descripcion']}, FechaVencimiento: {it['FechaVencimiento']}")
            eliminar = True
            break
        inventario.remove(proyecto)

    if not eliminar:
        print('No existe el libro')
