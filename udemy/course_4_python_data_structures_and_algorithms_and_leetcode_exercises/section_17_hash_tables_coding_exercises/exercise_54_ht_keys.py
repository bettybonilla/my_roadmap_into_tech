"""
Implement the keys method for the HashTable class that returns a list of all the keys present in the hash table
- The method should perform the following tasks:
    1. Create an empty list named all_keys that will store the keys present in the hash table
    2. Iterate through the data_map list:
        - For each non-None element in data_map, iterate through the key-value pairs stored in the nested list
            - For each key-value pair, append the key (located at position 0) to the all_keys list
    3. Return the all_keys list containing all the keys present in the hash table
"""

from typing import Optional


class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def get_item(self, key: str) -> Optional[int]:
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

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

    def keys(self) -> list[str]:
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


if __name__ == "__main__":
    my_hash_table = HashTable()

    my_hash_table.set_item("bolts", 1400)
    my_hash_table.set_item("washers", 50)
    my_hash_table.set_item("lumber", 70)

    print(my_hash_table.keys())

    """
    EXPECTED OUTPUT:
    ----------------
    ['bolts', 'washers', 'lumber']
    """
