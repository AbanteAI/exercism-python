class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        plants_map = {
            "V": "Violets",
            "R": "Radishes",
            "C": "Clover",
            "G": "Grass"
        }

        index = self.students.index(student) * 2
        plants = []
        for row in self.diagram:
            plants.extend([plants_map[c] for c in row[index:index+2]])
        return plants