from src.sample.student import Student
from itertools import count


class StudentList:
    def __init__(self):
        self.students = []
        self.__auto_id = count(1, 1)

    def addStudent(self, name, surname):
        studentId = next(self.__auto_id)
        student = Student(name, surname, studentId)
        self.students.append(student)
        return "Dodano nowego ucznia: " + str(name) + " " + str(surname)

    def getAllStudents(self):
        result = ""
        for student in self.students:
            result += str(student.id) + ". " + str(student.name) + " " + str(student.surname) + "\n"
        return result

    def getStudentById(self, num):
        if type(num) != int:
            raise ValueError("Numer musi być liczbą całkowitą!")
        elif num <= 0:
            raise ValueError("Numer musi być liczbą dodatnią!")
        for student in self.students:
            if student.id == num:
                return student
        raise Exception("Uczeń o podanym numerze nie istnieje!")

    def deleteStudentById(self, num):
        if type(num) != int or num <= 0:
            raise ValueError("Numer musi być dodatnią liczbą całkowitą!")
        elif len(self.students) < num:
            raise ValueError("Uczeń o podanym numerze nie istnieje!")
        student = self.getStudentById(num)
        self.students.remove(student)
        del student
