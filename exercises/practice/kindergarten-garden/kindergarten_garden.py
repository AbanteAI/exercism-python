class Garden:
    def __init__(self, diagram, students=None):
        self.rows = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        student_index = self.students.index(student)
        plants = []
        for row in self.rows:
            plants.extend([self.plant_names[row[student_index * 2]], self.plant_names[row[student_index * 2 + 1]]])
        return plants