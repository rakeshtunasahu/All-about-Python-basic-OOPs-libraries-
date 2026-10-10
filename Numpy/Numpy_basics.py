import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.astype(float))
print(np.arange(1, 10))
print(np.zeros((2, 3)))
print(arr.reshape(5, 1))