class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def set_grade(self, course, grade):
        self.grades[course] = grade

    def get_grade(self, course):
        return self.grades[course]

    def get_gpa(self):
        return sum(self.grades.values())/len(self.grades)

sam = Student("Sam", 12, "Male", 6, {"math": 3.3})
sam.set_grade("eng", 4)
print(sam.get_gpa())
