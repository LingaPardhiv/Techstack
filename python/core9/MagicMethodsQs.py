#Q1
# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print(f'Deposited amount: {amount}')
#         else:
#             print("Deposit amount must be positive")
#
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print(f'Withdrawn amount: {amount}')
#
#     def __str__(self):
#         return f'Account Holder:{self.account_holder} , balance:{self.balance}'
#
#     def __add__(self,other):
#         return self.balance+other.balance
#
#     def __sub__(self,other):
#         return self.balance-other.balance
#
#     def __eq__(self,other):
#         return self.balance == other.balance
#
#     def __lt__(self,other):
#         return self.balance < other.balance
#
#     def __getattribute__(self,name):
#         return object.__getattribute__(self, name)
#
# acc1=BankAccount("arun",5000)
# acc2=BankAccount("karthik",10000)
#
# print(acc1)
# print(acc2)
#
# acc1.deposit(2000)
# acc2.withdraw(1000)