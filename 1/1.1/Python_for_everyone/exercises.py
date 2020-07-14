# Exercise 1: Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

import re

exp = input("Enter a regular expression: ")

search = re.compile(exp)
lineCount = 0
for line in open("mbox.txt", "r"):
    if search.search(line):
        lineCount += 1

print ("mbox.txt had %d lines that matched %s" %(lineCount, exp))