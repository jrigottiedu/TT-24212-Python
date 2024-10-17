"""
Veamos una versión del Menu Pre-entrega almacenando los datos en Diccionario
"""

# Declaración de variables
lista_productos = []


# Funciones
def agregar_producto(producto_nombre, producto_cantidad):
    lista_productos.append([producto_nombre, producto_cantidad])


def mostrar_productos():
    indice = 0
    while indice < len(lista_productos):
        print(
            f"Producto: {lista_productos[indice][0]}, Cantidad: {lista_productos[indice][1]}"
        )
        indice += 1


while True:
    print()
    print("-" * 30)
    print("menu")
    print("-" * 30)
    print("1. Ingresar producto")
    print("2. Listar")
    print('Ingrese "s" para terminar')
    print("-" * 30)
    print()
    opcion = input("Ingrese una opción: ").lower()
    print()

    if opcion == "1":
        producto_nombre = input("Ingrese el nombre del producto: ")
        producto_cantidad = input("Ingrese la cantidad del producto: ")
        agregar_producto(producto_nombre, producto_cantidad)

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "s":
        break
    else:
        print("Opción no válida")
