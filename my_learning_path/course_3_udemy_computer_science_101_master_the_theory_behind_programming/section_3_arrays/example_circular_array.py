class CircularArray:
    read_index = 0
    write_index = 0
    size = 0
    items = []

    def __init__(self, size):
        self.size = size
        for i in range(size):
            self.items.append(None)

    def get_next(self):
        if not all(self.items):
            return None
        item = self.items[self.read_index % self.size]
        self.read_index += 1
        return item

    def get_by_index(self, index):
        if index > self.size:
            # or throw
            return None
        item = self.items[index]
        return item

    def append(self, item):
        self.items[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.size

    def size(self):
        return self.size

    def __str__(self):
        s = ""
        for i in self.items:
            s += str(i) + "\n"
        return s


ca = CircularArray(5)
ca.append("hello")
ca.append("tiny")
ca.append("little")
ca.append("love")
ca.append("bug")
print(ca)
# replaces hello
ca.append("bye")
print(ca)


for i in range(ca.size * 2):
    print(i, ca.get_next())
