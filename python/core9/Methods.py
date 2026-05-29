# Q1
# Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if self.marks>40:
#             return True
#         return False
#
# s1=Student("Anbariv",50)
# s2=Student('Amith',30)
# print(s1.is_passed())
# print(s2.is_passed())

#Q2
# Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

# class Employee:
#     company_name='TechCorp'
#     def __init__(self,name):
#         self.name=name
#
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name=new_name
#
# e1=Employee('Anbariv')
# e2=Employee('Amith')
#
# print(e1.company_name)
# print(e2.company_name)
#
# Employee.change_company('HP')
#
# print('After Changing Company Name')
# print(e1.company_name)
# print(e2.company_name)

#Q3
# Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

# class MathOps:
#     @staticmethod
#     def is_even(num):
#         if num%2==0:
#             return True
#         return False
#
# obj=MathOps()
# print(obj.is_even(21))
# result=MathOps.is_even(18)
# print(result)

#Q4
# Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

# class Car:
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def display_specs(self):
#         print('Mileage of Car:',self.mileage,"Wheels in Car:",self.wheels)
#     @classmethod
#     def change_wheels(cls,wheels):
#         cls.wheels=wheels
#
# c=Car(20)
# c.display_specs()
# Car.change_wheels(5)
# c.display_specs()

#Q5
# Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(c):
        return (c*9/5)+32
    def show_conversion(self):
        print(self.celsius)
        f=Temperature.to_fahrenheit(self.celsius)
        print(f)

t=Temperature(0)
t.show_conversion()
