# reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
        current = self.tail()
        current.next = Node(data)

    def is_empty(self):
        return self.head is None

    def tail(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        if self.is_empty():
            return
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    print("Original List")
    linked_list.print_list()
    linked_list.reverse()
    print("Reversed List")
    linked_list.print_list()


if __name__ == "__main__":
    main()
