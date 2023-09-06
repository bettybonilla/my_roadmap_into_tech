"""
The below shows how we can use the pdb built-in Python module with the
pdb.set_trace() method to set breakpoints in our code which pauses execution of
our code to allow us to step through our code one line at a time in terminal
"""

import pdb

# Common pdb commands:
# l - Stands for list and lists where you are in your program
# n - Stands for next line and will move the breakpoint to the next line in
# your program
# c - Stands for continue and will continue executing the rest of the program
# as nornal regardless of where you placed your breakpoint
# p - Stands for print and will print the value of a variable that conflicts
# with a pdb command
# a - Stands for all values and will list all variables and their values

first = "First"
second = "Second"
# It's best to place the pdb.set_trace() method a line before or a couple
# lines before where our code is actually breaking
# In terminal, it will point to the next line waiting to execute, which will
# be the line after the pdb.set_trace() method, and then we can use the pdb
# commands above to step through our code one line at a time - Terminal will
# be waiting for you to enter a pdb command
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)


# However, pdb is most commonly used on one line, import pdb; pdb.set_trace(),
# where we're debugging our code only while we're debugging and then deleted
# once we're finished since it's not meant to be included in our program
# # fmt: skip is used since Black will re-format otherwise
# Also, be careful with using pdb commands as variable names!
# If you do use a pdb command as a variable name, you must use the p command
# along with the variable name in order to print the value of that variable
def add_numbers(a, b, c, d) -> int:
    import pdb; pdb.set_trace()  # fmt: skip
    return a + b + c + d


print(add_numbers(1, 2, 3, 4))
