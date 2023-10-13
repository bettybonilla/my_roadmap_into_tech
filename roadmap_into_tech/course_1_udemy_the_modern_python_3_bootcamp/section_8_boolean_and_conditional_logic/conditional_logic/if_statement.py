"""
Below is an if statement example using the == equality operator
"""

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

# -----------------------------------------------------------------------------
# The code above has been refactored to the code below
# To further account for user input errors, string indexing can be used to
# check for the first character you expect in the string of the user input
# which helps eliminate the possibility of spelling errors breaking the program
# if name[0] == "v":
#     print("You're Team Edward")
# elif name[0] == "w":
#     print("You're Team Jacob")
# else:
#     print("Carry on, human")
