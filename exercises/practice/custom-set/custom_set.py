class CustomSet:
    def __init__(self, elements=[]):
        pass

    def isempty(self):
        return len(self.elements) == 0

    def issubset(self, other):
        return all(element in other.elements for element in self.elements)

    def isdisjoint(self, other):
        return all(element not in other.elements for element in self.elements)

    def __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

        self.elements = elements.copy() if elements else []

    def intersection(self, other):
        return CustomSet(element for element in self.elements if element in other.elements)

    def __sub__(self, other):
        return CustomSet(element for element in self.elements if element not in other.elements)

    def __add__(self, other):
        return CustomSet(self.elements + other.elements)
    def __contains__(self, element):
        pass

    def issubset(self, other):
        pass

    def isdisjoint(self, other):
        pass

    def __eq__(self, other):
        pass

    def add(self, element):
        pass

    def intersection(self, other):
        pass

    def __sub__(self, other):
        pass

    def __add__(self, other):
        pass
