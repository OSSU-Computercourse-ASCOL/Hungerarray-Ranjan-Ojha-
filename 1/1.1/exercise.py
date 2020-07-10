# --------------------------------------------
# Exercise: word Frequency
# --------------------------------------------

def make_dict (data):
    """
    Parameters
    ----------
    data : string
        a string containing all the words.
    Returns : dictionary
    -------
    """
    freq = {}
    for word in data:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def higest (dictionary):
    '''
    Parameters
    ----------
    dictionary : DICTIONARY
        use the dictionary that has just been generated.
    Returns : a tuple of list of word/s and their occurance
    -------
    '''
    maxm = max(dictionary.values())
    ls = []
    for key in dictionary.keys():
        if dictionary[key] == maxm:
            ls.append(key)
    if len(ls) == 1:
        return (ls[0], maxm)
    else:
        return (ls, maxm)

def atlest (dictionary, num):
    '''
    Parameters
    ----------
    dictionary : DICTIONARY
        contains data
    num : INT
        the least no. of times you wish for it to occur
    Returns a list of tuples, each tuple contains a list of words and their occurance
    -------
    '''
    ls = []
    for i in range(num,max(dictionary.values()) + 1):
        
        words = []
        for word in dictionary:
            if dictionary[word] == i:
                words.append(word)
        
        ls.append((words, i))
        
        
