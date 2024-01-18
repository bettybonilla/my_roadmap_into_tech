"""
The below shows what happens when you try to change/update a class attribute
with the . dot operator on the class vs. a class instance
"""


class Employee:
    # Public class attribute
    working_hours = 40

    def __init__(self, name: str):
        # Public instance attribute
        self.name = name


employee_one = Employee("John")
employee_two = Employee("Mary")
print(Employee.working_hours)
print(employee_one.working_hours)
print(employee_two.working_hours)
print("")

# When you change/update a class attribute with the . dot operator on the
# class, it will change/update for all class instances
Employee.working_hours = 45
print(Employee.working_hours)
print(employee_one.working_hours)
print(employee_two.working_hours)
print("")

# When you try to change/update a class attribute with the . dot operator on a
# class instance, it will only change/update for this specific class instance
# Python also creates a new instance attribute for this class instance called
# working_hours and assigns the value you gave it since Python first checks to
# see if there is an instance attribute called working_hours and since there
# wasn't, it created one and assigned the value you gave it
# However, for the employee_two class instance Python again first checks to
# see if there is an instance attribute called working_hours and since there
# wasn't, it then checks to see if there is a class attribute called
# working_hours and since there was, it prints that value
employee_one.working_hours = 40
print(employee_one.working_hours)
print(employee_two.working_hours)

# To reiterate, this raises an AttributeError since Python first checks to see
# if for this class instance there is an instance attribute called age, which
# returns False, and then it checks to see if for this class instance there is
# a class attribute called age, which also returns False so that's why it
# raised an AttributeError: 'Employee' object has no attribute 'age'
print(employee_one.age)
