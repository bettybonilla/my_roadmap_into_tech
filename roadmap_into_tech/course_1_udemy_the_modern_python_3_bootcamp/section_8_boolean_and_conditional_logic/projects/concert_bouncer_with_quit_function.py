'''
The program below acts as a concert bouncer using the quit() function
- In the US, you can get into concerts if you're 18 years old and older
- However, you can't drink until you're 21 years old and older
- Ages 18 to 20 years old have to wear special wristbands to show they're not
old enough to drink
- Ages 17 years old and below can't get into concerts at all
- NOTE: My Version - The below follows professional good practices
'''

# Ask for age
age = input("Stop right there! Enter your age: ").strip()

# This accounts for user input errors with empty strings
if age == "":
    print("YOU DIDN'T ENTER ANYTHING, ENTER YOUR AGE NOW!")
    quit(1)
    # The quit() function (alias for the exit() function or vice versa) tells
    # the computer to exit/quit running the program and it is important
    # because it follows the return early rule of terminating a program early
    # when there is an error which avoids unnecessary bugs and this allows to
    # safely implement logic later - When you terminate a program early on
    # errors, it also avoids the possibility of more code being executed
    # without intention and it is easier to bugfix
    # Using quit(0) means you told the program to exit/quit successfully
    # because there were no errors - Visually indicated with a green arrow in
    # terminal
    # Using quit(1) means you told the program to exit/quit unsuccessfully
    # because there were errors since the data was invalid - Visually indicated
    # with a red arrow in terminal
    # Using quit() means you told the program to exit/quit but don't want to
    # reveal whether successful or unsuccessful

# After accounting for user input errors with empty strings, now we can use
# the int() type conversion function to convert a non-empty string with a
# number into an integer
age = int(age)

# Finally, now that the age variable has been converted from a
# non-empty string with a number into an integer, it can be carried out in
# conditional logic which categorizes where the user input belongs and prints
# the appropriate message that corresponds
if age >= 18 and age <= 20:
    # 18-20 Special Entry: Can't drink, need wristband
    print("You can enter: You can't drink and need a wristband!")
elif age >= 21:
    # 21+ Normal Entry: Can drink, no wristband
    print("You can enter: You can drink and don't need a wristband!")
elif age <= 17:
    # 17- No Entry: Sorry too young
    print("You can't enter: Sorry kid, you're too young!")
