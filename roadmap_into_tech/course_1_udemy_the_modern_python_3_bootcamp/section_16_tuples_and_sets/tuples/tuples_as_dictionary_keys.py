"""
- Below the LOCATIONS dictionary is storing the coordinates as tuples which
are being used as keys for the different global offices of a company
- Lists cannot be used as keys in dictionaries and therefore throw the error
TypeError: unhashable type: 'list'
"""

LOCATIONS = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office",
}

print(LOCATIONS)
print(LOCATIONS[(40.7128, 74.0060)])

new_location = {[34.4454, 38.4123]: "random office"}
print(new_location)
