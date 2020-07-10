# --------------------------------------------
# Exercise: (self) Newton Rapson method
# --------------------------------------------


# finding the root for the function 

x = 1
eps = 0.0001
fun = x ** 2 - 24
der = 2 * x 

while abs(x ** 2 - 24) >= eps:
    x = x - fun / der
    fun = x ** 2 - 24
    der = 2 * x
    
print ("root:", x)
