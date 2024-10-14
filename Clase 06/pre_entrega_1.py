lista_productos = []
lista_productos.clear()

while True:
    print()
    print("-" * 30)
    print("Menu de opciones")
    print("1 Agregar producto")
    print("2 Ver productos")
    print("3 Salir")
    opcion = input("Su opción: ")
    if opcion == "1":
        nombre_producto = input("Nombre del producto: ")
        cantidad_producto = int(input("Cantidad del producto: "))
        lista_productos.append([nombre_producto, cantidad_producto])
        print(lista_productos)
        print("Producto ingresado exitosamente!")
    elif opcion == "2":
        # print(f"Producto: {nombre_producto} - cantidad: {cantidad_producto}")
        indice = 0
        while indice < len(lista_productos):
            producto = lista_productos[indice]
            print(f"Producto {producto[0]} - Cantidad: {producto[1]} ")
            indice += 1
    elif opcion == "3":
        break
    else:
        print("Opción no válida, por favor ingrese una opción válida")
