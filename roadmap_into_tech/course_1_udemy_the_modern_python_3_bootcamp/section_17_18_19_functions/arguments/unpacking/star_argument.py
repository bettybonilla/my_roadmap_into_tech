"""
The below shows how we can use the * star operator as an argument to the *args
parameter in a function to "unpack" values in lists or tuples as separate
individual arguments
"""


def sum_all_values(*args: int) -> int:
    print(args)

    total = 0

    for num in args:
        total += num
    return total


print(sum_all_values(1, 30, 2, 5, 6))

nums_list = [1, 2, 3, 4, 5, 6]
nums_tuple = (1, 2, 3, 4, 5, 6)

# The * star operator can be used as an argument with lists or tuples and will
# pass in and "unpack" each value as a separate individual argument to the
# *args parameter in the function, which will then be a tuple
print(sum_all_values(*nums_list))
print(sum_all_values(*nums_tuple))
