class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next_node


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        for value in reversed(values):
            self.push(value)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next()
        return count

    def head(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        return self.head.value()

    def push(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head is None:
            raise EmptyListException("The list is empty.")
        value = self.head.value()
        self.head = self.head.next()
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current = self.head
        while current:
            reversed_list.push(current.value())
            current = current.next()
        return reversed_list


class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        super().__init__(message)
