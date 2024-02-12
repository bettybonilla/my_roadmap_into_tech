"""
The below shows how we can use the different file modes
"""

# Writes text to an existing file or writes text to a non-existing file which gets newly created for you
# However it will overwrite previous content
with open("hello.txt", "w") as file:
    file.write("I was here first!\n")

# Adds text to the end of an existing file only or adds text to a non-existing file which gets newly created for you
# Does not overwrite previous content but instead adds content to the end of an existing file only - It always adds to
# the end of a file even if you use the .seek(0) method to move the cursor to the beginning of a file
with open("hello.txt", "a") as file:
    file.write("I was added with append.\n")

# Reads and writes to an existing file only (writing is based on cursor placement and will insert content but start
# overwriting the following content, not shift it over)
# You also cannot create new files, just update existing ones
# By default it starts the cursor at the beginning of a file
with open("hello.txt", "r+") as file:
    file.write("I was added using r+.")

# Inserts ":-)" at index 10 and overwrites "d u" since it does not shift it over
with open("hello.txt", "r+") as file:
    file.seek(10)
    file.write(":-)")
