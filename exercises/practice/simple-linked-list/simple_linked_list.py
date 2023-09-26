class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def value(self):
        pass

    def next(self):
        pass


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
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current_node = self._head

        while current_node is not None:
            reversed_list.push(current_node.value())
            current_node = current_node.next()

    def __len__(self):
        return self._length
    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()
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
class EmptyListException(Exception):
    pass
