class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students or [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ])

        self.plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }
        self.plants_per_student = {}
        for i, student in enumerate(self.students):
            start = i * 2
            end = start + 2
            plants = [
                self.plant_names[plant]
                for row in self.diagram
                for plant in row[start:end]
            ]
            self.plants_per_student[student] = plants
    def plants(self, student):
        return self.plants_per_student[student]