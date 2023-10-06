class Node:
    def __init__(self, value, succeeding=None, previous=None):
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.length -= 1
        return value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    if self.tail:
                        self.tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.length -= 1
                return
            current = current.next
        raise ValueError("Value not found")

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next