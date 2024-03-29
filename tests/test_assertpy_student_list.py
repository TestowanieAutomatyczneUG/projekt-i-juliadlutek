import unittest
from assertpy import *
from src.sample.studentList import StudentList
from src.sample.student import Student
import csv
from os.path import exists


class StudentListAssertpyTest(unittest.TestCase):
    def setUp(self):
        mariaKowalska = Student("Maria", "Kowalska", 1,
                                {"Matematyka": [5, 3], "Angielski": [5]})
        janNowak = Student("Jan", "Nowak", 2)
        self.temp = StudentList([mariaKowalska, janNowak])
        # Lista bez studentów
        self.temp2 = StudentList()

    # Testy do dodawania nowego studenta
    def test_add_student(self):
        assert_that(self.temp.addStudent("Maria", "Kowalska")).is_equal_to("Dodano nowego ucznia: Maria Kowalska")

    # W przypadku, kiedy podamy nieprawidłowe imię lub nieprawidłowe nazwisko
    def test_add_student_number_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(65, "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_number_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", 0) \
            .contains("Nazwisko ucznia musi być typu string!")

    def test_add_student_empty_string_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("", "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_empty_string_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", "") \
            .contains("Nazwisko ucznia musi być typu string!")

    def test_add_student_array_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(["Maria"], "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_array_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", ["Kowalska"]) \
            .contains("Nazwisko ucznia musi być typu string!")

    def test_add_student_boolean_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(True, "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_boolean_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", False) \
            .contains("Nazwisko ucznia musi być typu string!")

    def test_add_student_none_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(None, "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_none_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", None) \
            .contains("Nazwisko ucznia musi być typu string!")

    def test_add_student_float_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(65.267, "Kowalska") \
            .contains("Imię ucznia musi być typu string!")

    def test_add_student_float_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", 0.1) \
            .contains("Nazwisko ucznia musi być typu string!")

    # Testy do funkcji zapisującej listę uczniów do csv
    # Sprawdzamy, czy zapis się powiódł
    def test_write_to_csv_correct_output(self):
        assert_that(self.temp.writeToCsvStudentList('testCsv')).is_equal_to("Zapisano dane do pliku csv!")

    # Otwieramy plik i sprawdzamy czy nagłówek jest poprawny
    def test_write_to_csv_correct_header(self):
        if exists('./testCsv/studentList.csv'):
            csvFile = open('./testCsv/studentList.csv')
            csvreader = csv.reader(csvFile)
            header = next(csvreader)
            assert_that(header).contains("Id", "Imię", "Nazwisko", "Średnia")
        pass

    # Otwieramy plik i sprawdzamy czy wartości są poprawne
    def test_write_to_csv_correct_records(self):
        if exists('./testCsv/studentList.csv'):
            csvFile = open('./testCsv/studentList.csv')
            csvreader = csv.reader(csvFile)
            rows = []
            for row in csvreader:
                for el in row:
                    rows.append(el)
            assert_that(rows).contains('1', 'Maria', 'Kowalska', '4.5', '2', 'Jan', 'Nowak', 'Brak')
        pass

    # Sprawdzamy przypadek, kiedy nie ma żadnych studentów
    def test_write_to_csv_any_student(self):
        self.temp2.writeToCsvStudentList('testCsv2')
        csvFile = open('./testCsv2/studentList.csv')
        csvreader = csv.reader(csvFile)
        rows = []
        header = next(csvreader)
        for row in csvreader:
            if row != header:
                for el in row:
                    rows.append(el)
        assert_that(rows).is_empty()

    # Przypadki, kiedy podamy nieprawidłową nazwę katalogu
    def test_write_to_csv_dir_empty_str(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_dir_int(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(3) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_dir_float(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(-1.4) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_dir_bool(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(False) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_dir_none(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_dir_array(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Nazwa katalogu musi być typu string!")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
