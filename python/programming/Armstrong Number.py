a=int(input())
b=int(input())
for n in range(a,b+1):
    t=n
    dc=0
    while n!=0:
        n=n//10
        dc=dc+1
    n=t
    s=0
    while n!=0:
        r=n%10
        s=s+r**dc
        n=n//10
    if s==t:
        print(t,end=" ")