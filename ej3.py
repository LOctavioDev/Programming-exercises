# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

def sum_array(arr):
    if (type(arr) == type(None)) or (len(arr) <= 1):
        return 0
    else:
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)


array1 = None
array2 = [1, 1, 11, 2, 3]

print(sum_array(array1))