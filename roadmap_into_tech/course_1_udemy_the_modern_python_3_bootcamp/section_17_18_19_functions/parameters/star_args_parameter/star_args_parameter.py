"""
The below shows how you can use *args in a function
"""


# The sum_all_nums() function below adds up the 3 arguments provided which each
# correspond to an individual parameter
def sum_all_nums(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


print(sum_all_nums(4, 6, 9))


# However, we can use *args as a parameter to provide as many arguments as we
# want instead of having separate parameters for each argument like the 3
# originally provided above which corresponded to each individual parameter
def sum_all_nums(*args: int) -> int:
    # We need the * star operator in the parameter but we don't need it
    # outside of the parameter as shown below in the print() function
    # This prints the args provided in the function call as a tuple
    print(args)

    # Since our args is a tuple, we need to iterate through the tuple in order
    # to get the sum of all the args
    total = 0

    for num in args:
        total += num
    return total


# As mentioned, now we can pass in as many arguments as we want since we are
# using *args as a parameter
print(sum_all_nums(4, 6, 9))
print(sum_all_nums(4, 6, 9, 5, 10, 15, 1))
print(sum_all_nums(2, 6))


# The below shows that the parameter doesn't have to be named *args, it can be
# named anything you want as long as it starts with the * star operator
def sum_all_nums(*nums: int) -> int:
    print(nums)

    total = 0

    for num in nums:
        total += num
    return total


print(sum_all_nums(4, 6))
