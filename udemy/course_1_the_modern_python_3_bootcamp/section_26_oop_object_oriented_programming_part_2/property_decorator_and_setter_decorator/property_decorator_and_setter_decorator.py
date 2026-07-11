"""
The below shows how we can use the @property decorator to conveniently make an
instance method a getter and the @setter decorator to conveniently make an
instance method a setter
"""


class Human:
    def __init__(self, first_name: str, last_name: str, age: int):
        # Initialized all instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0
        self.set_age(age)

    # def get_age(self) -> int:
    #     return self._age

    # Setter method
    # This instance method is needed despite using the instance method with
    # the @setter decorator below since this instance method is a true setter
    # and passes in the data to set whereas the instance method with the
    # @setter decorator below allows you to conveniently change/update the
    # data by using the = assignment operator
    def set_age(self, age: int):
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # Getter method
    # The @property decorator makes the instance method below a getter and
    # therefore the get in get_age is no longer needed in the name
    @property
    def age(self) -> int:
        return self._age

    # Setter method
    # The getter and setter need to share the same name therefore, we've named
    # the instance method below age as well since we need to reference the
    # getter in order to use the @setter decorator:
    # @getter_name.setter
    @age.setter
    def age(self, age: int):
        self.set_age(age)

    # Getter method
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


p1 = Human("Jane", "Goodall", 50)
# print(p1.get_age())
# p1 = Human("Jane", "Goodall", -50)
# print(p1.get_age())

# By using the @property decorator and the @setter decorator we can now call
# age on the instance without parentheses even though they're methods since
# the @property decorator and the @setter decorator alters it to act as an
# instance attribute
# The @setter decorator allows you to conveniently change/update the data by
# using the = assignment operator
print(p1.age)
p1.age = -50
print(p1.age)
p1.age = 20
print(p1.age)
print(p1.full_name)
