'''
The program below acts as a concert bouncer using a nested conditional
- In the US, you can get into concerts if you're 18 years old and older
- However, you can't drink until you're 21 years old and older
- Ages 18 to 20 years old have to wear special wristbands to show they're not
old enough to drink
- Ages 17 years old and below can't get into concerts at all
- NOTE: Instructor's Code - The below follows unprofessional bad practices
since validating data inside conditional logic + nested conditionals should be
avoided
'''

# Ask for age
age = input("Stop right there! Enter your age: ").strip()

if age:
    age = int(age)
    if age >= 18 and age <= 20:
        # 18-20 Special Entry: Can't drink, need wristband
        print("You can enter: You can't drink and need a wristband!")
    elif age >= 21:
        # 21+ Normal Entry: Can drink, no wristband
        print("You can enter: You can drink and don't need a wristband!")
    elif age <= 17:
        # 17- No Entry: Sorry too young
        print("You can't enter: Sorry kid, you're too young!")
else:
    print("YOU DIDN'T ENTER ANYTHING, ENTER YOUR AGE NOW!")
