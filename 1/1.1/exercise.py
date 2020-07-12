#--------------------------------------------------------------------
# Exercise: Generators (genPrime)
#--------------------------------------------------------------------


def cachegenPrime():
    num = 2
    
    primeList = [2]
    
    # helper function to find out if the given no. is prime or not
    def isPrime(curr):
        # given a list of prime numbers
            # if the no. is divisible by any in the list return false
        for i in primeList:
            if not curr % i:
                return False
        
        # we know it is a prime, so add it to list and return true
        primeList.append(curr)
        return True
    
    # helper function to find out next prime from here onwards
    def nxtPrime(curr):
        curr += 1
        # keep on adding to curr until you reach next prime number
        while not isPrime(curr):
            curr += 1
        return curr
    
    while True:
        yield num
        num = nxtPrime(num)

def sqrtgenPrime():
    num = 2
    
    def prime(val):
        
        for i in range(2, int(val ** 0.5) + 1):
            if not val % i:
                return False
        return True
    
    def nxtPrime(curr):
        curr += 1
        while not prime(curr):
            curr += 1
        return curr
    
    while True:
        yield num
        num = nxtPrime(num)