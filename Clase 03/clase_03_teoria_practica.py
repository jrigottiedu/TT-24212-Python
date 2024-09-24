# comentarios 1 linea
"""
comentarios multiples lineas+
"""

cadena = "Hola, mundo"  # str (string)
entero = 45  # int (integer entero)
flotante = 15.5  # float (coma flotante)

# type()  tipo de dato de una variable

# print(type(cadena))
# print(f"el valor de cadena es {cadena} y el tipo de dato es {type(cadena)}")
# print(f"el valor de entero es {entero} y el tipo de dato es {type(entero)}")
# print(f"el valor de flotante es {flotante} y el tipo de dato es {type(flotante)}")

# print("El valor de entero es: " + str(entero))

# ingreso_enero = 1000
ingreso_enero_str = input(
    "Ingrese el monto de enero"
)  # guardo en ingreso_enero_str un string
print(type(ingreso_enero_str))
ingreso_enero_int = int(ingreso_enero_str)  # convierto un str a int
medio_ingreso = ingreso_enero_int / 2  # divido por 2
print("el monto ingresado es de: " + str(medio_ingreso))

# mejorar nuestro código
ingreso_enero_int = int(input("Ingrese el monto de enero"))
medio_ingreso = ingreso_enero_int / 2
print(f"el ingreso medio es {medio_ingreso}")


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

numero_1 = 10.3  # numero_1 sea float
numero_2 = 2  # numero_2 sea int
suma_variables = numero_1 + numero_2  # suma de 2 variables
suma_literales = 2 + 7  # suma de 2 literales
multiplicacion = 2 * numero_2
division = 9 / 2  # devuelve 4.5
division_entera = 9 // 2  # devuelve 4
modulo = 9 % 2  # devuelve 1
