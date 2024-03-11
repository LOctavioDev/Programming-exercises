def suma_and_avg(arr):
    total = sum(arr)
    average = total / len(arr)
    return total, average

arr = [10, 10, 9, 8, 10]  
    
total, average = suma_and_avg(arr)

print(f'SUM -> {total} || AVERAGE -> {average}')