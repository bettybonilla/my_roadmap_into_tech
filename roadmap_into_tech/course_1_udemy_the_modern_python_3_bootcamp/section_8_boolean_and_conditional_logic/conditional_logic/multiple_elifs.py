'''
Below is an example of how you can use multiple elif conditionals in a
conditional statement
'''

color = input("What's your favorite color? ").lower().strip()

if color == "purple":
    print("excellent choice!")
elif color == "teal":
    print("not bad!")
elif color == "seafoam":
    print("mediocre")
elif color == "pure darkness":
    print("I like how you think")
else:
    print("YOU MONSTER!")
