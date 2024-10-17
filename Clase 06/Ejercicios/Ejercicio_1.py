"""
Control de stock de productos


Desarrollá un programa que permita al usuario ingresar el nombre de varios productos
y la cantidad en stock que hay de cada uno. El programa debe seguir pidiendo que ingrese
productos hasta que el usuario decida salir, ingresando "salir" como nombre de producto.
Después de que el bucle termine, el programa debe mostrar la cantidad total de productos ingresados.  
"""

print(
    f"El programa le solicitará que ingrese productos hasta que escriba la parabra salir: "
)


condicion = ""
contador_productos = 0
while condicion != "salir":
    producto_nombre = input("Ingrese el nombre del producto: ")
    producto_cantidad = int(input("Ingrese la cantidad: "))
    contador_productos += 1
    condicion = input(
        'Ingrese "Salir" para terminar o cualquier otro para continuar: '
    ).lower()


print(f"Se ingresaron {contador_productos} productos")
