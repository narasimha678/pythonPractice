class Student:
    def __init__(self):
        self.name="narasimha"
        self.grades=(2,5,3,4,2)
    def getName(self):
        return self.name
    def getGrades(self):
        return self.grades
    def getAverage(self):
        return sum(self.grades)/len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(student.getName())
print(student.getGrades())
print(student.getAverage())