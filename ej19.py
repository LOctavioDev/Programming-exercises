# Problema 2: Promedio de calificaciones
# Escribe una función que reciba como entrada un arreglo de calificaciones (números decimales) y devuelva el promedio de estas calificaciones.

def average_array(array):
    sum_total = 0
    average_total = 0
    for index, value in enumerate(array):
        sum_total += value
    
    average_total = sum_total / len(array)
    return average_total

"""EXAMPLE"""

array = [9.7, 6.6, 10, 10, 10]

print(average_array(array))