horas_trabajadas = int(input("ingrese el valor de cantidad trabajadas:"))
valor_hora = int(input("ingrese el valor por hora:")) 

if  horas_trabajadas > 40:
    horas_normales = 40 
    horas_extra = horas_trabajadas - 40
    salario = (horas_normales * valor_hora) + (horas_extra * valor_hora * 1.5)
else:
    salario = horas_trabajadas * valor_hora

print("Pago total por horas extras:", salario)
    