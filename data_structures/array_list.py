class ArrayList:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        new_array[: self.size] = self.array
        self.array = new_array

    def get(self, idx):
        if idx >= self.size:
            print("Index is out of range.")
            return None
        return self.array[idx]

    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, idx, value):
        if idx >= self.size:
            print("Index is out of range.")
            return
        if self.size + 1 >= self.capacity:
            self._resize()
        self.array[idx + 1 : self.size + 1] = self.array[idx : self.size]
        self.array[idx] = value
        self.size += 1

    def pop(self, idx=-1):
        if idx >= self.size:
            print("Index is out of range.")
            return
        if self.size + 1 >= self.capacity:
            self._resize()
        if idx == -1:
            idx = self.size - 1
        self.array[idx : self.size] = self.array[idx + 1 : self.size + 1]
        self.array[self.size] = None
        self.size -= 1

    # TODO: Implement remove
    def remove(self, value):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        res = []
        for i in range(self.size):
            res.append(self.array[i])
        return str(res)


if __name__ == "__main__":
    array_list = ArrayList(2)
    array_list.append("Apple")
    array_list.append("Banana")
    array_list.append("Orange")
    print("Check __len__ function: ", len(array_list))
    print("Check __str__ function: ", array_list)
    print()

    print("Check get")
    print(array_list.get(100))
    print(array_list.get(1))
    print()

    print("Check insert")
    array_list.insert(100, "Lemon")
    array_list.insert(2, "Lemon")
    print(array_list)
    print()

    print("Check pop")
    array_list.pop(100)
    array_list.pop()
    print(array_list)
    array_list.pop(1)
    print(array_list)
    print()

    print("Check remove")
