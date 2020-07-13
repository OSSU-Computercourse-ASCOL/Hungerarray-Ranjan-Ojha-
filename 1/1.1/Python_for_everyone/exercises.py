# Exercise 3: Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

fname = input("Enter file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("%s : File not found" %fname)
    exit()

emails = dict()
for line in fhandle:
    if not line.startswith("From "): continue

    email = line.split()[1]
    emails[email] = emails.get(email, 0) + 1

print (emails)