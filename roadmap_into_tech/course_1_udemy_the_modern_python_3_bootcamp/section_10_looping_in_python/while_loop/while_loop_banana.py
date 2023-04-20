"""
Below is another example of a while loop
- NOTE: You MUST stop the program from running either by ending the while loop
or by pressing Ctrl + C to exit the program in terminal
"""

msg = input("What's the secret password?: ")

while msg != "banana":
    print("WRONG!")
    msg = input("What's the secret password?: ")
print("CORRECT!")
