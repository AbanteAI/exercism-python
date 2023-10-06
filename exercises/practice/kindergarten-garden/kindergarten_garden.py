class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else sorted(["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
        self.plant_names = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    def plants(self, student):
        student_index = self.students.index(student)
        plant_initials = [
            self.diagram[0][student_index * 2],
            self.diagram[0][student_index * 2 + 1],
            self.diagram[1][student_index * 2],
            self.diagram[1][student_index * 2 + 1],
        ]
        return [self.plant_names[initial] for initial in plant_initials]
