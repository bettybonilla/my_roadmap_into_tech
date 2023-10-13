"""
Model the details of a Spotify playlist in a single variable
- NOTE: Don't worry about dates and exact duration times of the songs
"""

spotify_playlist = {
    "Title": "Patagonia Bus Ride",
    "Author": "Colt Steele",
    "Songs": [
        {
            "Title": "Sad Saturdays",
            "Artist(s)": "JOBA",
            "Album": "Sad Saturdays",
            "Duration": 4.5,
        },
        {
            "Title": "Wasted Days",
            "Artist(s)": "Cloud Nothings",
            "Album": "Attack on Memory",
            "Duration": 9.0,
        },
        {
            "Title": "Tilted - Paradis Remix",
            "Artist(s)": ["Christine and the Queens", "Paradis"],
            "Album": "Tilted (Paradis Remix)",
            "Duration": 6.0,
        },
    ],
}

# print(spotify_playlist)

total_duration_of_playlist = 0

for song in spotify_playlist["Songs"]:
    # print(song)
    # print(song["Duration"])
    total_duration_of_playlist += song["Duration"]
print(total_duration_of_playlist, "min")
