# --------------------------------------------
# Exercise: check in sorted string
# --------------------------------------------

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if not len(aStr) or not len(char):
        return False
    
    curr = len(aStr) // 2
    if aStr[curr] == char:
        return True
    else:
        if aStr[curr] < char:
            isIn(char, aStr[:curr])
        else:
            isIn(char, aStr[curr + 1:])

print(isIn("h","abcdhijkl"),
isIn("c",""),
isIn("","ahr"), isIn("",""))