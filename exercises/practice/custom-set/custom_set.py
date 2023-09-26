class CustomSet:
        self.elements = set(elements)

        return len(self.elements) == 0

        return element in self.elements

        return self.elements.issubset(other.elements)

        return self.elements.isdisjoint(other.elements)

        return self.elements == other.elements

        self.elements.add(element)

        return CustomSet(self.elements.intersection(other.elements))

        return CustomSet(self.elements.difference(other.elements))

        return CustomSet(self.elements.union(other.elements))
