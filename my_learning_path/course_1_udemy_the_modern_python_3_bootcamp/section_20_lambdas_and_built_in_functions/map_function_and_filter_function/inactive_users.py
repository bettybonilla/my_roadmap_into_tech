"""
Below the filter() function is used to filter the inactive users who still
haven't made their first tweet yet so that we can use this filtered list to
send a reminder email to encourage them to tweet
"""

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []},
]

# List of inactive users using filter() function
inactive_users = list(filter(lambda user: not user["tweets"], users))
print(inactive_users)

# Alternative code using list comprehension
inactive_users2 = [user for user in users if not user["tweets"]]
print(inactive_users2)

# List of inactive usernames only using map() function and filter() function
usernames = list(
    map(
        lambda user: user["username"].upper(),
        filter(lambda user: not user["tweets"], users),
    )
)
print(usernames)

# Alternative code using list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(usernames2)
