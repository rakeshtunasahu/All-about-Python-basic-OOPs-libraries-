import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([[4,3],[4,1],[5,2],[1,9]])
c=np.array([[[4,5],[4,1]],[[5,2],[8,9]]])
print(a)
print(b)
print(c)


## ndim:-its checks the dimensions of the array
print(np.ndim(a))
print(np.ndim(b))
print(np.ndim(c))

## shape:- its checks the shape or the array
print(np.shape(a))
print(np.shape(b))
print(np.shape(c))

## size:- its checks the size or the array
print(np.size(a))
print(np.size(b))
print(np.size(c))

## itemsize:- its tells about how much it take a size in memory
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

## dtype:- its tell about the bytes using in the array
print(a.dtype) 
print(b.dtype)
print(c.dtype)