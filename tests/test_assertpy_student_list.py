import unittest
from assertpy import *
from src.sample.studentList import StudentList
import csv
from os.path import exists


class StudentListAssertpyTest(unittest.TestCase):
    def setUp(self):
        self.temp = StudentList()

    def test_add_student(self):
        assert_that(self.temp.addStudent("Maria", "Kowalska")).is_equal_to("Dodano nowego ucznia: Maria Kowalska")

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

    def test_write_to_csv_correct_output(self):
        self.temp.addStudent("Maria", "Kowalska")
        self.temp.addStudent("Jan", "Nowak")
        maria = self.temp.getStudentById(1)
        maria.addStudentLecture("Matematyka")
        maria.addStudentGrade("Matematyka", 5)
        maria.addStudentGrade("Matematyka", 3)
        maria.addStudentLecture("Angielski")
        maria.addStudentGrade("Angielski", 5)
        assert_that(self.temp.writeToCsvStudentList('testCsv')).is_equal_to("Zapisano dane do pliku csv!")

    def test_write_to_csv_correct_header(self):
        if exists('./testCsv/studentList.csv'):
            csvFile = open('./testCsv/studentList.csv')
            csvreader = csv.reader(csvFile)
            header = next(csvreader)
            assert_that(header).contains("Id", "Imię", "Nazwisko", "Średnia")
        pass

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

    def test_write_to_csv_any_student(self):
        self.temp.writeToCsvStudentList('testCsv')
        csvFile = open('./testCsv/studentList.csv')
        csvreader = csv.reader(csvFile)
        rows = []
        header = next(csvreader)
        for row in csvreader:
            if row != header:
                for el in row:
                    rows.append(el)
        assert_that(rows).is_empty()

    def test_write_to_csv_dir_empty_str(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Nazwa pliku musi być typu string!")

    def test_write_to_csv_dir_int(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(3) \
            .contains("Nazwa pliku musi być typu string!")

    def test_write_to_csv_dir_float(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(-1.4) \
            .contains("Nazwa pliku musi być typu string!")

    def test_write_to_csv_dir_bool(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(False) \
            .contains("Nazwa pliku musi być typu string!")

    def test_write_to_csv_dir_none(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Nazwa pliku musi być typu string!")

    def test_write_to_csv_dir_array(self):
        assert_that(
            self.temp.writeToCsvStudentList) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Nazwa pliku musi być typu string!")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
