# --------------------------------------------
# Exercise: palindrome recursive
# --------------------------------------------

def palindrome (x):
    """
    Parameters
    ----------
    x : STRING

    Returns bool
    -------
    the return value determines wheather the given string is palindrome or not.
    """
    def parse (x):
        """
        Parameters
        ----------
        x : string
        Returns string
        -------
        parses the string to be fit for checking
        """
        parsed = ''
        for ch in x:
            if ch.isalpha():
                parsed += ch
        return parsed.lower()
    
    def recur(x):
        """
        Parameters
        ----------
        x : string
        Returns bool
        -------
        palindrome check
        """
        if len(x) == 0 or len(x) == 1:
            return True
        else:
            if x[0] == x[- 1]:
                return recur (x[1:-1])
            else:
                return False
            
    x = parse(x)
    return recur(x)

palindrome("Able was I, ere I saw Elba")