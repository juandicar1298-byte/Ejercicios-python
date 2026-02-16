cantidad_inicial = int(input("Ingrese la cantidad inicial en inventario: "))
cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
cantidad_recibida = int(input("Ingrese la cantidad recibida: "))

inventario_final = cantidad_inicial - cantidad_vendida + cantidad_recibida

print("El inventario final es:", inventario_final)