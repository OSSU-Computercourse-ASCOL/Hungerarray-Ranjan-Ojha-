# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        total += float(num)
        count += 1
    except ValueError:
        print ("Invalid input")
        
print (total, count, total/count)
