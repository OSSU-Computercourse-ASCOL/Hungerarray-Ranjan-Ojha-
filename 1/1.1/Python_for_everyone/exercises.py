# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

fname = input("Enter file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("Counld not open the file", fname)
    exit()

days = dict()
for line in fhandle:
    if not line.startswith("From "): continue

    words = line.split()
    days[words[2]] = days.get(words[2], 0) + 1

print (days)