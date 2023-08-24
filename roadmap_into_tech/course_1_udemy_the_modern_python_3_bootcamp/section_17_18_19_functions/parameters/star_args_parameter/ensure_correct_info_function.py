"""
Below is another example of how you can use *args in a function to check for
specific input provided since, as mentioned, you're able to pass in as many
arguments as you want with the *args parameter
"""

from typing import Any


# In the ensure_correct_info() function below, the *args parameter is used to
# check if "Colt" and "Steele" were passed in as arguments and if they were it
# will return "Welcome back Colt!" otherwise, it will return "Not sure who you
# are..."
def ensure_correct_info(*args: Any) -> str:
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."


print(ensure_correct_info())
print(ensure_correct_info(1, True, "Steele", "Colt"))
print(ensure_correct_info("hello", False, 78))
