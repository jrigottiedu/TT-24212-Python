"""
# Declaramos una funcion <<def>>
def nombre_funcion():
    # Aqui va el codigo de la funcion
    print("Hola mundo")


def bucle_while():
    indice = 0
    while indice < 3:
        print(indice)
        indice += 1
    print("While finalizado")


# Llamar a la funcion / invocar a funcion
nombre_funcion()  # Llama a la funcion y ejecuta el codigo dentro de ella.

bucle_while()  # Llama a la funcion y ejecuta el codigo dentro de ella.

"""


# declaro funcion suma
def funcion_suma(a, b, c=0):  # 5, 3, 40
    suma = a + b + c
    multiplicacion = a * b * c
    diccionario_operaciones = {"suma": suma, "multiplicacion": multiplicacion}
    # print(f"la suma de a + b en la funcion es: {suma}")
    return diccionario_operaciones


numero_1 = 5
numero_2 = 3
numero_3 = 3
resultado = funcion_suma(
    numero_1, numero_2, 40
)  # invoco a la funcion y le paso a=5 y b=3
print(f"la suma de a + b + c en la funcion es: {resultado["suma"]}")
print(f"la multiplicacion de a x b x c en la funcion es: {resultado["multiplicacion"]}")

"""
#Declarar una funciona para guardar los datos en una lista
def guardar_datos_en_lista():
    lista_productos.append()    


lista_productos = []
nombre = input("Ingrese nombre: ")
cantidad = int(input("Ingrese cantidad: "))
lista_productos.append([nombre, cantidad])

print(lista_productos)
"""
