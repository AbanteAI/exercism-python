class School:
    def __init__(self):
        self.roster = {}
        pass

    def add_student(self, name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        if name in self.roster[grade]:
            raise ValueError(f"{name} is already enrolled in grade {grade}.")
        self.roster[grade].append(name)
        self.roster[grade].sort()
    def roster(self):
        all_students = []
        for grade in sorted(self.roster.keys()):
            all_students.extend(sorted(self.roster[grade]))
        return all_students

    def grade(self, grade_number):
        if grade_number in self.roster:
            return self.roster[grade_number]
        else:
            return []

    def added(self):
        for grade in self.roster.values():
            if len(grade) != len(set(grade)):
                return True
        return False