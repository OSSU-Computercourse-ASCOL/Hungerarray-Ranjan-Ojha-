# Finding Numbers in a Haystack

# Sample data: (There are 90 values with a sum=445833)
# Actual data: (There are 84 values and the sum ends with 868)
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

fname = input("Enter file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("%s file not found." %fname)
    exit()

data = fhandle.read()
numList = [int(num) for num in re.findall(r'(\d+)',data)]
print (sum(numList))