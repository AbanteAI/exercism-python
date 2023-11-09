class Garden:
    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    PLANT_CODES = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    def __init__(self, diagram, students=None):
        self.students = sorted(students) if students else self.DEFAULT_STUDENTS
        self.plant_rows = diagram.splitlines()
        self.student_plants = {student: [] for student in self.students}
        self._assign_plants_to_students()

    def _assign_plants_to_students(self):
        row_length = len(self.plant_rows[0])
        for row in self.plant_rows:
            for i, student in enumerate(self.students):
                if i * 2 < row_length:
                    plant_indices = range(i * 2, min(i * 2 + 2, row_length))
                    self.student_plants[student].extend([self.PLANT_CODES[row[index]] for index in plant_indices])

    def plants(self, student):
        return self.student_plants.get(student, [])
