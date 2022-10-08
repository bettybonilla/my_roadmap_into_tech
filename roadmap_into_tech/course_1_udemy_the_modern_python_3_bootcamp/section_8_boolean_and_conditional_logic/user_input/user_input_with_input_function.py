'''
The below shows 2 ways you can get user input with the input() function
'''

# This is how you can get user input by using a seperate line with
# the print() function
print("What's your favorite color?")
data = input()
print("You said " + data)

# This is another way you can get user input by using one line with
# the input() function as opposed to using a seperate line with
# the print() function
data = input("What's your favorite color? ")
print("You said " + data)
