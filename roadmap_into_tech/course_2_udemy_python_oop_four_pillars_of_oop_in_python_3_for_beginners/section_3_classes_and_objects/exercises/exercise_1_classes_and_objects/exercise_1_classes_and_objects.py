"""
Write an object-oriented program that performs the following tasks:
- Define a class called Employee and create an instance of that class
- Create an attribute called name and assign it with a value
- Change the name you previously defined within a method and call this method
by making use of the object you created
"""


class Employee:
    name = "Ben"

    def change_name(self, new_name: str):
        self.name = new_name


employee_one = Employee()
print(employee_one.name)
employee_one.change_name("David")
print(employee_one.name)
