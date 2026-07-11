"""
Write a function called copy which takes in a file name and a new file name and copies the contents of the first file to
the second file
- Ex:
    copy('story.txt', 'story_copy.txt')  # None
    # Expect the contents of story.txt and story_copy.txt to be the same
- NOTE: We've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to
work with - This is also the text used in the tests
"""


def copy(file_name: str, new_file_name: str):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as file:
        file.write(text)


if __name__ == "__main__":
    copy("story.txt", "story_copy.txt")
