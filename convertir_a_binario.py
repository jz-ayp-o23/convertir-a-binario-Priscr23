"""
Diseña un programa para convertir un número base 10 a binario.
750722
"""
#Entradas
numero = int(input("Introduzca un múmero: "))

#Procedimientos
binario = []

if numero == 0:
    binario.append(0)
else:
    while numero > 0:
        residuo = numero % 2
        binario.insert(0, residuo)  # Insertar el residuo al principio de la lista
        numero = numero // 2

# Imprimir el número binario
print(f"El número {numero} en binario es {binario}")


