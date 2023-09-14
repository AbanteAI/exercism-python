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
        self._head = None
        self._length = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self._length

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty")
        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current_node = self._head
        while current_node:
            reversed_list.push(current_node.value())
            current_node = current_node.next()
        return reversed_list
    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.value()
            current_node = current_node.next()


class EmptyListException(Exception):
    pass
