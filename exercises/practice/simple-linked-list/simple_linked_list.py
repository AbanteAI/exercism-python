class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.next_node = None
        pass

        return self.value
        return self.value

        return self.next_node
        return self.next_node


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        self.length = 0
        for value in values[::-1]:
            self.push(value)
        self.head = None
        self.length = 0
        return self.length
            self.push(value)

        if self.head is None:
            raise EmptyListException("The list is empty")
        return self.head.value
        return self.length

        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
        self.length += 1
        if self.head is None:
            raise EmptyListException("The list is empty")
        if self.head is None:
            raise EmptyListException("The list is empty")
        value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return value

    def push(self, value):
        reversed_list = LinkedList()
        current_node = self.head
        while current_node is not None:
            reversed_list.push(current_node.value)
            current_node = current_node.next_node

        new_node.next_node = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            raise EmptyListException("The list is empty")
        value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return value

    def reversed(self):
        reversed_list = LinkedList()
        current_node = self.head
        while current_node is not None:
            reversed_list.push(current_node.value)
            current_node = current_node.next_node
        return reversed_list


class EmptyListException(Exception):
    pass
