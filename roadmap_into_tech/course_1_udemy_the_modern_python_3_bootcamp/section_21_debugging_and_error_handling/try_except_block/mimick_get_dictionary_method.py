"""
The below mimicks the .get() dictionary method with a try/except block
"""


def get_key(dictionary: dict, key: str) -> str | None:
    # The try block contains code that may cause an exception/error if the
    # dictionary key doesn't exist, otherwise it will return the dictionary key
    try:
        return dictionary[key]
    # If the dictionary key doesn't exist, instead of returning an error
    # message, we will return None which mimicks the .get() dictionary method
    # The KeyError error type is used since this is the particular
    # exception/error that would occur
    except KeyError:
        return None


person = {"name": "Ricky"}

print(get_key(person, "name"))
print(get_key(person, "city"))
