"""
- NOTE: Be aware that pickling can bring up security issues if you‘re using an untrusted source - To guarantee your
data’s safety, only unpickle what comes from a trustworthy source or make sure it’s something you serialized yourself.
However, also NEVER STORE OR PICKLE SENSITIVE DATA in your programs - The strings command in terminal can be used to
very easily get data from any file even if it's been serialized to binary.
"""

import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
# Use the open() function and pass in the file name you want to use for your special pickle file with .pickle as the
# file extension - The .pickle file extension is not a real file format however it makes it easy to tell that this is a
# pickle file
# Then use the "wb" file mode (b stands for binary) to write to the file since you will be serializing the data which
# converts it to a byte stream (binary)
with open("pets.pickle", "wb") as file:
    # Then you can use the pickle.dump() function and pass in the object you want to dump into the pickle file (you can
    # also use a tuple to pass in multiple objects) and then pass in the pickle file
    # Those objects will be stored and serialized in the pickle file you passed in - For convenience, you should always
    # open pickle files in Sublime
    pickle.dump(blue, file)

# To unpickle an object:
# Use the open() function and pass in your pickle file
# Then use the "rb" file mode (as mentioned b stands for binary) to read to the file since you will be de-serializing
# the data which was converted to a byte stream (binary)
# with open("pets.pickle", "rb") as file:
#     # Then you can use the pickle.load() function by saving it to a variable and passing in the pickle file
#     # When you use the pickle.load() function, any code inside will execute (as mentioned this can be a security risk)
#     # Comment out the previous with statement and the blue instance then run the code
#     zombie_blue = pickle.load(file)
#     print(zombie_blue)
#     zombie_blue.play()
