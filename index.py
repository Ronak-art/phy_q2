class SavingAccount:

    def saving_balance (self,savings):
        print(self.savings)

    def __init__(self, savings, annual_interest_rate, monthly_interest):
        self.savings = savings
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest = (savings * annual_interest_rate) / 12


annual_interest_rate = int(input("Enter a value for annual interest rate: "))
savings1 = int(input("Enter a value for saver1 amount initially in account: "))
savings2 = int(input("Enter a value for saver2 amount initially in account: "))
print( )
monthly_interest = 0

saver1 = SavingAccount(savings1, annual_interest_rate, monthly_interest)
print(f"Monthly intrest for saver 1 is {saver1.monthly_interest}")
savings1 = savings1 + saver1.monthly_interest
print(f"Balance for saver1 after 1 month = {savings1}")
print( )
saver2 = SavingAccount(savings2, annual_interest_rate, monthly_interest)
print(f"Monthly intrest for saver 2 is {saver2.monthly_interest}")
savings2 = savings2 + saver2.monthly_interest
print(f"Balance for saver 2 after 1 month = {savings2}")
print( )
print( )
n = int(input("Enter no. of months (for which you want to calculate Balance & monthly Interest): "))
x = 0
for x in range(n) :
    print( )
    print( )
    print(f"Proceedings for month {x+2}" )
    annual_interest_rate = int(input(f"Enter a value for annual interest rate for month {x+2}: "))
    print( )
    saver1 = SavingAccount(savings1, annual_interest_rate, monthly_interest)
    print(f"Monthly interest for saver 1 after {x+2} month is {saver1.monthly_interest}")
    savings1 = savings1 + saver1.monthly_interest
    print(f"Balance for saver 1 after {x+2} month = {savings1}")
    print()
    saver2 = SavingAccount(savings2, annual_interest_rate, monthly_interest)
    print(f"Monthly intrest for saver 2 after {x+2} month is {saver2.monthly_interest}")
    savings2 = savings2 + saver2.monthly_interest
    print(f"Balance for saver 1 after {x+2} month = {savings2}")