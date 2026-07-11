"""
- NOTE: Although you can use this package for complex Python objects, YOU SHOULD STILL ONLY USE THE JSON BUILT-IN MODULE
AND NOT RELY ON AN EXTERNAL MODULE
"""

import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Charles", "Tabby")

# To pickle the c Cat instance using jsonpickle:
# Use the open() function and pass in the file name you want to use for your JSON file with .json as the file extension
# Then use the "w" file mode to write to the file since you're not serializing anything to binary
with open("cat.json", "w") as file:
    # Then you can use the jsonpickle.encode() function by saving it to a variable and passing in the complex Python
    # object which encodes it into a JSON string
    frozen = jsonpickle.encode(c)
    # Prints the complex Python object as a JSON string
    print(frozen)
    # Writes it to the cat.json file
    file.write(frozen)

# To unpickle the c Cat instance using jsonpickle:
# Use the open() function and pass in your JSON file
# Comment out the previous with statement and the c instance then run the code
# with open("cat.json") as file:
#     # Then use the .read() method on the opened file and save it to a variable
#     text = file.read()
#     # Then you can use the jsonpickle.decode() function and pass in the file which decodes it to the Python object from
#     # a JSON string
#     # When you use the jsonpickle.decode() function, any code inside will execute (as mentioned this can be a security
#     # risk)
#     unfrozen = jsonpickle.decode(text)
#     # Prints the Python object
#     print(unfrozen)
