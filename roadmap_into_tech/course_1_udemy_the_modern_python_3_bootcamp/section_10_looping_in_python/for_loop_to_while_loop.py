"""
Below is an example of how you can turn a for loop to a while loop
- NOTE: Although you can turn a for loop to a while loop, always choose the
best loop for the situation since it shows actual understanding and intent
"""

# The code below is a for loop that prints numbers 1 to 10
for num in range(1, 11):
    print(num)

print("")

# The code below is a while loop that prints numbers 1 to 10
num = 0

while num < 10:
    num += 1
    print(num)

print("")

# This is another way of writing the while loop above
num = 1

while num < 11:
    print(num)
    num += 1
