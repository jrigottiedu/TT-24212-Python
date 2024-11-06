"""
Mostrar los códigos de productos ingresados

En un sistema de inventario, cada producto tiene un código que lo identifica. 
Escribí un programa que permita ingresar los códigos de 4 productos 
y luego mostrálos uno por uno, junto con su posición en la lista.

Ejemplo: si los códigos ingresados son "P001", "P002", "P003", "P004", el programa debe mostrar:  

Tips: 

Utilizá un bucle for y range() para recorrer los códigos e imprimirlos.
"""

codigos = ["p001", "p002", "p003"]

buscar = input("Ingrese el codigo: ")

if buscar in codigos:
    posicion = codigos.index(buscar)  # capturo el indice del codigo en mi lista
    print("Posicion encontrada: ", posicion)
else:
    print("Posicion no encontrada")  # si no lo encuentra, muestra un mensaje de
