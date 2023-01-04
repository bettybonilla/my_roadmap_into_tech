from random import randint

RED = "red"
BlUE = "blue"
YELLOW = "yellow"

# It can be a good idea to have 2 variables for your user input in case you
# need to look at the original unmodified user input data for future
# bugfixes, etc.
# The x variable is the unmodified user input data
# The validate_x variable is the modified user input data using the
# .strip() method and .lower() method
x = input("What's your favorite color?: ")
validate_x = x.lower().strip()

if validate_x == "":
    print("Please provide a color")
    quit(1)

# If the user doesn't input what is in the list [] then print "Hmm I guess you
# don't like primary colors"
if validate_x not in [RED, BlUE, YELLOW]:
    print("Hmm, I guess you don't like primary colors")

# The None value acts as a placeholder for a variable so that you can
# define/assign it later
# By using the None value, as shown below the pet_color variable can be
# dynamically assigned in the conditional logic
pet_color = None
response = "Cool, my pets favorite color is {0}"
n = randint(0, 2)

if n == 0:
    pet_color = "green"
elif n == 1:
    pet_color = "orange"
elif n == 2:
    pet_color = "purple"

if pet_color is not None:
    print(response.format(pet_color))

quit(0)

# colors = ["orange", "purple", "pink"]
# print(f"my pets favorite color is {choice(colors)}")

# def choice(list):
# 	return list[randint(0, len(list)-1)]
