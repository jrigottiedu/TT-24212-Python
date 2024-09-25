"""
Calculadora de Propinas

Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante. 

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
 
Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina). 
Finalmente, muestra los resultados en la pantalla.

"""

# Ingreso de datos
# cuenta y el porcentaje de propina
cuenta = None
porcentaje_propina = None

cuenta = float(input("Ingrese el monto de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))

if porcentaje_propina < 10:  # porcenta_propina < 10 es la condicion
    print("El porcentaje de propina es menor a 10%")
elif porcentaje_propina < 50:
    print("El porcentaje de propina es menor a 50%")
else:
    print("El porcentaje de la propina el mayor a 50%")

# Proceso
# calular la propina
propina = cuenta * (porcentaje_propina / 100)
cuenta_con_propina = cuenta + propina


# Salida
# mostrar en pantalla la cuenta con la propina
print(
    f"El valor de la propina es {propina} y el total a pagar es de: {cuenta_con_propina:.1f}"
)
