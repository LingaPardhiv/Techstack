#Fibonacci Numbers for n count Numbers
n=int(input())
a=0
b=1
c=c1=0
while c1<=n:
    c1+=1
    print(a,end=" ")
    c=a+b
    a=b
    b=c
