arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

print(arr.astype(float))
print(arr.reshape(3, 2))
print(arr.flatten())
print(arr.T)

new_arr = arr.copy()
print(new_arr)