class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        self.students = sorted(students)
        self.mapping = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    def plant_initial_to_name(self, initial):
        return self.mapping[initial]

    def plants(self, student):
        index = self.students.index(student)
        plants_initials = self.diagram[0][index * 2:index * 2 + 2] + self.diagram[1][index * 2:index * 2 + 2]
        return [self.plant_initial_to_name(initial) for initial in plants_initials]
