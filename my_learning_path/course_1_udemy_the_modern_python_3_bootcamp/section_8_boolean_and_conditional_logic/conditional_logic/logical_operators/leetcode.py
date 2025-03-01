"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz",
"13","14","FizzBuzz"]
"""

# -----------------------------------------------------------------------------
# TODO: Revisit after learning arrays and for loops
# The code below is correct but incomplete so it would not be ready for
# submission
# -----------------------------------------------------------------------------


def process_data(n):
    n = int(n)
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")


n = input("Enter a number: ")
process_data(n)
print(str(n), type(str(n)))

# -----------------------------------------------------------------------------
# The code below has been refactored to the code above
# n = input("Enter a number: ")
# n = int(n)

# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# else:
#     print(str(n), type(str(n)))
