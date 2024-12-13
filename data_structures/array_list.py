


class ArrayList:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        print(len(self.array))

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        new_array[:self.size] = self.array
        self.array = new_array

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, idx, value):
        pass

    def pop(self, idx=0):
        pass

    def remove(self, value):
        pass

    def get(self, idx):
        return self.array[idx]

    def __len__(self):
        return self.size


if __name__ == '__main__':
    array_list = ArrayList(2)
    array_list.append("apple")
    print(len(array_list))
