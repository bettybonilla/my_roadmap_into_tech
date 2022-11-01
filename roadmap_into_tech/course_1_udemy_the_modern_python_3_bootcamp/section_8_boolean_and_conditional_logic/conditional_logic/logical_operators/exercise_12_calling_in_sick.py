'''
- In this exercise you will be given a few variables that will be set randomly
to boolean values (True or False):
    - actually_sick - When you legit have the flu!
    - kinda_sick - You're feeling under the weather and it's enough to treat
    yourself with a day off (if you can spare it)
    - hate_your_job - Work sucks, I know...
- You're also given a random number of sick_days between 0 and 10
- Finally, there is a variable called calling_in_sick that you must set to
True or False based on the following scenarios:
    - Set to True if:
        - You're actually_sick and you have sick_days remaining
        - You're kinda_sick and hate_your_job and you have sick_days remaining
    - Otherwise, set to False if:
        - The tests check that the value of calling_in_sick is correct based
        on the conditions specified above
'''

# NO TOUCHING =================================================================
# Randomly assigns values to these four variables
from random import choice, randint
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING =================================================================

# Set this to True or False with boolean logic and conditionals!
# The None value acts as a placeholder for a variable so that you can
# define/assign it later
# By using the None value, as shown below the calling_in_sick variable can be
# dynamically assigned in the conditional logic
calling_in_sick = None

# YOUR CODE GOES HERE:
print("actually_sick =", actually_sick)
print("kinda_sick =", kinda_sick)
print("hate_your_job =", hate_your_job)
print("sick_days =", sick_days)

if actually_sick and sick_days > 0:
    calling_in_sick = True
    print("calling_in_sick =", calling_in_sick)
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
    print("calling_in_sick =", calling_in_sick)
else:
    calling_in_sick = False
    print("calling_in_sick=", calling_in_sick)
