#1Q
class BankAccount:
    def __init__(self,acc,bal):
        self.account_number=acc
        self.__balance=bal

    def deposit(self,amount):
        self.__balance+=amount
        print('Amount Deposited')

    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(f'Withdrawn Amount : {amount}')
        elif self.__balance<0:
            print("Balance is Negative")
        else:
            print(f'Balance Not Sufficient')

    def getbalance(self):
        return self.__balance

obj=BankAccount('12535346',50000)
obj.deposit(1000)
obj.withdraw(2000)
print(obj.getbalance())
obj.__balance=20000
print(obj.getbalance())
#2Q
