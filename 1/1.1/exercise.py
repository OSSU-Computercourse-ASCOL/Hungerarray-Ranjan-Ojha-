# --------------------------------------------
# Exercise: (self) Integer to Binary
# --------------------------------------------

conv = int (input ("Number: "))
binary = 0
pos = 0

if conv < 0:
    isneg = True
    conv = abs(conv)
else:
    isneg = False
    
while conv != 0:
    binary += (conv % 2) * 10 ** pos
    conv //= 2
    pos += 1
if not isneg:
    print ("Binary:", binary)    
else:
    print ("Binary:", -binary)