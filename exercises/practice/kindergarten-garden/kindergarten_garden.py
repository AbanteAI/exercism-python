class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]
        self.parse_diagram(diagram)
        self.assign_plants(students)
    def parse_diagram(self, diagram):
        self.rows = diagram.split("\n")
        self.plants = {
            "V": "Violets",
            "R": "Radishes",
            "G": "Grass",
            "C": "Clover"
        }
        
    def assign_plants(self, students):
        self.students = sorted(students)
        self.student_plants = {student: [] for student in self.students}
        for i, student in enumerate(self.students):
            for row in self.rows:
                self.student_plants[student].append(self.plants[row[i * 2]])
                self.student_plants[student].append(self.plants[row[i * 2 + 1]])

    def get_student_plants(self, student):
        return self.student_plants[student]