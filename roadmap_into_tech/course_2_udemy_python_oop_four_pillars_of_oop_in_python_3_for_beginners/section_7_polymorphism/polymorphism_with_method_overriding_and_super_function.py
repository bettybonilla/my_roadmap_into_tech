"""
The below shows polymorphism using method overriding and the super() function
"""


# Base parent class
class Employee:
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 40

    def display_number_of_working_hours(self):
        print(self.set_number_of_working_hours)


# Subclass child class AKA derived class
class Trainee(Employee):
    # Uses method overriding to override the set value of this method from the
    # Employee base parent class
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 45

    # Uses the super() function to reset this method back to the set value
    # of the Employee base parent class
    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours()


e = Employee()
e.set_number_of_working_hours()
print("Number of working hours of employee:", end=" ")
e.display_number_of_working_hours()
t = Trainee()
t.set_number_of_working_hours()
print("Number of working hours of trainee:", end=" ")
t.display_number_of_working_hours()
t.reset_number_of_working_hours()
print("Number of working hours of trainee after reset:", end=" ")
t.display_number_of_working_hours()
