'''
The below shows an example of explicit type conversion (type casting) and how
you can convert data type values yourself (explicitly) to another data type by
using type conversion functions
(Ex: int(), float(), str(), etc.)
'''

num_int = 123
num_str = "456"

print("data type of num_int:", num_int, type(num_int))
print("data type of num_str:", num_str, type(num_str))

# This is explicit type conversion (type casting) because you cannot
# add numbers and strings so therefore you have to convert the data type value
# of the num_str variable yourself (explicitly) to an int data type by using
# the type conversion function int()
num_str = int(num_str)
print("data type of num_str after type casting:", num_str, type(num_str))

# Now that the data type value of the num_str variable has been converted into
# an int from a str, you can add num_int + num_str
num_sum = num_int + num_str
print("value of num_sum:", num_sum)

# The data type value of num_sum also remains an int
print("data type of num_sum:", num_sum, type(num_sum))
