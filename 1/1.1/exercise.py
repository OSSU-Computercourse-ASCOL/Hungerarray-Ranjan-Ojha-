# --------------------------------------------
# Exercise: guess my number
# --------------------------------------------

print ("Please think of a number between 0 and 100!")

lwr = 0
upr = 100

while True:
    curr = (lwr + upr) // 2
    print ("Is your secret number " + str(curr) + "?")
    test = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if test == "h":
        upr = curr
    elif test == "l":
        lwr = curr
    elif test == "c":
        break
    else:
        print ("Sorry, I did not understand your input.")
        
print ('Game over. Your secret number was:', curr)