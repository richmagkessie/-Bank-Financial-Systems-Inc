# This is the parent class known as BankDetails  
class BankDetails:
    def __init__(self, account_number, account_balance, interest_rate):
        self.account_number = account_number
        self.account_balance = account_balance
        self.interest_rate = interest_rate

# certificate_of_deposit child class of BankDetails 
class certificate_of_deposit(BankDetails):
    def __init__(self,  account_number, account_balance, account_maturity_date, interest_rate):
        super().__init__(account_number, account_balance, interest_rate) 
        self.account_maturity_date = account_maturity_date

# function to print users saving accounts bank details after users input
    def Savings(self):
        print("This is your Saving accounts details")      
        print("---------------------------------------")
        print("Account number : " , self.account_number)
        print("Account_balance : ", self.account_balance,"Ghana Cedis")
        print("Interest rate : " , self.interest_rate,"%")
        print()

# # function to print users certificate of deposit details after users input
    def COD (self):
        print("This is your certificate of deposit details")
        print("----------------------------------------------")      
        print("Account number : " , self.account_number)
        print("Account balance : ", self.account_balance,"Ghana Cedis")
        print("Interest rate : " , self.interest_rate,"%")
        print("Account maturity_date : ", self.account_maturity_date)

# accepting users details to complete the details
account_number =  str(input (" Enter your account number: "))
account_balance = float(input("Enter your balance: "))
account_maturity_date = input("Enter a valid account maturity date in (00/00/0000) format: ")
interest_rate = float(input("Enter the interest rate: "))
print()

# making certificate of deposit with users input
certificate_of_deposit1 = certificate_of_deposit( account_number,account_balance, account_maturity_date, interest_rate)

# printing certificate of deposit details
print(certificate_of_deposit1.COD())

print()

# printing saving accounts details
print(certificate_of_deposit1.Savings())

