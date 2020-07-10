# --------------------------------------------
# Exercise: gcdIter
# --------------------------------------------

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        min = a
    else:
        min = b
    
    while min != 1 and  (a % min or b % min):
        min -= 1
    return min


        