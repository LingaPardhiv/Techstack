import numpy as n

#creation
l1 = [73,54,32,56,23,45]
print("li ->",l1)
arr1=n.array(l1)
print('arr1 ->',arr1)

# n1=int(input("enter the number"))
# print('n1 ->',n1)
# l2=[]
# for i in range(n1):
#     l2.append(i+(12*i))
# print('l2 ->',l2)
# arr2=n.array(l2)
# print('arr2 ->',arr2)

#indexing
print('arr1 ->',arr1)
print(arr1[1])
print(arr1[-1])

#slicing
print(arr1[2:])
print(arr1[2:5])
print(arr1[:-2])
print(arr1[1:-1])
print(arr1[0:5:2])

