class School:
    def __init__(self):
        self.roster_dict = {}
        self.added_list = []

    def add_student(self, name, grade):
        if grade not in self.roster_dict:
            self.roster_dict[grade] = []
        if name not in self.roster_dict[grade]:
            self.roster_dict[grade].append(name)
            self.roster_dict[grade].sort()
            self.added_list.append(True)
        else:
            self.added_list.append(False)

    def roster(self):
        sorted_roster = []
        for grade in sorted(self.roster_dict.keys()):
            sorted_roster.extend(self.roster_dict[grade])
        return sorted_roster

    def grade(self, grade_number):
        if grade_number in self.roster_dict:
            return self.roster_dict[grade_number]
        else:
            return []

