class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        largest = index
        length = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2
        if left < length and self.heap[largest] < self.heap[left]:
            largest = left
        if right < length and self.heap[largest] < self.heap[right]:
            largest = right
        if self.heap[largest] != self.heap[index]:
            self._swap(index, largest)
            self._bubble_down(largest)

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    heap = MaxHeap()
    # Insert elements
    heap.insert(10)
    heap.insert(4)
    heap.insert(15)
    heap.insert(20)
    heap.insert(3)

    print("Heap after insertions:", heap)

    # Extract minimum elements
    print("Extracted max:", heap.extract_max())
    print("Heap after extraction:", heap)

    print("Extracted max:", heap.extract_max())
    print("Heap after extraction:", heap)
