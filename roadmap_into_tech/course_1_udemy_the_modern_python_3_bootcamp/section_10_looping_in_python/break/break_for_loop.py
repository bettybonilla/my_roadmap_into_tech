"""
- Below is an example of how you would use the break keyword to exit out of a
for loop
- Even though the program intended to print numbers 1-100, using the if
conditional along with the break keyword, the program will now exit early
after printing numbers 1-3
"""

for x in range(1, 101):
    print(x)
    if x == 3:
        break
