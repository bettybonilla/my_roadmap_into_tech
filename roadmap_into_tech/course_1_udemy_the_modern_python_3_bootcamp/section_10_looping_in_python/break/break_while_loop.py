"""
- Below is an example of how you would use the break keyword to exit out of a
while loop
- Without the if conditional along with break keyword, the while loop would
continue to prompt infinitely
"""

# While True loops will loop forever until it hits the break keyword
while True:
    command = input("Type 'exit' to exit: ")
    if command == "exit":
        break
