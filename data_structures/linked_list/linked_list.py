class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val)

    def delete(self, val):
        dummy = Node("")
        dummy.next = self.head
        tmp = dummy
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
                self.head = dummy.next
                return
            tmp = tmp.next
        print("There is no {0} in linkedLists".format(val))

    def print_list(self):
        tmp = self.head
        count = 0
        while tmp:
            print("{0}: {1}".format(count, tmp.val))
            tmp = tmp.next
            count += 1


if __name__ == "__main__":
    print("Test append function")
    linked_lists = LinkedList()
    linked_lists.append("Apple")
    linked_lists.append("Banana")
    linked_lists.append("Lemon")
    linked_lists.append("Melon")
    linked_lists.print_list()
    print()

    print("Test delete function")
    linked_lists.delete("Apple")
    linked_lists.delete("Lemon")
    linked_lists.delete("Melon")
    linked_lists.delete("Orange")
    linked_lists.print_list()
