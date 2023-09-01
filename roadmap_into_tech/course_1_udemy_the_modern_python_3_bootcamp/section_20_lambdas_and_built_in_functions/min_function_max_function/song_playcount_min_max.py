"""
The below uses the min() function and max() function to return the smallest
playcount or the largest playcount from the songs list
"""

songs = [
    {"Title": "Happy Birthday", "Playcount": 1},
    {"Title": "Survive", "Playcount": 6},
    {"Title": "YMCA", "Playcount": 99},
    {"Title": "Toxic", "Playcount": 30},
]

# Returns the dictionary with the smallest or largest playcount
print(min(songs, key=lambda song: song["Playcount"]))
print(max(songs, key=lambda song: song["Playcount"]))

# You can also specify to just return the dictionary key "Title" to get the
# actual song with the smallest or largest playcount
print(min(songs, key=lambda song: song["Playcount"])["Title"])
print(max(songs, key=lambda song: song["Playcount"])["Title"])
