"""
The below shows the difference between static methods and instance methods
"""


class Employee:
    # Public instance method
    def employee_details(self):
        self.name = "Ben"

    # Public static method
    # This method would still work if we use the self parameter however it is
    # not necessary since it doesn't need access to a particular
    # instance/object of a class or their instance attributes
    # However, without it Python will raise an error
    # Therefore, we can use the @staticmethod decorator to tell Python that it
    # doesn’t need to pass the self parameter which avoids the error
    # Using the @staticmethod decorator is a good way to differentiate static
    # methods from instance methods since, although you can also use the self
    # parameter, you can more easily tell them apart in code when you use the
    # @staticmethod decorator for static methods since instance methods
    # require the self parameter but don't require a decorator above them
    @staticmethod
    def welcome_message() -> str:
        return "Welcome to our company!"


employee = Employee()
# Initializes the name instance attribute
# However, this is why instance attributes should go in the __init__ dunder
# method since anytime we create a new instance of a class Python will look
# for the __init__ dunder method inside the class and will automatically run
# the code inside the __init__ dunder method which sets and initializes the
# data (attributes) that each instance/object of a class should have
employee.employee_details()
print(employee.name)
print(employee.welcome_message())
