class Garden:
    PLANT_NAMES = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }
    DEFAULT_STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    def __init__(self, diagram, students=None):
        self.diagram = diagram.splitlines()
        self.students = sorted(students) if students is not None else self.DEFAULT_STUDENTS

    def plants(self, student):
        index = self.students.index(student) * 2
        plants_symbols = self.diagram[0][index:index+2] + self.diagram[1][index:index+2]
        return [self.PLANT_NAMES[symbol] for symbol in plants_symbols]
