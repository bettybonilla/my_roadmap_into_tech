"""
The below takes kilometers and converts it into miles by asking for user input
on how many kilometers the user ran today
"""

print("How many kilometers did you run today?")
kms = input()

# The input() function automatically (implicitly) always converts
# whatever data/value is entered into a string so therefore you need to use the
# float() type conversion function in order to convert the
# input() function value from a str data type to a float data type
kms = float(kms)

# Now that the kms variable has been converted from a str data type to a
# float data type, you can use it in the formula to convert kilometers into
# miles
miles = kms / 1.60934

# Next, the round() function is used to round the result to 2 decimal places
miles = round(miles, 2)

# Lastly, an f-string is used to interpolate the variables kms and miles in
# the string inside of the print() function to tell the user how many miles
# they ran
print(f"Your {kms} km run was {miles} mi!")
