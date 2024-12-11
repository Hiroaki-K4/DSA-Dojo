class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.table = [None] * capacity

    def insert(self, key, value):
        print(hash(key))
        idx = hash(key)
        # TODO: Implement insert function
        if self.table[idx]:
            pass
        else:
            pass

    def pop(self, key):
        pass

    def find(self, key):
        pass


if __name__ == "__main__":
    capacity = 1024
    hash_table = HashTable(capacity)
    hash_table.insert("Apple", 0)
    hash_table.insert("Banana", 1)
    hash_table.insert("Orange", 2)
    hash_table.insert(1, 2)
