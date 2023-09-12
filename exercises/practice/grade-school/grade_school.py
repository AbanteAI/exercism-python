class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        if name not in self.students[grade]:
            self.students[grade].append(name)
            self.students[grade].sort()

    def roster(self):
        sorted_students = []
        for grade in sorted(self.students):
            sorted_students.extend(self.students[grade])
        return sorted_students

    def grade(self, grade_number):
        return self.students.get(grade_number, [])

