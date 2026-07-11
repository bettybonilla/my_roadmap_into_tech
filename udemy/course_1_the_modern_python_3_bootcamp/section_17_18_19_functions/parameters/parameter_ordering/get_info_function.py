"""
The below shows the proper parameter ordering to follow in functions
"""


# Proper parameter ordering:
# (parameters, *args, default parameters, **kwargs)
def get_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


print(get_info(1, 2, 3, last_name="Steele", job="Instructor"))
