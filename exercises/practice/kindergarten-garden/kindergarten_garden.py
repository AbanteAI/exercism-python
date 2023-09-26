class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]
    def plants(self, student):
        plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }
        student_plants = []
        for row in self.diagram:
        student_index = self.students.index(student)
        student_plants = [
            student_plants.append(plant_names[row[student_index * 2]])
            student_plants.append(plant_names[row[student_index * 2 + 1]])
        return student_plants
        ]
        return student_plants
