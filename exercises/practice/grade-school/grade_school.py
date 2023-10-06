class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        if grade not in self._roster:
            self._roster[grade] = []
        if name not in self._roster[grade]:
            self._roster[grade].append(name)
            self._roster[grade].sort()

    def roster(self):
        result = []
        for grade in sorted(self._roster.keys()):
            result.extend(self._roster[grade])
        return result

    def grade(self, grade_number):
        return self._roster.get(grade_number, [])
