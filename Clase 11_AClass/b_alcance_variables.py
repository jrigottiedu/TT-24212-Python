# Declaracion de variables "GLOBALES"
numero_1 = 5
numero_2 = 10


# Declaracion de funciones
def funcion_suma(numero_1, numero_2):
    suma = numero_1 + numero_2
    numero_1 = numero_1 + 1
    return suma


# Código principal
resultado = funcion_suma(numero_1, numero_2)  # 5, 10
print(f"La suma de los numeros es: {resultado}")
print(f"El valor de numero_1 es: {numero_1}")


lista = [1, 2, 3]
lista.pop(0)
print(lista)  # [2, 3]
