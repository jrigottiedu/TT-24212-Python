"""
Vimos algo de While a partir de una consulta,
pero solo a modo de referencia.
"""

# opcion = 1
# while opcion != 5:
#     opcion = int(input("Ingrese una opcion"))

# flag = True
# while flag == True:
#     opcion = int(input("Ingrese una opcion"))

#     if opcion == 5:  # para salir
#         flag = False
#     else:
#         flag = True

while True:
    opcion = int(input("Ingrese una opcion"))

    if opcion == 1:  # para salir
        print("Ingreso 1")
    elif opcion == 2:
        print("Ingreso 2")
    elif opcion == 5:
        break
    else:
        print("Opcion no valida")  # para mostrar mensaje de error
