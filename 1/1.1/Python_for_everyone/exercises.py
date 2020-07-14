# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

fname = input("Enter a file name: ")
try:
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("Did not find file %s" %fname)
    exit()

# make a histogram for hour
hourCount = dict()
for line in fhandle:
    if not line.startswith("From "): continue

    hour = line.split()[-2].split(":")[0]
    hourCount[hour] = hourCount.get(hour, 0) + 1

for (hour,count) in sorted(hourCount.items()):
    print (hour, count)
