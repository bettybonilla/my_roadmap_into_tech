"""
Below the happy_birthday() function includes type annotation/type hinting to
clearly specify the input data type expected for the name parameter
"""


# Type Annotation/Type Hinting
# In the happy_birthday() function below, it takes a string and is annotated as
# follows:
# The name parameter is expected to be of type str
def happy_birthday(name: str):
    print("Happy birthday to you...")
    print("Happy birthday to you...")
    print(f"Happy birthday dear {name}...")
    print("Happy birthday to you ! ! !")


happy_birthday("Charlie")

# References
# https://docs.python.org/3/library/typing.html
