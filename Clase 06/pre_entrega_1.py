# Declaramos una variable tipo list para almacenar temporalmente los productos y cantidades ingresadas
lista_productos = []
lista_productos.clear()

# Comenzamos con un Bucle del tipo while, que se ejecutará hasta que el usuario ingrese 3
while True:
    print("Menú de opciones")
    print("1. alta de producto")
    print("2. listar producto")
    print("3. salir")

    # Pedimos al usuario que ingrese una opción y la convertimos a minúscula
    opcion = input("\nIngrese la opción que desee: ").lower()

    # Opción 1: debemos solicitar nombre y cantidad del producto
    # Para nuestra demo almacenamos el dato en la list
    # En la versión final tendremos una función encargada de persistir el dato en la DB
    if opcion == "1":
        # Bloque de codigo para alta de producto
        nombre_producto = input("Nombre de producto: ")
        cantidad_producto = int(input("Cantidad: "))
        lista_productos.append(nombre_producto)
        lista_productos.append(cantidad_producto)

    # Opción 2: mostramos la list con un print
    # En la versión final tendremos una función que trae los datos de la DB
    elif opcion == "2":
        # Bloque de codigo para listar de producto
        print(f"Lista de productos: {lista_productos}")

    # Opción 3: el Bucle while debe terminar para salir
    elif opcion == "3":
        break

    # Si la opción ingresada no es válida, mostramos un mensaje de error
    else:
        print("Opcione  no válida, por favor intente de nuevo")
