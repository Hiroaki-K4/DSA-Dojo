class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if not self.top:
            print("There are no elements")
            return
        val = self.top.val
        self.top = self.top.next
        return val

    def push(self, val):
        new = Node(val)
        new.next = self.top
        self.top = new

    def peek(self):
        if not self.top:
            print("There are no elements")
            return
        return self.top.val

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    print("isEmpty: ", stack.isEmpty())
    print("pop: ", stack.pop())

    val_1 = "Apple"
    val_2 = "Banana"
    val_3 = "Lemon"
    stack.push("Apple")
    stack.push("Banana")
    stack.push("Lemon")
    print("push: ", val_1)
    print("push: ", val_2)
    print("push: ", val_3)

    print("peek: ", stack.peek())
    print("isEmpty: ", stack.isEmpty())
    print("pop: ", stack.pop())
    print("peek: ", stack.peek())
    print("pop: ", stack.pop())
    print("peek: ", stack.peek())
    print("pop: ", stack.pop())
    print("peek: ", stack.peek())
