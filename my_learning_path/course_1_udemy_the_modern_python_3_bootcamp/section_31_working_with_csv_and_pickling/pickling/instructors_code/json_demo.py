import json


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Charles", "Tabby")

# The json.dumps() function takes in a Python object and encodes it into a JSON string
# Result: '["foo", {"bar": ["baz", null, 1.0, 2]}]'
j = json.dumps(["foo", {"bar": ("baz", None, 1.0, 2)}])
print(j)

# However the json.dumps() function can't turn the complex Cat class into a JSON string therefore instead we have to
# make an instance of Cat and then call the __dict__ dunder method on it inside the json.dumps() function
# Result: '{"name": "Charles", "breed": "Tabby"}'
j = json.dumps(c.__dict__)
print(j)
