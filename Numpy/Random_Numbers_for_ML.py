import numpy as np
import pandas as pd
np.random.seed(42)

print(np.random.randint(0, 10, 5))
print(np.random.rand(3))

arr = np.array([10, 20, 30, 40, 50])
np.random.shuffle(arr)

print(arr)