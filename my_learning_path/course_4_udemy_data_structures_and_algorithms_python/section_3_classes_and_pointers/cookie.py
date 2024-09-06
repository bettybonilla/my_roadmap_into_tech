"""
The below represents a class in code
"""


class Cookie:
    # Initializer AKA constructor
    def __init__(self, color: str):
        # Instance attribute
        self.color = color

    # Instance method (getter) - ONLY returns data so a return statement is used
    def get_color(self) -> str:
        return self.color

    # Instance method (setter) - ONLY sets data so a return statement is not used
    def set_color(self, color: str):
        self.color = color


if __name__ == "__main__":
    # Instantiates and sets the cookie_one variable and the cookie_two variable to both be a type of Cookie AKA Cookie
    # instance/object
    # The cookie_one variable, which is a type of Cookie AKA Cookie instance/object, its self.color is green
    # The cookie_two variable, which is a type of Cookie AKA Cookie instance/object, its self.color is blue
    cookie_one = Cookie("green")
    cookie_two = Cookie("blue")

    print("Cookie one is", cookie_one.get_color())
    print("Cookie two is", cookie_two.get_color())

    # The cookie_one variable is now set to yellow so its self.color is now yellow
    cookie_one.set_color("yellow")
    print("")

    print("Cookie one is now", cookie_one.get_color())
    print("Cookie two is still", cookie_two.get_color())
