"""
Create a HashTable class that represents a hash table data structure with a fixed-size array implementation
- The HashTable class should have the following components:
    - An __init__ method that initializes a new hash table with a given size (default size is 7) - The __init__ method
    should perform the following task:
        - Create a list named data_map of length size, initialized with None values, which will be used to store the
        key-value pairs in the hash table - Set the data_map attribute of the HashTable class to this list
"""


class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def __hash(self, key: str) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


if __name__ == "__main__":
    my_hash_table = HashTable()
    my_hash_table.print_table()

    """
    EXPECTED OUTPUT:
    ----------------
    0 : None
    1 : None
    2 : None
    3 : None
    4 : None
    5 : None
    6 : None
    """
