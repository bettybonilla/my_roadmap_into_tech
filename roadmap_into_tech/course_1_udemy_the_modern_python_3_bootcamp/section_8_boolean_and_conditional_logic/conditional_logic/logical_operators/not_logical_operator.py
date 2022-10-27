'''
The below is a conditional statement using the not logical operator
- Movie ticket price for ages 2 to 8 years old: 2 dollars
- Movie ticket price for ages 65 years old and older: 5 dollars
- Movie ticket price for everyone else: 10 dollars
'''

age = input("Enter your age: ").strip()
age = int(age)

# Anything inside parentheses () will be the opposite value when you use
# the not logical operator in front of it
if not ((age >= 2 and age <= 8) or age >= 65):
    print("YOU ARE NOT A CHILD OR SENIOR SO YOU PAY 10 DOLLARS!")
else:
    print("YOU ARE A CHILD OR SENIOR!")
