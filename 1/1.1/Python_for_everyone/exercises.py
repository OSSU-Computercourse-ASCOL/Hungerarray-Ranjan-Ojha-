# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

fname = input("Enter a file name: ")
fhandle = open(fname, "r")

for line in fhandle:
    line = line.rstrip()
    print(line.upper())

