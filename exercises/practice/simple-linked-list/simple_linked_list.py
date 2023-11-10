class EmptyListException(Exception):
    """Exception raised when the linked list is empty."""
    def __init__(self, message="The list is empty."):
        self.message = message
        super().__init__(self.message)
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
        current = self._head
        count = 0
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
