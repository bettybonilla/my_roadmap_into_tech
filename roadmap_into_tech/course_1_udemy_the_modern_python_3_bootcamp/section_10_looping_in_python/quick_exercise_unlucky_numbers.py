"""
- Loop through numbers 1-20 (inclusive)
- For 4 and 13, print “x is unlucky”
- For even numbers, print “x is even”
- For odd numbers, print “x is odd”
"""

for i in range(1, 21):
    if i == 4 or i == 13:
        state = "unlucky"
    elif i % 2 == 0:
        state = "even"
    elif i % 2 == 1:
        state = "odd"
    print(f"{i} is {state}")

# The code below has been refactored to the code above
# Below there are 3 print statements being used however the code above follows
# the DRY (Don't Repeat Yourself) principle by using 1 print statement instead
# and interpolating variables with an f-string - Anytime you see repetition,
# you should implement the DRY principle
# for i in range(1, 21):
#     if i == 4 or i == 13:
#         print(i, "is UNLUCKY!")
#     elif i % 2 == 0:
#         print(i, "is even")
#     elif i % 2 == 1:
#         print(i, "is odd")
