# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3


def stray(arr):
    unique_number = 0
    freq_dict = {}
    
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
            
    for key, value in freq_dict.items():
        if value == 1:
            unique_number = key
            break

    return unique_number 

arreglo = [10, 10, 100, 9, 23, 9, 23]

print(stray(arreglo))
