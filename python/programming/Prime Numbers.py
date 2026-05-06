#Alternative Prime Numbers in a given Range
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc=fc+1
    if fc==2:
        c+=1
        if c%2==1:
            if c!=1:
                print(",",end="")
            print(i,end="")

#if a number is prime number print its position if not print not a prime number
def isPrime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
n=int(input())
c=0
if isPrime(n):
    for i in range(1,n+1):
        if isPrime(i):
            c+=1
    print(c)
else:
    print("Not a Prime Number")