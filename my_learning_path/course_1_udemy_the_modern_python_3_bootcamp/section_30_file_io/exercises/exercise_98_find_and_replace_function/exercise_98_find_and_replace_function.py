"""
Write a function called find_and_replace which takes in a file name, a word to search for, and a replacement word which
will replace all instances of the searched word in the file with the replacement word
- Ex:
    find_and_replace('story.txt', 'Alice', 'Colt')
    # story.txt now contains the first chapter of my new book, Colt's Adventures in Wonderland
- NOTE: We've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to
work with - This is also the text used in the tests
"""


def find_and_replace(file_name: str, search_word: str, replacement_word: str):
    with open(file_name, "r+") as file:
        text = file.read()
        replacement_text = text.replace(search_word, replacement_word)
        file.seek(0)
        file.write(replacement_text)
        # Removed extra text at the bottom
        file.truncate()


if __name__ == "__main__":
    find_and_replace("story.txt", "Alice", "Colt")
