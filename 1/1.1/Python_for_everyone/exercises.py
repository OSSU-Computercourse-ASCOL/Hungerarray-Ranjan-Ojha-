# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

fname = input("Enter a file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("Could not open file %s" %fname)
    exit()

# make a dictionary by reading file for each letter
letterCount = dict()
for line in fhandle:
    for letter in line.lower():
        if not letter.isalpha(): continue
        letterCount[letter] = letterCount.get(letter, 0) + 1

# print in descending order or letters frequency
for elem in sorted(letterCount.items(), key= lambda letter: letter[1], reverse=True):
    print (elem[0], elem[1])
