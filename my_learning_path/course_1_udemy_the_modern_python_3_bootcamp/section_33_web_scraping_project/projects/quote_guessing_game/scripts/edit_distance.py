"""
A Naive recursive Python program to find minimum number operations to convert str1 to str2

References
- https://www.geeksforgeeks.org/edit-distance-dp-5/
"""


def edit_distance(str1: str, str2: str, m: int, n: int) -> int:

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(
        edit_distance(str1, str2, m, n - 1),  # Insert
        edit_distance(str1, str2, m - 1, n),  # Remove
        edit_distance(str1, str2, m - 1, n - 1),  # Replace
    )


# Driver code
if __name__ == "__main__":
    string1 = "GEEXSFRGEEKKS"
    string2 = "GEEKSFORGEEKS"
    print(edit_distance(string1, string2, len(string1), len(string2)))
