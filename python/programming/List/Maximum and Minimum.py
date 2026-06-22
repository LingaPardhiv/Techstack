# Maximum and Minimum
# 19Q
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
k=int(input())
for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[n-k])
print(a)