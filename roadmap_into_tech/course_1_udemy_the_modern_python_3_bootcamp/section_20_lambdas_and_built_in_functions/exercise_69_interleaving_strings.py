"""
Write a function called interleave that accepts two strings
- It should return a new string containing the 2 strings interwoven or zipped
together
    - Ex:
        interleave('hi','ha')  # 'hhia'
        interleave('aaa', 'zzz')  # 'azazaz'
        interleave('lzr','iad')  # 'lizard'
- This might seem like an easy task using the zip() function, but in fact
there are a couple of intermediate steps to go from zip() back to a single
string
    - If you need help, I've written up a basic walkthrough of the steps:
        1. Suppose we call interleave('hi', 'ha')
        2. Then zip() the two strings together, giving you a list of tuples
        (once you convert from the default zip_object) - [('h','h'), ('i','a')]
        3. For each of the tuples in the list, join them together using "".join
        resulting in ['hh', 'ia'] - Easiest if you use a list comp. since you
        need to join each tuple
        4. Finally, join the items in the list together using "".join again,
        resulting in 'hhia'
"""


def interleave(string1: str, string2: str) -> str:
    return "".join(["".join(i) for i in zip(string1, string2)])


print(interleave("hi", "ha"))
print(interleave("aaa", "zzz"))
print(interleave("lzr", "iad"))
