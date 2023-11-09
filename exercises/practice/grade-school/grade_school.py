class School:
    def __init__(self):
        self._students = {}

    def add_student(self, name, grade):
        if grade not in self._students:
            self._students[grade] = []
        if name in self._students[grade]:
            return False
        self._students[grade].append(name)
        return True

    def roster(self):
        all_students = []
        for grade in sorted(self._students):
            all_students.extend(sorted(self._students[grade]))
        return all_students

    def grade(self, grade_number):
        if grade_number in self._students:
            return sorted(self._students[grade_number])
        return []

