ventas = int(input("Ingrese el valor de las ventas mensuales: "))

if ventas > 1_000_000:
    comision = ventas * 0.10
else:
    comision = ventas * 0.05

print("La comisión es de:", comision)