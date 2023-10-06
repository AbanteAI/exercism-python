class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        index = self.students.index(student) * 2
        plants_row1 = self.diagram[0][index:index+2]
        plants_row2 = self.diagram[1][index:index+2]
        return [self._plant_name(p) for p in plants_row1 + plants_row2]

    def _plant_name(self, plant_code):
        return {
            "V": "Violets",
            "R": "Radishes",
            "C": "Clover",
            "G": "Grass"
        }[plant_code]
class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        index = self.students.index(student) * 2
        plants_row1 = self.diagram[0][index:index+2]
        plants_row2 = self.diagram[1][index:index+2]
        return [self._plant_name(p) for p in plants_row1 + plants_row2]

    def _plant_name(self, plant_code):
        return {
            "V": "Violets",
            "R": "Radishes",
            "C": "Clover",
            "G": "Grass"
        }[plant_code]