class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, val):
        new = Node(val)
        if not self.last:
            self.last = new
        else:
            self.last.next = new
            self.last = self.last.next
        if not self.first:
            self.first = self.last

    def remove(self):
        if not self.first:
            print("There are no elements")
            return None
        first = self.first.val
        self.first = self.first.next
        if not self.first:
            self.last = self.first
        return first

    def peek(self):
        if not self.first:
            print("There are no elements")
            return None
        return self.first.val

    def isEmpty(self):
        if not self.first:
            return True
        else:
            return False


if __name__ == "__main__":
    queue = Queue()
    print("isEmpty: ", queue.isEmpty())
    print("pop: ", queue.remove())

    val_1 = "Apple"
    val_2 = "Banana"
    val_3 = "Lemon"
    queue.add("Apple")
    queue.add("Banana")
    queue.add("Lemon")
    print("add: ", val_1)
    print("add: ", val_2)
    print("add: ", val_3)

    print("peek: ", queue.peek())
    print("isEmpty: ", queue.isEmpty())
    print("remove: ", queue.remove())
    print("peek: ", queue.peek())
    print("remove: ", queue.remove())
    print("peek: ", queue.peek())
    print("remove: ", queue.remove())
    print("peek: ", queue.peek())
