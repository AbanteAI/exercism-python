class Garden:
    PLANT_NAMES = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets",
    }

    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = sorted(students) if students else [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ]

    def _split_diagram(self):
        return self.diagram.split("\n")

    def _get_student_plant_abbreviations(self, student):
        index = self.students.index(student) * 2
        rows = self._split_diagram()
        return [rows[0][index], rows[0][index + 1], rows[1][index], rows[1][index + 1]]

    def plants(self, student):
        abbreviations = self._get_student_plant_abbreviations(student)
        return [self.PLANT_NAMES[abbr] for abbr in abbreviations]