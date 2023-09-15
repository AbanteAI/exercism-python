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
        for value in reversed(values):
            self.push(value)

    def __len__(self):
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.next()
        return count

    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current = self._head
        while current:
            reversed_list.push(current.value())
            current = current.next()
        return reversed_list
    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()
class EmptyListException(Exception):
    pass
