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

# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_fahrenheit(c):
#         return (c*9/5)+32
#     def show_conversion(self):
#         print(self.celsius)
#         f=Temperature.to_fahrenheit(self.celsius)
#         print(f)
#
# t=Temperature(0)
# t.show_conversion()

#Q6
# Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation

# class Book:
#     total_books=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.total_books+=1
#
#     @classmethod
#     def from_string(cls,book_str):
#         title,author=book_str.split("-")
#         return cls(title,author)
#
#     @staticmethod
#     def is_valid(title):
#         return len(title)>=3
#
# b=Book('Harry Potter','JKRowling')
# print(b.is_valid(b.title))
# b1=Book.from_string("Python-Guido van Rossum")
# print(b1.is_valid(b1.title))

# Q7
# Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.

# class Employee:
#     bonus_rate=0.1
#
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#
#     def final_salary(self):
#         final=self.base_salary+(self.base_salary*Employee.bonus_rate)
#         return final
#
#     @classmethod
#     def update_bonus(cls,new_rate):
#         Employee.bonus_rate=new_rate
#         print("Updated bonus")
#
#     @staticmethod
#     def is_valid_salary(sal):
#         return sal>0
#
# e1=Employee("Anbariv",30000)
# e2=Employee("Amit",40000)
# #Before Updating bonus
# print(e1.final_salary())
# print(e2.final_salary())
# #Updating Bonus
# Employee.update_bonus(0.2)
# #After Updating bonus
# print(e1.final_salary())
# print(e2.final_salary())

#Q8
#  Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

# class Course:
#     total_students=0
#     def __init__(self,student_name):
#         self.student_name=student_name
#
#     def enroll(self):
#         Course.total_students+=1
#
#     @classmethod
#     def show_total(cls):
#         print(cls.total_students)
#
#     @staticmethod
#     def is_eligible(age):
#         return age>=18
#
# s1=Course('Anbariv')
# s2=Course('Satish')
#
# s1.enroll()
# s2.enroll()
#
# Course.show_total()
# print(s1.is_eligible(20))
# print(s2.is_eligible(16))

#Q9
# Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

# class BankAccount:
#     bank_name='SBI'
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.balance=balance
#
#     def deposit(self,amount):
#         if BankAccount.validate_amount(amount):
#             self.balance+=amount
#             print("Deposited Successfully")
#         else:
#             print("Invalid deposit amount")
#
#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name=new_name
#         print("Bank name changed successfully")
#
#     @staticmethod
#     def validate_amount(amount):
#         return amount>0
#
# b1=BankAccount('amith',2000)
# b2=BankAccount('Anbariv',5000)
#
# b1.deposit(2000)
# b2.deposit(-100)
#
# BankAccount.change_bank_name('HDFC')
# print(b1.bank_name)

#Q10
# . Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print("Pass")
        else:
            print("Fail")

    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
        print("Updated Passing Marks")

    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return "A"
        elif marks>=70 and marks<90:
            return "B"
        else:
            return "C"

s1=Student('Anbariv',95)
s2=Student('Anish',60)

s1.result()
s2.result()

Student.update_passing_marks(65)

s1.result()
s2.result()

print(s1.grade_category(s1.marks))
print(s2.grade_category(s2.marks))