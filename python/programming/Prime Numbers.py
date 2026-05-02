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