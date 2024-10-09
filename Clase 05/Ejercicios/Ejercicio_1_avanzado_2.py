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
tabla_productos={
    "mouse": 11,
    "teclado": 15,
    "webcam": 5
}

reponer_stock = []

# Función mostrar Menú
def mostrar_menu():
    print("\n Ingrese una opción:")
    print("1. Consultar Stock")
    print("2. salir")

def verificar_stock():
    reponer_stock = []
    if tabla_productos["mouse"] <= UMBRAL_STOCK:
        reponer_stock.append("mouse")
    if tabla_productos["teclado"] <= UMBRAL_STOCK:
        reponer_stock.append("teclado")
    if tabla_productos["webcam"] <= UMBRAL_STOCK:
        reponer_stock.append("webcam")

    print(f"Debe reponer stock de:")
    for producto in reponer_stock:
        print(producto)

# Entrada
while True:
    mostrar_menu()
    opcion = int(input("Su elección es: "))
    
# Proceso & Salida

    if opcion == 1:
        verificar_stock()
    elif opcion == 2:
        break
    else: 
        print("Ingrese una opción válida")




