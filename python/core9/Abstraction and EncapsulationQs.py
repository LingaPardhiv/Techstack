#1Q
# class BankAccount:
#     def __init__(self,acc,bal):
#         self.account_number=acc
#         self.__balance=bal
#
#     def deposit(self,amount):
#         self.__balance+=amount
#         print('Amount Deposited')
#
#     def withdraw(self,amount):
#         if self.__balance>amount:
#             self.__balance-=amount
#             print(f'Withdrawn Amount : {amount}')
#         elif self.__balance<0:
#             print("Balance is Negative")
#         else:
#             print(f'Balance Not Sufficient')
#
#     def getbalance(self):
#         return self.__balance
#
# obj=BankAccount('12535346',50000)
# obj.deposit(1000)
# obj.withdraw(2000)
# print(obj.getbalance())
# obj.__balance=20000
# print(obj.getbalance())
#2Q
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=0
        self.update_marks(marks)

    def update_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")

    def getmarks(self):
        return self.__marks

s1=Student('Anish',55)
print(s1.getmarks())
s1.update_marks(80)
print(s1.getmarks())
s1.__marks=20
print(s1.getmarks())