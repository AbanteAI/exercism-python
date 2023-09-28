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
        if self.head is None:
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
        node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.length -= 1
        return node.value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.length -= 1
        return node.value

    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current == self.head:
                    self.shift()
                elif current == self.tail:
                    self.pop()
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.length -= 1
                break
            current = current.next
        else:
            raise ValueError("Value not found")