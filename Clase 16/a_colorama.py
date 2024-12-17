# Ejecutar desde la consola el modulo colorama
# pip install colorama

# Importamos init y otros metodos de colorama
from colorama import init, Fore, Style, Back

# Inicializamos colorama ya que prepara el entorno para usar colores y estilos en la consola, especialmente en sistemas Windows
init()  # Inicializa Colorama

# Para que el estilo no se propague
init(autoreset=True)

# Para cambiar el color del texto
print(Fore.RED + "Este texto es rojo.")
print("Este texto es verde.")


print(Fore.GREEN + "Este texto es verde.")

print("Este texto vuelve al color original automáticamente.")

# Para cambiar el color del fondo
print(Back.YELLOW + "Aviso: el stock de este producto es muy bajo.")

# Para cambiar el estilo del texto
print(Style.BRIGHT + Fore.BLUE + "Bienvenido/a a la gestión de inventario.")
print(Style.DIM + "Nota: asegúrate de ingresar un ID válido.")
print(
    Back.YELLOW + Fore.RED + "Alerta: el stock de este producto es crítico. Se recomienda reponer."
)
