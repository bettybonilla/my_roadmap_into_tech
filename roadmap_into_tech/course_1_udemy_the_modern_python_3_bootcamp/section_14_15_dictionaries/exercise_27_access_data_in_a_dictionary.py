"""
Given the dictionary below:
1. artist = {
2.     "first": "Neil",
3.     "last": "Young",
4. }
- Declare a variable called full_name that is equal to artist's first and
last name with a space in between
- You must reference the values associated with those keys in the artist
dictionary
    1. print(full_name)
    2. # Neil Young
"""

artist = {
    "first": "Neil",
    "last": "Young",
}
print(artist)

full_name = artist["first"] + " " + artist["last"]
print(full_name)

# # Alternative code using .format() method
# full_name = "{} {}".format(artist["first"], artist["last"])
# print(full_name)

# Alternative code using an f-string
# full_name = f"{artist['first']} {artist['last']}"
# print(full_name)
