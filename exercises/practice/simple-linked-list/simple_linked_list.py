class Node:
    def __init__(self, value):
        pass

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=[]):
        pass

    def __len__(self):
        pass

    def head(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass


class EmptyListException(Exception):
    pass
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.length = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self.length

    def head(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        return self.head

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current = self.head
