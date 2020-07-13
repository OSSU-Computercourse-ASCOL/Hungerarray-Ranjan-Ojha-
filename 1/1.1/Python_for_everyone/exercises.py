# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

fhandle = open("words.txt", "r")
words = dict()

for line in fhandle:
    for word in line.split():
        words[word] = 0

search = input("Enter the word to search for: ")
if search in words:
    print ("Found")
else:
    print ("Not found")