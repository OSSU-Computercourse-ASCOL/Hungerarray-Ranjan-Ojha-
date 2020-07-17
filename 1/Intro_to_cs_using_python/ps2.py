# -------------------------------------------------------------------------
# set 3
# -------------------------------------------------------------------------

balance = 999999
annualInterestRate = 0.18

def currBal (bal, ir, mp):
    return (bal - mp) * (1 + ir / 12)

# if there were no interest on our sum then we would have to pay this much
lwr = balance / 12

# if we paid all at the end then we would pay this much it is larger simply because of the fact that we aren't paying anything at the end of the month
upr = (balance * ( 1 + annualInterestRate/12) ** 12) / 12

payment = (lwr + upr) / 2

while True:
    mnth = 0
    testBalance = balance
    
    while mnth < 12:
        mnth += 1
        testBalance = currBal(testBalance, annualInterestRate, payment)
    
    if abs(testBalance - 0) < 0.0001:
        break
    elif testBalance < 0:
        upr = payment
    else:
        lwr = payment
    payment = (lwr + upr) / 2

print ("Lowest Payment:", round(payment, 2))


 