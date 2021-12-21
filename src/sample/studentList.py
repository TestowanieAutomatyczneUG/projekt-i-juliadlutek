from src.sample.student import Student
from itertools import count
import csv
import os


# Klasa studentlist przechowuje listę obiektów klasy Student
class StudentList:
    def __init__(self):
        self.students = []
        self.__auto_id = count(1, 1)

    # Funkcja, która pobiera imie i nazwisko, a następnie tworzy obiekt klasy Student z automatycznie wygenerowanym
    # id i dodaje go do listy studentów
    def addStudent(self, name, surname):
        studentId = next(self.__auto_id)
        student = Student(name, surname, studentId)
        self.students.append(student)
        return "Dodano nowego ucznia: " + str(name) + " " + str(surname)

    # Funkcja, która pobiera listę wszystkich studentów
    def getAllStudents(self):
        result = ""
        for student in self.students:
            result += str(student.id) + ". " + str(student.name) + " " + str(student.surname) + "\n"
        return result

    # Funkcja, która pobiera studenta po id
    def getStudentById(self, num):
        if type(num) != int:
            raise ValueError("Numer musi być liczbą całkowitą!")
        elif num <= 0:
            raise ValueError("Numer musi być liczbą dodatnią!")
        for student in self.students:
            if student.id == num:
                return student
        raise Exception("Uczeń o podanym numerze nie istnieje!")

    # Funkcja, która usuwa studenta po id
    def deleteStudentById(self, num):
        if type(num) != int or num <= 0:
            raise ValueError("Numer musi być dodatnią liczbą całkowitą!")
        elif len(self.students) < num:
            raise ValueError("Uczeń o podanym numerze nie istnieje!")
        student = self.getStudentById(num)
        self.students.remove(student)
        del student

    # Funkcja, która zapisuje listę studentów w formacie csv w podanym katalogu.
    # Plik z listą zawiera kolumny id, imię, nazwisko, średnia ze wszystkich przedmiotów
    # Jeśli uczeń nie ma przypisanych żadnych przedmiotów, w kolumie średnia zostaje wpisane "Brak"
    def writeToCsvStudentList(self, dirName):
        if type(dirName) != str or not dirName:
            raise ValueError("Nazwa katalogu musi być typu string!")
        header = ['Id', 'Imię', 'Nazwisko', 'Średnia']
        try:
            os.mkdir(f"./{dirName}")
        except OSError as e:
            pass
        with open(f"./{dirName}/studentList.csv", 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for student in self.students:
                if student.lectures:
                    data = [student.id, student.name, student.surname, student.getStudentFinalAverage()]
                    writer.writerow(data)
                else:
                    data = [student.id, student.name, student.surname, "Brak"]
                    writer.writerow(data)
        return "Zapisano dane do pliku csv!"
