#Fibonacci Numbers for n count Numbers
# n=int(input())
# a=0
# b=1
# c=c1=0
# while c1<=n:
#     c1+=1
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#if a number is fibonacci number print its position if not print not a fibonacci number
def isfibo(n):
    a=0
    b=1
    c=0
    while a<=n:
        if a==n:
            return True
        c=a+b
        a=b
        b=c
s=int(input())
c1=0
if isfibo(s):
    for i in range(1,s+1):
        if isfibo(i):
            c1+=1
    print(c1)
else:
    print("Not a Fibonacci Number")