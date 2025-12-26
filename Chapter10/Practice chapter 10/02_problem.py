# Create account class with 2 attributes - balance & Account no. 
# Create methods for debit, credit & printing the balance.

class Account: 
    def __init__(self,bal, Acc):
        self.balance = bal
        self.account_no = Acc
        
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs,", amount, "was debited")
        print("Current balance =", self.get_balance())
    
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited, enjoy broooo")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance
    
    

acct1 = Account(10000, 690901501251)
acct1.debit(1000)
acct1.credit(2999)
acct1.credit(200000)
acct1.debit(9500)






        