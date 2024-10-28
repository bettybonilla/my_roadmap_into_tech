"""
The below represents a hash table in code
"""

from typing import Optional


class HashTable:
    # Initializer AKA constructor
    # You should always have a prime number of addresses - A prime number increases the amount of randomness for how the
    # key-value pairs are going to be distributed in the hash table and reduces collisions
    def __init__(self, size: int = 7):
        # Creates the data_map list with 7 items initialized to None
        self.data_map = [None] * size

    # Returns the value for the specified key of the key-value pair at the address index in the HashTable object
    def get_item(self, key: str) -> Optional[int]:
        # Sets the index variable to the address index in the data_map list
        index = self.__hash(key)
        # Only checks an already existing list at the index in the data_map list
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # Sets/stores the key-value pair to the address index in the HashTable object with separate chaining
    def set_item(self, key: str, value: int):
        # Sets the index variable to the address index in the data_map list
        index = self.__hash(key)
        # Initializes an empty list at the index in the data_map list if a list hasn't already been created
        if self.data_map[index] is None:
            self.data_map[index] = []
        # Otherwise, adds the key-value pair to the newly created or already existing list at the index in the data_map
        # list
        self.data_map[index].append([key, value])

    # Hashing algorithm which returns the address index in the HashTable object where the key-value pair will be stored
    def __hash(self, key: str) -> int:
        my_hash = 0
        for letter in key:
            # The ord() function gets the ASCII integer value for each letter as you iterate through the loop
            # Then you multiply by prime number 23 - You can use any prime number here
            # Then the % modulo operator is used with prime number 7 since, if you divide any number by 7, the remainder
            # will be between 0 and 6 and this will give you the address index in the data_map list where your key-value
            # pair will be stored
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # Returns all the keys in the HashTable object
    def keys(self) -> list[str]:
        all_keys = []
        for i in range(len(self.data_map)):
            # Only checks already existing lists in the data_map list
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    # Prints the HashTable object
    def display_hash_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


if __name__ == "__main__":
    print("\n----- Test: Instantiates a Hash Table -----\n")
    my_hash_table = HashTable()
    print("hash table:")
    my_hash_table.display_hash_table()

    print("\n----- Test: Sets/stores a key-value pair in the Hash Table -----\n")
    my_hash_table.set_item("bolts", 1400)
    print("hash table:")
    my_hash_table.display_hash_table()

    print(
        "\n----- Test: Sets/stores multiple key-value pairs in the Hash Table -----\n"
    )
    my_hash_table.set_item("washers", 50)
    my_hash_table.set_item("lumber", 70)
    print("hash table:")
    my_hash_table.display_hash_table()

    print("\n----- Test: Gets the value for the key in the Hash Table -----\n")
    print("value for bolts:", my_hash_table.get_item("bolts"))
    print("value for washers:", my_hash_table.get_item("washers"))
    print("value for nails:", my_hash_table.get_item("nails"))

    print("\n----- Test: .keys() on Hash Table -----\n")
    print("keys in hash table:", my_hash_table.keys())
