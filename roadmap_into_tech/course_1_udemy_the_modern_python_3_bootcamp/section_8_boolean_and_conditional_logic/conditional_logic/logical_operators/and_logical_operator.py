'''
The below is a conditional statement that checks someone's age by using
the and logical operator
- In the US, infants usually get into the movies for free up until 2 years old
- For ages 2 to 8 years old, there is a child ticket price
'''

# When dealing with age, use the int() type conversion function instead of the
# float() type conversion function since ages are meant to be whole numbers
# Any user input errors with floats should be accounted for separately
age = input("Enter your age: ").strip()
age = int(age)

# Both sides of the and logical operator need to be True in order for the
# entire statement to be True
if age >= 2 and age <= 8:
    print("YOU PAY CHILD TICKET PRICE!")
elif age < 2:
    print("YOU GET IN FOR FREE BABY!")
else:
    print("YOU PAY ADULT TICKET PRICE!")
