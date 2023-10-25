# Static Method
class Student:
    school = "mySchool"  # Class/ Static variable

    def __init__(self, m1, m2, m3):  # Instance Method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance Method
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod  # Decorator
    def getSchool(cls):  # Class Method
        return cls.school

    @staticmethod  # Decorator
    def info():  # Static Method
        print("THIS IS STUDENT CLASS")


s1 = Student(43, 26, 75)
print(s1.avg())
print(Student.getSchool())
Student.info()
