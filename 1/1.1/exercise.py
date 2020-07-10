# --------------------------------------------
# Exercise: gcdRecur
# --------------------------------------------

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        # gcd(a,0) = a
        return a
    else:
        # gcd(a, b) = gcd(b, a Euler division b 
        # attributed to gcd (a,b) = gcd(a, a-b)
        return gcdRecur(b, a % b)
    
gcdRecur (100, 200)
