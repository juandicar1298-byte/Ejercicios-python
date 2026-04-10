import os
import sys
import subprocess

# Títulos descriptivos para cada algoritmo
TITULOS = {
    1:  "Suma y promedio de tres números enteros",
    2:  "Área de un rectángulo",
    3:  "Conversión de Celsius a Fahrenheit",
    4:  "Cálculo de salario semanal",
    5:  "Salario con recargo por horas extras",
    6:  "Factura de producto (precio × cantidad)",
    7:  "Descuento por compra mayor a $200.000",
    8:  "Descuento por porcentaje (con detalle)",
    9:  "Descuento por porcentaje (precio final)",
    10: "Suma de precios de múltiples productos",
    11: "Comisión fija del 5% sobre ventas",
    12: "Comisión variable según meta de ventas",
    13: "Promedio de notas y estado de aprobación",
    14: "Nota definitiva ponderada (talleres/parcial/final)",
    15: "Mayor entre dos números",
    16: "Determinar si un número es par o impar",
    17: "Cálculo de edad según año de nacimiento",
    18: "Clasificación por rango de edad",
    19: "Conversión de pesos colombianos a dólares",
    20: "Cálculo de interés simple",
    21: "Cálculo de interés compuesto",
    22: "Control de inventario (entradas y salidas)",
    23: "Costo de envío según peso del paquete",
    24: "Factura de consumo de agua",
    25: "Total y promedio de ventas ingresadas",
    26: "Área y perímetro de un círculo",
}

ARCHIVOS = {i: f"{i}.py" for i in range(1, 26)}
ARCHIVOS[26] = "funciones.py"

TOTAL = 26

# Directorio donde están los scripts (mismo que index.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def mostrar_menu():
    print()
    print("=" * 56)
    print("   TALLER 1 — Algoritmos Básicos en Python")
    print("   Autor: Juan Diego Cartagena")
    print("=" * 56)
    print()
    for num in range(1, TOTAL + 1):
        print(f"  {num:>2}. {TITULOS[num]}")
    print()
    print("   0. Salir")
    print()
    print("=" * 56)


def ejecutar(opcion):
    archivo = ARCHIVOS.get(opcion)
    ruta = os.path.join(BASE_DIR, archivo)

    print()
    print("-" * 56)
    print(f"  Algoritmo {opcion}: {TITULOS[opcion]}")
    print("-" * 56)
    print()

    if os.path.exists(ruta):
        subprocess.run([sys.executable, ruta])
    else:
        print(f"  [Error] No se encontró el archivo: {archivo}")
        print(f"  Asegúrate de que '{archivo}' esté en la misma carpeta que index.py.")


while True:
    mostrar_menu()
    opcion = input("  Seleccione una opción: ").strip()

    if opcion == "0":
        print()
        print("  ¡Hasta luego!")
        print()
        break
    elif opcion.isdigit() and 1 <= int(opcion) <= TOTAL:
        ejecutar(int(opcion))
        print()
        input("  Presiona ENTER para volver al menú... ")
    else:
        print()
        print("  [!] Opción no válida. Ingresa un número entre 0 y", TOTAL)
        input("  Presiona ENTER para continuar... ")