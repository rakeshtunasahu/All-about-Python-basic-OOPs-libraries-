
import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[1:4])
print(arr[arr > 30])

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(np.add(a, b))
print(np.multiply(a, b))
print(a + 10)

A = np.array([[1, 2], [3, 4]])
print(A.T)