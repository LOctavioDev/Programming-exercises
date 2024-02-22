# Problema 1: Suma de elementos
# Escribe una función que reciba como entrada un arreglo de números enteros y devuelva la suma de todos los elementos en el arreglo.

def sum_array(array):
    sum_total = 0
    for index, value in enumerate(array):
        sum_total += value
    
    return sum_total


"""EXAMPLE"""

array = [1,2,3,4,5]

print(sum_array(array))