from functools import reduce
l=[5, 10, 15, 20, 25, 30]
sq=list(map(lambda x:x**2,l))
di = list(filter(lambda x:x%5 == 0,sq))
v = reduce(lambda x,y: x+y,di)
v1= reduce(lambda x,y: x+y,filter(lambda x:x%5 == 0,map(lambda x:x**2,l)))
print(v)