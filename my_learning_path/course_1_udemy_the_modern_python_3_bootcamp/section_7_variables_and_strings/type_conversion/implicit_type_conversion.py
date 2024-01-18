"""
The below shows an example of implicit type conversion and how
data type values are automatically converted in the background (implicitly)
to another data type
"""

num_int = 123
num_flo = 1.23

# You can print more than one thing inside the print() function for clarity
print("data type of num_int:", num_int, type(num_int))
print("data type of num_flo:", num_flo, type(num_flo))

# This is implicit type conversion because whenever you do math
# the result will be converted into a float automatically
num_new = num_int + num_flo
print("value of num_new:", num_new)

print("data type of num_new:", num_new, type(num_new))
