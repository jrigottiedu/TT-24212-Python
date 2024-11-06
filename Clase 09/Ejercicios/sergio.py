lista_productos = []


def agregar_producto(producto, cantidad_ingresada, precio):
    lista_productos.append([producto, cantidad_ingresada, precio])


def mostrar_productos():
    indice = 0
    while indice < len(lista_productos):
        print(
            f"{"-*" * 15} \nProducto: {lista_productos[indice][0]} \nCantidad: {lista_productos[indice][1]} \nPrecio unitario: $ {lista_productos[indice][2]}"
        )
        indice += 1


while True:
    print("-" * 30)
    print("Menu principal ")
    print("-" * 30)
    print(
        "\n1.Buscar producto \n2.lista \n3.Agregar producto \n4.Actualizar stock \n5.Eliminar producto \n6.Salir"
    )

    print("-" * 30)
    opcion = input("Ingrese una opción: ")
    print("-" * 30)

    if opcion == "3":
        while True:
            producto = str(input("Ingrese nombre de producto: "))
            cantidad_ingresada = int(input("Cantidad a ingresar: "))
            precio = str(input("Precio unitario: "))
            agregar_producto(producto, cantidad_ingresada, precio)

            print("-" * 11, "******", "-" * 11)
            confirmar_ingreso = str(
                input("Quiere agregar otro producto? (S/N): ")
            ).lower()
            print()
            print("-" * 11, "******", "-" * 11)

            if confirmar_ingreso == "n":
                break

    elif opcion == "2":
        print("-" * 11, "******", "-" * 11)
        mostrar_productos()
        print("-" * 11, "******", "-" * 11)

        volver = str(input("Volver al menu (S): ").lower())

    elif opcion == "6":
        break

    elif opcion == "4":  # actualizar stock
        while True:
            nombre_producto = input("\nIngrese nombre del producto: ")  # cafe
            nombre_inexistente = True
            for (
                lista
            ) in lista_productos:  # lista=[producto, cantidad_ingresada, precio]
                if nombre_producto == lista[0]:
                    # nombre_producto = False
                    nombre_inexistente = (
                        False  # indica q se encontro el nombre_producto
                    )

                    print(f"producto {lista[0]} \ncantidad {lista[1]} ")
                    venta = int(input("Ingrese cantidad vendida: "))

                    while venta > lista[1] or venta <= 0:
                        print("Reintente Error")
                        venta = int(input("Ingrese cantidad vendida: "))

                    lista[1] = lista[1] - venta

                    print(
                        f"Actualizacion: \nProducto: {lista[0]} \nCantidad: {lista[1]}"
                    )
                    break

            if nombre_inexistente:
                print("\n Nombre no encontrado")

            continuar = input(
                "\n Ingrese S para salir o cualquier letra para continuar: "
            )
            if continuar.lower() == "s":
                break

    else:
        print("-" * 11, "******", "-" * 11)
        print("Opcion no valida")
        print("-" * 11, "******", "-" * 11)
