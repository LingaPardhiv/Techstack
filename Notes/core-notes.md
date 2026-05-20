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