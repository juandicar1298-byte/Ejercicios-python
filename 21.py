capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés (ejemplo 0.05 para 5%): "))
periodos = int(input("Ingrese el número de períodos: "))

monto_final = capital * (1 + tasa) ** periodos

print("El monto final es:", monto_final)