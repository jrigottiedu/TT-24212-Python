"""
Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. 
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, 
si no hay, que avise que hay que reponerlo. 

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.

"""

# declaracion de variables
UMBRAL_STOCK = 10  # hardcoding en el codigo/app
id_producto = int(input("Ingrese el id del producto "))

# funcion que a partir del id_producto retorne el stock_actual
stock_actual = get_stock_actual(id_producto)

# comprobacion
if stock_actual < UMBRAL_STOCK:
    print("Stock bajo")
else:
    print("Stock suficiente")
