#Q1
# class Animal:
#     def make_sound(self):
#         print('Animal sound')
#
# class Dog(Animal):
#     def make_sound(self):
#         print('Dog Sound')
#
# class Cat(Animal):
#     def make_sound(self):
#         print('Cat sound')
#
# class Cow(Animal):
#     def make_sound(self):
#         print('Cow sound')
#
# animals = [Dog(),Cat(),Cow()]
#
# for a in animals:
#     a.make_sound()

#Q2
# class Car:
#     def start(self):
#         print('car start')
# class Computer:
#     def start(self):
#         print('computer start')
# class WashingMachine:
#     def start(self):
#         print('Washing Machine start')
#
# def operate(device):
#     device.start()
#
# operate(Car())
# operate(Computer())
# operate(WashingMachine())

#Q3
# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b
#     def __eq__(self,other):
#         return self.a+self.b==other.a+other.b
# v1=Vector(1,2)
# v2=Vector(3,4)
# print(v1+v2)
# print(v1==v2)

#Q4
# class Transport:
#     def move(self):
#         print('Transport')
#
# class Bus(Transport):
#     def move(self):
#         print('Bus')
#         super().move()
#
# class Bike(Transport):
#     def move(self):
#         print('Bike')
#         super().move()
#
# b1=Bus()
# b2=Bike()
# b1.move()
# b2.move()

#Q6
# class Payment:
#     def process(self,amount):
#         print(f'Amount processed {amount}')
# class CreditCardPayment(Payment):
#     def process(self,amount,card_type):
#         print(f'Amount processed {amount}, card type {card_type}')
#
# p=Payment()
# p.process(20000)
# c=CreditCardPayment()
# c.process(10000,"Visa-card")

#Q8
# class Account:
#     def withdraw(self):
#         print(f'Withdraw amount')
#
# class SavingsAccount(Account):
#     def withdraw(self):
#         print(f'SavingsAccount Withdrawal')
#
# class PremiumSavingsAccount(SavingsAccount):
#     def withdraw(self):
#         super().withdraw()
#         print(f'PremiumSavingsAccount Withdrawal')
#
# a=Account()
# a.withdraw()
# s=SavingsAccount()
# s.withdraw()
# p=PremiumSavingsAccount()
# p.withdraw()

#Q9
# def draw(shape):
#     shape.draw()
#
# class Circle:
#     def draw(self):
#         print("Drawing a Circle")
#
# class Square:
#     def draw(self):
#         print("Drawing a Square")
#
# class Rectangle:
#     def draw(self):
#         print('Drawing a rectangle')
#
# class Car:
#     def draw(self):
#         print('Drawing a car')
#
# draw(Circle())
# draw(Square())
# draw(Rectangle())
# draw(Car())

#Q10
# class UPI:
#     def pay(self):
#         print('Payment done using UPI')
#
# class Card:
#     def pay(self):
#         print('Payment done using card')
#
# class Cash:
#     def pay(self):
#         print('Payment done using cash')
#
# def process_payment(payment_method):
#     payment_method.pay()
#
# process_payment(UPI())
# process_payment(Card())
# process_payment(Cash())
