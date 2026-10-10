import numpy as np
import pandas as pd
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.matmul(A, B))
print(np.eye(3))
print(np.linalg.inv(A))
print(np.linalg.norm(a))

C = np.array([[2, 1], [1, 3]])
d = np.array([5, 6])

print(np.linalg.solve(C, d))