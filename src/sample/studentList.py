from src.sample.student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def addStudent(self, name, surname):
        student = Student(name, surname)
        self.students.append(student)
        return "Dodano nowego ucznia: " + str(name) + " " + str(surname)

    def getAllStudents(self):
        return