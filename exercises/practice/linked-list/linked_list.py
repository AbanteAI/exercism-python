class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value, None, self.tail)
        if self.tail:
            self.tail.succeeding = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        self.length -= 1
        return value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value, self.head, None)
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.succeeding

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
                self.length -= 1
                return
            current = current.succeeding
        raise ValueError("Value not found")
