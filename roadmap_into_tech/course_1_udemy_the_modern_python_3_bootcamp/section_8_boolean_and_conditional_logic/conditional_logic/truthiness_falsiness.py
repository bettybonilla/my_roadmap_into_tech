'''
Below is an example showing that certain things have a default inherit
truthiness or falsiness
- NOTE: Any empty string is naturally falsy, any string that isn't empty is
naturally truthy however if your intention is to purposely set True values to
naturally falsy things then naturally truthy things will be False values and
they lose their default inherit truthiness or falsiness
'''

animal = input("Enter your favorite animal: ")

if animal:
    print(animal + "s" + " are my favorite too!")
else:
    # If the user doesn’t enter anything and presses enter this will result in
    # an empty string which is falsy because it will not print anything
    # therefore this else conditional is added to tell the user they didn’t
    # enter anything
    print("YOU DIDN'T ENTER ANYTHING!")
