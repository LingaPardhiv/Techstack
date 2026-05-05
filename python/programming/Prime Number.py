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
