'''
Below is an example showing truthiness to show that certain things have a
default inherit truthiness or falsiness
- NOTE: Any string that isn't empty is truthy, any empty string is falsy
'''

animal = input("Enter your favorite animal: ")

if animal:
    print(animal + "s" + " are my favorite too!")
    # If the user doesn’t enter anything and presses enter this will result in
    # an empty string which is falsy because it will not print anything
    # therefore, the else conditional is added to tell the user they didn’t
    # enter anything
else:
    print("YOU DIDN'T ENTER ANYTHING!")
