"""
The below uses the sorted() function with lambda functions to sort the users
list in different ways by dictionary keys
"""

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "I love candy"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []},
]

# Sorts the users list by dictionary key "username" alphabetically
print(sorted(users, key=lambda user: user["username"]))

# Sorts the users list by dictionary key "tweets" from least active to most
# active based on the number of tweets by using the len() function
print(sorted(users, key=lambda user: len(user["tweets"])))

# Sorts the users list by dictionary key "tweets" from most active to least
# active based on the number of tweets by using the len() function
print(sorted(users, key=lambda user: len(user["tweets"]), reverse=True))
