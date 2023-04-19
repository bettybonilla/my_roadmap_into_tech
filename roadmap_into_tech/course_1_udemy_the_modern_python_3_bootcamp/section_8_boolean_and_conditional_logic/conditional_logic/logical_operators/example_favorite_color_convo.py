from random import randint

RED = "red"
BlUE = "blue"
YELLOW = "yellow"

# It can be a good idea to have 2 variables for your user input in case you
# need to look at the original unaltered user input data for future
# bugfixes, etc.
# The x variable is the unaltered user input data
# The x_validated variable is the altered user input data using the
# .strip() method and .lower() method
x = input("What's your favorite color?: ")
x_validated = x.lower().strip()

if x_validated == "":
    print("Please provide a color")
    quit(1)

# If the user doesn't input what is in the list [] then print "Hmm I guess you
# don't like primary colors"
if x_validated not in [RED, BlUE, YELLOW]:
    print("Hmm, I guess you don't like primary colors")

# The None value acts as a placeholder for a variable so that you can
# define/assign it later
# By using the None value, as shown below the pet_color variable can be
# dynamically assigned in the conditional logic
n = randint(0, 2)
response = "Cool, my pets favorite color is {}"

pet_color = None
if n == 0:
    pet_color = "green"
elif n == 1:
    pet_color = "orange"
elif n == 2:
    pet_color = "purple"

if pet_color:
    print(response.format(pet_color))

quit(0)

# colors = ["orange", "purple", "pink"]
# print(f"my pets favorite color is {choice(colors)}")

# def choice(list):
# 	return list[randint(0, len(list)-1)]
