import numpy as np

##creating 1D  numpy arrays:-

a=np.array([2,4,5,6])
print(a)
print(type(a))

##creating 2D and 3D arrays:-

b=np.array([[4,5,3],[4,7,1]],[[5,2],[1,9]])
print(b)
print(type(b))

c=np.array([[[4,5],[4,1]],[[5,2],[8,9]]])
print(c)
print(type(c))

##dtype:- it changes the datatypes

d=([[4,6,7],[5,4,3]])
print(np.array(d,dtype=float))

## Arange:-it creates a range in array

e=np.arange(1,11)
print(e)
print(type(e))

## reshape:-it reshapes the array

f=np.arange(1,17).reshape(2,8)
print(f)

## ones and zeros:- it intialize the matrix to 1 or 0

g=np.ones((3,5))
print(g)

h=np.zeros((2,4))
print(h)

##random :- it creates random number in any dimensional array

i=np.random.random((3,4))
print(i)

##linspace:- it cerates a linear space between the numbers

j=np.linspace(1,16,9)
print(j)

## identity:- it creates and identity matix

k=np.identity(4)
print(k)

