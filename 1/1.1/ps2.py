# -------------------------------------------------------------------------
# set 1
# -------------------------------------------------------------------------

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def currBal (bal, ir, mr):
    return bal * (1-mr) * (1 + ir / 12)

mnth = 0
while mnth < 12:
    mnth += 1
    balance = currBal(balance, annualInterestRate, monthlyPaymentRate)
    
print ("Remaining balance:", round(balance, 2))

    


