class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        allergy_items = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }
        return bool(self.score & allergy_items[item])

    @property
    @property
    def lst(self):
        allergy_items = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }
        return [item for item, value in allergy_items.items() if self.score & value]
