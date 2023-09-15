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
        new_node = Node(value, succeeding=self.head)
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1





    def __len__(self):
        return self.size