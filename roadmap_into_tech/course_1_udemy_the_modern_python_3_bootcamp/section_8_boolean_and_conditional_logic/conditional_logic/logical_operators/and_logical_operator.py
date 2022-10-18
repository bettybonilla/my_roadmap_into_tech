'''
The below is a conditional statement that checks someone's age by using
the and logical operator
- In the US, infants usually get into the movies for free up until 2 years old
- From 2 to 8 years old, there is a child ticket price
'''

# Both sides of the and logical operator need to be True in order for the
# entire statement to be True
age = input("Enter your age: ")
age = float(age)

if age >= 2 and age <= 8:
    print("YOU PAY CHILD TICKET PRICE!")
elif age < 2:
    print("YOU GET IN FOR FREE BABY!")
else:
    print("YOU PAY ADULT TICKET PRICE!")
