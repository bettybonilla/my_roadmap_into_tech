'''
- At the top of the file is some starter code that randomly picks a number
between 1 and 10 and saves it to a variable called choice. Don't touch
those lines! (please)
- Your job is to write a simple conditional to check if choice is 7
- If choice is 7, print "lucky". Otherwise, print "unlucky".
'''

# NO TOUCHING -----------------------------------------------------------------
# Picks random number from 1-10
from random import randint
choice = randint(1, 10)
# NO TOUCHING -----------------------------------------------------------------

# YOUR CODE GOES HERE:
print(choice)

if choice == 7:
    print("lucky")
else:
    print("unlucky")
