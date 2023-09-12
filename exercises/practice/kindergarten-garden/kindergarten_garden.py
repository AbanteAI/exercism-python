class Garden:
    def __init__(self, diagram, students):
    PLANT_NAMES = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets"
    }
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student_name):
        student_index = self.students.index(student_name)
        plant_codes = [
            self.diagram[0][student_index * 2],
            self.diagram[0][student_index * 2 + 1],
            self.diagram[1][student_index * 2],
            self.diagram[1][student_index * 2 + 1]
        ]
        return [self.PLANT_NAMES[code] for code in plant_codes]