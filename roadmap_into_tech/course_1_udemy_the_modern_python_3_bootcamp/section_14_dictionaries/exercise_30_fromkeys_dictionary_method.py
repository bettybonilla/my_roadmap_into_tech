"""
- Imagine we're creating a video game and want to model the initial starting
state of our game - I've provided you with a list of strings called
game_properties
- Use dict.fromkeys to generate a new dictionary using the provided
game_properties list - Initialize all values to 0
- Save the result in a variable called initial_game_state
- Hint: The end result should look like this:
    {'current_score': 0, 'high_score': 0, 'number_of_lives': 0,
    'items_in_inventory': 0, 'power_ups': 0, 'ammo': 0, 'enemies_on_screen': 0,
    'enemy_kills': 0, 'enemy_kill_streaks': 0, 'minutes_played': 0,
    'notifications': 0, 'achievements': 0}
"""

# NO TOUCHING =================================================================
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements",
]
# NO TOUCHING =================================================================

# YOUR CODE GOES HERE:
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)
