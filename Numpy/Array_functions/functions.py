import numpy as np
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a1)
print(a2)

## max functions

a=np.max(a1)
print(a)

##minimum number

a=np.min(a2)
print(a)

##sum

a=np.sum(a2)
print(a)

##product

a=np.prod(a1)
print(a)

##axis:- axis mean findng the things in particular row and colunmn

a=np.max(a1,axis=1)
print(a)

a=np.min(a2,axis=0)
print(a)

## mean:- calculate the mean of the array

a=np.mean(a1,axis=0)
print(a)
a=np.mean(a1)
print(a)

##median :- calculate the median of the array in particular row and column

a=np.median(a2)
print(a)

##standard deviation

arr = np.array([10, 20, 30, 40, 50])

std = np.std(arr)

print("Array:", arr)
print("Standard Deviation:", std)

## variance

arr = np.array([10, 20, 30, 40, 50])

var = np.var(arr)

print("Array:", arr)
print("Variance:", var)