class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = self.calculate_allergies()
        
    def calculate_allergies(self):
        allergy_items = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
        return [item for item, value in allergy_items.items() if self.score & value]

    def allergic_to(self, item):
        return item in self.allergies

    @property
        return self.allergies
