"""
You have been given an array of strings, where each string may contain only lowercase English letters
- You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table
(dictionary) - The function should return a list of lists, where each inner list contains a group of anagrams
- Ex:
    - If the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return
    [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two
    strings are anagrams of each other, and the last string has no anagrams in the input array
"""


def group_anagrams(strings: list[str]) -> list[list[str]]:
    # Remember it's good practice to have your variables right above the logic your going to use it with to minimize the
    # vertical distance within your code
    anagram_dict = {}
    for word in strings:
        sorted_word = sorted(word)
        sorted_word_ascii = ""
        for letter in sorted_word:
            sorted_word_ascii += str(ord(letter))
        if sorted_word_ascii not in anagram_dict:
            anagram_dict[sorted_word_ascii] = [word]
        else:
            anagram_dict[sorted_word_ascii].append(word)
    # print(anagram_dict)
    anagram_list = []
    for value in anagram_dict.values():
        anagram_list.append(value)
    return anagram_list


if __name__ == "__main__":
    print("1st set:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print("\n2nd set:")
    print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

    print("\n3rd set:")
    print(
        group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"])
    )

    """
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]
    """
