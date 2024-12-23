class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # Add the new value to the end of the heap
        self.heap.append(val)
        # Bubble it up to maintain the heap property
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None  # Heap is empty
        # Swap the root with the last element
        self._swap(0, len(self.heap) - 1)
        # Remove the minimum value (original root)
        min_val = self.heap.pop()
        # Bubble down the new root to maintain the heap property
        self._bubble_down(0)
        return min_val

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        # Bubble up until the root or the heap property is satisfied
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        length = len(self.heap)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if the left child exists and is smaller
        if left < length and self.heap[left] < self.heap[smallest]:
            smallest = left
        # Check if the right child exists and is smaller
        if right < length and self.heap[right] < self.heap[smallest]:
            smallest = right
        # If the smallest value is not the current index, swap and recurse
        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    heap = MinHeap()
    # Insert elements
    heap.insert(10)
    heap.insert(4)
    heap.insert(15)
    heap.insert(20)
    heap.insert(3)

    print("Heap after insertions:", heap)

    # Extract minimum elements
    print("Extracted min:", heap.extract_min())
    print("Heap after extraction:", heap)

    print("Extracted min:", heap.extract_min())
    print("Heap after extraction:", heap)
