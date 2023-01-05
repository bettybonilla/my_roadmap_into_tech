def validate_data(age):
    if age == "":
        print("YOU DIDN'T ENTER ANYTHING, ENTER YOUR AGE NOW!")
        return False
    return True


"""
Validating data inside definitions with conditional logic is acceptable and
the exception to the general rule
- Doing type conversion inside the definition below also ensures that the
original data type of the age variable (str) can be used if needed later
without having to use type conversion again to convert it back to a
str from an int
- This is because, even though type conversion inside this defintion converts
the age variable from a str to an int, as shown below after this definition
is executed the age variable goes back to it's original data type (str)
"""


def process_data(age):
    age = int(age)
    if age >= 18 and age <= 20:
        # 18-20 Special Entry: Can't drink, need wristband
        print("You can enter: You can't drink and need a wristband!")
    elif age >= 21:
        # 21+ Normal Entry: Can drink, no wristband
        print("You can enter: You can drink and don't need a wristband!")
    elif age <= 17:
        # 17- No Entry: Sorry too young
        print("You can't enter: Sorry kid, you're too young!")


# Ask for age
age = input("Stop right there! Enter your age: ").strip()

if validate_data(age):
    process_data(age)

print("age:", age, type(age))
