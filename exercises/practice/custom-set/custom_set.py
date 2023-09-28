class CustomSet:
    def __init__(self, elements=[]):
        pass

class CustomSet:
    def __init__(self, elements=[]):
        pass

    def isempty(self):
        # Check if the set is empty
        pass

    def __contains__(self, element):
        # Check if an element is present in the set
        pass

    def issubset(self, other):
        # Check if the set is a subset of another set
        pass

    def isdisjoint(self, other):
        # Check if the set is disjoint from another set
        pass

    def __eq__(self, other):
        # Check if the set is equal to another set
        pass

    def add(self, element):
        # Add an element to the set
        if element not in self.elements:
            self.elements.append(element)

    def __eq__(self, other):
        # Check if the set is equal to another set
        if isinstance(other, CustomSet):
            return set(self.elements) == set(other.elements)
        return False

    def intersection(self, other):
        # Find the intersection of the set with another set
        if isinstance(other, CustomSet):
            return CustomSet([element for element in self.elements if element in other.elements])
        return CustomSet()

    def __sub__(self, other):
        # Find the difference between the set and another set
        if isinstance(other, CustomSet):
            return CustomSet([element for element in self.elements if element not in other.elements])
        return self

    def __add__(self, other):
        # Find the union of the set with another set
        if isinstance(other, CustomSet):
            return CustomSet(self.elements + [element for element in other.elements if element not in self.elements])
        return self
        pass