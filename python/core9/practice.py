# class Details:
#     name = "Rohan"
#     age = 20
#
#     def info(self):
#         print(f'My name is {self.name} and I am {self.age} years old.')
#
# obj1 = Details()
# obj1.info()

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this function")
#     return mfx
#
# @greet
# def add(a,b):
#     print(a+b)
#
# add(1,2)

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Amount: {amount} deposited successfully')
        else:
            print("Amount Invalid")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print('Withdrawn Amount:',amount)

    def __str__(self):
        return f'Account Holder: {self.account_holder} Balance: {self.balance}'

    def __add__(self,other):
        return self.balance + other.balance

    def __sub__(self,other):
        return self.balance - other.balance

    def __eq__(self,other):
        return self.balance == other.balance

    def __lt__(self,other):
        return self.balance < other.balance

    def __getattribute__(self,name):
        if name in ("balance", "account_holder"):
            print(f'Accessing attribute: {name}')
        return object.__getattribute__(self,name)

b1=BankAccount('Anbariv',50000)
b2=BankAccount("Amith",40000)

b1.deposit(1000)
b2.withdraw(2000)

print(b1)
print(b2)

print(b1+b2)
print(b1-b2)
print(b1==b2)
print(b1<b2)
print(b1.account_holder)