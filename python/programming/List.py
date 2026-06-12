#1Q
# n=int(input())
# a=[]
# for i in range(0,n):
#     a.append(int(input()))
# print(a)
#2Q
# b=[1000,2000]
# b.insert(1,100)
# print(b)
#3Q
# a=[1,2,3,4]
# b=[1000,2000]
# a.extend(b)
# print(a)
#4Q
# a=[1,2,3,4]
# a.remove(2)
# print(a)
#5Q
# a=[1,2,3]
# a.pop(0)
# print(a)
#6Q
# a=[1,5,6,34]
# print(a.index(6))
#7Q
# a=[1,2,2,44,2,34,5]
# print(a.count(2))
#8Q
# a=[1,2,2,224,21,3]
# print(a[0]+a[len(a)-1])
#9Q
# a=[12,2,4,5,5]
# idx=int(input())
# s=0
# for i in range(idx+1):
#     s+=a[i]
# print(s)
#10Q
# b=[1,2,3,4,5,6]
# s=c=0
# for i in b:
#     if i%2==1:
#         s+=i
#         c+=1
# print(s/c)
#11Q
# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     return fc==2
# a=[2,23,4,5,7,11]
# for i in a:
#     if isprime(i):
#         print(i,end=" ")
#13Q
# a=[1,2,34,5,6]
# print(a[::-1])
#14Q
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# keyVal=int(input())
# for i in range(1,n):
#     for j in range(i,n):
#         if a[i]+a[j]==keyVal:
#             print(a[i],a[j])

#Maximum and Minimum
#19Q
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# k=int(input())
# for i in range(0,n-1):
#     for j in range(0,n-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a[n-k])

#Taking input with spaces
a=list(map(int,input().split()))
print(a)

#Question
# a=[10,20,30,40,50]
# b=[]
# sum=0
# for i in a:
#     sum+=i
#     b.append(sum)
# print(b)

#Question
# b=[]
# c=0
# k=1
# while c<5:
#     if k%2==0:
#         b.append(k)
#         c+=1
#     k+=1
# print(b)

#Question
# a=[]
# c=0
# p=2
# n=5
# x=(n*(n+1))//2
# while c<x:
#     fc=0
#     for i in range(1,p+1):
#         if p%i==0:
#             fc+=1
#     if fc==2:
#         a.append(p)
#         c+=1
#     p+=1
# z=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a[z],end=" ")
#         z=z+1
#     print()
# for i in range(1,n+1):
#     k=i
#     z=n-1
#     for j in range(1,i+1):
#         print(a[k-1],end=" ")
#         k=k+z
#         z=z-1
#     print()