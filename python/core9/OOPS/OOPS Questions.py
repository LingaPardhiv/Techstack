#  Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.

from abc import ABC, abstractmethod
class Account(ABC):
    interest=0.05
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def calc_interest(self):
        pass
class SavingsAccount(Account):
    def __init__(self, bal):
        self.__bal = bal
    def deposit(self,amount):
        self.__bal+=amount
    def withdraw(self, amount):
        self.__bal-=amount
    def calc_interest(self):
        self.__bal=self.__bal * (self.__bal * self.interest )/100
        return self.__bal
class CurrentAccount(Account):
    def __init__(self, bal):
        self.__bal = bal
    def deposit(self,amount):
        self.__bal+=amount
    def withdraw(self, amount):
        self.__bal-=amount
    def calc_interest(self):
        self.__bal=self.__bal * (self.__bal * self.interest )/100
        return self.__bal
class FixedDepositAccount(Account):
    interest=0.1
    def __init__(self, bal):
        self.__bal = bal
    def deposit(self,amount):
        self.__bal+=amount
    def withdraw(self, amount):
        self.__bal-=amount
    def calc_interest(self):
        self.__bal=self.__bal * (self.__bal * self.interest )/100
        return self.__bal
acc1=SavingsAccount(2000000000)
acc2=FixedDepositAccount(2000000000)
acc3=CurrentAccount(2000000000)
l=[acc1,acc2,acc3]
def print_calc_interest(obj):
    return obj.calc_interest()
for i in l:
    print(print_calc_interest(i))
