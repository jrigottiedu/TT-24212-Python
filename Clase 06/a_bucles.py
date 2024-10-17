"""
Bucles

while
contadores
acumuladores
"""

# La estructura de un Bucle while se compone de:
# 1. La palabra reservada while
# 2. La condición (mientras sea True se ejecutará, en cuanto sea False se termina)
# 3. Los : al final y la indentación
# Ejemplo: while + condicion + :

# Declaramos e inicializamos la variable condicion con el valor bool True
condicion = True

# Mientras la variable condición sea True se ejecutará el Bucle while
while condicion:
    check = input("Ingrese x para salir o cualquier tecla para continuar: ").lower()
    if check == "x":
        condicion = False

# --------------------------------------------------------------------------------
# Introducimos el concepto de contador

# Declaramos e inicializamos la variable contador en 0
contador = 0

# mientras el valor de la variable contador sea menor a 0, la condición sera True
while contador < 10:
    print(contador)

    # El contador se puede incremantar de dos maneras:
    # contador = contador + 1  # forma 1
    contador += 1  # forma 2


# --------------------------------------------------------------------------------
# Introducimos el concepto de acumulador

contador = 0  # define la cantidad de veces que se ejecuta el Bucle
acumulador = 0  # almacenar la suma de los valores ingresados

while contador < 3:
    valor = float(input("Ingrese un número: "))

    # usamos el acumulador para almacenar la suma de los valores ingresados
    acumulador = acumulador + valor

    print(f"acumulacion parcial: {acumulador}")
    contador += 1  # Siempre tiene que estar

print(f"acumulacion final: {acumulador}")

"""
Desafío: refactorizamos el código del Ejercio 2 - clase 2 incorporando lo aprendido

Ingreso promedio

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 
"""

# Declaración e inicialización de variables
CANTIDAD_MESES = 6  # la usamos como constante
contador_meses = 0  # contador
acumulador_sueldos = 0  # acumulador

print()  # print para generar un espacio en blanco

# Bucle while que se ejecuta tantas veces como sea CANTIDAD_MESES
while contador_meses < CANTIDAD_MESES:
    contador_meses = contador_meses + 1  # incrememtamos el contador
    ingreso = float(input(f"Ingrese el sueldo del mes {contador_meses}: "))
    acumulador_sueldos = (
        acumulador_sueldos + ingreso
    )  # acumulamos los ingresos mensuales
    print(f"sumar parcial {acumulador_sueldos} ")  # impresiones parciales

promedio = acumulador_sueldos / contador_meses  # calculamos el promedio
print(f"\nEl ingreso promedio en el semestre es de {promedio}")


# ---------------------------------------------------------------------
# Bucles y cadenas
# veamos ahora como usar Bucles con cadenas

# Declaraos e inicializamos la variable cadena con el tipo de dato str Python
cadena = "Python"
indice = 0  # hace las veces de un contador
print(cadena)

# usamos la función len() que recibe como argumento una cadena y retorna la longitud
# esto nos va a permitir recorrer todos los caracteres de la cadena
while indice < len(cadena):  # len(cadena) para cadena = "Python" retorna 6
    # print(cadena[indice]) # en cada iteración retorna P - y - t - h - o - n
    print(f"cadena[{indice}]: {cadena[indice]}")  # más descriptivo
    indice += (
        1  # incrementamos el contador/indice para que apunte al siguiente caracter
    )

# ----------------------------------------------------------------------
# Más de Bucles y cadenas
# usando la estructura anterior, veamos como transformar
# la cadena origina Python en PyThOn

cadena = "Python"
indice = (
    0  # hace las veces de un contador y permite recorrer cada caracter de la cadena
)
print(cadena)

while indice < len(cadena):  # len(cadena)=> 6
    # bloque de código que los indices pares imprima el caracter en mayuscula
    if indice % 2 == 0:  # estoy en indices pares
        print(cadena[indice].upper())
    # y que los indice impares imprima en minuscula => usar %
    else:
        print(cadena[indice].lower())
    indice += 1  # incrementamos el contador / indice
