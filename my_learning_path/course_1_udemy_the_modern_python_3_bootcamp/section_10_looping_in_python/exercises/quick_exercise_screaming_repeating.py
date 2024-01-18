"""
Print a repeating print statement based on the number entered from the
user input
"""

mom = input("How many times do I have to tell you?! ")

mom = int(mom)

for i in range(mom):
    print("CLEAN UP YOUR ROOM!")
    # This shows the index of the i item variable as it loops through the
    # iterable and that's why it's able to return each print statement the
    # number of times entered from the user input
    # print(f"i = {i}: CLEAN UP YOUR ROOM!")
    # Adding 1 to the i item variable more easily shows the actual position of
    # the i item variable as it loops through the iterable
    # print(f"i = {i + 1}: CLEAN UP YOUR ROOM!")
