lista_productos = []
lista_productos.clear()

while True:
    print("Menú de opciones")
    print("1. alta de producto")
    print("2. listar producto")
    print("3. salir")
    opcion = input("\nIngrese la opción que desee: ").lower()

    if opcion == "1":
        # Bloque de codigo para alta de producto
        nombre_producto = input("Nombre de producto: ")
        cantidad_producto = int(input("Cantidad: "))
        lista_productos.append(nombre_producto)
        lista_productos.append(cantidad_producto)
    elif opcion == "2":
        # Bloque de codigo para listar de producto
        print(f"Lista de productos: {lista_productos}")

    elif opcion == "3":
        break
    else:
        print("Opcione  no válida, por favor intente de nuevo")
