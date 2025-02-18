class Besanth:
    def __init__(self, name, course, passout):
        self.name = name
        self.course = course
        self.passout = passout
    def greet(self):
        print("Hello, Welcome")
    def details(self):
        print("name of the student",self.name)
        print("course of the student",self.course)
        print("passout year of the student",self.passout)

b1 = Besanth("besanth", "python", 2022)
b1.greet()
b1.details()

print("--------------------------------------------------")

class Apex:
    def __init__(self, name, marks, course):
        self.name=name
        self.marks=marks
        self.course=course
    def greet(self):
        print("Hello, Hi")
    def details(self):
        print("My name is:",self.name)
        print("My marks is",self.marks)
        print("My course is",self.course)
a1 = Apex("Yogee",95,"Python")
a1.greet()
a1.details()
        