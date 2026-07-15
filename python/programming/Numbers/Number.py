#if a digit given is present in before(decrement) of the given number then print the Number
n=int(input())
d=int(input())
for i in range(n-1,0,-1):
    t=i
    z=0
    while t!=0:
        r=t%10
        if r==d:
            z=1
            break
        t=t//10
    if z==1:
        print(i)
        break