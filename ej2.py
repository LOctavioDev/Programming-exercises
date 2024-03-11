num_user = int(input("Ingresa la cantidad de números que quieres: "))
arreglo = []
suma = 0

for i in range(num_user):
    variable = int(input("Número a sumar: "))
    arreglo.append(variable)
    
for numerado in arreglo:
    suma += numerado
    
print("La suma de los números es:", suma)
