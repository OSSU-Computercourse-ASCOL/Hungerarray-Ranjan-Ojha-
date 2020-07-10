# --------------------------------------------
# Exercise: (self) Newton Rapson method
# --------------------------------------------


# finding the root for the function [f(x) = x **2 - 24]

curr = 1
eps = 0.0001

while abs(curr ** 2 - 24) >= eps:
    curr = ( curr ** 2 + 24) / (2 * curr)
    
print ("root:", curr)
