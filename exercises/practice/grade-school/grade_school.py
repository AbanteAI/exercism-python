class School:
    def __init__(self):
        self.roster_dict = {}

    def add_student(self, name, grade):
        if grade in self.roster_dict:
            self.roster_dict[grade].append(name)
        else:
            self.roster_dict[grade] = [name]

    def roster(self):
        roster = []
        for grade in sorted(self.roster_dict.keys()):
            roster.extend(sorted(self.roster_dict[grade]))
        return roster

    def grade(self, grade_number):
        if grade_number in self.roster_dict:
            return sorted(self.roster_dict[grade_number])
        else:
            return []

    def added(self):
        return self.roster_dict
    def added(self):
        return self.roster_dict
