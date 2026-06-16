#29Q
# a=[2,2,2,3,4,3,5,6,7,7,8]
# n=len(a)
# for i in range(0,n):
#     f=0
#     for j in range(i,-1,-1):
#         if(a[i]==a[j]):
#             f=f+1
#     print(a[i],f)

#30Q
# a=[2,2,2,3,4,3,5,6,7,7,8]
# n=len(a)
# for i in range(0,n):
#     f=0;b=0;
#     for j in range(0,n):
#         if(a[i]==a[j]):
#             f=f+1
#     for j in range(i-1,-1,-1):
#         if(a[i]==a[j]):
#             b=b+1
#     if b==0:
#         print(a[i],f)

#31Q
# a=[2,2,2,3,4,3,5,6,7,7,8]
# n=len(a)
# max=0
# x=0
# for i in range(0,n):
#     f=0
#     for j in range(0,n):
#         if(a[i]==a[j]):
#             f=f+1
#     if(f>max):
#         max=f
#         x=a[i]
# print(x)

#32Q
# a=[2,2,2,3,4,3,5,6,7,7,8]
# n=len(a)
# for i in range(0,n):
#     f=0
#     for j in range(0,n):
#         if(a[i]==a[j]):
#             f=f+1
#     if f==1:
#         print(a[i])

#34Q
a=[2,2,2,3,4,3,5,6,7,7,8]
n=len(a)
for i in range(0,n):
    f=0
    for j in range(0,n):
        if(a[i]==a[j]):
            f=f+1
    if f>1:
        print(a[i])