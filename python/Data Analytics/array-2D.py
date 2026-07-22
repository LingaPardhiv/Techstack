import numpy as n
#2d array
l3 = [[21,34,53,65,34,65],[243,3,45,64,32,21],[23,43,55,77,65,76]]
print(l3)
arr3=n.array(l3)
print("arr3 ->",arr3)

#indexing
print(arr3[0,3])
print(arr3[1,2])

#slicing
print(arr3[0,1:4])
print(arr3[1,2:])
print("arr3 ->",arr3)
# print(arr3[1:4,2:6])
print(arr3[0,1:6:2])

# Attributes
print(n.shape(arr3))
print(n.size(arr3))
print(n.ndim(arr3))
print(len(arr3))
print(type(arr3))
print(arr3.dtype)
print(arr3.astype(float))
print(arr3.flatten())

print(n.zeros((3,3)))
print(n.ones((4,4)))
print((n.eye(3,3).astype(int)))

#Mathematical operations
l4=[[12,23,45,53,54,67],[23,45,46,78,48,74],[23,56,78,43,78,84]]
arr4=n.array(l4)
print(l4,l3)
print(arr4,arr3)
#add
print(arr3+arr4)
print(n.add(arr3,arr4))
#sub
print(arr3-arr4)
print(n.subtract(arr3,arr4))
#product
print(arr3*arr4)
print(n.multiply(arr3,arr4))
#divison
print(arr3/arr4)
print(n.divide(arr3,arr4))

print(n.sqrt(arr3))
print(n.sqrt(arr4))
print(n.pow(arr4,2))