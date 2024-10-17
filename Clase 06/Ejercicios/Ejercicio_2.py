"""
Validación de precios de productos

Escribí un programa que permita al usuario ingresar el precio de un producto, 
pero que sólo acepte valores mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero), 
el programa debe mostrar un mensaje de error, y volver a pedir el valor hasta que se ingrese uno válido. 
Al final, el programa debe mostrar el precio aceptado.  

"""

condicion_global = True
while condicion_global == True:
    while True:
        precio_producto = float(input("Ingrese el precio del producto: "))
        while precio_producto <= 0:
            print("Error: El precio no puede ser menor o igual a 0.")
            precio_producto = float(input("\nIngrese el precio del producto: "))

        print(f"El precio ingresador fue {precio_producto}")
        continuar = input(
            "Presions  's' para continuar o cualquier otra tecla para salir: "
        ).lower()
        if continuar == "s":
            break
