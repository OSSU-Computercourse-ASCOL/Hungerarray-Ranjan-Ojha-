# --------------------------------------------
# Exercise: (self) Real number to Binary
# --------------------------------------------

conv = float (input ("Number: "))

p = 0
while p != 17 and conv % 1 != 0:
    p += 1
    conv = conv * 2
conv = int (conv)

result = ''
while conv > 0:
    result = str(conv % 2) + result
    conv //= 2
print (result[:-p] + "." + result[-p:])

