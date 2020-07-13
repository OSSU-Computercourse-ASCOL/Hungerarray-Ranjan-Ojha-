# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

fname = input("Enter file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("%s : File not found" %fname)
    exit()

domains = dict()
for line in fhandle:
    if not line.startswith("From "): continue

    email = line.split()[1]
    domain = email.split("@")[1]
    domains[domain] = domains.get(domain, 0) + 1

print (domains)
