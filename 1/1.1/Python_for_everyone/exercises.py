# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

try:
    fname = input("Enter file name: ")
    fhandle = open(fname, "r")
except FileNotFoundError:
    print ("Invalid File Name")
    quit()

lineCount = 0
total = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    strt = line.find(":")
    total += float(line[strt + 1:])
    lineCount += 1

print ("Average spam confidence:", round(total/lineCount, 12))

