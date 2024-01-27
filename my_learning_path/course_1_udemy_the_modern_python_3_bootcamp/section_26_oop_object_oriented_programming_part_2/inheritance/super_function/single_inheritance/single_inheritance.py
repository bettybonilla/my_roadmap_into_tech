"""
The below shows how we can use the super() function for single inheritance
which allows a subclass child class to inherit from one base parent class
"""


# Base parent class
class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def __str__(self) -> str:
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound: str) -> str:
        return f"This animal says {sound}"


# Subclass child class
class Cat(Animal):
    def __init__(self, name: str, breed: str, fav_toy: str):
        # This would be duplication since the Animal base parent class already
        # initializes these instance attributes in its __init__ dunder method
        # self.name = name
        # self.species = species
        # Instead, we can use the super() function which allows us to access
        # methods of the base parent class that the current subclass child
        # class is inheriting from in its signature which makes class
        # inheritance more manageable and extensible since you can extend the
        # functionality of previously built classes without implementing their
        # functionality again to avoid duplication
        # You don’t have to provide the self parameter since it will be
        # automatically passed in so instead you just provide the parameters
        # from the method you’re calling on the super() function - In this
        # case, the __init__ dunder method from the Animal base parent class
        # Since the species for a Cat instance will always be "cat", we can
        # also set a default value of "cat" to the species parameter below and
        # therefore we don't need the species parameter in the __init__ dunder
        # method above for Cat since it won't be necessary to provide it
        # whenever we instantiate a new Cat instance
        super().__init__(name, species="cat")
        self.breed = breed
        self.fav_toy = fav_toy

    def play(self) -> str:
        return f"{self.name} plays with {self.fav_toy}"


blue = Cat("Blue", "Scottish Fold", "string")
print(blue)
print(blue.make_sound("meow"))
print(blue.species)
print(blue.breed)
print(blue.fav_toy)
print(blue.play())
