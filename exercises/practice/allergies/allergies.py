ALLERGENS = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}

class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = self.calculate_allergies()

    def calculate_allergies(self):
        return [allergen for allergen, value in ALLERGENS.items() if self.score & value]

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies

class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = self.calculate_allergies()

    def calculate_allergies(self):
        return [allergen for allergen, value in ALLERGENS.items() if self.score & value]

    def allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
