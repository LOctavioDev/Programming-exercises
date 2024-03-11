def bubble_sort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    

array1 = [1,3,72,2,7,41,1]

bubble_sort(array1)

print(f'ARRGELO ORDENADO: {array1}')