# Comentario en linea

"""
Comentar múltiples lineas:
Comentario linea 1
Comentario linea 2
Comentario linea 3
"""


# creamos la variable cadena y le asignamos el valor "1234"
cadena = "1234"

# creamos la variable entero y le asignamos el valor 45
entero = 45

# creamos la variable flotante y le asignamos el valor 56.2
flotante = 56.2


# la funcion type() nos devuelve el tipo de dato de una variable
# type(cadena)

# la funcion print() imprime en pantalla el string que reciba como argumento
# print("Hola mundo")
# nombre = "Juan"
# print(nombre)

# imprimimos el tipo de dato de la variable cadena

# print(type(cadena))
# print(type(entero))
# print(type(flotante))

# mejoramos la impresión en consola o terminal concatenando
# Que es concatenar? Unir 2 string o cadenas
# print("Hola" "mundo")
# print("Hola" + "mundo")
# print("Hola", "mundo")

# print("El tipo de dato de la variable cadena es:" + str(type(cadena)))
# Queremos mostrar en pantalla el valor y el tipo de una variable

# print(
#     "El valor de la variable cadena es: "
#     + cadena
#     + " y el tipo de dato es: "
#     + str(type(cadena))
# )

# print(
#     "El valor de la variable entero es: "
#     + str(entero)
#     + " y el tipo de dato es: "
#     + str(type(entero))
# )

# print(
#     "El valor de la variable entero es: ",
#     entero,
#     " y el tipo de dato es: ",
#     str(type(entero)),
# )

# usamos f para formatear el contenido de print
# print(
#     f"El valor de la variable entero es: {entero} y el tipo de dato es: {type(entero)}"
# )

# str(variabe) convierte el tipo de dato de la variable a string
# vamos a ver ahora, int(cadena)
# print(f"El valor de cadena es {cadena} y el tipo de dato es {type(cadena)}")
# x = 10
# print(f"El valor de x es {x} y el tipo de dato es {type(x)}")
# y = x + int(cadena)  # sumando un str con un int ERROR

# print(
#     f"El resultado de la suma la guardamos en y, con valor {y} con tipo de dato {type(y)}"
# )

"""
Operadores de asignación =
"""
cantidad = 10
precio = 120.5
nombre = "Adrian"
entregado = True

# print(f"El valor de cantidad es: {cantidad}")

"""
Expresiones y sentencias
Una expresión es una unidad de código que devuelve un valor
Esta formada por una combinación de operandos (variables y literales) y operadores
"""

# x = 5 + 2  # sumamos 2 literales
# print(f"la suma de 5 + 2 es: {x}")

# x = 5
# y = x + 2  # sumando una variables con un literal
# print(f"la suma de 5 + 2 es: {y}")

# a = 6
# b = a < 10
# print(f"Que devuelve la expresión a < 10? {b}")

# b = None
# print(f"El valor de b es: {b} y el tipo de dato es: {type(b)}")
# print(f"b es None? {b is None}")


"""
Operadores aritméticos
Los utilizamos para realizar operaciones matemáticas
+ Suma
- Resta
* Multiplicación
/ División
// División entera (redondea hacia abajo)
% Módulo
** Potencia
Raiz (usamos notacion exponencial)
"""

# suma = 2 + 5
# resta = 10 - 5
# multiplicacion = 5 * 3
# division = 9 / 2
# divicion_entera = 9 // 2
# modulo = 9 % 2
# potencia = 2**4
# raiz = 125 ** (1 / 3)


# print(
#     f"suma: {suma}, \nresta: {resta}, \nmultiplicacion: {multiplicacion}, \ndivision: {division}, \ndivision entera: {divicion_entera}, \nmodulo: {modulo}, \npotencia: {potencia}, \nraiz: {raiz}"
# )


"""
Función input
Proporciona un mecanismo para el ingreso de datos a nuestro programa
Permite mostrar texto - como lo haría print
Devuelve un string con el valor de lo ingresado
"""

# nombre = input("Ingrese su nombre: ")
# print(f"El valor de nombre es {nombre} y el tipo de dato es {type(nombre)}")
# edad = input("Ingrese su edad: ")
# print(f"El valor de nombre es {edad} y el tipo de dato es {type(edad)}")
