import datetime

inventario = []


def agregar_inventario(producto, precio):
    inventario.append({'Producto': producto, 'Precio': precio})


def mostrar_inventario():
    for it in inventario:
        print(
            f"Producto: {it['Producto'] }, Precio: {it['Precio']}")

def actualizar_inventario(invenProducto):
    for it, value in inventario:
        if it == precio:
            inventario[it] = print(f"Precio: {it['Precio']}")
    
def eliminar_inventario(invenProducto):
    eliminar = False
    for it in inventario:
        if invenProducto.lower() in it['Producto'].lower():
            print(
                f"Producto: {it['Producto'] }, Precio: {it['Precio']}")
            eliminar = True
            break
        inventario.remove(invenProducto)

    if not eliminar:
        print('No existe el libro')
