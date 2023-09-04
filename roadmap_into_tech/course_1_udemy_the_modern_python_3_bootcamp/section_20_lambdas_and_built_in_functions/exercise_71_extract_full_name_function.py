"""
Write a function called extract_full_name
- This function should accept a list of dictionaries and return a new list of
strings with the first and last name keys in each dictionary concatenated
    - Ex:
        names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt',
        'last': 'Steele'}]
        extract_full_name(names)  # ['Elie Schoppik', 'Colt Steele']
"""


# Using list comprehension
def extract_full_name(names_list: list[dict]) -> list[str]:
    return [name["first"] + " " + name["last"] for name in names_list]


# Alternative code using the map() function
# def extract_full_name(names_list: list[dict]) -> list[str]:
#     return list(map(lambda x: f"{x['first']} {x['last']}", names_list))


names = [
    {"first": "Elie", "last": "Schoppik"},
    {"first": "Colt", "last": "Steele"},
]

print(extract_full_name(names))
