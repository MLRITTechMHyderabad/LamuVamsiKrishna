class InsufficientFundsError(Exception):
    def __init__(self, msg):
        self.msg=msg
        super().__init__(msg)
    pass
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        try:
            if(amount<0):
                raise ValueError("Withdraw amount should be >0")
            if(amount>self.balance):
                raise InsufficientFundsError("InsufficientFundsError")
            else:
                self.balance-=amount
                print(self.balance)
        except Exception as e:
            print(e)

account=BankAccount(100)
account.withdraw(500)
    