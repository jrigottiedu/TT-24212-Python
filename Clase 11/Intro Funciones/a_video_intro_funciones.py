# Qué es una función?
# Es un bloque de código que realiza una tarea específica
# Ayuda a estructurar el programa
# hacerlo mas fácil de leer y mantener
# permite reutilizar código
# Puede no recibir ningún argumento, uno o varios
# Puede o no devolver un valor
# Devuelve múltiples valores usando tuplas, listas o diccionarios


# Declaración de funciones
def nombre_funcion():
    # Cuerpo de la función
    valor = "Test"
    return valor


# 1. Declaramos una función que no recibe ningún argumento y no retorna ningún valor
def funcion_1():
    # Cuerpo de la función
    print(
        """Menú principal
          1. Alta de producots
          2. Mostrar productos
          3. Salir"""
    )


# Llamar o invocar a la funcion_1
# print(f"\n 1. Función que no recibe ningún argumento y no retorna ningún valor")
# funcion_1()


# 2. Declaramos una función que recibe un argumento y no retorna ningún valor
def funcion_2(mensaje):
    print(mensaje)


# Llamar o invocar a la funcion_2
# print(f"\n 2. Función que recibe un argumento y no retorna ningún valor")
# mensaje = """Menú principal
#   1. Alta de producots
#   2. Mostrar productos
#   3. Salir"""
# funcion_2(mensaje)


# 3. Declaramos una función que recibe múltiples argumentos y no retorna ningún valor
def funcion_3(numero_1, numero_2):
    suma = numero_1 + numero_2
    print(suma)


# Llamar o invocar a la funcion_3
# print(f"\n 3. Función que recibe múltiples argumentos y no retorna ningún valor")
# a = 5
# b = 10
# funcion_3(a, b)


# 4. Declaramos una función que recibe múltiples argumentos y retorna un valor
def funcion_4(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma


# Llamar o invocar a la funcion_4
# print(f"\n 4. Función que recibe múltiples argumentos y retorna un valor")
# a = 5
# b = 10
# suma = funcion_4(a, b)
# print(f"La suma de a y b es: {suma}")


# 5. Declaramos una función que recibe múltiples argumentos y retorna multiples valores
def funcion_5(numero_1, numero_2):
    suma = numero_1 + numero_2
    multiplicacion = numero_1 * numero_2
    # respuesta = (suma, multiplicacion)  # retorna con tupla
    return suma, multiplicacion


# Llamar o invocar a la funcion_5
# print(
#     f"\n 5. Declaramos una función que recibe múltiples argumentos y retorna multiples valores"
# )
# a = 5
# b = 10
# resultado = funcion_5(a, b)
# print(resultado[0], resultado[1])
# print(f"Suma: {resultado[0]} - Multiplicación: {resultado[1]}")
# suma, multiplicacion = funcion_5(a, b)
# print(f"Suma: {suma} - Multiplicación: {multiplicacion}")


# *** Argumentos por defecto ***
# Declaramos una función que suma números
def sumar(numero_1, numero_2=100):
    suma = numero_1 + numero_2
    print(f"La suma es {suma}")


# Llamar o invocar a la función sumar
# a = 5
# b = 10
# sumar(a, b)


# *** Argumentos nombrados ***
# Declaramos una función que suma muestre los argumentos recibidos
def mostrar_argumentos(numero_1, numero_2):
    print(f"Argumento 1: {numero_1}, Argumento 2: {numero_2}")


# Llamamos o invocamos a la función mostrar_argumentos
# a = 5
# b = 10
# mostrar_argumentos(numero_2=b, numero_1=50)  # Llamada con argumentos


# # *** Alcance de las variables ***
# variable_global = "Python"


# Declaramos una función que hace un print en consola
def mostrar_mensaje():
    saludo = "Bienvenidos a: "  # saludo es una variable local
    print(saludo, variable_global)


# Llamar o invocar a la función mostrar_mensaje
# mostrar_mensaje()


# *** Variables mutables e inmutables en Python ***
numero_global = 10
lista_global = [1, 2]


# Declaramos una función que incrementa un número
def incrementar():
    global numero_global  # Indicamos que queremos modificar la variable global
    numero_global += 1
    lista_global[0] += 1
    lista_global[1] += 1


# Llamamos o invocamos a la función incrementar
# print(f"Numero global: {numero_global}")
# print(f"Lista global: {lista_global}")
# incrementar()
# print(f"Numero global incrementado: {numero_global}")
# print(f"Lista global incrementada: {lista_global}")


# *** Funciones que llaman a Funciones ***
# Declaramos la función ingresar 2 números
def ingresar_numeros():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    return a, b


# Declaramos la función sumar 2 números
def sumar_numeros(a, b):
    suma = a + b
    return suma


# Declaramos la función ingresar y suma 2 números
def ingresar_sumar_numeros():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    suma = sumar_numeros(a, b)
    return suma


# Llamar o invocar a las funciones
# a, b = ingresar_numeros()
# resultado = sumar_numeros(a, b)
# print("La suma de los números es: ", resultado)
print("La suma de los números es: ", ingresar_sumar_numeros())
