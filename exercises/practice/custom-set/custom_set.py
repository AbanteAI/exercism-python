class CustomSet:
    def __init__(self, elements=None):
        self._elements = set(elements) if elements is not None else set()

    def isempty(self):
        return len(self._elements) == 0

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        return self._elements.issubset(other._elements)

    def isdisjoint(self, other):
        return self._elements.isdisjoint(other._elements)

    def __eq__(self, other):
        return self._elements == other._elements

    def add(self, element):
        self._elements.add(element)

    def intersection(self, other):
        return CustomSet(self._elements.intersection(other._elements))

    def __sub__(self, other):
        return CustomSet(self._elements - other._elements)

    def __add__(self, other):
        return CustomSet(self._elements.union(other._elements))
