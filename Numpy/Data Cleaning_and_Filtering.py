arr = np.array([10, 20, np.nan, 40, 50])

print(np.isnan(arr))
print(np.nanmean(arr))
print(np.nan_to_num(arr, nan=0))

values = np.array([-10, 20, 30, 110])

print(np.where(values < 0, 0, values))
print(np.unique([10, 20, 10, 30, 20]))
print(np.sort(values))
print(np.clip(values, 0, 100))