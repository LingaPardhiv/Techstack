#7th question
# from functools import reduce
# chars = ['P', 'y', 't', 'h', 'o', 'n']
# result = reduce(lambda x, y: x + y, chars)
# print(result)

#1st question
# l=  [[1, 2], [3, 4], [5, 6]]
# k = list(map(lambda x:x+[5],l))
# print(k)

#2nd question
# d = {"apple": 100, "banana": 40, "cherry": 150}
# print(d.keys())
# print(d.values())
# print(d.items())
# f=dict(filter(lambda x:x[1]>50,d.items()))
# print(f)

# 3rd question
# k=input()
# print(k.split())
# print(type(k))
#
# k=list(map(int,input().split()))
# m=-10**6
# for i in k:
#     if m<i:
#         m=i
#
# from functools import reduce
# print(reduce(lambda x,y:x if x>y else y,k))
# print(m)

# 10th question
from functools import reduce
l=[5, 10, 15, 20, 25, 30]
sq=list(map(lambda x:x**2,l))
di = list(filter(lambda x:x%5 == 0,sq))
v = reduce(lambda x,y: x+y,di)

v1= reduce(lambda x,y: x+y,filter(lambda x:x%5 == 0,map(lambda x:x**2,l)))
print(v)
