# Core Notes

Class:

A class is a blueprint or template for creating objects. It defines the 
properties and methods that an object of that class will have.

Basic Syntax:
```
class Details:
    name="Rohan"
    age=20
```
Object:

An Object is an instance of a class, and it contains its own data
and methods

Basic Syntax:
```
obj1 = Details()
```

self Parameter:

The self parameter is a reference of the current instance of the class, 
and is used to access variables that belongs to the class

Example:
```
class Details:
    name="Rohan"
    age=20
    
    def info(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
    
obj1 = Details()
obj1.info()    
```
Output:
```
My name is Rohan and I am 20 years old.
```
Constructor:

A constructor is a special method in a class used to create and
initialize an object of a class. Constructor is a unique function 
that gets called automatically when an object is created of a class.

Syntax:
```
def init(self):
    # initializations
```

Decorator:

A decorator is a function that takes another function as an argument 
and returns a new function that modifies the behaviour of the original 
function. The new function is often referred to as a "decorated" 
function.

Syntax:
```
@decorator_function
def my_function():
    pass
```
Example:
```
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def add(a,b):
    print(a+b)

add(1,2)
```