# ## scalar operations:
# aithmetic:-  +, -, *, /, **.
# addition

import numpy as np
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
result = arr1 + arr2
print(result)


## subtraction
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
result = arr1 - arr2
print(result)

## multiplication 

arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 3, 4])
result = arr1 * arr2

print(result)

## division 

arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 4, 5])
result = arr1 / arr2

print(result)

## floor division 

arr1 = np.array([10, 20, 30])
arr2 = np.array([3, 4, 7])
result = arr1 // arr2
print(result)

##modules 

arr1 = np.array([10, 20, 30])
arr2 = np.array([3, 4, 7])
result = arr1 % arr2

print(result)

## power 
arr = np.array([2, 3, 4])
result = arr ** 2

print(result)

## square root 
arr = np.array([4, 9, 16, 25])

print(np.sqrt(arr)) 

## expotential 
arr = np.array([1, 2, 3])
print(np.exp(arr))

##
# all this can br perform to the matrix of the array.


import numpy as np

# 15. np.argmax() - Index of Maximum Value

arr = np.array([10, 50, 30, 80, 20])
print("Array:", arr)
print("Index of Maximum Value:", np.argmax(arr))
print()

# 16. np.argmin() - Index of Minimum Value

arr = np.array([10, 50, 30, 80, 20])
print("Array:", arr)
print("Index of Minimum Value:", np.argmin(arr))
print()


# 17. np.std() - Standard Deviation

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Standard Deviation:", np.std(arr))
print()


# 18. np.var() - Variance

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Variance:", np.var(arr))
print()


# 19. np.abs() - Absolute Value

arr = np.array([-10, -5, 20, -30])
print("Array:", arr)
print("Absolute Values:", np.abs(arr))
print()


# 20. np.round() - Round Decimal Values

arr= np.array([2.3456, 5.6789, 8.9999])
print("Array:", arr)
print("Rounded (2 Decimal Places):", np.round(arr, 2))
print()


# 21. Comparison Operations

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Greater than 25:")
print(arr > 25)
print("Less than 25:")
print(arr < 25)
print("Greater than or Equal to 30:")
print(arr >= 30)
print("Less than or Equal to 30:")
print(arr <= 30)
print("Equal to 20:")
print(arr == 20)
print("Not Equal to 20:")
print(arr != 20)
print()


# 22. Boolean Filtering

arr = np.array([10, 20, 30, 40, 50, 60])
print("Array:", arr)
print("Values Greater than 30:")
print(arr[arr > 30])
print("Values Between 20 and 50:")
print(arr[(arr >= 20) & (arr <= 50)])
print()


# 23. Broadcasting

arr = np.array([10, 20, 30])
print("Original Array:", arr)
print("Add 5:")
print(arr + 5)
print("Multiply by 10:")
print(arr * 10)
vector = np.array([1, 2, 3])
print("Add Another Array:")
print(rr + vector)
print()


# 24. np.matmul() - Matrix Multiplication

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)
print()
print("Matrix B:")
print(B)
print()
print("Matrix Multiplication (A x B):")
print(np.matmul(A, B))
print()


# 25. np.dot() - Dot Product

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vector A:", a)
print("Vector B:", b)
print("Dot Product:")
print(np.dot(a, b))
print()
# ##relational operations:-  <,>,>=,<=,!=,==.
# this can do operations comaprison.
##vector operations:-   doinf operations on both array like add,subtract,and all.
