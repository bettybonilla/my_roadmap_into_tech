"""
Given a person variable:
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
- Create a dictionary called answer that makes each first item in each list a
key and the second item a corresponding value - That's a terrible explanation,
I think it'll be easier if you just look at the end goal:
    {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
- There are many potential solutions for this
"""

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Using the dict() function
answer = dict(person)
print(answer)

# Alternative code using a dictionary comprehension
# answer = {key: value for key, value in person}
# print(answer)
