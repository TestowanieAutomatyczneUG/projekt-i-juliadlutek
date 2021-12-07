from src.sample.student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def addStudent(self, name, surname):
        student = Student(name, surname)
        self.students.append(student)
        return "Dodano nowego ucznia: " + str(name) + " " + str(surname)

    def getAllStudents(self):
        result = ""
        i = 1
        for student in self.students:
            result += str(i) + ". " + str(student.name) + " " + str(student.surname) + "\n"
            i += 1
        return result
