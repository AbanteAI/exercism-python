class Zipper:
    def __init__(self, tree, parent=None, prev=None, next=None):
        self.tree = tree
        self.parent = parent
        self.prev = prev
        self.next = next

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree

    def value(self):
        return self.tree[0]

    def prev(self):
        return Zipper(self.prev, self.parent, self.prev.prev, self)

    def next(self):
        return Zipper(self.next, self.parent, self, self.next.next)

    def up(self):
        return self.parent

    def set_value(self, value):
        self.tree[0] = value
        return self

    def insert_before(self, subtree):
        return Zipper(subtree, self.parent, self.prev, self)

    def insert_after(self, subtree):
        return Zipper(subtree, self.parent, self, self.next)

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        elif self.next:
            self.next.prev = None
        return self.next if self.next else self.prev

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def to_tree(self):
        return self.tree

    def value(self):
        return self.tree[0]

    def prev(self):
        return Zipper(self.prev, self.parent, self.prev.prev, self)

    def next(self):
        return Zipper(self.next, self.parent, self, self.next.next)

    def up(self):
        return self.parent

    def set_value(self, value):
        self.tree[0] = value
        return self

    def insert_before(self, subtree):
        return Zipper(subtree, self.parent, self.prev, self)

    def insert_after(self, subtree):
        return Zipper(subtree, self.parent, self, self.next)

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        elif self.next:
            self.next.prev = None
        return self.next if self.next else self.prev
