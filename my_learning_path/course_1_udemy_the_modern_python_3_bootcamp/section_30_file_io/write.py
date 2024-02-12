"""
The below shows how we can write to files by writing text to an existing file or writing text to a non-existing file
which gets newly created for you
- NOTE: When you pass in “w” as an argument to the mode parameter, it will overwrite anything that was already in the
file
"""

# After running the program, this text was writen to the empty haiku.txt file
with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")

# However, then this text overwrote whatever was already in the haiku.txt file
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out!")

# Then, the lol.txt file was newly created and this text was writen to the file
with open("lol.txt", "w") as file:
    file.write("haha" * 1000)
