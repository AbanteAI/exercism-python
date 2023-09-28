class School:
    def __init__(self):
        pass

    def add_student(self, name, grade):
        pass

    def roster(self):
        pass

    def grade(self, grade_number):
        pass

    def added(self):
        pass
class School:
    def __init__(self):
        self.roster_dict = {}

    def add_student(self, name, grade):
        if grade in self.roster_dict:
            self.roster_dict[grade].append(name)
        else:
            self.roster_dict[grade] = [name]

    def roster(self):
        roster_list = []
        for grade in sorted(self.roster_dict.keys()):
            roster_list.extend(sorted(self.roster_dict[grade]))
        return roster_list

    def grade(self, grade_number):
        if grade_number in self.roster_dict:
            return sorted(self.roster_dict[grade_number])
        else:
            return []

    def added(self):
        added_dict = {}
        for grade in self.roster_dict:
            for student in self.roster_dict[grade]:
                if student in added_dict:
                    added_dict[student] += 1
                else:
                    added_dict[student] = 1
        return added_dict