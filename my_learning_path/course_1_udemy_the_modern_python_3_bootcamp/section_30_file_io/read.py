"""
The below shows how you can read files using a Python program instead of the terminal Python interpreter
"""

file = open("hello_world.txt")
# The mode parameter’s default is set to “r” which means read
print(file)
# Prints what is inside the entire file as one large string including the newline at the end because the default is set
# to -1 which is the index and therefore reads to the end of the file
print(file.read())
# Moves the cursor to index 0 which is the beginning of the file
print(file.seek(0))
# Returns a list of strings of all the lines in the file comma separated at the newline characters and it moves the
# cursor to the end of the file
print(file.readlines())

# Alternative code to using print(file.read())
# This while loop is to show how to read to the end of the file which prints what is inside the entire file as one large
# string including the newline at the end and then exits after there's nothing left to read
print(file.seek(0))
while True:
    text = file.read()

    if not text:
        break
    print(text)

# After the while loop exits, the cursor is at the end of the file, so it returns an empty string when we try to read it
# again
print("returns empty string here", file.read())
print(file.closed)
file.close()
print(file.closed)
