#Q1
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Deposited amount: {amount}')
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f'Withdrawn amount: {amount}')

    def __str__(self):
        return f'Account Holder:{self.account_holder} , balance:{self.balance}'

    def __add__(self,other):
        return self.balance+other.balance

    def __sub__(self,other):
        return self.balance-other.balance

    def __eq__(self,other):
        return self.balance == other.balance

    def __lt__(self,other):
        return self.balance < other.balance

    def __getattribute__(self,name):
        return object.__getattribute__(self, name)

acc1=BankAccount("arun",5000)
acc2=BankAccount("karthik",10000)

print(acc1)
print(acc2)

acc1.deposit(2000)
acc2.withdraw(1000)

#Q2
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        return self.price*self.quantity

    def __str__(self):
        return f'Product {self.name} , price {self.price} , quantity {self.quantity}'

    def __add__(self,other):
        return self.total_price() + other.total_price()

    def __mul__(self,number):
        return self.price*number

    def __gt__(self,other):
        return self.total_price() > other.total_price()

    def __eq__(self,other):
        return self.price == other.price

    def __getattr__(self,attr):
        return "Attribute not found"

    def __setattr__(self,key,value):
        if key=="price" and value<0:
            print("price value cannot be negative")
        else:
            super().__setattr__(key,value)

p1 = Product("Laptop", 50000, 2)
p2 = Product("Phone", 30000, 3)

print(p1)
print("Total Price of p1:", p1.total_price())
print("Combined Total:", p1 + p2)
print("Price multiplied:", p1 * 2)
print("p1 has greater value:", p1 > p2)
print("Prices are equal:", p1 == p2)
print(p1.color)
p1.price = -1000
print(p1.price)