"""
Below the happy_birthday() function includes type annotation to clearly specify
the input expected in the name argument
"""


# Type annotation
# In the happy_birthday() function below, it takes a string and is annotated as
# follows:
# The name argument is expected to be of type str
def happy_birthday(name: str):
    print("Happy birthday to you...")
    print("Happy birthday to you...")
    print(f"Happy birthday dear {name}...")
    print("Happy birthday to you ! ! !")


happy_birthday("Charlie")

# References
# https://docs.python.org/3/library/typing.html
