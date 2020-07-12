import time
# implementing a isPrime function using caching

def cacheisPrime(curr, primeList):
    
    def chkPrime(val):
        if val in primeList:
            return True
        
        for i in primeList:
            if not val % i:
                return False
        
        primeList.append(val)
        return True
    
    for i in range(2, curr):
        chkPrime(i)
        
    return chkPrime(curr)


# implementing a isPrime function using squareroot method

def sqrtisPrime(curr):
    
    for i in range(2, int(curr ** 0.5) + 1):
        if not curr % i:
            return False
        
    return True


strt= time.time()
primeList = [2]
for i in range(1000, 50000, 1000):
    print(i, cacheisPrime(i, primeList), end='\n')
print (time.time() - strt)
print()

strt= time.time()
for i in range(1000, 100000, 1000):
    print(i, sqrtisPrime(i), end='\n')
print (time.time() - strt)
    
    