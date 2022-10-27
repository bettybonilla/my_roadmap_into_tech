def validate_data(age):
    if age == "":
        print("YOU DIDN'T ENTER ANYTHING, ENTER YOUR AGE NOW!")
        return False
    return True


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
