# index.py

import os # interacción con el sistema operativo(archivos, directorios, rutas, variables de entorno, etc.) 
import sys # 
import subprocess


while True:
    
    print(" ===================================================")
    print(" taller 1 - algoritmos basicos en phyton ")
    print("by Juan Diego Cartagena")
    print(" menu principal ")
    print("====================================================")

    for i in range(1, 26):
        print(f"{i}. Ejecutar Algoritmo {i}")
    print("0. salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("saliendo ...")
        break 
    
    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"a{opcion}.py"

        if os.path.exists(archivo):
            # ejecutar el script con el intérprete actual
            subprocess.run([sys.executable, archivo])
        else:
            print(f"no existe {archivo}")

    else:
        print("opción no valida ")
    


    input("\n preciona ENTER para continuar ... ")

