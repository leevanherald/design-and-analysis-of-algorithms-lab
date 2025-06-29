class CustomLinkedList:
    class Node:
        """A node in the custom linked list."""

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        """Adds a node to the end of the list."""
        new_node = self.Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        """Removes and returns the first element in the list."""
        if not self.head:
            raise RuntimeError("List is empty")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return value

    def get_first(self):
        """Returns the first element in the list without removing it."""
        if not self.head:
            raise RuntimeError("List is empty")
        return self.head.value

    def get_size(self):
        """Returns the size of the list."""
        return self.size


def josy(n):
    """Solves the Josephus problem using a custom linked list."""
    linked_list = CustomLinkedList()
    for i in range(1, n + 1):
        linked_list.add(i)

    turn = False
    while linked_list.get_size() > 1:
        if turn:
            linked_list.remove_first()
        else:
            temp = linked_list.remove_first()
            linked_list.add(temp)
        turn = not turn

    return linked_list.get_first()


if __name__ == "__main__":
    for i in range(2, 26):
        result = josy(i)
        print(f"n={i}, josephus={result}")
