#Magic Methods
# class B:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a + other.a
#
# b1=B(25)
# b2=B(34)
# print(b1+b2)

class B:
    k=[]
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        B.k.append(other)
        return B.k

b1=B(25)
print(b1+"Hello")

