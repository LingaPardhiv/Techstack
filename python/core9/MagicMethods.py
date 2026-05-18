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

# class B:
#     k=[]
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         B.k.append(other)
#         return B.k
#
# b1=B(25)
# print(b1+"Hello")

#create a class Vector with instance Variables x,y as their co-ordinates
# let's take v1,v2 as vector objects
# v1+v2-> should return addition of co-ordinates
# v1-v2

# class Vector:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def __add__(self,other):
#         return self.x+other.x,self.y+other.y
#     def __sub__(self,other):
#         return self.x-other.x,self.y-other.y
#
# v1=Vector(1,2)
# v2=Vector(3,4)
# print(v1+v2)
# print(v1-v2)

class B:
    def __init__(self,x):
        self.x=x
        self.y=25

    def __setattr__(self,key,value):
        if key=='x':
            if x>=0:
                super().__setattr__(key,value)
            else:
                print("Wrong Value")
        super().__setattr__(key,value)

    def __getattribute__(self,name):
        if name=='x':
            pin=input()
            if pin=="522651":
                return super(),__getattr__(name)

    def __getattr__(self,name):
        return "Not found"

    def __repr__(self):
        return f' '

