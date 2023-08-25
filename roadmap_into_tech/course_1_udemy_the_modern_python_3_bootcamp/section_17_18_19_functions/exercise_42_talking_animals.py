"""
Write a function called speak that accepts a single parameter, animal
- If animal is "pig", it should return "oink"
- If animal is "duck", it should return "quack"
- If animal is "cat", it should return "meow"
- If animal is "dog", it should return "woof"
- If animal is anything else, it should return "?"
- If animal is not specified, it should default to "dog"
    - Ex:
        speak("pig")  # "oink"
        speak("duck")  # "quack"
        speak("cat")  # "meow"
        speak("dog")  # "woof"
        speak("banana")  # "?"
        speak()  # "woof"
"""


# Using conditional logic
def speak(animal: str = "dog") -> str:
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    return "?"


print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("dog"))
print(speak("banana"))
print(speak())


# Alternative code using a dictionary and conditional logic
# def speak(animal: str = "dog") -> str:
#     noises = {
#         "pig": "oink",
#         "duck": "quack",
#         "cat": "meow",
#         "dog": "woof",
#     }

#     noise = noises.get(animal)

#     if noise:
#         return noise
#     return "?"


# print(speak("pig"))
# print(speak("duck"))
# print(speak("cat"))
# print(speak("dog"))
# print(speak("banana"))
# print(speak())


# Refactored code to the code above
# def speak(animal: str = "dog") -> str:
#     noises = {
#         "pig": "oink",
#         "duck": "quack",
#         "cat": "meow",
#         "dog": "woof",
#     }

#     return noises.get(animal, "?")


# print(speak("pig"))
# print(speak("duck"))
# print(speak("cat"))
# print(speak("dog"))
# print(speak("banana"))
# print(speak())
