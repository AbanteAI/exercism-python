class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        node = Node(value, None, self.tail)
        if self.tail:
            self.tail.succeeding = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def pop(self):
        if not self.tail:
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        self.size -= 1
        return value

    def shift(self):
        if not self.head:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def unshift(self, value):
        node = Node(value, self.head, None)
        if self.head:
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.previous:
                    current.previous.succeeding = current.succeeding
                else:
                    self.head = current.succeeding

                if current.succeeding:
                    current.succeeding.previous = current.previous
                else:
                    self.tail = current.previous

                self.size -= 1
                return
            current = current.succeeding
        raise ValueError("Value not found")

    def __len__(self):
        return self.size