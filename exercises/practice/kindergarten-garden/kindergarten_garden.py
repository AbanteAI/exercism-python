class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.splitlines()
        self.students = sorted(students) if students is not None else [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, name):
        plant_symbols = {
            'V': 'Violets',
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass'
        }
        student_index = self.students.index(name) * 2
        plants = []
        for row in self.diagram:
            plants.extend([plant_symbols[row[student_index]], plant_symbols[row[student_index + 1]]])
        return plants