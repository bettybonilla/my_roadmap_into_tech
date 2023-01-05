"""
The below is a conditional statement that checks if someone lives in
California by using the or logical operator
- NOTE: This example does not take into account all the cities in California
"""

city = input("Where do you live? ").lower().strip()

# Only one side of the or logical operator needs to be True in order for the
# entire statement to be True
if city == "san francisco" or city == "los angeles":
    print("YOU LIVE IN CALIFORNIA!")
else:
    print("YOU LIVE SOMEWHERE ELSE")
