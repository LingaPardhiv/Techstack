#Q1
# class Animal:
#     def sound(self):
#         print("animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# obj=Animal()
# obj.sound()
#
# obj1=Dog()
# obj1.sound()

# Q2
# class A:
#     def show(self):
#         print("A class")
#
# class B(A):
#     def show(self):
#         print("B class")
#         super().show()
#
# obj=B()
# obj.show()

#Q3
# class A:
#     def display(self):
#         print("Class A")
#
# class B(A):
#     def display(self):
#         print("Class B")
#
# class C(B):
#     def display(self):
#         print("Class C")
#
# obj=C()
# obj.display()

#Q4
# class Vehicle:
#     def type(self):
#         print("This is a Vehicle")
#
# class Car(Vehicle):
#     def wheels(self):
#         print("4 wheels")
#
# class Bike(Vehicle):
#     def wheels(self):
#         print("2 Wheels")
#
# c=Car()
# b=Bike()
#
# c.type()
# c.wheels()
#
# b.type()
# b.wheels()

#Q5
# class Employee:
#     def salary(self):
#         basic_salary=30000
#         print(f'Employee Salary : {basic_salary}')
#
# class Manager(Employee):
#     def salary(self):
#         basic_salary=30000
#         incentive=10000
#         total_salary=basic_salary + incentive
#         print(f'Manager Salary : {total_salary}')
#
# e=Employee()
# e.salary()
#
# m=Manager()
# m.salary()

# Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.
# class Father:
#     def skills(self):
#         print("Father skills")
#
# class Mother:
#     def skills(self):
#         print("Mother skills")
#
# class Child(Father,Mother):
#     pass
#
# obj=Child()
# obj.skills()
# print(Child.mro())

# Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor.

class Person:
    def __init__(self,name):
        self.name = name
        print("person constructor called")

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
        print("student constructor called")

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll)

obj1=Student("arjun",22)
obj1.display()

# Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.

# class University:
#     university_name="JNTU Hyderabad"
#
#     @classmethod
#     def show_university(cls):
#         print("University name",cls.university_name)
#
# class College(University):
#     college_name = "St.Martin's Engineering College"
#
# print(College.university_name)
# College.show_university()

# Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.

# class MathOps:
#     @staticmethod
#     def add(a,b):
#         return a + b
#
# class AdvancedOps(MathOps):
#     pass
#
# result= AdvancedOps.add(10,20)
# print(result)

