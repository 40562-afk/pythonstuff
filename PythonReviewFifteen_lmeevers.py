class Student:
    def __init__(self, name, grade):
        self.name  = name
        self.grade = grade

    def getInfo(self):
        print(f"name: {self.name} grade: {self.grade}")
    
Bob = Student("Bob", 90)
Louis = Student("Louis", 85)
Kacey = Student("Kacey", 101)

class School:
    def __init__(self, student):
        self.student = student
    
    def getStudent(self):
        print(f"student: {self.student}")

cool_school = School(Louis)
doom_school = School(Bob)
pool_school = School(Kacey)

cool_school.getStudent()
doom_school.getStudent()
pool_school.getStudent()