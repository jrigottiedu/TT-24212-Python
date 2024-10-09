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

# Entrada
stock_actual = int(input("Ingrese el stock actual del producto: "))

# Proceso
if stock_actual >= UMBRAL_STOCK:
    informe_stock = "No hacer pedido"
else:
    informe_stock = "Hacer pedido"
# Salida
print(f"Contol de stock: {informe_stock}")


