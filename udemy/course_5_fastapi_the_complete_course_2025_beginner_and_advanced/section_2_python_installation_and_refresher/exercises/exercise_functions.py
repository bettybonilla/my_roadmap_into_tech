"""
Create a function that takes in 3 parameters (first_name, last_name, age) and returns a dictionary based on those values
"""


def personal_info(first_name: str, last_name: str, age: int) -> dict[str, str | int]:
    my_dict = {"first_name": first_name, "last_name": last_name, "age": age}
    return my_dict


if __name__ == "__main__":
    print(personal_info("Betty", "Bonilla", 31))
