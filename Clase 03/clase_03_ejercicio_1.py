"""
Operaciones Básicas

Crea un programa que solicite al usuario dos números enteros. 
Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
Muestra el resultado de cada operación en un formato claro y amigable. 
Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".
"""

# Entrada de datos
numero_1 = int(input("Ingrese el primer número entero"))
numero_2 = int(input("Ingrese el segundo número entero"))


# Proceso
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
modulo = numero_1 % numero_2


# Salida
print("La suma de los dos números es: ", suma)
print("La resta de los números es: ", resta)
print("La multiplicación de los números es: ", multiplicacion)
print("El módulo es: ", modulo)
