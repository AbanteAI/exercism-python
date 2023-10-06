class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = students or [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        plants_mapping = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

        index = self.students.index(student) * 2
        row1 = self.diagram.split("\n")[0][index:index + 2]
        row2 = self.diagram.split("\n")[1][index:index + 2]

        return [
            plants_mapping[plant]
            for plant in (row1 + row2)
        ]