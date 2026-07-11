"""
The below uses the sorted() function with a lambda to sort the songs list by
song playcount
"""

songs = [
    {"Title": "Happy Birthday", "Playcount": 1},
    {"Title": "Survive", "Playcount": 6},
    {"Title": "YMCA", "Playcount": 99},
    {"Title": "Toxic", "Playcount": 30},
]

# Sorts the songs list by dictionary key "Playcount" from least played song to
# most played song
print(sorted(songs, key=lambda song: song["Playcount"]))

# Sorts the songs list by dictionary key "Playcount" from most played song to
# least played song
print(sorted(songs, key=lambda song: song["Playcount"], reverse=True))
