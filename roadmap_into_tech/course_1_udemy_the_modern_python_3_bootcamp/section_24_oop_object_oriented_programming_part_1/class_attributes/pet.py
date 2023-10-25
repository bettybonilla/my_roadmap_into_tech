"""
Below we've defined the Pet class to only allow certain species as pets
"""


class Pet:
    _allowed_species = ["cat", "dog", "fish", "bird"]

    def __init__(self, name: str, species: str):
        self.name = name
        self.set_species(species)
    # Instance method (setter)
    # Proper setter method which sets an allowed species to an instance/object
    def _set_species(self, species: str):
        # Validation
        species = species.lower().strip()

        # Error catching/handling
        if species not in self._allowed_species:
            raise ValueError(f"You can't have a {species} as a pet!")
        # Instead of setting and initializing this instance attribute in the
        # __init__ dunder method above, it is placed in this method which is
        # called in the __init__ dunder method above and does validation and
        # error catching/handling so that's why it's placed after these steps
        self.species = species

    # Instance method (getter)
    # Proper getter method which returns the _allowed_species private class
    # attribute
    # Users are supposed to ONLY use this getter method to access the
    # _allowed_species private class attribute
    # Private class attributes always contain getter + setter methods since
    # users are not supposed to directly access them - Below is a setter
    # method which is called in the __init__ dunder method above
    # Public class attributes don't need getter + setter methods since users
    # are supposed to directly access them by using the . dot operator
    def get_allowed_species(self) -> list[str]:
        return self._allowed_species

    # Instance method (convenience - intended for internal use only)
    # Made private since users should ONLY use the proper getter method above
    # This is not a getter method since getter methods always return data,
    # not print data
    # When you have a function or method ALWAYS use a return statement instead
    # of a print statement since print statements are used for testing and
    # debugging, not in production environments
    # You can have several instance methods for your own convenience however
    # make sure they are ALWAYS made private like this one
    def _print_allowed_species(self):
        print(self._allowed_species)


cat = Pet("Sadie", "cat")
dog = Pet("Hachi", "dog")
# tiger = Pet("Tony", "tiger")

print(cat.name, cat.species)
print(dog.name, dog.species)

# As mentioned, users are not supposed to directly access private class
# attributes with the . dot operator and therefore you shouldn't use
# print(Pet._allowed_species) - Users should only directly access public class
# attributes with the . dot operator
# Instead, you should use a proper getter method to access private class
# attributes - Above, a proper getter method is provided which should be used
# to access the _allowed_species private class attribute
print(Pet._allowed_species)
# Returns the _allowed_species private class attribute
print(cat.get_allowed_species())
# Prints the _allowed_species private class attribute
# As mentioned, this instance method is used for convenience and intended for
# internal use only
cat._print_allowed_species()

print(cat.species)
print(cat.get_allowed_species())
Pet._allowed_species.append("mouse")
print(cat.get_allowed_species())
cat.set_species("mouse")
print(cat.species)

print(dog.species)
print(dog.get_allowed_species())
dog.set_species(" BiRd  ")
print(dog.species)
print("")

# As mentioned, a class attribute is shared with all instances/objects of a
# class and the class itself
# Therefore, each instance/object will have it's own _allowed_species
# attribute and, since it is shared, it references and points to the same
# memory ID as Pet._allowed_species
# To prove this, we can use the id() function which is a built-in Python
# function that returns the memory ID of an object - This would be an integer
# which also represents the memory address of the object so it can be used to
# check if two variables/objects refer to the same address/location in memory
# However, keep in mind that everytime you run your program your object will
# return a different memory ID
print(Pet._allowed_species)
print(cat._allowed_species)
print(dog._allowed_species)
print(id(Pet._allowed_species))
print(id(cat._allowed_species))
print(id(dog._allowed_species))
print(id(Pet._allowed_species) == id(cat._allowed_species))
print(id(Pet._allowed_species) == id(cat._allowed_species) == id(dog._allowed_species))
