"""
Implement the set_item method for the HashTable class that inserts a key-value pair into the hash table
- The method should perform the following tasks:
    1. Calculate the hash value of the given key by calling the private __hash method and store the result in a variable
    named index
    2. Check if the data_map list at the calculated index is None - If it is, create an empty list at that index in
    data_map
    3. Append the key-value pair as a list containing two elements [key, value] to the list at the calculated index in
    data_map
"""


class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def set_item(self, key: str, value: int):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

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

    my_hash_table.set_item("bolts", 1400)
    my_hash_table.set_item("washers", 50)
    my_hash_table.set_item("lumber", 70)

    my_hash_table.print_table()

    """
    EXPECTED OUTPUT:
    ----------------
    0 : None
    1 : None
    2 : None
    3 : None
    4 : [['bolts', 1400], ['washers', 50]]
    5 : None
    6 : [['lumber', 70]]
    """
