# --------------------------------------------
# trying and implementing binary search
# --------------------------------------------

test = float (input ("Number: "))

# permissible error
eps = 0.0001
lwr = 0.0
if test < 1:
    upr = 1
else:
    upr = test

# computation
ans = (lwr + upr) / 2
while abs(ans ** 2 - test) >= eps:
    if test > 0 and ans ** 2 > test:
        upr = ans
    elif test > 0 and ans ** 2 < test:
        lwr = ans
    elif test < 0 and ans ** 2 > test:
        lwr = ans
    elif test < 0 and ans ** 2 < test:
        upr = ans
    ans = (lwr + upr) / 2

print (ans)