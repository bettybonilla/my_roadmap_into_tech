import os


# Using a clamp is typical in gaming and in programming in general so that your values are within an acceptable and
# expected specific range, ensuring that they never fall below a minimum value or exceed above a maximum value
def clamp(value: int, min_value: int, max_value: int) -> int:
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value

    # Alternative code
    # return max_value(min_value, min_value(value, max_value))


# Returns the exported environ_var variable from the profile file (bash profile/os) which should be used in production
# for security purposes since it won't be committed
# Otherwise, returns the default_value variable which should be used for testing purposes only since it will be
# committed however it won't be used in production
def get_exported_environ_var(environ_var: str, default_value: str) -> str:
    exported_environ_var = os.getenv(environ_var)
    if not exported_environ_var:
        return default_value
    return exported_environ_var
