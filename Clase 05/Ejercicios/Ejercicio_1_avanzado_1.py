"""
Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. 
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, 
si no hay, que avise que hay que reponerlo. 

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.

"""

# Declaración de variables
UMBRAL_STOCK = 10
# Generamos un diccionario que simula el stock en nuestro inventatio
# En el proyecto, estos datos se almacenan en una Base de Datos

# Diccionario
tabla_productos = {"mouse": 10, "teclado": 15, "webcams": 5}

# Entrada
condicion_bucle = True

while condicion_bucle:
    print("\n Ingrese el producto a consultar stock:")
    print("1. mouse")
    print("2. teclado")
    print("3. webcam")
    print("4. salir")
    opcion = int(input("Su elección es: "))

    # Proceso & Salida

    if opcion == 1:
        if tabla_productos["mouse"] <= UMBRAL_STOCK:
            print("Hacer pedido de mouse")
        else:
            print("No hay necesidad de hacer pedido de mouse")
    elif opcion == 2:
        if tabla_productos["teclado"] <= UMBRAL_STOCK:
            print("Hacer pedido de teclado")
        else:
            print("No hay necesidad de hacer pedido de teclado")
    elif opcion == 3:
        if tabla_productos["webcams"] <= UMBRAL_STOCK:
            print("Hacer pedido de webcams")
        else:
            print("No hay necesidad de hacer pedido de webcams")
    elif opcion == 4:
        condicion_bucle = False
    else:
        print("Ingrese una opción válida")
