# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
try:
    grade = float(input ("Enter Grade: "))
    if not (0 <= grade and grade <= 1):
        raise ValueError("Out of Range")
except:
    print (ValueError)
    exit()

if grade >= 0.9 : ch = "A"
elif grade >= 0.8 : ch = "B"
elif grade >= 0.7 : ch = "C"
elif grade >= 0.6 : ch = "D"
else: ch = "F"

print (ch)