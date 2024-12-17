class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def insert(self, key, value) -> None:
        idx = hash(key) % self.capacity
        if self.table[idx]:
            node = self.table[idx]
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            node.next = Node(key, value)
        else:
            self.table[idx] = Node(key, value)

    def pop(self, key) -> None:
        idx = hash(key) % self.capacity
        if self.table[idx]:
            node = self.table[idx]
            if node.key == key:
                if not node.next:
                    self.table[idx] = None
                    return
                else:
                    self.table[idx] = node.next
                    return
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next

    def get(self, key):
        idx = hash(key) % self.capacity
        if self.table[idx]:
            node = self.table[idx]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return None

    def find(self, key) -> bool:
        idx = hash(key) % self.capacity
        if self.table[idx]:
            node = self.table[idx]
            while node:
                if key == node.key:
                    return True
                node = node.next
        return False


if __name__ == "__main__":
    capacity = 3
    hash_table = HashTable(capacity)

    test_case_1 = ["Apple", 0]
    test_case_2 = ["Banana", 1]
    test_case_3 = ["Orange", 2]
    test_case_4 = ["Lemon", 3]
    test_case_5 = ["Melon", 4]

    hash_table.insert(test_case_1[0], test_case_1[1])
    hash_table.insert(test_case_2[0], test_case_2[1])
    hash_table.insert(test_case_3[0], test_case_3[1])
    hash_table.insert(test_case_4[0], test_case_4[1])

    print("TEST: insert and get function")
    print("Key: {0}, Value: {1}".format(test_case_1[0], hash_table.get(test_case_1[0])))
    print("Key: {0}, Value: {1}".format(test_case_2[0], hash_table.get(test_case_2[0])))
    print("Key: {0}, Value: {1}".format(test_case_3[0], hash_table.get(test_case_3[0])))
    print("Key: {0}, Value: {1}".format(test_case_4[0], hash_table.get(test_case_4[0])))
    print()

    print("TEST: find function")
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_1[0], hash_table.find(test_case_1[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_2[0], hash_table.find(test_case_2[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_3[0], hash_table.find(test_case_3[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_4[0], hash_table.find(test_case_4[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_5[0], hash_table.find(test_case_5[0])
        )
    )
    print()

    hash_table.pop(test_case_1[0])
    hash_table.pop(test_case_3[0])
    hash_table.pop(test_case_5[0])
    print("TEST: pop function")
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_1[0], hash_table.find(test_case_1[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_2[0], hash_table.find(test_case_2[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_3[0], hash_table.find(test_case_3[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_4[0], hash_table.find(test_case_4[0])
        )
    )
    print(
        "Is there {0} in hash table? -> {1}".format(
            test_case_5[0], hash_table.find(test_case_5[0])
        )
    )
