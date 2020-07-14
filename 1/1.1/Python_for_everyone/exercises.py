# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the num-
# ber of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.

fname = input ("Enter a file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("%s Couldn't open the file." %fname)
    exit()

# count the number of messages from each person using a dictionary
messCount = dict()
for line in fhandle:
    if not line.startswith("From "): continue
    email = line.split()[1]
    messCount[email] = messCount.get(email, 0) + 1

# list of count and email sorted in reverse order
lst = sorted([(count, email) for (email, count) in messCount.items()], reverse=True)
print (lst[0][1], lst[0][0])