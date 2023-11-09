class School:
        self._students = {}
        self._added_students = []

    def add_student(self, name, grade):
        if grade not in self._students:
            self._students[grade] = []
        if name not in self._students[grade]:
            self._students[grade].append(name)
            self._students[grade].sort()
            self._added_students.append(True)
        else:
            self._added_students.append(False)

    def roster(self):
        all_students = []
        for grade in sorted(self._students):
            all_students.extend(self._students[grade])
        return all_students

    def grade(self, grade_number):
        if grade_number in self._students:
            return sorted(self._students[grade_number])
        return []
    def added(self):
        return self._added_students

