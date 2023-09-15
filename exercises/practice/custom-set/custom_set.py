class CustomSet:
    def __init__(self, elements=[]):
        self.elements = list(set(elements))

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(x in other.elements for x in self.elements)

    def isdisjoint(self, other):
        return all(x not in other.elements for x in self.elements)

    def __eq__(self, other):
        return set(self.elements) == set(other.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        return CustomSet([x for x in self.elements if x in other.elements])

    def __sub__(self, other):
        return CustomSet([x for x in self.elements if x not in other.elements])

    def __add__(self, other):
        return CustomSet(self.elements + other.elements)
