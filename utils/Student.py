class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        result = 0
        for m in self.marks:
            result += m
        result /= len(self.marks)
        return result > 50
