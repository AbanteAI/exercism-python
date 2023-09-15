class Allergies:

class Allergies:
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return self.score & item != 0

    @property
    def lst(self):
        allergies = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }
        return [allergies[item] for item in allergies if self.allergic_to(item)]
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }
        return [allergies[item] for item in allergies if self.allergic_to(item)]