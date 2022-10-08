'''
Below is an if statement example using the == equality operator
'''

# To account for user input errors, the .lower() method is used to convert the
# user input entered to all lowercase and the .strip() method is used to remove
# leading (front) and trailing (end) whitespaces
name = input("Who's better vampires or werewolves? ").lower().strip()

if name == "vampires":
    print("You're Team Edward")
elif name == "werewolves":
    print("You're Team Jacob")
else:
    print("Carry on, human")
