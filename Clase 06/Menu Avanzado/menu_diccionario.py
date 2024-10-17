"""
Veamos una versión del Menu Pre-entrega almacenando los datos en Diccionario
"""

# Declaración de variables
diccionario_productos = {}


# Funciones
def agregar_producto(producto_nombre, producto_cantidad):
    diccionario_productos.update({producto_nombre: producto_cantidad})


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
        for producto, cantidad in diccionario_productos.items():
            print(f"Producto: {producto}, Cantidad: {cantidad}")

    elif opcion == "s":
        break
    else:
        print("Opción no válida")
