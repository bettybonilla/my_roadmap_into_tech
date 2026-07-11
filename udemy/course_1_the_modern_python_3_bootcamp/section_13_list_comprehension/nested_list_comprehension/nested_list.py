"""
The below shows how you can access nested lists using a double for loop
"""

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for location in coords:
    # Prints the 3 locations
    print(location)
    # Prints each coordinate within the 3 locations
    for i in location:
        print(i)
