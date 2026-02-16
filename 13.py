nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("El promedio es:", promedio)

if promedio >= 3.0:
    print("El estudiante aprueba")
else:
    print("El estudiante no aprueba")