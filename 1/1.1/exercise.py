def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    high = 0
    for i in aDict.values():
        if high < len(i):
            high = len(i)
    for elem in aDict:
        if len(aDict[elem]) == high:
            return elem
    
    return 

print (biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))