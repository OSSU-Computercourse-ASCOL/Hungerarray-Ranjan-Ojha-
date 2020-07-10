# -------------------------------------------------------------------------
# set 2
# -------------------------------------------------------------------------

balance = 3329
annualInterestRate = 0.2

def currBal (bal, ir, mp):
    return (bal - mp) * (1 + ir / 12)

payment = 10
while True:
    mnth = 0
    testBalance = balance
    while mnth < 12:
        mnth += 1
        testBalance = currBal(testBalance, annualInterestRate, payment)
    if testBalance < 1:
        break;
    payment += 10

print ("Lowest Payment:", payment)


 