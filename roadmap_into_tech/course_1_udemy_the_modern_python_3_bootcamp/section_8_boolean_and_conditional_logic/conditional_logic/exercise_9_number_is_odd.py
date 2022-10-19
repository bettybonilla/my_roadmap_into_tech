'''
- You will be provided with a random number in a variable called num
- Use a conditional statement to check if the number is odd. If num is odd,
print "odd". Otherwise print "even".
- Hint: Use modulus % to figure out if the number is odd!
'''

# NO TOUCHING ======================================
# Picks random number from 1-1000
from random import randint
num = randint(1, 1000)
# NO TOUCHING ======================================

# YOUR CODE GOES HERE:
print(num)

if num % 2 == 1:
    print("odd")
elif num % 2 == 0:
    print("even")
