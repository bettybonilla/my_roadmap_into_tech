"""
- Below is another example of how you would use the break keyword to exit out
of a for loop using the quick_exercise_screaming_repeating.py file
- If the user input is greater than or equal to the number 4 then the print
statement is printed and then the break keyword exits the program
"""

mom = input("How many times do I have to tell you?! ")

mom = int(mom)

for i in range(mom):
    print("CLEAN UP YOUR ROOM!")
    if mom >= 4:
        print("Do your ears even work anymore?!")
        break
