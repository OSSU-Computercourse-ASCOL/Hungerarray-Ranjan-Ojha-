# Exercise 4: Add code to the previous program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

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

# added these
mostEmail = None
mostCount = None
for email,count in emails.items():
    if mostCount is None or mostCount < count: 
        mostEmail = email
        mostCount = count

print (mostEmail, mostCount)