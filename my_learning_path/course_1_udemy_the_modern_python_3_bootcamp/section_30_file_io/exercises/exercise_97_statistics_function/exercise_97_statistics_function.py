"""
Write a function called statistics which takes in a file name and returns a dictionary with the number of lines, words,
and characters in the file
- Ex:
    statistics('story.txt')
    # {'lines': 172, 'words': 2145, 'characters': 11228}
- NOTE: We've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to
work with - This is also the text used in the tests
"""


def statistics(file_name: str) -> dict[str, int]:
    with open(file_name) as file:
        file_stats = {"lines": len(file.readlines())}
        file.seek(0)

        text = file.read()
        # The .split() method splits a string into a list of strings after breaking the given string by the specified
        # separator - If a separator is not provided, whitespace is used as the default
        words_list = text.split()
        words = {"words": len(words_list)}
        file.seek(0)

        characters = {"characters": len([char for char in text])}

        file_stats.update(words)
        file_stats.update(characters)
        return file_stats


# Alternative code
# def statistics(file_name: str) -> dict[str, int]:
#     with open(file_name) as file:
#         lines = file.readlines()
#
#         return {
#             "lines": len(lines),
#             "words": sum(len(line.split()) for line in lines),
#             "characters": sum(len(line) for line in lines),
#         }


if __name__ == "__main__":
    print(statistics("story.txt"))
