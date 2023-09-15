class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        if grade not in self._roster:
            self._roster[grade] = []
        
        # Check if the student is already in any grade
        for grade_number, students in self._roster.items():
            if name in students and grade_number != grade:
                raise ValueError(f"{name} is already in a grade.")
        
        if name not in self._roster[grade]:
            self._roster[grade].append(name)
            self._roster[grade].sort()
            if name in students:
                raise ValueError(f"{name} is already in a grade.")
        
        if name not in self._roster[grade]:
            self._roster[grade].append(name)
            self._roster[grade].sort()

    def roster(self):
        sorted_roster = []
        for grade in sorted(self._roster):
            sorted_roster.extend(self._roster[grade])
        return sorted_roster

    def grade(self, grade_number):
        return self._roster.get(grade_number, [])

