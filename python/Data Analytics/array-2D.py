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

#concatenation
l5 = [[32,43,34,32,43,45],[23,54,23,65,43,67]]
l6 = [[43,56,87,23,65,65],[34,65,76,54,43,24]]
arr5=n.array(l5)
print("arr5 ->",arr5)
arr6=n.array(l6)
print("arr5 ->",arr5)
print(arr5+arr6)
print(n.concatenate([arr5,arr6]))
#vertical concatenation
print(n.concatenate([arr5,arr6], axis=0))
print("vstack -> \n",n.vstack([arr5,arr6]))
#horizontal concatenation
print(n.concatenate([arr5,arr6], axis=1))
print("hstack -> \n",n.hstack([arr5,arr6]))

#appending
print('arr5 -> ',arr5,'arr6 -> ',arr6)
print(n.append(arr5,90))
print(n.append(arr6,[34,54,56]))
print(n.append(arr5,arr6))

#insert
print('arr5 -> ',arr5,'arr6 -> ',arr6)
print(n.insert(arr6,4,90))
#vertical insertion
print(n.insert(arr6,1,67,axis=0))
print(n.insert(arr6,[0,1],[1,2,3,4,5,6],axis=0))
#horizontal insertion
print(n.insert(arr6,4,78,axis=1))

#deletion
print('arr5 -> \n',arr5,'\n arr6 -> \n',arr6)
print(n.delete(arr6,3))
#rows removal
print(n.delete(arr6,1,axis=0))
#column removal
print(n.delete(arr6,3,axis=1))

#sorting
print(n.sort(arr6))

#searching
print(n.where(arr6==56))
print(n.where(arr6==43))
print("arr6 -> \n",arr6)
print(n.where(arr6%2==0))

l1 = [73,54,323,56,23,45]
print("li ->",l1)
arr1=n.array(l1)
print('arr1 ->',arr1)

#filteration
print("arr1 -> \n",arr1)
na=n.array([False,True,False,True,True,False])
print('na -> \n',na)
print(arr1[na])
print(arr1[arr1>=100])

# Aggregate Functions
print('arr6 ->',arr6)
print(n.sum(arr6))
print(n.mean(arr6))
print(n.max(arr6))
print(n.min(arr6))
print(n.size(arr6))
print(n.cumsum(9))
print(n.cumprod(6))

price = [50,100,150,200,250]
print("Price -> \n", price)
products_Quantity = n.array([2,6,3,4,1])
print("products_Quantity -> \n",products_Quantity)

customer = n.array([[50,100,150,200,250],[2,6,3,4,1]])
print("Customer -> \n",customer)
print(n.cumprod(customer))
items_total = n.cumprod(customer, axis = 0)
print("items_total -> \n",items_total)
total_bill = n.sum(items_total[1])
print("total_bill -> \n",total_bill)

# statistical functions
print("arr6 -> \n",arr6)
print(n.mean(arr6))
print(n.median(arr6))

import statistics as s
print(arr6.flatten())
print(s.mode(arr6.flatten()))

print(n.std(arr6))
print(n.var(arr6))