class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node

    def remove(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.previous is not None:
                    current.previous.succeeding = current.succeeding
                else:
                    self.head = current.succeeding

                if current.succeeding is not None:
                    current.succeeding.previous = current.previous
                else:
                    self.tail = current.previous

                return True
            current = current.succeeding
        return False

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.succeeding
        return count
    def push(self, value):
        self.append(value)

    def pop(self):
        if self.tail is None:
            raise IndexError("Cannot pop from an empty list")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail is not None:
            self.tail.succeeding = None
        else:
            self.head = None
        return value

    def unshift(self, value):
        self.prepend(value)

    def shift(self):
        if self.head is None:
            raise IndexError("Cannot shift from an empty list")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None
        return value

    def __len__(self):
    def delete(self, value):
        return self.remove(value)
        return self.length()
