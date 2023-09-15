class Garden:
    PLANT_TYPES = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
    def __init__(self, diagram, students):
        self.diagram = diagram.split()
        self.students = sorted(students)
    def plants(self, student):
        index = self.students.index(student) * 2
        student_plants = []

        for row in self.diagram:
            student_plants.append(self.PLANT_TYPES[row[index]])
            student_plants.append(self.PLANT_TYPES[row[index + 1]])

        return student_plants
