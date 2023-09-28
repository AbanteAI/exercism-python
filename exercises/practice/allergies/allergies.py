class Allergies:

    def __init__(self, score):
        self.score = score
        pass

    def allergic_to(self, item):
        return item in self.lst
        return item in self.lst
        return item in self.lst
        pass

    @property
    def lst(self):
        allergens = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }
        allergic_to = []
        for allergen, score in allergens.items():
            if self.score & score:
                allergic_to.append(allergen)
        return allergic_to
