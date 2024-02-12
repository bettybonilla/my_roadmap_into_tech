"""
Write a function called copy_and_reverse which takes in a file name and a new file name and copies the reversed contents
of the first file to the second file
- Ex:
    copy_and_reverse('story.txt', 'story_reversed.txt')  # None
    # Expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
- NOTE: We've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to
work with - This is also the text used in the tests
"""


def copy_and_reverse(file_name: str, new_file_name: str):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as file:
        file.write("".join(list(reversed(text))))

    # Alternative code using slicing
    # with open(new_file_name, "w") as new_file:
    #     new_file.write(text[::-1])


if __name__ == "__main__":
    copy_and_reverse("story.txt", "story_reversed.txt")
