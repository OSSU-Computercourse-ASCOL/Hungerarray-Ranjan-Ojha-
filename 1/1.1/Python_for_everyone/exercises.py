# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(ls):
    ls.pop(0)
    ls.pop(-1)

def middle(ls):
    return ls[1:-1]

from string import ascii_lowercase
ls  = list(ascii_lowercase)


print ("Before chop: \n", ls)
chop(ls)
print (ls)
print ("After chop: \n", ls)

ls = list(ascii_lowercase)
print ("Before middle: \n", ls)
print (middle(ls))
print ("After middle: \n", ls)