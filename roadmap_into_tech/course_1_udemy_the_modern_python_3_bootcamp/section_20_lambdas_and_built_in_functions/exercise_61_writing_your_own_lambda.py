"""
Write a lambda that accepts a single number and cubes it - Save it in a
variable called cube
- Ex:
    cube(2)  # 8
    cube(3)  # 27
    cube(8)  # 512
- NOTE: This challenge has tests ensuring that cube is actually a lambda
rather than a function so don't cheat by making it a plain old function :)
"""

cube = lambda num: num**3

print(cube(2))
print(cube(3))
print(cube(8))
