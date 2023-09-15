class Allergies:
    allergen_values = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(self.score & allergen_values[item])

    @property
    def lst(self):
        allergen_list = []
        for allergen, value in allergen_values.items():
            if self.score & value:
                allergen_list.append(allergen)
        return allergen_list
