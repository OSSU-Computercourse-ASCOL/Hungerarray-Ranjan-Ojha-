# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

currMax = None
currMin = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if currMax is None or currMax < num:
            currMax = num
        if currMin is None or currMin > num:
            currMin = num    
    except ValueError:
        print ("Invalid input")

print ("Maximum is", currMax)
print ("Minimum is", currMin)
