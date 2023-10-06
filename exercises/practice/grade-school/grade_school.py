class School:
    def __init__(self):
        pass

    def add_student(self, name, grade):
        self.roster = []
        self.roster.append((grade, name))

        return [student[1] for student in sorted(self.roster, key=lambda x: (x[0], x[1]))] if self.roster else []
        return [student[1] for student in sorted(self.roster, key=lambda x: (x[0], x[1]))]

    def grade(self, grade_number):
        return [student[1] for student in sorted(self.roster, key=lambda x: x[1])]

    def added(self):
        return True
