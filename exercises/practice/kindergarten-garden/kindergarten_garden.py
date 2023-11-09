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
        """
        Create a Garden from a string diagram and an optional list of students.

        :param diagram: str - A string representing the garden rows.
        :param students: list - An optional list of student names.
        """
        self.diagram = diagram.splitlines()
        self.students = sorted(students) if students is not None else self.DEFAULT_STUDENTS

    def plants(self, student):
        """
        Get the list of plants for a given student.

        :param student: str - The student's name.
        :return: list - The list of plant names that the student is responsible for.
        """
        student_index = self.students.index(student) * 2
        return [
            self.PLANT_NAMES[self.diagram[row][student_index + i]]
            for row in range(2)
            for i in range(2)
        ]