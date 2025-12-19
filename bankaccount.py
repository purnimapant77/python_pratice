class BalanceException(Exception):
    pass


class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print(f"\nAccount '{self.name}' created\n Balance: '${self.balance}'")
        
    def getbalance(self):
        print(f"\nAccount:'{self.name}'\nBalance:'{self.balance}'")
    
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("\nDeposited..........")
        self.getbalance()
        
    def vibleTranscaction(self,amount):
        if self.balance>amount:
            return
        else:
            raise BalanceException(f"\nsorry, account: '{self.name}' only have balance of '{self.balance:.2f}'")
    
    def withdraw(self,amount):
        try:
            self.vibleTranscaction(amount)
            self.balance=self.balance-amount
            print("\nwithdrawl complete........")
            self.getbalance()
        except BalanceException as error:
            print(f"withdrawl interrupted:{error}")
            
    def transfer(self,amount,account):
        try:
            self.vibleTranscaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            account.getbalance()
            print("\nTransfer complete!")
        except BalanceException as error:
            print(f"transfer interrupted:{error}")