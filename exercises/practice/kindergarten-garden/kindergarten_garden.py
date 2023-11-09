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
        self.students = sorted(students) if students is not None else self.DEFAULT_STUDENTS
        self.plant_rows = diagram.splitlines()
        self.student_plants = {student: [] for student in self.students}
        self._assign_plants_to_students()

    def _assign_plants_to_students(self):
        for row in self.plant_rows:
            for i, student in enumerate(self.students):
                plants_codes = row[i*2:(i+1)*2]
                self.student_plants[student].extend([self.PLANT_CODES[code] for code in plants_codes])

    def plants(self, student):
        student_plants = self.student_plants[student][:2] + self.student_plants[student][2:]
        return student_plants
