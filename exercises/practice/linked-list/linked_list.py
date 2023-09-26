class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value, None, self.tail)
        if self.tail:
            self.tail.succeeding = new_node
        if not self.head:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        if not self.tail:
            raise IndexError("Cannot pop from an empty linked list")
        value = self.tail.value
        if self.tail.previous:
            self.tail.previous.succeeding = None
            self.tail = self.tail.previous
        else:
            self.head = None
            self.tail = None
        return value

    def shift(self):
        if not self.head:
        if not self.head:
            raise IndexError("Cannot shift from an empty linked list")
        if self.head.succeeding:
            self.head.succeeding.previous = None
            self.head = self.head.succeeding
        else:
            self.head = None
            self.tail = None
        return value

    def unshift(self, value):
        new_node = Node(value, self.head, None)
        if self.head:
            self.head.previous = new_node
        if not self.tail:
            self.tail = new_node
        self.head = new_node

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.succeeding
        return length