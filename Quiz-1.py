import numpy as np

#Q1 - Write a function that returns the sum of an array of integers

arr = [1, 3, 5]
N = len(arr)

def arraySum(arr, N):
    if len(arr)== 1:
        return arr[0]
    else:
        return arr[0]+arraySum(arr[1:], N)

result1 = arraySum(arr, N)

#Q2 - Given two arrays of equal length, return a new array that is the sum of each index.

array1 = np.array([1, 3, 5])
array2 = np.array([2, 4, 6])

array_total = array1 + array2

result2 = arraySum(array_total, N)



#Answers
print("Q1")
print(result1)
print("Q2")
print(result2)
print("Q3")
print("1/6")