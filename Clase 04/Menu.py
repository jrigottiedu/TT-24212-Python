"""
Menú principal

Consigna
Crea un programa que solicite al usuario dos números enteros. 
Que muestre un menú de opciones (operaciones matematicas)
Que informe el resultado
"""

# Entrada
numero_1 = int(input("Ingrese el numero_1: "))
numero_2 = int(input("Ingrese el numero_1: "))

print("Seleccione la operación a realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Su elección es:"))
print(f"su opcion fue: {opcion}")

# Proceso
if opcion == 1:
    suma = numero_1 + numero_2
    print(f"El resultado de la suma es: {suma}")  # Salida

elif opcion == 2:  # sino si
    resta = numero_1 - numero_2
    print(f"El resultado de la resta es: {resta}")  # Salida

elif opcion == 3:
    multiplicacion = numero_1 * numero_2
    print(f"El resultado de la multiplicacion es: {multiplicacion}")  # Salida

elif opcion == 4:
    division = numero_1 / numero_2
    print(f"El resultado de la division es: {division}")  # Salida
else:
    print("Opción no válida - Ingrese un número del 1 al 4")  # Salida


"""
A mejorar:
1. pensar en alternativas al uso de if/elif/else
2. incorporar el código a un bucle (podría ser un While) con alguna condición de fin. 
Por ejemplo, ingrese X para salir. 
"""
