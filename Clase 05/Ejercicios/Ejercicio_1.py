"""
Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. 
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, 
si no hay, que avise que hay que reponerlo. 

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.

"""


# funciones
def consultar_stock(id_producto):
    return 5


# declaracion de variables
UMBRAL_STOCK = 10  # hardcoding en el codigo/app

# entrada (este dato esta en la Base de Datos)
# stock_actual = int(input("Ingrese el stock"))
# en nuestro programa el usaurio ingresa el producto o ID de producto
id_producto = int(input("Ingrese el ID del producto a consultar: "))
stock_actual = consultar_stock(
    id_producto
)  # consultar_stock es una funcion que devuelve el nivel de stock

# comprobacion
if stock_actual < UMBRAL_STOCK:
    print(
        f"Stock actual es {stock_actual} la diferencia {UMBRAL_STOCK - stock_actual} hacer pedido "
    )
else:
    print("Stock suficiente")
# proceso

# salida
