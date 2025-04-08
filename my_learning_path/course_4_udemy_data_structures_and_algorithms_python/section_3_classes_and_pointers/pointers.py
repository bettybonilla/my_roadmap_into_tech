"""
The below represents pointers in code
"""

# The num2 variable points to the num1 variable which is assigned to the 11 integer
# Therefore, the num2 variable also equates to the same 11 integer
num1 = 11
num2 = num1

print("Before num2 value is updated")
print("num1 =", num1)
print("num2 =", num2)
print("num1 == num2:", num1 == num2)
print("")

# The id() function is a Python built-in function which returns the memory ID of a variable/object - This is an integer
# which also represents the memory address of the variable/object so it can be used to check if two variables/objects
# refer to the same address/location in memory
# However, keep in mind that everytime you run your program your variable/object will return a different memory ID
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))
print("num1 and num2 point to the same memory address:", id(num1) == id(num2))

print("")
print("--------------------------------------------------------------------")
print("")

# Integers are immutable data types therefore when you update the num2 variable pointing to the num1 variable, the value
# of the num1 variable does not get updated as well
num2 = 22

print("After num2 value is updated")
print("num1 =", num1)
print("num2 =", num2)
print("num1 == num2:", num1 == num2)
print("")

print("num1 points to:", id(num1))
print("num2 points to:", id(num2))
print("num1 and num2 point to the same memory address:", id(num1) == id(num2))

print("")
print("--------------------------------------------------------------------")
print("")

# The dict2 variable points to the dict1 variable which is assigned to the {"value": 11} dictionary
# Therefore, the dict2 variable also equates to the same {"value": 11} dictionary
dict1 = {"value": 11}
dict2 = dict1

print("Before value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict1 == dict2:", dict1 == dict2)
print("")

print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict1 and dict2 point to the same memory address:", id(dict1) == id(dict2))

print("")
print("--------------------------------------------------------------------")
print("")

# Dictionaries are mutable data types therefore when you update the dict2 variable pointing to the dict1 variable, the
# value of the dict1 variable does get updated as well
dict2["value"] = 22

print("After value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict1 == dict2:", dict1 == dict2)
print("")

print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict1 and dict2 point to the same memory address:", id(dict1) == id(dict2))
