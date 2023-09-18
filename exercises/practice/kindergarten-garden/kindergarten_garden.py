STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANT_ABBREVIATIONS = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.students = sorted(students)
        self.diagram = diagram.split('\n')

    def plants(self, student):
        index = self.students.index(student) * 2
        student_plants = [self.diagram[0][index], self.diagram[0][index + 1],
                          self.diagram[1][index], self.diagram[1][index + 1]]
        return [PLANT_ABBREVIATIONS[p] for p in student_plants]