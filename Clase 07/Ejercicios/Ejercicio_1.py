"""
Clase 07 - Ejercicio 1

Registro de productos en un inventario

Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. 
El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más. 
Luego, deberás mostrar todos los productos ingresados al inventario.


Tips: 

Usá una lista para almacenar los productos.
Diseña la lista pensando en el TFI.
Pueden usar lista de listas, como vimos en el ejercicio de hoy "e_listas_tuplas_desafio.py"
"""

# Inventario de una tiena

# Declaracion de variables
inventario = []

print("\nMenu\n")
print("Alta de productos, para terminar ingrese 'salir'")


producto = input("Ingrese el nombre del producto o salir para terminar: ")
while producto.lower() != "salir":
    cantidad = input("Ingrese la cantidad de unidades: ")
    precio = input("Ingrese el precio unitario: ")
    inventario.append([producto, cantidad, precio])
    producto = input("Ingrese el nombre del producto o salir para terminar: ")


print("\nLos productos ingresados fueron: \n")
indice = 0
print("Producto \t\tUnidades \tPrecio")
while indice < len(inventario):
    print(f"{inventario[indice][0]} \t\t{inventario[indice][1]} \t\t{inventario[indice][2]}")
    indice += 1
