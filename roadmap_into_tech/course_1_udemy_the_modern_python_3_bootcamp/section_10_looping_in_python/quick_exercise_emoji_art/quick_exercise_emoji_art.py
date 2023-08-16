"""
Print the 😀 emoji incrementing from 1 to 10 using both a for loop and a
while loop
- NOTE: The time module is imported and the time.sleep() method is used to
show the execution and formation of the loops
"""

import time

EMOJI = "😀"

# Solution using time.sleep() method with a for loop and a while loop
y = 0

while y < 10:
    y += 1
    for x in range(y):
        print(EMOJI, end="", flush=True)
        time.sleep(0.25)
    print("")
    time.sleep(1)

# =============================================================================
# The code below has been refactored to the code above
# Solution without using time.sleep() method with a for loop and a while loop
# y = 0

# while y < 10:
#     y += 1
#     for x in range(y):
#         print(EMOJI, end="")
#     print("")
# =============================================================================
# The code below has been refactored to the code above
# Solution using time.sleep() method with a double for loop which is a for loop
# nested inside another for loop
# for y in range(1, 11):
#     # This nested for loop along with print(EMOJI, end="") starts the path
#     # for a right-angled triangle to form
#     for x in range(y):
#         # The end="" is a parameter you can add inside a print() function
#         # that will print data in a single line which allows for the EMOJI
#         # variable to appear right next to each other - Try end="hello" to
#         # see the difference
#         # The flush parameter when set to True prints whatever data is in the
#         # print() function one at a time - In this case each piece of data
#         # prints one at a time after 0.25 sec since the time.sleep() method
#         # is set to 0.25
#         # The default is set to False which prints whatever data is in the
#         # print() function immediately all at once since this is more memory
#         # efficient and it is costly to print data one at a time
#         print(EMOJI, end="", flush=True)
#         # Sleeps/suspends execution of the program for 0.25 sec
#         time.sleep(0.25)
#     # Provides a new line every loop to continue the right-angled triangle
#     # until completion
#     print("")
#     # Sleeps/suspends execution of the program for 1 sec
#     time.sleep(1)
# =============================================================================
# The code below has been refactored to the code above
# Solution with one for loop (preferred code)
# for i in range(1, 11):
#     # print(f"i = {i}")
#     # print(EMOJI * i, f"i = {i}")
#     print(EMOJI * i)

# Solution with one while loop (alternative code)
# y = 0

# while y < 10:
#     y += 1
#     print(EMOJI * y)
