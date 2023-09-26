class School:
    def __init__(self):
        pass

    def add_student(self, name, grade):
    def add_student(self, name, grade):
        if not hasattr(self, "students"):
            self.students = {}
        if grade not in self.students:
            self.students[grade] = []
        if name in self.students[grade]:
            raise ValueError(f"{name} is already enrolled in grade {grade}.")
        self.students[grade].append(name)
        self.students[grade].sort()
        return "OK"
            self.students = {}
        if grade not in self.students:
            self.students[grade] = []
        if name in self.students[grade]:
            raise ValueError(f"{name} is already enrolled in grade {grade}.")
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        all_students = []
        for grade in sorted(self.students.keys()):
            all_students.extend(self.students[grade])
        return all_students

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        else:
            return []

    def added(self):
    def added(self):
        all_students = []
        for grade in sorted(self.students.keys()):
            all_students.extend(self.students[grade])
        return all_students
