# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

import re

fname = input("Enter file: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("%s file was not found." %fname)
    exit()

# extracting the number as a list
numList = list()
for line in fhandle:
    numList.extend(re.findall(r"^New Revision: ([0-9]*)", line))

# comupting average (since the list stores values as string converted them to int first)
print( sum([int(elem) for elem in numList]) // len(numList))