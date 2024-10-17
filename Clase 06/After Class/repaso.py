"""
PREGUNTA 1: sobre lista_productos.clear()

En la clase 7 veremos listas y tuplas.
Por ahora quedemosnos con el concepto de que

lista_productos.clear()

borra el contenido de la lista.

"""

# Repasamos la creación del Menú para nuestro PFI
# Opcion 1: alta de productos (guardamos los datos en una lista)
# Opcion 2: mostrar productos (hacemos un print de la lista)

# Aprovechamos el enunciado del ejercicio para agregar un contador y un acumulador

# Declaracion de variables
lista_productos = []  # list para almacenar los datos ingresados
contador_productos = 0  # contador para  saber cuantos productos se han ingresado
acumulador_productos = 0  # acumulador para saber el stock de todos los productos

# Armamos un Bucle while que finaliza cuando el usuario ingresa s
while True:
    print()
    print("-" * 30)
    print("menu")
    print("-" * 30)
    print("1. Ingresar producto")
    print("2. Listar")
    print('Ingrese "s" para terminar')

    opcion = input("Ingrese una opción: ").lower()

    # Definimos las funcionalidades de la opcion 1 - Alta de productos
    if opcion == "1":
        producto_nombre = input("Ingrese el nombre del producto: ")
        producto_cantidad = input("Ingrese la cantidad del producto: ")
        lista_productos.append(producto_nombre)
        lista_productos.append(producto_cantidad)
        contador_productos += 1
        contador_productos += producto_cantidad

    # Definimos las funcionalidades de la opcion 2 - Mostrar productos
    elif opcion == "2":
        # print(f"Nombre producto {producto_nombre} y cantidad {producto_cantidad}")
        print(lista_productos)

    # Definimos las funcionalidades de la opcion s - salir
    elif opcion == "s":
        break

    # Alertamos  al usuario si ingresa una opcion invalida
    else:
        print("Opción no válida")

# Al finalizar el Bucle mostramos la cantidad de productos ingresados
print(f"La cantidad de productos cargados fue: {contador_productos}")

# Y el total de stock
print(f"El stock de todos los productos es: {acumulador_productos}")
