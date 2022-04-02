class Atm(object):
    def __init__(self,AtmCardNumber,PinNumber):
        self.PinNumber=PinNumber
        self.AtmCardNumber=AtmCardNumber 
        self.Balance=1000
    print("WELCOME!")
    

    def CashWithDrawal(self):
        amt=input("ENTER AMOUNT")
        print(amt,"rupees withdrawed")
    def BalanceInq(self):
        print("Check your balance inquiry here")
       
       
cash=Atm(3456,585954942)
cash.CashWithDrawal()
cash.BalanceInq()
print(cash.Balance)
    

